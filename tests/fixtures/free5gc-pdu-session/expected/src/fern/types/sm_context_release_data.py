

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cause import Cause
from .ng_ap_cause import NgApCause
from .user_location import UserLocation


class SmContextReleaseData(UniversalBaseModel):
    cause: typing.Optional[Cause] = None
    ng_ap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngApCause"), pydantic.Field(alias="ngApCause")
    ] = None
    f_5g_mm_cause_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="5gMmCauseValue"), pydantic.Field(alias="5gMmCauseValue")
    ] = None
    ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="ueLocation"), pydantic.Field(alias="ueLocation")
    ] = None
    ue_time_zone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueTimeZone"), pydantic.Field(alias="ueTimeZone")
    ] = None
    add_ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="addUeLocation"), pydantic.Field(alias="addUeLocation")
    ] = None
    vsmf_release_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="vsmfReleaseOnly"), pydantic.Field(alias="vsmfReleaseOnly")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
