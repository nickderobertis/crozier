

import typing

AtlasBusinessMetadataDefCategory = typing.Union[
    typing.Literal[
        "PRIMITIVE",
        "OBJECT_ID_TYPE",
        "ENUM",
        "STRUCT",
        "CLASSIFICATION",
        "ENTITY",
        "ARRAY",
        "MAP",
        "RELATIONSHIP",
        "BUSINESS_METADATA",
    ],
    typing.Any,
]
