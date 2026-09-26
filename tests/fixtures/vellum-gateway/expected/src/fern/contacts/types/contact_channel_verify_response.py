

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact_channel_verify_response_channel import ContactChannelVerifyResponseChannel


class ContactChannelVerifyResponse(UniversalBaseModel):
    ok: bool
    channel: ContactChannelVerifyResponseChannel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
