

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_items_items_request_items_item_field_data import UpdateItemsItemsRequestItemsItemFieldData


class UpdateItemsItemsRequestItemsItem(UniversalBaseModel):
    """
    The fields that define the schema for a given Item are based on the Collection that Item belongs to. Beyond the user defined fields, there are a handful of additional fields that are automatically created for all items
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the Item
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
        typing.Optional[str],
        FieldMetadata(alias="lastPublished"),
        pydantic.Field(alias="lastPublished", description="The date the item was last published"),
    ] = None
    """
    The date the item was last published
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the item was last updated"),
    ] = None
    """
    The date the item was last updated
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the item was created"),
    ] = None
    """
    The date the item was created
    """

    is_archived: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isArchived"),
        pydantic.Field(alias="isArchived", description="Boolean determining if the Item is set to archived"),
    ] = None
    """
    Boolean determining if the Item is set to archived
    """

    is_draft: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDraft"),
        pydantic.Field(
            alias="isDraft",
            description="Sets the item's draft state. The resulting status depends on whether the item has been published before:\n\n- **Item that has never been published:** `isDraft: true` results in a `Draft` status.\n- **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.\n\nSetting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).",
        ),
    ] = None
    """
    Sets the item's draft state. The resulting status depends on whether the item has been published before:
    
    - **Item that has never been published:** `isDraft: true` results in a `Draft` status.
    - **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.
    
    Setting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).
    """

    field_data: typing_extensions.Annotated[
        typing.Optional[UpdateItemsItemsRequestItemsItemFieldData],
        FieldMetadata(alias="fieldData"),
        pydantic.Field(alias="fieldData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
