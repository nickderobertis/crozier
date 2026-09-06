

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_products_request_product_field_data import CreateProductsRequestProductFieldData


class CreateProductsRequestProduct(UniversalBaseModel):
    field_data: typing_extensions.Annotated[
        typing.Optional[CreateProductsRequestProductFieldData],
        FieldMetadata(alias="fieldData"),
        pydantic.Field(
            alias="fieldData",
            description="Contains content-specific details for a product, covering both standard (e.g., title, description) and custom fields tailored to the product setup.",
        ),
    ] = None
    """
    Contains content-specific details for a product, covering both standard (e.g., title, description) and custom fields tailored to the product setup.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
