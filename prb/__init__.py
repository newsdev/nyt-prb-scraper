import argparse
import csv
import datetime
import sys

from bs4 import BeautifulSoup
from dateutil import parser as dateparser
import requests
import ujson as json


documents = {
    'initial_review': {
        'document_types': {
            "1": "Government's Unclassified Summary",
            "2": "Opening Statements of Detainee's Representatives",
            "3": "Detainee's Written Submission",
            "4": "Transcript of Public Session",
            "5": "Transcript of Detainee Session",
            "6": "Unclassified Summary of Final Determination",
        },
        'selector': 'table#dnn_ctr45104_Default_List_grdData',
        'url': 'http://www.prs.mil/Review-Information/Initial-Review/'
    },
    'file_review': {
        'document_types': {
            "1": "Government's Unclassified Summary",
            "2": "Detainee's Written Submission",
            "3": "Unclassified Summary of Final Determination/Memorandum for the Record",
        },
        'selector': 'table#dnn_ctr18549_Default_List_grdData',
        'url': 'http://www.prs.mil/Review-Information/File-Review/',
    },
    'full_review': {
        'document_types': {
            "1": "Government's Unclassified Summary",
            "2": "Opening Statements of Detainee's Representatives",
            "3": "Detainee's Written Submission",
            "4": "Transcript of Public Session",
            "5": "Transcript of Detainee Session",
            "6": "Unclassified Summary of Final Determination",
        },
        'selector': 'table#dnn_ctr20067_Default_List_grdData',
        'url': 'http://www.prs.mil/Review-Information/Full-Review/'
    },
}


argparser = argparse.ArgumentParser(description='Return PRB documents')
argparser.add_argument('-o', '--output', action='store')
argparser.add_argument('--json', action='store_true')
argparser.add_argument('--csv', action='store_true')
argparser.add_argument('--tsv', action='store_true')

args = argparser.parse_args()


def _parse_date(date_string):
    if date_string.strip() == "":
        return None

    date_string = dateparser.parse(date_string).date()

    return date_string.strftime("%Y-%m-%d")


def _fix_url(url):
    if not u"http://www.prs.mil" in url:
        url = u"http://www.prs.mil" + url
    return url


def _scrape(page):
    data = []

    request = requests.get(page['url'])
    soup = BeautifulSoup(request.content, "lxml")

    review_table = soup.select(page['selector'])[0]
    rows = review_table.select('tr')

    for row in rows:
        cells = row.select('td')
        if len(cells) > 0:
            for link in cells[5].select('a'):
                if page['document_types'].get(link.text.strip(), None):
                    document = {}
                    document['review_type'] = page['url'].split('http://www.prs.mil/Review-Information/')[1].lower().strip().replace('/','')
                    document['review_url'] = page['url']
                    document['name'] = cells[0].text.split(' (')[0].strip()
                    document['isn'] = cells[0].text.split('ISN ')[1].split(')')[0].strip()
                    document['notification_date'] = _parse_date(cells[1].text.strip())
                    document['hearing_or_review_date'] = _parse_date(cells[2].text.strip())
                    document['final_determination_date'] = _parse_date(cells[3].text.strip())
                    document['type_name'] = page['document_types'][link.text.strip()]
                    document['type_id'] = link.text.strip()
                    document['url'] = _fix_url(link.attrs['href'].strip())
                    document['denied'] = False
                    document['denial'] = None
                    document['id'] = "%(isn)s-%(review_type)s-%(type_id)s-%(hearing_or_review_date)s" % document
                    if "Detainee-Request" in link.attrs['href'].strip() or "DetaineeRequest" in link.attrs['href'].strip():
                        document['url'] = None
                        document['denied'] = True
                        document['denial'] = 'At the request of the detainee.'

                    data.append(document)
    return data


def _output_csv(data):
    writer = csv.DictWriter(sys.stdout, fieldnames=sorted(data[0].keys(), key=lambda x:x), dialect=csv.excel)
    writer.writeheader()

    for p in data:
        writer.writerow(p)


def _output_tsv(data):
    writer = csv.DictWriter(sys.stdout, fieldnames=sorted(data[0].keys(), key=lambda x:x), dialect=csv.excel_tab)
    writer.writeheader()

    for p in data:
        writer.writerow(p)


def _output_json(data):
    sys.stdout.write(json.dumps(data))


def _output(data):
    if args.json:
        _output_json(data)

    elif args.tsv:
        _output_tsv(data)

    elif args.output and args.output == 'json':
        _output_json(data)

    elif args.output and args.output == 'tsv':
        _output_tsv(data)

    else:
        _output_csv(data)


def initial_review():
    _output(_scrape(documents['initial_review']))


def file_review():
    _output(_scrape(documents['file_review']))


def full_review():
    _output(_scrape(documents['full_review']))
