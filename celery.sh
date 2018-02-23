#!/usr/bin/env bash

celery -A site_task worker --loglevel=info --config=config.celery_setting