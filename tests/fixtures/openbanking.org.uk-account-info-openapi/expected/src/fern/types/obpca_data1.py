

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1credit_interest import ObpcaData1CreditInterest
from .obpca_data1other_fees_charges import ObpcaData1OtherFeesCharges
from .obpca_data1overdraft import ObpcaData1Overdraft
from .obpca_data1product_details import ObpcaData1ProductDetails


class ObpcaData1(UniversalBaseModel):
    credit_interest: typing_extensions.Annotated[
        typing.Optional[ObpcaData1CreditInterest],
        FieldMetadata(alias="CreditInterest"),
        pydantic.Field(
            alias="CreditInterest",
            description="Details about the interest that may be payable to the PCA account holders",
        ),
    ] = None
    """
    Details about the interest that may be payable to the PCA account holders
    """

    other_fees_charges: typing_extensions.Annotated[
        typing.Optional[ObpcaData1OtherFeesCharges],
        FieldMetadata(alias="OtherFeesCharges"),
        pydantic.Field(
            alias="OtherFeesCharges",
            description="Contains details of fees and charges which are not associated with either borrowing or features/benefits",
        ),
    ] = None
    """
    Contains details of fees and charges which are not associated with either borrowing or features/benefits
    """

    overdraft: typing_extensions.Annotated[
        typing.Optional[ObpcaData1Overdraft],
        FieldMetadata(alias="Overdraft"),
        pydantic.Field(alias="Overdraft", description="Details about Overdraft rates, fees & charges"),
    ] = None
    """
    Details about Overdraft rates, fees & charges
    """

    product_details: typing_extensions.Annotated[
        typing.Optional[ObpcaData1ProductDetails],
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
