

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOverdraft(UniversalBaseModel):
    """
    Borrowing details
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None
    overdraft_tier_band_set: typing_extensions.Annotated[
        typing.List[ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem],
        FieldMetadata(alias="OverdraftTierBandSet"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
