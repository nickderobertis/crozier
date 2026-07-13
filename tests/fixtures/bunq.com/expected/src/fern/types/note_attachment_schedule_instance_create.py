

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bunq_id import BunqId


class NoteAttachmentScheduleInstanceCreate(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[BunqId], FieldMetadata(alias="Id")] = pydantic.Field(default=None)
    """
    The id of the created item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
