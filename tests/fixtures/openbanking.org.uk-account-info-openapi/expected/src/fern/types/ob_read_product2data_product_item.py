

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .ob_read_product2data_product_item_other_product_type import ObReadProduct2DataProductItemOtherProductType
from .ob_read_product2data_product_item_product_type import ObReadProduct2DataProductItemProductType
from .obbca_data1 import ObbcaData1
from .obpca_data1 import ObpcaData1


class ObReadProduct2DataProductItem(UniversalBaseModel):
    """
    Product details associated with the Account
    """

    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    bca: typing_extensions.Annotated[
        typing.Optional[ObbcaData1], FieldMetadata(alias="BCA"), pydantic.Field(alias="BCA")
    ] = None
    marketing_state_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MarketingStateId"),
        pydantic.Field(
            alias="MarketingStateId", description="Unique and unambiguous identification of a  Product Marketing State."
        ),
    ] = None
    """
    Unique and unambiguous identification of a  Product Marketing State.
    """

    other_product_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductType],
        FieldMetadata(alias="OtherProductType"),
        pydantic.Field(alias="OtherProductType", description="Other product type details associated with the account."),
    ] = None
    """
    Other product type details associated with the account.
    """

    pca: typing_extensions.Annotated[
        typing.Optional[ObpcaData1], FieldMetadata(alias="PCA"), pydantic.Field(alias="PCA")
    ] = None
    product_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ProductId"),
        pydantic.Field(
            alias="ProductId",
            description="The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers.",
        ),
    ] = None
    """
    The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers.
    """

    product_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ProductName"),
        pydantic.Field(
            alias="ProductName",
            description="The name of the Product used for marketing purposes from a customer perspective. I.e. what the customer would recognise.",
        ),
    ] = None
    """
    The name of the Product used for marketing purposes from a customer perspective. I.e. what the customer would recognise.
    """

    product_type: typing_extensions.Annotated[
        ObReadProduct2DataProductItemProductType,
        FieldMetadata(alias="ProductType"),
        pydantic.Field(
            alias="ProductType", description="Product type : Personal Current Account, Business Current Account"
        ),
    ]
    """
    Product type : Personal Current Account, Business Current Account
    """

    secondary_product_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SecondaryProductId"),
        pydantic.Field(
            alias="SecondaryProductId",
            description="Any secondary Identification which  supports Product Identifier to uniquely identify the current account banking products.",
        ),
    ] = None
    """
    Any secondary Identification which  supports Product Identifier to uniquely identify the current account banking products.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
