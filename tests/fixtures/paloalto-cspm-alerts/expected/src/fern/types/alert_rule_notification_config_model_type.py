

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertRuleNotificationConfigModelType(enum.StrEnum):
    """
    Integration type
    """

    EMAIL = "email"
    SLACK = "slack"
    SPLUNK = "splunk"
    AMAZON_SQS = "amazon_sqs"
    JIRA = "jira"
    MICROSOFT_TEAMS = "microsoft_teams"
    WEBHOOK = "webhook"
    AWS_SECURITY_HUB = "aws_security_hub"
    GOOGLE_CSCC = "google_cscc"
    SERVICE_NOW = "service_now"
    PAGER_DUTY = "pager_duty"
    AZURE_SERVICE_BUS_QUEUE = "azure_service_bus_queue"
    DEMISTO = "demisto"
    AWS_S3 = "aws_s3"
    SNOWFLAKE = "snowflake"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
        splunk: typing.Callable[[], T_Result],
        amazon_sqs: typing.Callable[[], T_Result],
        jira: typing.Callable[[], T_Result],
        microsoft_teams: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
        aws_security_hub: typing.Callable[[], T_Result],
        google_cscc: typing.Callable[[], T_Result],
        service_now: typing.Callable[[], T_Result],
        pager_duty: typing.Callable[[], T_Result],
        azure_service_bus_queue: typing.Callable[[], T_Result],
        demisto: typing.Callable[[], T_Result],
        aws_s3: typing.Callable[[], T_Result],
        snowflake: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertRuleNotificationConfigModelType.EMAIL:
            return email()
        if self is AlertRuleNotificationConfigModelType.SLACK:
            return slack()
        if self is AlertRuleNotificationConfigModelType.SPLUNK:
            return splunk()
        if self is AlertRuleNotificationConfigModelType.AMAZON_SQS:
            return amazon_sqs()
        if self is AlertRuleNotificationConfigModelType.JIRA:
            return jira()
        if self is AlertRuleNotificationConfigModelType.MICROSOFT_TEAMS:
            return microsoft_teams()
        if self is AlertRuleNotificationConfigModelType.WEBHOOK:
            return webhook()
        if self is AlertRuleNotificationConfigModelType.AWS_SECURITY_HUB:
            return aws_security_hub()
        if self is AlertRuleNotificationConfigModelType.GOOGLE_CSCC:
            return google_cscc()
        if self is AlertRuleNotificationConfigModelType.SERVICE_NOW:
            return service_now()
        if self is AlertRuleNotificationConfigModelType.PAGER_DUTY:
            return pager_duty()
        if self is AlertRuleNotificationConfigModelType.AZURE_SERVICE_BUS_QUEUE:
            return azure_service_bus_queue()
        if self is AlertRuleNotificationConfigModelType.DEMISTO:
            return demisto()
        if self is AlertRuleNotificationConfigModelType.AWS_S3:
            return aws_s3()
        if self is AlertRuleNotificationConfigModelType.SNOWFLAKE:
            return snowflake()
