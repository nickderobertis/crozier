

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonCommentTicketWrite(UniversalBaseModel):
    body: str = pydantic.Field()
    """
    The contents of the comment in plain text or HTML format.
    """

    task_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="taskId"),
        pydantic.Field(alias="taskId", description="Task or Issue to which comment must belong"),
    ]
    """
    Task or Issue to which comment must belong
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
