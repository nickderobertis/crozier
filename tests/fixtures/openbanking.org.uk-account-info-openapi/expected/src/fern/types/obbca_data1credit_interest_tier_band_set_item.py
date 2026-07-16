

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1credit_interest_tier_band_set_item_calculation_method import (
    ObbcaData1CreditInterestTierBandSetItemCalculationMethod,
)
from .obbca_data1credit_interest_tier_band_set_item_destination import (
    ObbcaData1CreditInterestTierBandSetItemDestination,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItem,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_method import (
    ObbcaData1CreditInterestTierBandSetItemTierBandMethod,
)


class ObbcaData1CreditInterestTierBandSetItem(UniversalBaseModel):
    """
    The group of tiers or bands for which credit interest can be applied.
    """

    calculation_method: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemCalculationMethod],
        FieldMetadata(alias="CalculationMethod"),
    ] = pydantic.Field(default=None)
    """
    Methods of calculating interest
    """

    destination: typing_extensions.Annotated[
        ObbcaData1CreditInterestTierBandSetItemDestination, FieldMetadata(alias="Destination")
    ] = pydantic.Field()
    """
    Describes whether accrued interest is payable only to the BCA or to another bank account
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Optional additional notes to supplement the Tier Band Set details
    """

    tier_band: typing_extensions.Annotated[
        typing.List[ObbcaData1CreditInterestTierBandSetItemTierBandItem], FieldMetadata(alias="TierBand")
    ] = pydantic.Field()
    """
    Tier Band Details
    """

    tier_band_method: typing_extensions.Annotated[
        ObbcaData1CreditInterestTierBandSetItemTierBandMethod, FieldMetadata(alias="TierBandMethod")
    ] = pydantic.Field()
    """
    The methodology of how credit interest is paid/applied. It can be:-
    
    1. Banded
    Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.
    
    2. Tiered
    Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.
    
    3. Whole
    The same interest rate is applied irrespective of the BCA balance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
