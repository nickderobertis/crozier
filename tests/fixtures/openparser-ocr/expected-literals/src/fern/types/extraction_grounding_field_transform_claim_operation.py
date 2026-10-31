

import typing

ExtractionGroundingFieldTransformClaimOperation = typing.Union[
    typing.Literal[
        "date_time_format",
        "numeric_format",
        "quantity_magnitude",
        "unit_conversion",
        "currency_code",
        "boolean_alias",
        "text_normalization",
        "enum_alias",
    ],
    typing.Any,
]
