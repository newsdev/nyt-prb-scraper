import sys

from bs4 import BeautifulSoup
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


def _scrape(page):
    payload = []

    request = requests.get(page['url'])
    soup = BeautifulSoup(request.content, "lxml")

    review_table = soup.select(page['selector'])[0]
    rows = review_table.select('tr')

    for row in rows:
        cells = row.select('td')
        if len(cells) > 0:
            detainee = {}
            detainee['name'] = cells[0].text.split(' (')[0].strip()
            detainee['isn'] = cells[0].text.split('ISN ')[1].split(')')[0].strip()
            detainee['notification_date'] = cells[1].text.strip()
            detainee['hearing_or_review_date'] = cells[2].text.strip()
            detainee['final_determination_date'] = cells[3].text.strip()
            detainee['missing_documents'] = []
            detainee['documents'] = []

            for link in cells[4].select('a'):
                if page['document_types'].get(link.text.strip(), None):
                    document = {}
                    document['type_name'] = page['document_types'][link.text.strip()]
                    document['type_id'] = link.text.strip()
                    document['url'] = link.attrs['href'].strip()
                    document['denied'] = False
                    document['denial'] = None
                    if "Detainee-Request" in link.attrs['href'].strip() or "DetaineeRequest" in link.attrs['href'].strip():
                        document['url'] = None
                        document['denied'] = True
                        document['denial'] = 'At the request of the detainee.'
                    detainee['documents'].append(document)

            for d in page['document_types'].keys():
                if d not in [z['type_id'] for z in detainee['documents']]:
                    detainee['missing_documents'].append(d)

            payload.append(detainee)
    return payload


def _output(data):
    sys.stdout.write(json.dumps(data))


def initial_review():
    _output(_scrape(documents['initial_review']))


def file_review():
    _output(_scrape(documents['file_review']))


def full_review():
    _output(_scrape(documents['full_review']))
