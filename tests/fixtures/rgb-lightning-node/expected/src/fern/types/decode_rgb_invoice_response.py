

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_schema import AssetSchema
from .assignment import Assignment
from .bitcoin_network import BitcoinNetwork
from .recipient_type import RecipientType


class DecodeRgbInvoiceResponse(UniversalBaseModel):
    recipient_id: str
    recipient_type: RecipientType
    asset_schema: typing.Optional[AssetSchema] = None
    asset_id: typing.Optional[str] = None
    assignment: Assignment
    network: BitcoinNetwork
    expiration_timestamp: typing.Optional[int] = None
    transport_endpoints: typing.List[str]
    unknown_query_params: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
