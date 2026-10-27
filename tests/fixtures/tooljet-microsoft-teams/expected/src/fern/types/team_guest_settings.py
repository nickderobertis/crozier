

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TeamGuestSettings(UniversalBaseModel):
    allow_create_update_channels: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowCreateUpdateChannels"),
        pydantic.Field(alias="allowCreateUpdateChannels"),
    ] = None
    allow_delete_channels: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDeleteChannels"), pydantic.Field(alias="allowDeleteChannels")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
