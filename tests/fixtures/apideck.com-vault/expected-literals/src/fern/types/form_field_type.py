

import typing

FormFieldType = typing.Union[
    typing.Literal[
        "text",
        "checkbox",
        "tel",
        "email",
        "url",
        "textarea",
        "select",
        "filtered-select",
        "multi-select",
        "datetime",
        "date",
        "time",
        "number",
    ],
    typing.Any,
]
