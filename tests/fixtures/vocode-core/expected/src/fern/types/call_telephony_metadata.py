

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CallTelephonyMetadata_TelephonyMetadataTwilio(UniversalBaseModel):
    type: typing.Literal["telephony_metadata_twilio"] = "telephony_metadata_twilio"
    call_sid: typing.Optional[str] = None
    call_status: typing.Optional[str] = None
    transfer_call_sid: typing.Optional[str] = None
    transfer_call_status: typing.Optional[str] = None
    conference_sid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CallTelephonyMetadata_TelephonyMetadataVonage(UniversalBaseModel):
    type: typing.Literal["telephony_metadata_vonage"] = "telephony_metadata_vonage"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CallTelephonyMetadata = typing_extensions.Annotated[
    typing.Union[CallTelephonyMetadata_TelephonyMetadataTwilio, CallTelephonyMetadata_TelephonyMetadataVonage],
    pydantic.Field(discriminator="type"),
]
