

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1other_fees_charges_fee_charge_cap_item import ObpcaData1OtherFeesChargesFeeChargeCapItem
from .obpca_data1other_fees_charges_fee_charge_detail_item import ObpcaData1OtherFeesChargesFeeChargeDetailItem


class ObpcaData1OtherFeesCharges(UniversalBaseModel):
    """
    Contains details of fees and charges which are not associated with either borrowing or features/benefits
    """

    fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[typing.List[ObpcaData1OtherFeesChargesFeeChargeCapItem]], FieldMetadata(alias="FeeChargeCap")
    ] = pydantic.Field(default=None)
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge
    """

    fee_charge_detail: typing_extensions.Annotated[
        typing.List[ObpcaData1OtherFeesChargesFeeChargeDetailItem], FieldMetadata(alias="FeeChargeDetail")
    ] = pydantic.Field()
    """
    Other fees/charges details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
