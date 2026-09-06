

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .multiple_items_items_item_field_data import MultipleItemsItemsItemFieldData


class MultipleItemsItemsItem(UniversalBaseModel):
    """
    A Collection Item represents a single entry in your collection. Each item includes:

    - **System metadata** - Automatically managed fields like IDs and timestamp <br/>
    - **Status flags** - Controls for managing content state: `isDraft`, `isArchived `<br/>
    - **Content fields** - Stored in `fieldData`. Each item needs a `name` and `slug`, and may include additional fields matching your collection's schema definition.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
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
        pydantic.Field(alias="isArchived", description="Boolean determining if the Item is in an archived state."),
    ] = None
    """
    Boolean determining if the Item is in an archived state.
    """

    is_draft: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDraft"),
        pydantic.Field(
            alias="isDraft",
            description="Whether the item is created in a draft state. A new item has never been published, so `isDraft: true` gives it a `Draft` status. Set `isDraft: false` to queue the item to publish on the next site publish.",
        ),
    ] = None
    """
    Whether the item is created in a draft state. A new item has never been published, so `isDraft: true` gives it a `Draft` status. Set `isDraft: false` to queue the item to publish on the next site publish.
    """

    field_data: typing_extensions.Annotated[
        MultipleItemsItemsItemFieldData, FieldMetadata(alias="fieldData"), pydantic.Field(alias="fieldData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
