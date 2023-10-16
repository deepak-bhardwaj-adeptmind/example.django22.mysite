#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
import os
import sys
from django.contrib import admin
from django.urls import path
from mysite.settings import SECRET_KEY
from prefect import Flow, task


def run_actions():
    print("##### CHECK FOR ENV VALUES")
    mms_url = os.environ["MMS_URL"]
    print(f"Fetched MMS_URL value is {mms_url}")

    print("##### CHECK FOR INSTALLED REQUIREMENTS")
    # urlpatterns = [
    #     path('admin/', admin.site.urls),
    # ]
    # print(f"urlpatterns created are - {urlpatterns}")
    print(f"Flow object is - {Flow.__dict__}")

    print("####### Add a sample file.")
    data = {
        "morguard": "en_ca",
        "hammerson": "fr_fr",
        "oxford": "en_ca",  # update
        "oxford_fr": "fr_ca",  # update
        "oxford_pl": "pl_ca"  # update
    }
    with open("sample_config.json", "w") as f:
        json.dump(data, f)

    feeds_could_not_be_added = []
    feeds_could_not_be_removed = []
    smt_added_feeds = smt_removed_feeds = []
    # generate logs for the feeds which couldn't be added and removed.
    feeds_could_not_be_added_logs = (
        f"{len(feeds_could_not_be_added)}/{len(smt_added_feeds)} feeds couldn't be added."
        f" Here is the list : {_convert_feeds_to_display_format(feeds_could_not_be_added)}"
    )
    feeds_could_not_be_removed_logs = (
        f"{len(feeds_could_not_be_removed)}/{len(smt_removed_feeds)} feeds couldn't be removed."
        f" Here is the list : {_convert_feeds_to_display_format(feeds_could_not_be_removed)}"
    )

    # generate logs for the feeds which have been added and removed.
    successfully_added_feeds = []
    for feed in smt_added_feeds:
        if feed not in feeds_could_not_be_added:
            successfully_added_feeds.append(feed)

    successfully_removed_feeds = []
    for feed in smt_removed_feeds:
        if feed not in feeds_could_not_be_removed:
            successfully_removed_feeds.append(feed)
    successfully_added_feeds_logs = (
        f"{len(successfully_added_feeds)}/{len(smt_added_feeds)} feeds have been added."
        f" Here is the list : {_convert_feeds_to_display_format(successfully_added_feeds)}"
    )
    successfully_removed_feeds_logs = (
        f"{len(successfully_removed_feeds)}/{len(smt_removed_feeds)} feeds have been removed."
        f" Here is the list : {_convert_feeds_to_display_format(successfully_removed_feeds)}"
    )

    integration_logs = '\n'.join(
        [
            "##########################################################",
            feeds_could_not_be_added_logs,
            feeds_could_not_be_removed_logs,
            "##########################################################",
            successfully_added_feeds_logs,
            successfully_removed_feeds_logs
        ]
    )
    print("-----------------git push origin --delete feed_integration_automate")
    print(integration_logs)
    return integration_logs


if __name__ == '__main__':
    run_actions()
