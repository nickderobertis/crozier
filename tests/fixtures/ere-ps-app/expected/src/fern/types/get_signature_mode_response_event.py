

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .comfort_signature_status_enum import ComfortSignatureStatusEnum
from .duration import Duration
from .session_info import SessionInfo
from .status import Status


class GetSignatureModeResponseEvent(UniversalBaseModel):
    status: typing.Optional[Status] = None
    comfort_signature_status: typing_extensions.Annotated[
        typing.Optional[ComfortSignatureStatusEnum],
        FieldMetadata(alias="comfortSignatureStatus"),
        pydantic.Field(alias="comfortSignatureStatus"),
    ] = None
    comfort_signature_max: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="comfortSignatureMax"), pydantic.Field(alias="comfortSignatureMax")
    ] = None
    comfort_signature_timer: typing_extensions.Annotated[
        typing.Optional[Duration],
        FieldMetadata(alias="comfortSignatureTimer"),
        pydantic.Field(alias="comfortSignatureTimer"),
    ] = None
    session_info: typing_extensions.Annotated[
        typing.Optional[SessionInfo], FieldMetadata(alias="sessionInfo"), pydantic.Field(alias="sessionInfo")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    answert_to_activate_comfort_signature: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="answertToActivateComfortSignature"),
        pydantic.Field(alias="answertToActivateComfortSignature"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
