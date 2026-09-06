

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .create_items_items_response_field_data import CreateItemsItemsResponseFieldData


class CreateItemsItemsResponse(UniversalBaseModel):
    """
    The fields that define the schema for a given Item are based on the Collection that Item belongs to. Beyond the user defined fields, there are a handful of additional fields that are automatically created for all items
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the Item
    """

    cms_locale_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="cmsLocaleIds"),
        pydantic.Field(
            alias="cmsLocaleIds", description="Array of identifiers for the locales where the item will be created"
        ),
    ]
    """
    Array of identifiers for the locales where the item will be created
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
        bool,
        FieldMetadata(alias="isArchived"),
        pydantic.Field(alias="isArchived", description="Boolean determining if the Item is set to archived"),
    ]
    """
    Boolean determining if the Item is set to archived
    """

    is_draft: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isDraft"),
        pydantic.Field(
            alias="isDraft",
            description="Whether the item is created in a draft state. A new item has never been published, so `isDraft: true` gives it a `Draft` status. Set `isDraft: false` to queue the item to publish on the next site publish.",
        ),
    ]
    """
    Whether the item is created in a draft state. A new item has never been published, so `isDraft: true` gives it a `Draft` status. Set `isDraft: false` to queue the item to publish on the next site publish.
    """

    field_data: typing_extensions.Annotated[
        CreateItemsItemsResponseFieldData, FieldMetadata(alias="fieldData"), pydantic.Field(alias="fieldData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
