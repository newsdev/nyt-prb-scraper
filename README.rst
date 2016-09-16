NYT PRB Scraper
===============

From `their website <http://www.prs.mil/>`__: "The Periodic Review
Secretariat (PRS) develops and administers the periodic review process
for eligible Guantanamo Bay detainees, including provision of personal
representatives to detainees."

Usage
-----

The PRB engages in three different forms of review for a Guantanamo
detainee's documents: An initial review, a file review and a full
review. Technically, a fourth type, the subsequent full review, is
available. To date, no subsequent full reviews have been posted.

Initial review
~~~~~~~~~~~~~~

::

    initial_review > initial_review.json

File review
~~~~~~~~~~~

::

    file_review > file_review.json

Full review
~~~~~~~~~~~

::

    full_review > full_review.json

Schema
------

\`\`\`python [ { 'name': 'Mustafa Faraj Muhammad Masud al-Jadid
al-Uzaybi', 'isn': '10017', 'notification\_date': '4/4/2016',
'hearing\_or\_review\_date': '8/16/2016', 'final\_determination\_date':
'', 'missing\_documents' ['4','6'], 'documents': [ { 'type\_name':
'Government's Unclassified Summary', 'type\_id': '1', 'url':
'http://www.prs.mil/Portals/60/Documents/ISN10017/160331\_U\_ISN10017\_GOVERNMENTS\_UNCLASSIFIED\_SUMMARY\_PUBLIC.pdf',
'denied': False, 'denial': None }, ... ] }, ...]

Output
------

The scrapers return JSON.
