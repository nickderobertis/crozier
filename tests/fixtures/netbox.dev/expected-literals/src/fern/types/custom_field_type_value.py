

import typing

CustomFieldTypeValue = typing.Union[
    typing.Literal[
        "text",
        "longtext",
        "integer",
        "decimal",
        "boolean",
        "date",
        "url",
        "json",
        "select",
        "multiselect",
        "object",
        "multiobject",
    ],
    typing.Any,
]
