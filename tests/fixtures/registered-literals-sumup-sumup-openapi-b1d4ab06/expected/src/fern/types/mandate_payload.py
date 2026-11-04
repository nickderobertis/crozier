

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mandate_payload_type import MandatePayloadType


class MandatePayload(UniversalBaseModel):
    """
    Mandate details used when a checkout should create a reusable card token for future recurring or merchant-initiated payments.
    """

    type: MandatePayloadType = pydantic.Field()
    """
    Type of mandate to create for the saved payment instrument.
    """

    user_agent: str = pydantic.Field()
    """
    Browser or client user agent observed when consent was collected.
    """

    user_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    IP address of the payer when the mandate was accepted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
