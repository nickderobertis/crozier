

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_page_settings_response_open_graph import UpdatePageSettingsResponseOpenGraph
from .update_page_settings_response_seo import UpdatePageSettingsResponseSeo


class UpdatePageSettingsResponse(UniversalBaseModel):
    """
    The Page object
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the Page
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="Unique identifier for the Site"),
    ] = None
    """
    Unique identifier for the Site
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the Page
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    slug of the Page (derived from title)
    """

    parent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentId"),
        pydantic.Field(alias="parentId", description="Identifier of the parent folder"),
    ] = None
    """
    Identifier of the parent folder
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Unique identifier for a linked Collection, value will be null if the Page is not part of a Collection.",
        ),
    ] = None
    """
    Unique identifier for a linked Collection, value will be null if the Page is not part of a Collection.
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the Page was created"),
    ] = None
    """
    The date the Page was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the Page was most recently updated"),
    ] = None
    """
    The date the Page was most recently updated
    """

    archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the Page has been archived
    """

    draft: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the Page is a draft
    """

    can_branch: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canBranch"),
        pydantic.Field(
            alias="canBranch",
            description="Indicates whether the Page supports [Page Branching](https://university.webflow.com/lesson/page-branching). Pages that are already branches cannot be branched again.",
        ),
    ] = None
    """
    Indicates whether the Page supports [Page Branching](https://university.webflow.com/lesson/page-branching). Pages that are already branches cannot be branched again.
    """

    is_branch: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isBranch"),
        pydantic.Field(
            alias="isBranch",
            description="Indicates whether the Page is a Branch of another Page [Page Branching](https://university.webflow.com/lesson/page-branching)",
        ),
    ] = None
    """
    Indicates whether the Page is a Branch of another Page [Page Branching](https://university.webflow.com/lesson/page-branching)
    """

    branch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="branchId"),
        pydantic.Field(
            alias="branchId", description="If the Page is a Branch of another Page, this is the ID of the Branch"
        ),
    ] = None
    """
    If the Page is a Branch of another Page, this is the ID of the Branch
    """

    seo: typing.Optional[UpdatePageSettingsResponseSeo] = pydantic.Field(default=None)
    """
    SEO-related fields for the Page
    """

    open_graph: typing_extensions.Annotated[
        typing.Optional[UpdatePageSettingsResponseOpenGraph],
        FieldMetadata(alias="openGraph"),
        pydantic.Field(alias="openGraph", description="Open Graph fields for the Page"),
    ] = None
    """
    Open Graph fields for the Page
    """

    locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localeId"),
        pydantic.Field(alias="localeId", description="Unique ID of the page locale"),
    ] = None
    """
    Unique ID of the page locale
    """

    published_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publishedPath"),
        pydantic.Field(alias="publishedPath", description="Relative path of the published page URL"),
    ] = None
    """
    Relative path of the published page URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
