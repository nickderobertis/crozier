

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItem,
)


class ObReadProduct2DataProductItemOtherProductTypeCreditInterest(UniversalBaseModel):
    """
    Details about the interest that may be payable to the Account holders
    """

    tier_band_set: typing_extensions.Annotated[
        typing.List[ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItem],
        FieldMetadata(alias="TierBandSet"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
