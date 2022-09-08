from celery import shared_task
import logging
logger = logging.getLogger(__name__)


@shared_task
def sync_pull_geo_json_and_sync_countries():
    logger.info("Syncing geojson and preparing to update db with latest country data")
