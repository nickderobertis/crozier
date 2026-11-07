

import typing

WorkflowStatus = typing.Union[
    typing.Literal["published", "draft", "auto_generated", "importing", "import_failed"], typing.Any
]
