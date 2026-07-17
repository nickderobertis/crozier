

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_credit_interest import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterest,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterest,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem,
)
from .ob_read_product2data_product_item_other_product_type_overdraft import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraft,
)
from .ob_read_product2data_product_item_other_product_type_product_details import (
    ObReadProduct2DataProductItemOtherProductTypeProductDetails,
)
from .ob_read_product2data_product_item_other_product_type_repayment import (
    ObReadProduct2DataProductItemOtherProductTypeRepayment,
)
from .ob_supplementary_data1 import ObSupplementaryData1


class ObReadProduct2DataProductItemOtherProductType(UniversalBaseModel):
    """
    Other product type details associated with the account.
    """

    credit_interest: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeCreditInterest],
        FieldMetadata(alias="CreditInterest"),
        pydantic.Field(
            alias="CreditInterest", description="Details about the interest that may be payable to the Account holders"
        ),
    ] = None
    """
    Details about the interest that may be payable to the Account holders
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Description of the Product associated with the account"),
    ]
    """
    Description of the Product associated with the account
    """

    loan_interest: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeLoanInterest],
        FieldMetadata(alias="LoanInterest"),
        pydantic.Field(
            alias="LoanInterest", description="Details about the interest that may be payable to the SME Loan holders"
        ),
    ] = None
    """
    Details about the interest that may be payable to the SME Loan holders
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Long name associated with the product"),
    ]
    """
    Long name associated with the product
    """

    other_fees_charges: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem]],
        FieldMetadata(alias="OtherFeesCharges"),
        pydantic.Field(alias="OtherFeesCharges"),
    ] = None
    overdraft: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeOverdraft],
        FieldMetadata(alias="Overdraft"),
        pydantic.Field(alias="Overdraft", description="Borrowing details"),
    ] = None
    """
    Borrowing details
    """

    product_details: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeProductDetails],
        FieldMetadata(alias="ProductDetails"),
        pydantic.Field(alias="ProductDetails"),
    ] = None
    repayment: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepayment],
        FieldMetadata(alias="Repayment"),
        pydantic.Field(alias="Repayment", description="Repayment details of the Loan product"),
    ] = None
    """
    Repayment details of the Loan product
    """

    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1],
        FieldMetadata(alias="SupplementaryData"),
        pydantic.Field(alias="SupplementaryData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
