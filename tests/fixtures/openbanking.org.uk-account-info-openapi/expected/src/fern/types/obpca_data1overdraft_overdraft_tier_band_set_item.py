

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_tier_band_method import (
    ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod,
)


class ObpcaData1OverdraftOverdraftTierBandSetItem(UniversalBaseModel):
    """
    Tier band set details
    """

    authorised_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AuthorisedIndicator"),
        pydantic.Field(
            alias="AuthorisedIndicator", description="Indicates if the Overdraft is authorised (Y) or unauthorised (N)"
        ),
    ] = None
    """
    Indicates if the Overdraft is authorised (Y) or unauthorised (N)
    """

    buffer_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BufferAmount"),
        pydantic.Field(
            alias="BufferAmount",
            description="When a customer exceeds their credit limit, a financial institution will not charge the customer unauthorised overdraft charges if they do not exceed by more than the buffer amount. Note: Authorised overdraft charges may still apply.",
        ),
    ] = None
    """
    When a customer exceeds their credit limit, a financial institution will not charge the customer unauthorised overdraft charges if they do not exceed by more than the buffer amount. Note: Authorised overdraft charges may still apply.
    """

    identification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Identification"),
        pydantic.Field(
            alias="Identification",
            description="Unique and unambiguous identification of a  Tier Band for a overdraft product.",
        ),
    ] = None
    """
    Unique and unambiguous identification of a  Tier Band for a overdraft product.
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(
            alias="Notes", description="Optional additional notes to supplement the overdraft Tier Band Set details"
        ),
    ] = None
    """
    Optional additional notes to supplement the overdraft Tier Band Set details
    """

    overdraft_fees_charges: typing_extensions.Annotated[
        typing.Optional[typing.List[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem]],
        FieldMetadata(alias="OverdraftFeesCharges"),
        pydantic.Field(alias="OverdraftFeesCharges", description="Overdraft fees and charges details"),
    ] = None
    """
    Overdraft fees and charges details
    """

    overdraft_tier_band: typing_extensions.Annotated[
        typing.List[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem],
        FieldMetadata(alias="OverdraftTierBand"),
        pydantic.Field(alias="OverdraftTierBand", description="Provides overdraft details for a specific tier or band"),
    ]
    """
    Provides overdraft details for a specific tier or band
    """

    overdraft_type: typing_extensions.Annotated[
        typing.Optional[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType],
        FieldMetadata(alias="OverdraftType"),
        pydantic.Field(
            alias="OverdraftType",
            description="An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.",
        ),
    ] = None
    """
    An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.
    """

    tier_band_method: typing_extensions.Annotated[
        ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod,
        FieldMetadata(alias="TierBandMethod"),
        pydantic.Field(
            alias="TierBandMethod",
            description="The methodology of how overdraft is charged. It can be:\n'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable). \n'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation\n'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.",
        ),
    ]
    """
    The methodology of how overdraft is charged. It can be:
    'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable). 
    'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation
    'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
