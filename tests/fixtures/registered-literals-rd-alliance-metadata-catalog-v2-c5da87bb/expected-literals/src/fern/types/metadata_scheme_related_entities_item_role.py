

import typing

MetadataSchemeRelatedEntitiesItemRole = typing.Union[
    typing.Literal[
        "parent scheme",
        "child scheme",
        "input to mapping",
        "output from mapping",
        "maintainer",
        "funder",
        "user",
        "tool",
        "endorsement",
    ],
    typing.Any,
]
