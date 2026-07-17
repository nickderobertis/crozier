

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1credit_interest import ObbcaData1CreditInterest
from .obbca_data1other_fees_charges_item import ObbcaData1OtherFeesChargesItem
from .obbca_data1overdraft import ObbcaData1Overdraft
from .obbca_data1product_details import ObbcaData1ProductDetails


class ObbcaData1(UniversalBaseModel):
    credit_interest: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterest],
        FieldMetadata(alias="CreditInterest"),
        pydantic.Field(
            alias="CreditInterest",
            description="Details about the interest that may be payable to the BCA account holders",
        ),
    ] = None
    """
    Details about the interest that may be payable to the BCA account holders
    """

    other_fees_charges: typing_extensions.Annotated[
        typing.Optional[typing.List[ObbcaData1OtherFeesChargesItem]],
        FieldMetadata(alias="OtherFeesCharges"),
        pydantic.Field(
            alias="OtherFeesCharges",
            description="Contains details of fees and charges which are not associated with either Overdraft or features/benefits",
        ),
    ] = None
    """
    Contains details of fees and charges which are not associated with either Overdraft or features/benefits
    """

    overdraft: typing_extensions.Annotated[
        typing.Optional[ObbcaData1Overdraft],
        FieldMetadata(alias="Overdraft"),
        pydantic.Field(alias="Overdraft", description="Borrowing details"),
    ] = None
    """
    Borrowing details
    """

    product_details: typing_extensions.Annotated[
        typing.Optional[ObbcaData1ProductDetails],
        FieldMetadata(alias="ProductDetails"),
        pydantic.Field(alias="ProductDetails"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
