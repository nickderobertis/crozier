

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_products_request_sku_field_data import CreateProductsRequestSkuFieldData


class CreateProductsRequestSku(UniversalBaseModel):
    field_data: typing_extensions.Annotated[
        typing.Optional[CreateProductsRequestSkuFieldData],
        FieldMetadata(alias="fieldData"),
        pydantic.Field(alias="fieldData", description="Standard and Custom fields for a SKU"),
    ] = None
    """
    Standard and Custom fields for a SKU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
