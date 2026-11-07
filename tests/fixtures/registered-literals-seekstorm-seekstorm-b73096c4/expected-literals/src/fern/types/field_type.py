

import typing

FieldType = typing.Union[
    typing.Literal[
        "U8",
        "U16",
        "U32",
        "U64",
        "I8",
        "I16",
        "I32",
        "I64",
        "Timestamp",
        "F32",
        "F64",
        "Bool",
        "String16",
        "String32",
        "StringSet16",
        "StringSet32",
        "Point",
        "Text",
        "Json",
        "Binary",
    ],
    typing.Any,
]
