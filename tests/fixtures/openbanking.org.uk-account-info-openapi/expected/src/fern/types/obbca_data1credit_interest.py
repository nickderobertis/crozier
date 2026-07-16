

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1credit_interest_tier_band_set_item import ObbcaData1CreditInterestTierBandSetItem


class ObbcaData1CreditInterest(UniversalBaseModel):
    """
    Details about the interest that may be payable to the BCA account holders
    """

    tier_band_set: typing_extensions.Annotated[
        typing.List[ObbcaData1CreditInterestTierBandSetItem], FieldMetadata(alias="TierBandSet")
    ] = pydantic.Field()
    """
    The group of tiers or bands for which credit interest can be applied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
