

import typing

NotificationCategory = typing.Union[
    typing.Literal[
        "NEW_ORGANIZATION",
        "STUDY_SHARED",
        "TEMPLATE_SHARED",
        "CONVERSATION_NOTIFICATION",
        "ANNOTATION_NOTE",
        "WALLET_SHARED",
    ],
    typing.Any,
]
