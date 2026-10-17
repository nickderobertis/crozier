

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostA2ARequestParamsHistoryLength(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Task (run) identifier to retrieve.
    """

    context_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="contextId"),
        pydantic.Field(alias="contextId", description="Context identifier (thread_id) for the task."),
    ]
    """
    Context identifier (thread_id) for the task.
    """

    history_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="historyLength"),
        pydantic.Field(alias="historyLength", description="Maximum number of history messages to include."),
    ] = None
    """
    Maximum number of history messages to include.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
