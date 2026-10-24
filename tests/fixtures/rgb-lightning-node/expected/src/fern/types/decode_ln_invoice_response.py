

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bitcoin_network import BitcoinNetwork


class DecodeLnInvoiceResponse(UniversalBaseModel):
    amt_msat: typing.Optional[int] = None
    expiry_sec: int
    timestamp: int
    asset_id: typing.Optional[str] = None
    asset_amount: typing.Optional[int] = None
    description: typing.Optional[str] = None
    description_hash: typing.Optional[str] = None
    payment_hash: str
    payment_secret: str
    payee_pubkey: typing.Optional[str] = None
    network: BitcoinNetwork

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
