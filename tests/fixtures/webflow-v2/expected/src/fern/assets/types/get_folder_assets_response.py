

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetFolderAssetsResponse(UniversalBaseModel):
    """
    Asset Folder details
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the Asset Folder
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="User visible name for the Asset Folder"),
    ] = None
    """
    User visible name for the Asset Folder
    """

    parent_folder: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentFolder"),
        pydantic.Field(alias="parentFolder", description="Pointer to parent Asset Folder (or null if root)"),
    ] = None
    """
    Pointer to parent Asset Folder (or null if root)
    """

    assets: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of Asset instances in the folder
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The unique ID of the site the Asset Folder belongs to"),
    ] = None
    """
    The unique ID of the site the Asset Folder belongs to
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date that the Asset Folder was created on"),
    ] = None
    """
    Date that the Asset Folder was created on
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date that the Asset Folder was last updated on"),
    ] = None
    """
    Date that the Asset Folder was last updated on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
