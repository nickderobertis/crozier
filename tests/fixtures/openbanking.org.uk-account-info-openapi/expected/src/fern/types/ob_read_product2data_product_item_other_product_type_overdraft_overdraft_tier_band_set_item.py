

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem,
)
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem,
)
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_type import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType,
)
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_tier_band_method import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod,
)


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItem(UniversalBaseModel):
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
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    overdraft_fees_charges: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem
            ]
        ],
        FieldMetadata(alias="OverdraftFeesCharges"),
        pydantic.Field(alias="OverdraftFeesCharges"),
    ] = None
    overdraft_tier_band: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem
        ],
        FieldMetadata(alias="OverdraftTierBand"),
        pydantic.Field(alias="OverdraftTierBand"),
    ]
    overdraft_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType],
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
        ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod,
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
