

import typing

ExternalSigningServiceEnvelopeStatus = typing.Union[
    typing.Literal[
        "completed",
        "created",
        "declined",
        "deleted",
        "delivered",
        "processing",
        "sent",
        "signed",
        "template",
        "voided",
        "expired",
    ],
    typing.Any,
]
