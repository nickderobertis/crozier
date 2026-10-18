

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostA2ARequestParamsTwo(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Task (run) identifier to cancel.
    """

    context_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="contextId"),
        pydantic.Field(alias="contextId", description="Context identifier (thread_id) for the task."),
    ]
    """
    Context identifier (thread_id) for the task.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
