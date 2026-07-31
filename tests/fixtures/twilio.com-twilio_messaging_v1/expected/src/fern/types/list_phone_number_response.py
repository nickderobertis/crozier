

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_phone_number_response_meta import ListPhoneNumberResponseMeta
from .messaging_v1service_phone_number import MessagingV1ServicePhoneNumber


class ListPhoneNumberResponse(UniversalBaseModel):
    meta: typing.Optional[ListPhoneNumberResponseMeta] = None
    phone_numbers: typing.Optional[typing.List[MessagingV1ServicePhoneNumber]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
