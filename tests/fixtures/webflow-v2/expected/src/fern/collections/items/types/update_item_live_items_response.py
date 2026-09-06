

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_item_live_items_response_field_data import UpdateItemLiveItemsResponseFieldData


class UpdateItemLiveItemsResponse(UniversalBaseModel):
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
            description="Whether the item is in a draft state. Together with `lastPublished`, this determines the status shown in the Webflow UI. See [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing) for the full mapping.",
        ),
    ] = None
    """
    Whether the item is in a draft state. Together with `lastPublished`, this determines the status shown in the Webflow UI. See [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing) for the full mapping.
    """

    field_data: typing_extensions.Annotated[
        UpdateItemLiveItemsResponseFieldData, FieldMetadata(alias="fieldData"), pydantic.Field(alias="fieldData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
