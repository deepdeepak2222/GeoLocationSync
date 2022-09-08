import os
import time

# set the default Django settings module for the 'celery' program.
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from celery.signals import setup_logging

# from geo_loc.celery_logging import LOGGING_CELERY

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geo_loc.settings")

from django.conf import settings  # noqa


@setup_logging.connect
def configure_logging(sender=None, **kwargs):
    import logging.config

    # logging.config.dictConfig(LOGGING_CELERY)


app = Celery("geo_loc")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        # 'add-every-10-seconds': {
        #     'task': 'brain.tasks.add',
        #     'schedule': timedelta(seconds=10),
        #     'args': (16, 16)
        # },
        # "publish-schedule-card-60-seconds": {
        #     "task": "core.tasks.publish_cards",
        #     "schedule": timedelta(seconds=60),
        #     "args": (int(time.time()),),
        # },
        # "lms_periodic_csap_certificate_check": {
        #     "task": "csap_certificate.tasks.periodic_csap_certificate_check",
        #     "schedule": timedelta(hours=3),
        # },
        # # 'publish-vault-all-card-60-seconds': {
        # #     'task': 'cadmin.tasks.vault_auto_publish',
        # #     'schedule': timedelta(seconds=90),
        # #     'args': (int(time.time()),)
        # # },
        # # 'expire-one-time-token-60-seconds': {
        # #     'task': 'core.tasks.expire_token',
        # #     'schedule': timedelta(seconds=60)
        # # },
        # # 'update_stats_cache-30-minutes': {
        # #     'task': 'core.tasks.update_graph_cache',
        # #     'schedule': timedelta(seconds=1800),
        # # },
        # "update_other_cache-30-minutes": {
        #     "task": "core.tasks.update_cache_data",
        #     "schedule": timedelta(seconds=1800),
        # },
        # "unlock_locked_account": {
        #     "task": "core.tasks.unlock_account",
        #     "schedule": timedelta(seconds=60),
        # },
        # "close_poll_time": {
        #     "task": "core.tasks.close_poll",
        #     "schedule": timedelta(seconds=60),
        # },
        # "expire_alert_acknowledgements": {
        #     "task": "core.tasks.expire_alert_acknowledgement",
        #     "schedule": timedelta(seconds=60),
        # },
        # "check_password_expiry_once_in_a_day": {
        #     "task": "core.tasks.check_password_expiry",
        #     "schedule": crontab(hour=12, minute=00),
        # },
        # "flexera-60-minutes": {
        #     "task": "integrations.flexera.create_card_flexera_enhanced",
        #     "schedule": timedelta(seconds=3600),
        # },
        # "flexera-24-hours": {
        #     "task": "integrations.flexera.create_updated_advisories",
        #     "schedule": crontab(hour=12, minute=00),
        # },
        # # 'lsisao-flexera-24-hours': {
        # #     'task': 'integrations.flexera.create_daily_report',
        # #     'schedule': crontab(hour=12, minute=00),
        # #     'args': (int(time.time()),)},
        # # 'intel471': {
        # #     'task': 'integrations.intel471.create_intel471_report',
        # #     'schedule': timedelta(seconds=7200),
        # # },
        # "intel471": {
        #     "task": "integrations.intel471.create_intel_471_cards",
        #     "schedule": timedelta(seconds=7200),
        # },
        # "alienvault": {
        #     "task": "integrations.alienvault.get_pulses",
        #     "schedule": timedelta(seconds=7200),
        # },
        # "daily-report-allowed-domain-list": {
        #     "task": "core.tasks.daily_report_allowed_domain",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # "custom-rss-feed-to-alert": {
        #     "task": "core.tasks.parse_custom_rss_feed",
        #     "schedule": timedelta(seconds=600),
        # },
        # "fetch-email-feeds": {
        #     "task": "csap_email.tasks.automatic_email_polling",
        #     "schedule": timedelta(seconds=300),
        # },
        # "daily-login-report-end-user": {
        #     "task": "user_logs.tasks.daily_login_report_end_user",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # "daily-login-report-dashboard": {
        #     "task": "user_logs.tasks.daily_login_report_dashboard",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # "daily-login-failed-report-webapp": {
        #     "task": "user_logs.tasks.daily_login_failed_report_webapp",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # "daily-accounts-lockout": {
        #     "task": "user_logs.tasks.daily_lockouts",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # # },
        # # 'update_intel_incident_data-23-hours':{
        # #     'task': 'core.tasks.update_intel_data',
        # #     'schedule': timedelta(seconds=82800)
        # # }
        # # 'weekly-report-stats-collector': {
        # #     'task': 'user_logs.tasks.weekly_stats',
        # #     'schedule': crontab(hour=0, minute=0o1)
        # # },
        # "weekly-report-send-mail": {
        #     "task": "user_logs.tasks.weekly_report_email",
        #     "schedule": crontab(hour=12, minute=00, day_of_week=1),
        # },
        # "active_directory_sync": {
        #     "task": "integrations.sync_data_integration.fetch_users",
        #     "schedule": timedelta(seconds=21600),
        # },
        # "unlock-locked-intel": {
        #     "task": "web_api.organization_management_web.tasks.unlock_locked_intel",
        #     "schedule": timedelta(seconds=60),
        # },
        # "weekly-user-email-role-report-send-mail": {
        #     "task": "user_logs.tasks.send_weekly_user_mail_role_report",
        #     "schedule": crontab(hour=12, minute=00, day_of_week=3, day_of_month="1-7"),
        # },
        # "check-pending-mail-every-30-minutes": {
        #     "task": "web_api.organization_management_web.sendmail.check_pending_mail",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "check-pending-mail-analyst-every-30-minutes": {
        #     "task": "web_api.organization_management_web.sendmail.check_analyst_pending_mail",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "due_date_exceed_mail": {
        #     "task": "web_api.actions.tasks.send_action_mails_due_date_exceed",
        #     "schedule": crontab(hour=12, minute=00),
        # },
        # "check-event-reminder-emails-every-5-minutes": {
        #     "task": "events.tasks.queue_event_reminders",
        #     "schedule": timedelta(seconds=300),
        # },
        "run-report-scheduler-function": {
            "task": "geo_loc.tasks.sync_pull_geo_json_and_sync_countries",
            "schedule": timedelta(seconds=20),
        },
        # "check-expire-whitelist-indicators": {
        #     "task": "core.tasks.expire_whitelist_indicators",
        #     "schedule": crontab(hour=12, minute=00),
        # },
        # # Synch tactic techniques weekly once(Every monday 11:00 O clock)
        # "weekly-synch-tactic-techniques": {
        #     "task": "attack_framework.tasks.weekly_synch_tactic_techniques",
        #     "schedule": crontab(hour=11, minute=00, day_of_week=1),
        # },
        # "check-sector-pending-mail-every-30-minutes": {
        #     "task": "web_api.organization_management_web.sendmail.check_pending_mail_sector",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "check-scheduled-dashboard-report-every-10-minutes": {
        #     "task": "custom_dashboard.tasks.check_scheduled_dashboard_reports",
        #     "schedule": timedelta(seconds=600),
        # },
        # "sync-rss-feed-urls": {
        #     "task": "csapfeeds.tasks.get_all_feed_urls",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "sync-rss-feed-data": {
        #     "task": "csapfeeds.tasks.get_all_feed_data",
        #     "schedule": timedelta(seconds=3600),
        # },
        # "sync-partner-feed-urls": {
        #     "task": "csapfeeds.csappartnerfeeds.tasks.get_all_partnerfeed_sources",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "sync-partner-feed-data": {
        #     "task": "csapfeeds.csappartnerfeeds.tasks.create_partnerfeed_card",
        #     "schedule": timedelta(seconds=3600),
        # },
        # "publish-vault-card": {
        #     "task": "csapfeeds.tasks.csapfeeds_direct_publish",
        #     "schedule": timedelta(seconds=301),
        # },
        # "threat-assessment-sla-mails": {
        #     "task": "web_api.alerts.tasks.send_threat_assessment_sla_mails",
        #     "schedule": timedelta(minutes=15),
        # },
        # "fetch_salesforce_users": {
        #     "task": "salesforce_integration.tasks.get_salesforce_users",
        #     "schedule": timedelta(seconds=21600),
        # },
        # "fetch-alert-from-polling-communities": {
        #     "task": "integrations.sharing_community_push.fetch_alerts_from_communities",
        #     "schedule": crontab(minute="*/10"),
        # },
        # "sync-tenant-sharing-config": {
        #     "task": "isac_sharing.tasks.sync_tenant_config_task",
        #     "schedule": crontab(hour=00, minute=45),
        # },
        # "poll-isac-sharing-source-request": {
        #     "task": "isac_sharing.tasks.poll_isac_sharing_request_task",
        #     "schedule": crontab(minute="*/10"),
        # },
        # "poll-isac-sharing-target-request": {
        #     "task": "isac_sharing.tasks.poll_isac_sharing_request_management_task",
        #     "schedule": crontab(minute="*/12"),
        # },
        # "clean-event-directory": {
        #     "task": "core.tasks.clean_event_directory",
        #     "schedule": crontab(hour=00, minute=30),
        # },
        # "domain-expiry-report-member-admin": {
        #     "task": "core.tasks.email_member_admins_domain_expire",
        #     "schedule": crontab(hour=00, minute=15),
        # },
        # "poll-threat-defender-content": {
        #     "task": "cadmin.threat_defender.tasks.poll_community_shared_content_task",
        #     "schedule": crontab(hour="*/3", minute=0),
        # },
        # "poll-threat-defender-content-dropdown-options": {
        #     "task": "cadmin.threat_defender.tasks.run_mitre_polling_service_task",
        #     "schedule": crontab(hour=6, minute=15),
        # },
        # "unlock-locked-survey": {
        #     "task": "cadmin.survey.tasks.unlock_locked_survey",
        #     "schedule": timedelta(seconds=60),
        # },
    }
)

# app.conf.task_routes = {
#     "core.tasks.send_push_notification": {"queue": "notification"},
#     "core.tasks.send_push_email_notification": {"queue": "notification"},
# }


@app.task(bind=True)
def debug_task(self):
    print(("Request: {0!r}".format(self.request)))
