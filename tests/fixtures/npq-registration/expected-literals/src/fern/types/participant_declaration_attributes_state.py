

import typing

ParticipantDeclarationAttributesState = typing.Union[
    typing.Literal[
        "submitted", "eligible", "payable", "paid", "voided", "ineligible", "awaiting_clawback", "clawed_back"
    ],
    typing.Any,
]
