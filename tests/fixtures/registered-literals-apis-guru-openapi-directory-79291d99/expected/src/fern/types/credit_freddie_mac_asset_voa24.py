

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_detail import AssetDetail
from .asset_holder import AssetHolder
from .asset_owners import AssetOwners
from .credit_freddie_mac_asset_transactions_voa24 import CreditFreddieMacAssetTransactionsVoa24
from .validation_sources import ValidationSources


class CreditFreddieMacAssetVoa24(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_detail: typing_extensions.Annotated[
        AssetDetail, FieldMetadata(alias="ASSET_DETAIL"), pydantic.Field(alias="ASSET_DETAIL")
    ]
    asset_holder: typing_extensions.Annotated[
        AssetHolder, FieldMetadata(alias="ASSET_HOLDER"), pydantic.Field(alias="ASSET_HOLDER")
    ]
    asset_owners: typing_extensions.Annotated[
        AssetOwners, FieldMetadata(alias="ASSET_OWNERS"), pydantic.Field(alias="ASSET_OWNERS")
    ]
    asset_transactions: typing_extensions.Annotated[
        CreditFreddieMacAssetTransactionsVoa24,
        FieldMetadata(alias="ASSET_TRANSACTIONS"),
        pydantic.Field(alias="ASSET_TRANSACTIONS"),
    ]
    validation_sources: typing_extensions.Annotated[
        ValidationSources, FieldMetadata(alias="VALIDATION_SOURCES"), pydantic.Field(alias="VALIDATION_SOURCES")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
