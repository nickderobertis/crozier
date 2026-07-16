

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObMerchantDetails1(UniversalBaseModel):
    """
    Details of the merchant involved in the transaction.
    """

    merchant_category_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="MerchantCategoryCode")
    ] = pydantic.Field(default=None)
    """
    Category code conform to ISO 18245, related to the type of services or goods the merchant provides for the transaction.
    """

    merchant_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="MerchantName")] = (
        pydantic.Field(default=None)
    )
    """
    Name by which the merchant is known.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
