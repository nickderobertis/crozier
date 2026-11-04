

import typing

WorkflowParameterType = typing.Union[
    typing.Literal["string", "integer", "float", "boolean", "json", "file_url", "credential_id"], typing.Any
]
