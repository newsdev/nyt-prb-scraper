NYT PRB Scraper
===============

From `their website <http://www.prs.mil/>`__: "The Periodic Review
Secretariat (PRS) develops and administers the periodic review process
for eligible Guantanamo Bay detainees, including provision of personal
representatives to detainees."

Usage
-----

The PRB engages in three different forms of review for a Guantanamo
detainee"s documents: An initial review, a file review and a full
review. Technically, a fourth type, the subsequent full review, is
available. To date, no subsequent full reviews have been posted.

Initial review
~~~~~~~~~~~~~~

.. code:: bash

    initial_review --csv > initial_review.csv
    initial_review --json > initial_review.json
    initial_review --tsv > initial_review.tsv

File review
~~~~~~~~~~~

.. code:: bash

    file_review --csv > file_review.csv
    file_review --json > file_review.json
    file_review --tsv > file_review.tsv

Full review
~~~~~~~~~~~

.. code:: bash

    full_review --csv > full_review.csv
    full_review --json > full_review.json
    full_review --tsv > full_review.tsv

Schema
------

Returns a row or an object for every document. Each document contains
the document-specific fields like ``type_name``, ``type_id``, and
``url`` as well as the detainee-specific fields like ``name`` and
``isn``. Builds a unique id for each document from
``isn-type_id-hearing_or_review_date``.

.. code:: json

    [
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"1",
            "url":"http:\/\/www.prs.mil\/Portals\/60\/Documents\/ISN037\/141105_U_ISN037_GOVERNMENT'S_UNCLASSIFIED_SUMMARY_PUBLIC.pdf",
            "type_name":"Government's Unclassified Summary",
            "id":"037-initial-review-1-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        },
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"2",
            "url":"http:\/\/www.prs.mil\/Portals\/60\/Documents\/ISN037\/141105_U_ISN037_PR_STATEMENT_PRB.pdf",
            "type_name":"Opening Statements of Detainee's Representatives",
            "id":"037-initial-review-2-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        },
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"3",
            "url":"http:\/\/www.prs.mil\/Portals\/60\/Documents\/ISN037\/141216_U_ISN037_DETAINEE_WRITTEN_SUBMISSION_PUBLIC.pdf",
            "type_name":"Detainee's Written Submission",
            "id":"037-initial-review-3-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        },
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"4",
            "url":"http:\/\/www.prs.mil\/LinkClick.aspx?fileticket=RFOMdQD69k4%3d&tabid=8447&portalid=60&mid=20067",
            "type_name":"Transcript of Public Session",
            "id":"037-initial-review-4-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        },
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"5",
            "url":"http:\/\/www.prs.mil\/Portals\/60\/Documents\/ISN037\/141105_U_ISN037_TRANSCRIPT_OF_DETAINEE_SESSION_PUBLIC.pdf",
            "type_name":"Transcript of Detainee Session",
            "id":"037-initial-review-5-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        },
        {
            "review_type": "full-review",
            "review_url": "http://www.prs.mil/Review-Information/Initial-Review/",
            "hearing_or_review_date":"2014-11-05",
            "denial":null,
            "name":"Abdel Malik Ahmed Abdel Wahab Al Rahabi",
            "type_id":"6",
            "url":"http:\/\/www.prs.mil\/LinkClick.aspx?fileticket=s0XT-7qYc94%3d&tabid=8447&portalid=60&mid=20067",
            "type_name":"Unclassified Summary of Final Determination",
            "id":"037-initial-review-6-2014-11-05",
            "isn":"037",
            "denied":false,
            "notification_date":"2014-08-26",
            "final_determination_date":"2014-12-05"
        }
    ]

Output
------

The scrapers can return CSV, JSON or TSV. The default if no options are
passed is CSV.
