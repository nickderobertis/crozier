

import typing

DocumentElementKind = typing.Union[
    typing.Literal[
        "text",
        "table",
        "figure",
        "formula",
        "key_value",
        "query_answer",
        "section",
        "selection_mark",
        "signature",
        "barcode",
        "link",
        "stamp",
        "other",
    ],
    typing.Any,
]
