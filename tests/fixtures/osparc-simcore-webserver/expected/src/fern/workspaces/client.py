

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_workspace_get import EnvelopeListWorkspaceGet
from ..types.envelope_list_workspace_group_get import EnvelopeListWorkspaceGroupGet
from ..types.envelope_workspace_get import EnvelopeWorkspaceGet
from ..types.envelope_workspace_group_get import EnvelopeWorkspaceGroupGet
from ..types.group_id_int import GroupIdInt
from .raw_client import AsyncRawWorkspacesClient, RawWorkspacesClient


OMIT = typing.cast(typing.Any, ...)


class WorkspacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspacesClient
        """
        return self._raw_client

    def list_workspaces(
        self,
        *,
        order_by: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListWorkspaceGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWorkspaceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.list_workspaces()
        """
        _response = self._raw_client.list_workspaces(
            order_by=order_by, filters=filters, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_workspace(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.create_workspace(
            name="name",
        )
        """
        _response = self._raw_client.create_workspace(
            name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    def get_workspace(
        self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        workspace_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.get_workspace(
            workspace_id=1,
        )
        """
        _response = self._raw_client.get_workspace(workspace_id, request_options=request_options)
        return _response.data

    def replace_workspace(
        self,
        workspace_id: int,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        workspace_id : int

        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.replace_workspace(
            workspace_id=1,
            name="name",
        )
        """
        _response = self._raw_client.replace_workspace(
            workspace_id, name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    def delete_workspace(self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.workspaces.delete_workspace(
            workspace_id=1,
        )
        """
        _response = self._raw_client.delete_workspace(workspace_id, request_options=request_options)
        return _response.data

    def create_workspace_group(
        self,
        workspace_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.create_workspace_group(
            workspace_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.create_workspace_group(
            workspace_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def replace_workspace_group(
        self,
        workspace_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.replace_workspace_group(
            workspace_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.replace_workspace_group(
            workspace_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def delete_workspace_group(
        self, workspace_id: int, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.delete_workspace_group(
            workspace_id=1,
            group_id=1,
        )
        """
        _response = self._raw_client.delete_workspace_group(workspace_id, group_id, request_options=request_options)
        return _response.data

    def list_workspace_groups(
        self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWorkspaceGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workspaces.list_workspace_groups(
            workspace_id=1,
        )
        """
        _response = self._raw_client.list_workspace_groups(workspace_id, request_options=request_options)
        return _response.data


class AsyncWorkspacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspacesClient
        """
        return self._raw_client

    async def list_workspaces(
        self,
        *,
        order_by: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListWorkspaceGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWorkspaceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.list_workspaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workspaces(
            order_by=order_by, filters=filters, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_workspace(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.create_workspace(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace(
            name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    async def get_workspace(
        self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        workspace_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.get_workspace(
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace(workspace_id, request_options=request_options)
        return _response.data

    async def replace_workspace(
        self,
        workspace_id: int,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGet:
        """
        Parameters
        ----------
        workspace_id : int

        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.replace_workspace(
                workspace_id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_workspace(
            workspace_id, name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    async def delete_workspace(
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
            await client.workspaces.delete_workspace(
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace(workspace_id, request_options=request_options)
        return _response.data

    async def create_workspace_group(
        self,
        workspace_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.create_workspace_group(
                workspace_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace_group(
            workspace_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def replace_workspace_group(
        self,
        workspace_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWorkspaceGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.replace_workspace_group(
                workspace_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_workspace_group(
            workspace_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def delete_workspace_group(
        self, workspace_id: int, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : int

        group_id : GroupIdInt

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
            await client.workspaces.delete_workspace_group(
                workspace_id=1,
                group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace_group(
            workspace_id, group_id, request_options=request_options
        )
        return _response.data

    async def list_workspace_groups(
        self, workspace_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWorkspaceGroupGet:
        """
        Parameters
        ----------
        workspace_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWorkspaceGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workspaces.list_workspace_groups(
                workspace_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workspace_groups(workspace_id, request_options=request_options)
        return _response.data
