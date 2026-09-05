

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.display_safe_str import DisplaySafeStr
from ..types.envelope_folder_get import EnvelopeFolderGet
from ..types.envelope_list_folder_get import EnvelopeListFolderGet
from .raw_client import AsyncRawFoldersClient, RawFoldersClient


OMIT = typing.cast(typing.Any, ...)


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

    def list_folders(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFolderGet:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFolderGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.list_folders()
        """
        _response = self._raw_client.list_folders(
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            folder_id=folder_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def create_folder(
        self,
        *,
        name: DisplaySafeStr,
        parent_folder_id: typing.Optional[int] = OMIT,
        workspace_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        name : DisplaySafeStr

        parent_folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.create_folder(
            name="name",
        )
        """
        _response = self._raw_client.create_folder(
            name=name, parent_folder_id=parent_folder_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def list_folders_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFolderGet:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFolderGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.list_folders_full_search()
        """
        _response = self._raw_client.list_folders_full_search(
            filters=filters, order_by=order_by, limit=limit, offset=offset, text=text, request_options=request_options
        )
        return _response.data

    def get_folder(
        self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        folder_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.get_folder(
            folder_id=1,
        )
        """
        _response = self._raw_client.get_folder(folder_id, request_options=request_options)
        return _response.data

    def replace_folder(
        self,
        folder_id: int,
        *,
        name: DisplaySafeStr,
        parent_folder_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        folder_id : int

        name : DisplaySafeStr

        parent_folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.replace_folder(
            folder_id=1,
            name="name",
        )
        """
        _response = self._raw_client.replace_folder(
            folder_id, name=name, parent_folder_id=parent_folder_id, request_options=request_options
        )
        return _response.data

    def delete_folder(self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        folder_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.delete_folder(
            folder_id=1,
        )
        """
        _response = self._raw_client.delete_folder(folder_id, request_options=request_options)
        return _response.data

    def move_folder_to_workspace(
        self,
        folder_id: int,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move folder to the workspace

        Parameters
        ----------
        folder_id : int

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folders.move_folder_to_workspace(
            folder_id=1,
            workspace_id=1,
        )
        """
        _response = self._raw_client.move_folder_to_workspace(folder_id, workspace_id, request_options=request_options)
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

    async def list_folders(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        folder_id: typing.Optional[int] = None,
        workspace_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFolderGet:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFolderGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.list_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folders(
            filters=filters,
            order_by=order_by,
            limit=limit,
            offset=offset,
            folder_id=folder_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def create_folder(
        self,
        *,
        name: DisplaySafeStr,
        parent_folder_id: typing.Optional[int] = OMIT,
        workspace_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        name : DisplaySafeStr

        parent_folder_id : typing.Optional[int]

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.create_folder(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_folder(
            name=name, parent_folder_id=parent_folder_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def list_folders_full_search(
        self,
        *,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFolderGet:
        """
        Parameters
        ----------
        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFolderGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.list_folders_full_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folders_full_search(
            filters=filters, order_by=order_by, limit=limit, offset=offset, text=text, request_options=request_options
        )
        return _response.data

    async def get_folder(
        self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        folder_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.get_folder(
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder(folder_id, request_options=request_options)
        return _response.data

    async def replace_folder(
        self,
        folder_id: int,
        *,
        name: DisplaySafeStr,
        parent_folder_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFolderGet:
        """
        Parameters
        ----------
        folder_id : int

        name : DisplaySafeStr

        parent_folder_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFolderGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.replace_folder(
                folder_id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_folder(
            folder_id, name=name, parent_folder_id=parent_folder_id, request_options=request_options
        )
        return _response.data

    async def delete_folder(self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        folder_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.delete_folder(
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder(folder_id, request_options=request_options)
        return _response.data

    async def move_folder_to_workspace(
        self,
        folder_id: int,
        workspace_id: typing.Optional[int],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Move folder to the workspace

        Parameters
        ----------
        folder_id : int

        workspace_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folders.move_folder_to_workspace(
                folder_id=1,
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_folder_to_workspace(
            folder_id, workspace_id, request_options=request_options
        )
        return _response.data
