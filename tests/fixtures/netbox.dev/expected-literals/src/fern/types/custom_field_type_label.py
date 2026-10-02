

import typing

CustomFieldTypeLabel = typing.Union[
    typing.Literal[
        "Text",
        "Text (long)",
        "Integer",
        "Decimal",
        "Boolean (true/false)",
        "Date",
        "URL",
        "JSON",
        "Selection",
        "Multiple selection",
        "Object",
        "Multiple objects",
    ],
    typing.Any,
]
