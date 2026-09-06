

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .avatar_frame import AvatarFrame
from .mini_profile_background import MiniProfileBackground


class LoginResponse(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="A URL to the JSON Schema for this object."),
    ] = None
    """
    A URL to the JSON Schema for this object.
    """

    avatar: str
    avatarframe: typing.Optional[AvatarFrame] = None
    avatarfull: str
    avatarhash: str
    avatarmedium: str
    communityvisibilitystate: int
    lastlogoff: dt.datetime
    loccountrycode: str
    mini_profile_background: typing.Optional[MiniProfileBackground] = None
    personaname: str
    primaryclanid: str
    profilebackground: typing.Optional[str] = None
    profileurl: str
    timecreated: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
