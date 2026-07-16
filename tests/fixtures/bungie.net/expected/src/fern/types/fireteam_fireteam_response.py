

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fireteam_fireteam_member import FireteamFireteamMember
from .fireteam_fireteam_summary import FireteamFireteamSummary


class FireteamFireteamResponse(UniversalBaseModel):
    alternates: typing_extensions.Annotated[
        typing.Optional[typing.List[FireteamFireteamMember]],
        FieldMetadata(alias="Alternates"),
        pydantic.Field(alias="Alternates"),
    ] = None
    members: typing_extensions.Annotated[
        typing.Optional[typing.List[FireteamFireteamMember]],
        FieldMetadata(alias="Members"),
        pydantic.Field(alias="Members"),
    ] = None
    summary: typing_extensions.Annotated[
        typing.Optional[FireteamFireteamSummary], FieldMetadata(alias="Summary"), pydantic.Field(alias="Summary")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
