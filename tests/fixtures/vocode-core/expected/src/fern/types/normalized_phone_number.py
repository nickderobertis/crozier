

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .normalized_phone_number_telephony_account_connection import NormalizedPhoneNumberTelephonyAccountConnection
from .normalized_phone_number_telephony_provider import NormalizedPhoneNumberTelephonyProvider


class NormalizedPhoneNumber(UniversalBaseModel):
    id: str
    user_id: str
    active: typing.Optional[bool] = None
    label: typing.Optional[str] = None
    inbound_agent: typing.Optional[str] = None
    outbound_only: typing.Optional[bool] = None
    example_context: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    number: str
    telephony_provider: typing.Optional[NormalizedPhoneNumberTelephonyProvider] = None
    telephony_account_connection: typing.Optional[NormalizedPhoneNumberTelephonyAccountConnection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
