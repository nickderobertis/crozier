

import typing

from ...types.email_notification import EmailNotification
from ...types.slack_bearer_notification import SlackBearerNotification
from ...types.slack_web_hook_notification import SlackWebHookNotification

CreateMonitorAlertRoutesItem = typing.Union[SlackWebHookNotification, SlackBearerNotification, EmailNotification]
