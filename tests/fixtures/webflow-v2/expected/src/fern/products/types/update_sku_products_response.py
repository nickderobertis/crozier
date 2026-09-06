

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_sku_products_response_field_data import UpdateSkuProductsResponseFieldData


class UpdateSkuProductsResponse(UniversalBaseModel):
    """
    The SKU object
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the Product
    """

    cms_locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cmsLocaleId"),
        pydantic.Field(alias="cmsLocaleId", description="Identifier for the locale of the CMS item"),
    ] = None
    """
    Identifier for the locale of the CMS item
    """

    last_published: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastPublished"),
        pydantic.Field(alias="lastPublished", description="The date the Product was last published"),
    ] = None
    """
    The date the Product was last published
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the Product was last updated"),
    ] = None
    """
    The date the Product was last updated
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the Product was created"),
    ] = None
    """
    The date the Product was created
    """

    field_data: typing_extensions.Annotated[
        UpdateSkuProductsResponseFieldData,
        FieldMetadata(alias="fieldData"),
        pydantic.Field(alias="fieldData", description="Standard and Custom fields for a SKU"),
    ]
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
