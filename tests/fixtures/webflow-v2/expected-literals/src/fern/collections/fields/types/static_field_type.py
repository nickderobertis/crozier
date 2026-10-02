

import typing

StaticFieldType = typing.Union[
    typing.Literal[
        "Color",
        "DateTime",
        "Email",
        "File",
        "Image",
        "Link",
        "MultiImage",
        "Number",
        "Phone",
        "PlainText",
        "RichText",
        "Switch",
        "VideoLink",
    ],
    typing.Any,
]
