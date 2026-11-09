

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_transaction import AssetTransaction


class AssetTransactions(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_transaction: typing_extensions.Annotated[
        typing.List[AssetTransaction],
        FieldMetadata(alias="ASSET_TRANSACTION"),
        pydantic.Field(alias="ASSET_TRANSACTION"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
