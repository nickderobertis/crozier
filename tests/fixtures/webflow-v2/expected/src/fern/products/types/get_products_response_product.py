

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_products_response_product_field_data import GetProductsResponseProductFieldData


class GetProductsResponseProduct(UniversalBaseModel):
    """
    The Product object
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

    is_archived: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isArchived"),
        pydantic.Field(alias="isArchived", description="Boolean determining if the Product is set to archived"),
    ] = None
    """
    Boolean determining if the Product is set to archived
    """

    is_draft: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDraft"),
        pydantic.Field(alias="isDraft", description="Boolean determining if the Product is set to draft"),
    ] = None
    """
    Boolean determining if the Product is set to draft
    """

    field_data: typing_extensions.Annotated[
        typing.Optional[GetProductsResponseProductFieldData],
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
