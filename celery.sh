#!/usr/bin/env bash

celery -A apps.site_task worker --loglevel=info --config=config.celery_setting