

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_transaction_description import AssetTransactionDescription
from .credit_freddie_mac_asset_transaction_detail_voe25 import CreditFreddieMacAssetTransactionDetailVoe25


class CreditFreddieMacAssetTransactionVoe25(UniversalBaseModel):
    """
    An object representing...
    """

    asset_transaction_description: typing_extensions.Annotated[
        typing.List[AssetTransactionDescription],
        FieldMetadata(alias="ASSET_TRANSACTION_DESCRIPTION"),
        pydantic.Field(
            alias="ASSET_TRANSACTION_DESCRIPTION",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ]
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_transaction_detail: typing_extensions.Annotated[
        CreditFreddieMacAssetTransactionDetailVoe25,
        FieldMetadata(alias="ASSET_TRANSACTION_DETAIL"),
        pydantic.Field(alias="ASSET_TRANSACTION_DETAIL"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
