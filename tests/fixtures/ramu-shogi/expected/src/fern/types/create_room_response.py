

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateRoomResponse(UniversalBaseModel):
    room_id: typing_extensions.Annotated[str, FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")]
    share_url: typing_extensions.Annotated[str, FieldMetadata(alias="shareUrl"), pydantic.Field(alias="shareUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
