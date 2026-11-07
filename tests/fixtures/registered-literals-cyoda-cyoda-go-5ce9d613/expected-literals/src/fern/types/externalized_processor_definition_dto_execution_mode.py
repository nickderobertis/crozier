

import typing

ExternalizedProcessorDefinitionDtoExecutionMode = typing.Union[
    typing.Literal["SYNC", "ASYNC_SAME_TX", "ASYNC_NEW_TX"], typing.Any
]
