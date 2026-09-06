

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsClient, RawAssetsClient
from .types.create_assets_response import CreateAssetsResponse
from .types.create_folder_assets_response import CreateFolderAssetsResponse
from .types.get_assets_response import GetAssetsResponse
from .types.get_folder_assets_response import GetFolderAssetsResponse
from .types.list_assets_response import ListAssetsResponse
from .types.list_folders_assets_response import ListFoldersAssetsResponse
from .types.update_assets_response import UpdateAssetsResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsClient
        """
        return self._raw_client

    def list(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssetsResponse:
        """
        List of assets uploaded to a site

        Required scope | `assets:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        folder_id : typing.Optional[str]
            Filter assets to those in the specified folder and all descendant folders.
            Must be a 24-character hex ObjectId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.list(
            site_id="580e63e98c9a982ac9b8b741",
            locale_id="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.list(
            site_id,
            locale_id=locale_id,
            offset=offset,
            limit=limit,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        parent_folder: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAssetsResponse:
        """
        The first step in uploading an asset to a site.


        This endpoint generates a response with the following information: `uploadUrl` and `uploadDetails`.


        Use these properties in the header of a [POST request to Amazson s3](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html) to complete the upload.


        To learn more about how to upload assets to Webflow, see our [assets guide](/data/docs/working-with-assets).

         Required scope | `assets:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including file extension. File names must be less than 100 characters.

        file_hash : str
            MD5 hash of the file

        parent_folder : typing.Optional[str]
            ID of the Asset folder (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.create(
            site_id="580e63e98c9a982ac9b8b741",
            file_name="file.png",
            file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
        )
        """
        _response = self._raw_client.create(
            site_id,
            file_name=file_name,
            file_hash=file_hash,
            parent_folder=parent_folder,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        asset_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAssetsResponse:
        """
        Get details about an asset

        Required scope | `assets:read`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.get(
            asset_id="580e63fc8c9a982ac9b8b745",
            locale_id="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.get(asset_id, locale_id=locale_id, request_options=request_options)
        return _response.data

    def delete(self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an Asset

        Required Scope: `assets: write`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.delete(
            asset_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.delete(asset_id, request_options=request_options)
        return _response.data

    def update(
        self,
        asset_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        display_name: typing.Optional[str] = OMIT,
        alt_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAssetsResponse:
        """
        Update details of an Asset.

        Required scope | `assets:write`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        display_name : typing.Optional[str]
            A human readable name for the asset. This value is not localizable.

        alt_text : typing.Optional[str]
            Alternate text describing the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.update(
            asset_id="580e63fc8c9a982ac9b8b745",
            locale_id="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.update(
            asset_id, locale_id=locale_id, display_name=display_name, alt_text=alt_text, request_options=request_options
        )
        return _response.data

    def list_folders(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFoldersAssetsResponse:
        """
        List Asset Folders within a given site

        Required scope | `assets:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFoldersAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.list_folders(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list_folders(site_id, request_options=request_options)
        return _response.data

    def create_folder(
        self,
        site_id: str,
        *,
        display_name: str,
        parent_folder: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFolderAssetsResponse:
        """
        Create an Asset Folder within a given site

        Required scope | `assets:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            A human readable name for the Asset Folder

        parent_folder : typing.Optional[str]
            An (optional) pointer to a parent Asset Folder (or null for root)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFolderAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.create_folder(
            site_id="580e63e98c9a982ac9b8b741",
            display_name="my asset folder",
        )
        """
        _response = self._raw_client.create_folder(
            site_id, display_name=display_name, parent_folder=parent_folder, request_options=request_options
        )
        return _response.data

    def get_folder(
        self, asset_folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFolderAssetsResponse:
        """
        Get details about a specific Asset Folder

        Required scope | `assets:read`

        Parameters
        ----------
        asset_folder_id : str
            Unique identifier for an Asset Folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderAssetsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assets.get_folder(
            asset_folder_id="6390c49774a71f0e3c1a08ee",
        )
        """
        _response = self._raw_client.get_folder(asset_folder_id, request_options=request_options)
        return _response.data


class AsyncAssetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsClient
        """
        return self._raw_client

    async def list(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssetsResponse:
        """
        List of assets uploaded to a site

        Required scope | `assets:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        folder_id : typing.Optional[str]
            Filter assets to those in the specified folder and all descendant folders.
            Must be a 24-character hex ObjectId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.list(
                site_id="580e63e98c9a982ac9b8b741",
                locale_id="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            site_id,
            locale_id=locale_id,
            offset=offset,
            limit=limit,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        parent_folder: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAssetsResponse:
        """
        The first step in uploading an asset to a site.


        This endpoint generates a response with the following information: `uploadUrl` and `uploadDetails`.


        Use these properties in the header of a [POST request to Amazson s3](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html) to complete the upload.


        To learn more about how to upload assets to Webflow, see our [assets guide](/data/docs/working-with-assets).

         Required scope | `assets:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including file extension. File names must be less than 100 characters.

        file_hash : str
            MD5 hash of the file

        parent_folder : typing.Optional[str]
            ID of the Asset folder (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.create(
                site_id="580e63e98c9a982ac9b8b741",
                file_name="file.png",
                file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id,
            file_name=file_name,
            file_hash=file_hash,
            parent_folder=parent_folder,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        asset_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAssetsResponse:
        """
        Get details about an asset

        Required scope | `assets:read`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.get(
                asset_id="580e63fc8c9a982ac9b8b745",
                locale_id="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(asset_id, locale_id=locale_id, request_options=request_options)
        return _response.data

    async def delete(self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an Asset

        Required Scope: `assets: write`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.delete(
                asset_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(asset_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        asset_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        display_name: typing.Optional[str] = OMIT,
        alt_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAssetsResponse:
        """
        Update details of an Asset.

        Required scope | `assets:write`

        Parameters
        ----------
        asset_id : str
            Unique identifier for an Asset on a site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        display_name : typing.Optional[str]
            A human readable name for the asset. This value is not localizable.

        alt_text : typing.Optional[str]
            Alternate text describing the image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.update(
                asset_id="580e63fc8c9a982ac9b8b745",
                locale_id="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            asset_id, locale_id=locale_id, display_name=display_name, alt_text=alt_text, request_options=request_options
        )
        return _response.data

    async def list_folders(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFoldersAssetsResponse:
        """
        List Asset Folders within a given site

        Required scope | `assets:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFoldersAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.list_folders(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folders(site_id, request_options=request_options)
        return _response.data

    async def create_folder(
        self,
        site_id: str,
        *,
        display_name: str,
        parent_folder: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFolderAssetsResponse:
        """
        Create an Asset Folder within a given site

        Required scope | `assets:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            A human readable name for the Asset Folder

        parent_folder : typing.Optional[str]
            An (optional) pointer to a parent Asset Folder (or null for root)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFolderAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.create_folder(
                site_id="580e63e98c9a982ac9b8b741",
                display_name="my asset folder",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_folder(
            site_id, display_name=display_name, parent_folder=parent_folder, request_options=request_options
        )
        return _response.data

    async def get_folder(
        self, asset_folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFolderAssetsResponse:
        """
        Get details about a specific Asset Folder

        Required scope | `assets:read`

        Parameters
        ----------
        asset_folder_id : str
            Unique identifier for an Asset Folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderAssetsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assets.get_folder(
                asset_folder_id="6390c49774a71f0e3c1a08ee",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder(asset_folder_id, request_options=request_options)
        return _response.data
