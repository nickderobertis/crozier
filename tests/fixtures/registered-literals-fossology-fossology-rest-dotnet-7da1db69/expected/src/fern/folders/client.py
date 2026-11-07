

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.folder import Folder
from ..types.get_folder_content import GetFolderContent
from ..types.info import Info
from .raw_client import AsyncRawFoldersClient, RawFoldersClient


class FoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFoldersClient
        """
        return self._raw_client

    def get_folders(
        self, *, group_name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Get all folders or from a specific group

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            List of folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.get_folders()
        """
        _response = self._raw_client.get_folders(group_name=group_name, request_options=request_options)
        return _response.data

    def get_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Get a single folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Details of the required folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.get_folder_by_id(
            id=1,
        )
        """
        _response = self._raw_client.get_folder_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    def unlink_content(self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Unlink a content from a folder

        Parameters
        ----------
        content_id : int
            ID of the content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Content is unlinked from the folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.unlink_content(
            content_id=1,
        )
        """
        _response = self._raw_client.unlink_content(content_id, request_options=request_options)
        return _response.data

    def get_all_folder_contents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetFolderContent]:
        """
        Get all contents of a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetFolderContent]
            Contents of the given folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.get_all_folder_contents(
            id=1,
        )
        """
        _response = self._raw_client.get_all_folder_contents(id, request_options=request_options)
        return _response.data

    def get_unlinkable_contents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFolderContent:
        """
        Get unlinkable contents of a folder by id. These contents are copied.

        Parameters
        ----------
        id : int
            ID of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderContent
            Unlinkable contents of the given folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.get_unlinkable_contents(
            id=1,
        )
        """
        _response = self._raw_client.get_unlinkable_contents(id, request_options=request_options)
        return _response.data


class AsyncFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFoldersClient
        """
        return self._raw_client

    async def get_folders(
        self, *, group_name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Get all folders or from a specific group

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            List of folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.get_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folders(group_name=group_name, request_options=request_options)
        return _response.data

    async def get_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Get a single folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Details of the required folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.get_folder_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    async def unlink_content(self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Unlink a content from a folder

        Parameters
        ----------
        content_id : int
            ID of the content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Content is unlinked from the folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.unlink_content(
                content_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlink_content(content_id, request_options=request_options)
        return _response.data

    async def get_all_folder_contents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetFolderContent]:
        """
        Get all contents of a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetFolderContent]
            Contents of the given folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.get_all_folder_contents(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_folder_contents(id, request_options=request_options)
        return _response.data

    async def get_unlinkable_contents(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFolderContent:
        """
        Get unlinkable contents of a folder by id. These contents are copied.

        Parameters
        ----------
        id : int
            ID of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFolderContent
            Unlinkable contents of the given folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.get_unlinkable_contents(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_unlinkable_contents(id, request_options=request_options)
        return _response.data
