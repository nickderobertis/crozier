

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_holder import AssetHolder
from .asset_owners import AssetOwners
from .credit_freddie_mac_asset_detail_voe25 import CreditFreddieMacAssetDetailVoe25
from .credit_freddie_mac_asset_transactions_voe25 import CreditFreddieMacAssetTransactionsVoe25


class CreditFreddieMacAssetVoe25(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_detail: typing_extensions.Annotated[
        CreditFreddieMacAssetDetailVoe25, FieldMetadata(alias="ASSET_DETAIL"), pydantic.Field(alias="ASSET_DETAIL")
    ]
    asset_holder: typing_extensions.Annotated[
        AssetHolder, FieldMetadata(alias="ASSET_HOLDER"), pydantic.Field(alias="ASSET_HOLDER")
    ]
    asset_owners: typing_extensions.Annotated[
        AssetOwners, FieldMetadata(alias="ASSET_OWNERS"), pydantic.Field(alias="ASSET_OWNERS")
    ]
    asset_transactions: typing_extensions.Annotated[
        CreditFreddieMacAssetTransactionsVoe25,
        FieldMetadata(alias="ASSET_TRANSACTIONS"),
        pydantic.Field(alias="ASSET_TRANSACTIONS"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
