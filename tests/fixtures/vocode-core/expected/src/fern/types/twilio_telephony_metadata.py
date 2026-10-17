

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TwilioTelephonyMetadata(UniversalBaseModel):
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
