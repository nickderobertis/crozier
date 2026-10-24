

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .htlc_status import HtlcStatus


class Payment(UniversalBaseModel):
    amt_msat: typing.Optional[int] = None
    asset_amount: typing.Optional[int] = None
    asset_id: typing.Optional[str] = None
    payment_hash: str
    inbound: bool
    status: HtlcStatus
    created_at: int
    updated_at: int
    payee_pubkey: str
    preimage: typing.Optional[str] = None
    description: typing.Optional[str] = None
    description_hash: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
