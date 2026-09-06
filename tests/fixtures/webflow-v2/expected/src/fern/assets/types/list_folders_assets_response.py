

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_folders_assets_response_asset_folders_item import ListFoldersAssetsResponseAssetFoldersItem
from .list_folders_assets_response_pagination import ListFoldersAssetsResponsePagination


class ListFoldersAssetsResponse(UniversalBaseModel):
    """
    The Asset Folders object
    """

    asset_folders: typing_extensions.Annotated[
        typing.Optional[typing.List[ListFoldersAssetsResponseAssetFoldersItem]],
        FieldMetadata(alias="assetFolders"),
        pydantic.Field(alias="assetFolders", description="A list of Asset folders"),
    ] = None
    """
    A list of Asset folders
    """

    pagination: typing.Optional[ListFoldersAssetsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
