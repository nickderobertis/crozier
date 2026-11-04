

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.folder import Folder
from .raw_client import AsyncRawFolderResourceClient, RawFolderResourceClient
from .types.post_folders_request_parent import PostFoldersRequestParent


OMIT = typing.cast(typing.Any, ...)


class FolderResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFolderResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFolderResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFolderResourceClient
        """
        return self._raw_client

    def get_folders(
        self, *, parent: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Retrieve a list of folders

        Parameters
        ----------
        parent : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            The list of folders

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.folder_resource.get_folders()
        """
        _response = self._raw_client.get_folders(parent=parent, request_options=request_options)
        return _response.data

    def post_folders(
        self,
        *,
        name: str,
        parent: typing.Optional[PostFoldersRequestParent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Create a new folder

        Parameters
        ----------
        name : str

        parent : typing.Optional[PostFoldersRequestParent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Created folder

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.folder_resource.post_folders(
            name="name",
        )
        """
        _response = self._raw_client.post_folders(name=name, parent=parent, request_options=request_options)
        return _response.data

    def delete_folders_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a folder

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.folder_resource.delete_folders_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_folders_id(id, request_options=request_options)
        return _response.data


class AsyncFolderResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFolderResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFolderResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFolderResourceClient
        """
        return self._raw_client

    async def get_folders(
        self, *, parent: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Folder]:
        """
        Retrieve a list of folders

        Parameters
        ----------
        parent : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            The list of folders

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.folder_resource.get_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folders(parent=parent, request_options=request_options)
        return _response.data

    async def post_folders(
        self,
        *,
        name: str,
        parent: typing.Optional[PostFoldersRequestParent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Create a new folder

        Parameters
        ----------
        name : str

        parent : typing.Optional[PostFoldersRequestParent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Created folder

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.folder_resource.post_folders(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_folders(name=name, parent=parent, request_options=request_options)
        return _response.data

    async def delete_folders_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a folder

        Parameters
        ----------
        id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.folder_resource.delete_folders_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folders_id(id, request_options=request_options)
        return _response.data
