

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1credit_interest_tier_band_set_item_calculation_method import (
    ObpcaData1CreditInterestTierBandSetItemCalculationMethod,
)
from .obpca_data1credit_interest_tier_band_set_item_destination import (
    ObpcaData1CreditInterestTierBandSetItemDestination,
)
from .obpca_data1credit_interest_tier_band_set_item_tier_band_item import (
    ObpcaData1CreditInterestTierBandSetItemTierBandItem,
)
from .obpca_data1credit_interest_tier_band_set_item_tier_band_method import (
    ObpcaData1CreditInterestTierBandSetItemTierBandMethod,
)


class ObpcaData1CreditInterestTierBandSetItem(UniversalBaseModel):
    """
    The group of tiers or bands for which credit interest can be applied.
    """

    calculation_method: typing_extensions.Annotated[
        typing.Optional[ObpcaData1CreditInterestTierBandSetItemCalculationMethod],
        FieldMetadata(alias="CalculationMethod"),
    ] = pydantic.Field(default=None)
    """
    Methods of calculating interest
    """

    destination: typing_extensions.Annotated[
        typing.Optional[ObpcaData1CreditInterestTierBandSetItemDestination], FieldMetadata(alias="Destination")
    ] = pydantic.Field(default=None)
    """
    Describes whether accrued interest is payable only to the PCA or to another bank account
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Optional additional notes to supplement the Tier Band Set details
    """

    tier_band: typing_extensions.Annotated[
        typing.List[ObpcaData1CreditInterestTierBandSetItemTierBandItem], FieldMetadata(alias="TierBand")
    ] = pydantic.Field()
    """
    Tier Band Details
    """

    tier_band_method: typing_extensions.Annotated[
        ObpcaData1CreditInterestTierBandSetItemTierBandMethod, FieldMetadata(alias="TierBandMethod")
    ] = pydantic.Field()
    """
    The methodology of how credit interest is charged. It can be:-
    
    1. Banded
    Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.
    
    2. Tiered
    Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.
    
    3. Whole
    The same interest rate is applied irrespective of the PCA balance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
