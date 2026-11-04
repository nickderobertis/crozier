

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueuePresentation(UniversalBaseModel):
    active: bool
    id: str
    waiting_messages: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="waitingMessages"),
        pydantic.Field(alias="waitingMessages", description="The count of queued messages"),
    ] = None
    """
    The count of queued messages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
