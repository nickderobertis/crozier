

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type_fee_category import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeTypeFeeCategory,
)


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType(UniversalBaseModel):
    """
    Other Fee/charge type which is not available in the standard code set
    """

    code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Code"),
        pydantic.Field(alias="Code", description="The four letter Mnemonic used within an XML file to identify a code"),
    ] = None
    """
    The four letter Mnemonic used within an XML file to identify a code
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Description to describe the purpose of the code"),
    ]
    """
    Description to describe the purpose of the code
    """

    fee_category: typing_extensions.Annotated[
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeTypeFeeCategory,
        FieldMetadata(alias="FeeCategory"),
        pydantic.Field(alias="FeeCategory", description="Categorisation of fees and charges into standard categories."),
    ]
    """
    Categorisation of fees and charges into standard categories.
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="Long name associated with the code")
    ]
    """
    Long name associated with the code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
