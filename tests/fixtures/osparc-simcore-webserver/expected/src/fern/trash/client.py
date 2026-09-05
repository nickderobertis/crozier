

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTrashClient, RawTrashClient


class TrashClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrashClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrashClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrashClient
        """
        return self._raw_client

    def empty_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.empty_trash()
        """
        _response = self._raw_client.empty_trash(request_options=request_options)
        return _response.data

    def project(
        self,
        project_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.project(project_id, force=force, request_options=request_options)
        return _response.data

    def untrash_project(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.untrash_project(
            project_id="project_id",
        )
        """
        _response = self._raw_client.untrash_project(project_id, request_options=request_options)
        return _response.data

    def folder(
        self,
        folder_id: int,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        folder_id : int

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.folder(
            folder_id=1,
        )
        """
        _response = self._raw_client.folder(folder_id, force=force, request_options=request_options)
        return _response.data

    def untrash_folder(self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.trash.untrash_folder(
            folder_id=1,
        )
        """
        _response = self._raw_client.untrash_folder(folder_id, request_options=request_options)
        return _response.data

    def workspace(
        self,
        workspace_id: int,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : int

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.workspace(
            workspace_id=1,
        )
        """
        _response = self._raw_client.workspace(workspace_id, force=force, request_options=request_options)
        return _response.data

    def untrash_workspace(self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        workspace_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trash.untrash_workspace(
            workspace_id=1,
        )
        """
        _response = self._raw_client.untrash_workspace(workspace_id, request_options=request_options)
        return _response.data


class AsyncTrashClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrashClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrashClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrashClient
        """
        return self._raw_client

    async def empty_trash(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.trash.empty_trash()


        asyncio.run(main())
        """
        _response = await self._raw_client.empty_trash(request_options=request_options)
        return _response.data

    async def project(
        self,
        project_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        force : typing.Optional[bool]

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
            await client.trash.project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.project(project_id, force=force, request_options=request_options)
        return _response.data

    async def untrash_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

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
            await client.trash.untrash_project(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.untrash_project(project_id, request_options=request_options)
        return _response.data

    async def folder(
        self,
        folder_id: int,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        folder_id : int

        force : typing.Optional[bool]

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
            await client.trash.folder(
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.folder(folder_id, force=force, request_options=request_options)
        return _response.data

    async def untrash_folder(self, folder_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.trash.untrash_folder(
                folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.untrash_folder(folder_id, request_options=request_options)
        return _response.data

    async def workspace(
        self,
        workspace_id: int,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : int

        force : typing.Optional[bool]

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
            await client.trash.workspace(
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace(workspace_id, force=force, request_options=request_options)
        return _response.data

    async def untrash_workspace(
        self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : int

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
            await client.trash.untrash_workspace(
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.untrash_workspace(workspace_id, request_options=request_options)
        return _response.data
