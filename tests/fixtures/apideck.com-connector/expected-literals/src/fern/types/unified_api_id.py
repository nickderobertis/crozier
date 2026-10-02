

import typing

UnifiedApiId = typing.Union[
    typing.Literal[
        "accounting",
        "ats",
        "calendar",
        "crm",
        "csp",
        "customer-support",
        "ecommerce",
        "email",
        "email-marketing",
        "expense-management",
        "file-storage",
        "form",
        "hris",
        "lead",
        "payroll",
        "pos",
        "procurement",
        "project-management",
        "script",
        "sms",
        "spreadsheet",
        "team-messaging",
        "issue-tracking",
        "time-registration",
        "transactional-email",
        "vault",
    ],
    typing.Any,
]
