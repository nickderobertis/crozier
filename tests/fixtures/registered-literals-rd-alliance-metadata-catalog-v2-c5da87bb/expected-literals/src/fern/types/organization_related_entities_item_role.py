

import typing

OrganizationRelatedEntitiesItemRole = typing.Union[
    typing.Literal[
        "maintained scheme",
        "maintained tool",
        "maintained mapping",
        "funded scheme",
        "funded tool",
        "funded mapping",
        "used scheme",
        "endorsement",
    ],
    typing.Any,
]
