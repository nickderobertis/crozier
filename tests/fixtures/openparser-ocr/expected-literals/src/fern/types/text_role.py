

import typing

TextRole = typing.Union[
    typing.Literal[
        "document_title",
        "heading",
        "paragraph",
        "line",
        "word",
        "symbol",
        "list",
        "list_item",
        "caption",
        "footnote",
        "page_header",
        "page_footer",
        "page_number",
        "code",
        "other",
    ],
    typing.Any,
]
