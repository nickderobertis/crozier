

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.workspace_file_delete_response import WorkspaceFileDeleteResponse
from ..types.workspace_file_entry_response import WorkspaceFileEntryResponse
from ..types.workspace_file_list_response import WorkspaceFileListResponse
from ..types.workspace_file_read_response import WorkspaceFileReadResponse
from .raw_client import AsyncRawWorkspaceFilesClient, RawWorkspaceFilesClient


OMIT = typing.cast(typing.Any, ...)


class WorkspaceFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceFilesClient
        """
        return self._raw_client

    def list_workspace_files_api(
        self,
        *,
        path: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileListResponse:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Workspace-relative path

        limit : typing.Optional[int]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.list_workspace_files_api()
        """
        _response = self._raw_client.list_workspace_files_api(
            path=path, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    def stat_workspace_file_api(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.stat_workspace_file_api(
            path="path",
        )
        """
        _response = self._raw_client.stat_workspace_file_api(path=path, request_options=request_options)
        return _response.data

    def read_workspace_file_api(
        self,
        *,
        path: str,
        cursor: typing.Optional[str] = None,
        max_chars: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileReadResponse:
        """
        Parameters
        ----------
        path : str

        cursor : typing.Optional[str]

        max_chars : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileReadResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.read_workspace_file_api(
            path="path",
        )
        """
        _response = self._raw_client.read_workspace_file_api(
            path=path, cursor=cursor, max_chars=max_chars, request_options=request_options
        )
        return _response.data

    def write_workspace_file_api(
        self,
        *,
        path: str,
        content: str,
        overwrite: bool,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        content : str

        overwrite : bool

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.write_workspace_file_api(
            path="path",
            content="content",
            overwrite=True,
        )
        """
        _response = self._raw_client.write_workspace_file_api(
            path=path,
            content=content,
            overwrite=overwrite,
            expected_sha256=expected_sha256,
            request_options=request_options,
        )
        return _response.data

    def delete_workspace_file_api(
        self,
        *,
        path: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileDeleteResponse:
        """
        Parameters
        ----------
        path : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileDeleteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.delete_workspace_file_api(
            path="path",
        )
        """
        _response = self._raw_client.delete_workspace_file_api(
            path=path, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data

    def patch_workspace_file_api(
        self,
        *,
        path: str,
        old: str,
        new: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        old : str

        new : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.patch_workspace_file_api(
            path="path",
            old="old",
            new="new",
        )
        """
        _response = self._raw_client.patch_workspace_file_api(
            path=path, old=old, new=new, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data

    def append_workspace_file_api(
        self,
        *,
        path: str,
        content: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        content : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_files.append_workspace_file_api(
            path="path",
            content="content",
        )
        """
        _response = self._raw_client.append_workspace_file_api(
            path=path, content=content, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data


class AsyncWorkspaceFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceFilesClient
        """
        return self._raw_client

    async def list_workspace_files_api(
        self,
        *,
        path: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileListResponse:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Workspace-relative path

        limit : typing.Optional[int]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.list_workspace_files_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workspace_files_api(
            path=path, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    async def stat_workspace_file_api(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.stat_workspace_file_api(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stat_workspace_file_api(path=path, request_options=request_options)
        return _response.data

    async def read_workspace_file_api(
        self,
        *,
        path: str,
        cursor: typing.Optional[str] = None,
        max_chars: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileReadResponse:
        """
        Parameters
        ----------
        path : str

        cursor : typing.Optional[str]

        max_chars : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileReadResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.read_workspace_file_api(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_workspace_file_api(
            path=path, cursor=cursor, max_chars=max_chars, request_options=request_options
        )
        return _response.data

    async def write_workspace_file_api(
        self,
        *,
        path: str,
        content: str,
        overwrite: bool,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        content : str

        overwrite : bool

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.write_workspace_file_api(
                path="path",
                content="content",
                overwrite=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_workspace_file_api(
            path=path,
            content=content,
            overwrite=overwrite,
            expected_sha256=expected_sha256,
            request_options=request_options,
        )
        return _response.data

    async def delete_workspace_file_api(
        self,
        *,
        path: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileDeleteResponse:
        """
        Parameters
        ----------
        path : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileDeleteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.delete_workspace_file_api(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace_file_api(
            path=path, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data

    async def patch_workspace_file_api(
        self,
        *,
        path: str,
        old: str,
        new: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        old : str

        new : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.patch_workspace_file_api(
                path="path",
                old="old",
                new="new",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_workspace_file_api(
            path=path, old=old, new=new, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data

    async def append_workspace_file_api(
        self,
        *,
        path: str,
        content: str,
        expected_sha256: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceFileEntryResponse:
        """
        Parameters
        ----------
        path : str

        content : str

        expected_sha256 : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceFileEntryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace_files.append_workspace_file_api(
                path="path",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_workspace_file_api(
            path=path, content=content, expected_sha256=expected_sha256, request_options=request_options
        )
        return _response.data
