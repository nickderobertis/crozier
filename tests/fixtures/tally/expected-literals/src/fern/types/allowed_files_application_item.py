

import typing

AllowedFilesApplicationItem = typing.Union[
    typing.Literal[
        "*", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".rar", ".json", ".gzip", ".odt"
    ],
    typing.Any,
]
