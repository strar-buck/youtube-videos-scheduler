from __future__ import absolute_import, unicode_literals

from .celery_app import app as celery_app

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fampay.settings")


__all__ = ("celery_app",)
