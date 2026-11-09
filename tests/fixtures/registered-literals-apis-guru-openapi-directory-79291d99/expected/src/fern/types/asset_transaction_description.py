

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssetTransactionDescription(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_transaction_description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AssetTransactionDescription"),
        pydantic.Field(
            alias="AssetTransactionDescription",
            description="Asset Transaction Description String up to 3 occurances 1 required.",
        ),
    ]
    """
    Asset Transaction Description String up to 3 occurances 1 required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
