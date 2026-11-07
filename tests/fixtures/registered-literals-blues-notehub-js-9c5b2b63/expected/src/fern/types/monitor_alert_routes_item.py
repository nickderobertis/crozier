

import typing

from .email_notification import EmailNotification
from .slack_bearer_notification import SlackBearerNotification
from .slack_web_hook_notification import SlackWebHookNotification

MonitorAlertRoutesItem = typing.Union[SlackWebHookNotification, SlackBearerNotification, EmailNotification]
