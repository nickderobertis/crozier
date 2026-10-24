

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .htlc_status import HtlcStatus


class SendPaymentResponse(UniversalBaseModel):
    payment_id: str
    payment_hash: typing.Optional[str] = None
    payment_secret: typing.Optional[str] = None
    status: HtlcStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
