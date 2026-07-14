

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection_id import ConnectionId
from ..types.geography import Geography
from ..types.notification import Notification
from ..types.webhook_config_write import WebhookConfigWrite
from ..types.workspace_id import WorkspaceId
from ..types.workspace_read import WorkspaceRead
from ..types.workspace_read_list import WorkspaceReadList
from .raw_client import AsyncRawWorkspaceClient, RawWorkspaceClient


OMIT = typing.cast(typing.Any, ...)


class WorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceClient
        """
        return self._raw_client

    def create_workspace(
        self,
        *,
        name: str,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        name : str

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.create_workspace(
            name="name",
        )
        """
        _response = self._raw_client.create_workspace(
            name=name,
            anonymous_data_collection=anonymous_data_collection,
            default_geography=default_geography,
            display_setup_wizard=display_setup_wizard,
            email=email,
            news=news,
            notifications=notifications,
            security_updates=security_updates,
            webhook_configs=webhook_configs,
            request_options=request_options,
        )
        return _response.data

    def delete_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

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
        client.workspace.delete_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.delete_workspace(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def get_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.get_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_workspace(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def get_workspace_by_connection_id(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.get_workspace_by_connection_id(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_workspace_by_connection_id(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    def get_workspace_by_slug(
        self, *, slug: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.get_workspace_by_slug(
            slug="slug",
        )
        """
        _response = self._raw_client.get_workspace_by_slug(slug=slug, request_options=request_options)
        return _response.data

    def list_workspaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> WorkspaceReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.list_workspaces()
        """
        _response = self._raw_client.list_workspaces(request_options=request_options)
        return _response.data

    def update_workspace_feedback(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

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
        client.workspace.update_workspace_feedback(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.update_workspace_feedback(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def update_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        initial_setup_complete: typing.Optional[bool] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        initial_setup_complete : typing.Optional[bool]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.update_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.update_workspace(
            workspace_id=workspace_id,
            anonymous_data_collection=anonymous_data_collection,
            default_geography=default_geography,
            display_setup_wizard=display_setup_wizard,
            email=email,
            initial_setup_complete=initial_setup_complete,
            news=news,
            notifications=notifications,
            security_updates=security_updates,
            webhook_configs=webhook_configs,
            request_options=request_options,
        )
        return _response.data

    def update_workspace_name(
        self, *, name: str, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspace.update_workspace_name(
            name="name",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.update_workspace_name(
            name=name, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data


class AsyncWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceClient
        """
        return self._raw_client

    async def create_workspace(
        self,
        *,
        name: str,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        name : str

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.create_workspace(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace(
            name=name,
            anonymous_data_collection=anonymous_data_collection,
            default_geography=default_geography,
            display_setup_wizard=display_setup_wizard,
            email=email,
            news=news,
            notifications=notifications,
            security_updates=security_updates,
            webhook_configs=webhook_configs,
            request_options=request_options,
        )
        return _response.data

    async def delete_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

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
            await client.workspace.delete_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workspace(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def get_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.get_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def get_workspace_by_connection_id(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.get_workspace_by_connection_id(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_by_connection_id(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    async def get_workspace_by_slug(
        self, *, slug: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.get_workspace_by_slug(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_by_slug(slug=slug, request_options=request_options)
        return _response.data

    async def list_workspaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> WorkspaceReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.list_workspaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workspaces(request_options=request_options)
        return _response.data

    async def update_workspace_feedback(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

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
            await client.workspace.update_workspace_feedback(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workspace_feedback(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def update_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        initial_setup_complete: typing.Optional[bool] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        initial_setup_complete : typing.Optional[bool]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.update_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workspace(
            workspace_id=workspace_id,
            anonymous_data_collection=anonymous_data_collection,
            default_geography=default_geography,
            display_setup_wizard=display_setup_wizard,
            email=email,
            initial_setup_complete=initial_setup_complete,
            news=news,
            notifications=notifications,
            security_updates=security_updates,
            webhook_configs=webhook_configs,
            request_options=request_options,
        )
        return _response.data

    async def update_workspace_name(
        self, *, name: str, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceRead:
        """
        Parameters
        ----------
        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspace.update_workspace_name(
                name="name",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workspace_name(
            name=name, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data
