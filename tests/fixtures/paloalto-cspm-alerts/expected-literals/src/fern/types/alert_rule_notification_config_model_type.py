

import typing

AlertRuleNotificationConfigModelType = typing.Union[
    typing.Literal[
        "email",
        "slack",
        "splunk",
        "amazon_sqs",
        "jira",
        "microsoft_teams",
        "webhook",
        "aws_security_hub",
        "google_cscc",
        "service_now",
        "pager_duty",
        "azure_service_bus_queue",
        "demisto",
        "aws_s3",
        "snowflake",
    ],
    typing.Any,
]
