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

.. code:: json

    [
        {
            "name": "Mustafa Faraj Muhammad Masud al-Jadid al-Uzaybi",
            "isn": "10017",
            "notification_date": "4/4/2016",
            "hearing_or_review_date": "8/16/2016",
            "final_determination_date": "",
            "missing_documents": ["4","6"],
            "documents": [
                {
                    "type_name": "Government's Unclassified Summary",
                    "type_id": "1",
                    "url": "http://www.prs.mil/Portals/60/Documents/ISN10017/160331_U_ISN10017_GOVERNMENTS_UNCLASSIFIED_SUMMARY_PUBLIC.pdf",
                    "denied": false,
                    "denial": null
                }
            ]
        }
    ]

Output
------

The scrapers return JSON.
