from datetime import datetime


def getAuthorizationHeaders():
    """Get the authorization headers to make teamwork api call"""
    headers = {
        "Authorization": "",
        "Content-Type": "application/json",
    }
    return headers


def formatDateTime(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
