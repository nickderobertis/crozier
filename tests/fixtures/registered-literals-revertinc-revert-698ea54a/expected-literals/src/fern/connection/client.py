

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection_import import ConnectionImport
from ..types.create_connection_webhook_response import CreateConnectionWebhookResponse
from ..types.delete_connection_response import DeleteConnectionResponse
from ..types.delete_connection_webhook_response import DeleteConnectionWebhookResponse
from ..types.get_all_connection_response import GetAllConnectionResponse
from ..types.get_connect_status_response import GetConnectStatusResponse
from ..types.get_connection_response import GetConnectionResponse
from ..types.get_connection_webhook_response import GetConnectionWebhookResponse
from ..types.import_connections_response import ImportConnectionsResponse
from .raw_client import AsyncRawConnectionClient, RawConnectionClient


OMIT = typing.cast(typing.Any, ...)


class ConnectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionClient
        """
        return self._raw_client

    def getconnection(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionResponse:
        """
        Get details of a connection for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.getconnection(
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.getconnection(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    def deleteconnection(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConnectionResponse:
        """
        Delete a connection for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConnectionResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.deleteconnection(
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.deleteconnection(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    def getallconnections(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAllConnectionResponse:
        """
        Get details of all the connection for a specific account at Revert.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllConnectionResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.getallconnections()
        """
        _response = self._raw_client.getallconnections(request_options=request_options)
        return _response.data

    def getwebhook(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionWebhookResponse:
        """
        Get details of a connection webhook for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionWebhookResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.getwebhook(
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.getwebhook(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    def createwebhook(
        self, *, revert_t_id: str, webhook_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateConnectionWebhookResponse:
        """
        Create a webhook endpoint that listens to a connection events of a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        webhook_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionWebhookResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.createwebhook(
            revert_t_id="x-revert-t-id",
            webhook_url="webhookUrl",
        )
        """
        _response = self._raw_client.createwebhook(
            revert_t_id=revert_t_id, webhook_url=webhook_url, request_options=request_options
        )
        return _response.data

    def deletewebhook(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConnectionWebhookResponse:
        """
        Delete the connection webhook for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConnectionWebhookResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.deletewebhook(
            revert_t_id="x-revert-t-id",
        )
        """
        _response = self._raw_client.deletewebhook(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    def getintegrationstatus(
        self, revert_public_token: str, *, tenant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectStatusResponse:
        """
        Get the OAuth connection event status. This endpoint responds with a `http.ServerResponse` instead of `json`.

        Parameters
        ----------
        revert_public_token : str

        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectStatusResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connection.getintegrationstatus(
            revert_public_token="revertPublicToken",
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.getintegrationstatus(
            revert_public_token, tenant_id=tenant_id, request_options=request_options
        )
        return _response.data

    def importconnections(
        self,
        *,
        revert_t_id: str,
        connections: typing.Sequence[ConnectionImport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportConnectionsResponse:
        """
        Import multiple connections for a specific environment. Use this to bulk import connections as a one-time exercise.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        connections : typing.Sequence[ConnectionImport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportConnectionsResponse


        Examples
        --------
        from fern import ConnectionImport, FernApi

        client = FernApi()
        client.connection.importconnections(
            revert_t_id="x-revert-t-id",
            connections=[
                ConnectionImport(
                    tp_id="hubspot",
                    tp_access_token="tp_access_token",
                    tp_refresh_token="tp_refresh_token",
                    tp_customer_id="tp_customer_id",
                    t_id="t_id",
                    app_client_id="app_client_id",
                    app_client_secret="app_client_secret",
                    app_id="app_id",
                )
            ],
        )
        """
        _response = self._raw_client.importconnections(
            revert_t_id=revert_t_id, connections=connections, request_options=request_options
        )
        return _response.data


class AsyncConnectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionClient
        """
        return self._raw_client

    async def getconnection(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionResponse:
        """
        Get details of a connection for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.getconnection(
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getconnection(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    async def deleteconnection(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConnectionResponse:
        """
        Delete a connection for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConnectionResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.deleteconnection(
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteconnection(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    async def getallconnections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAllConnectionResponse:
        """
        Get details of all the connection for a specific account at Revert.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllConnectionResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.getallconnections()


        asyncio.run(main())
        """
        _response = await self._raw_client.getallconnections(request_options=request_options)
        return _response.data

    async def getwebhook(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionWebhookResponse:
        """
        Get details of a connection webhook for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionWebhookResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.getwebhook(
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getwebhook(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    async def createwebhook(
        self, *, revert_t_id: str, webhook_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateConnectionWebhookResponse:
        """
        Create a webhook endpoint that listens to a connection events of a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        webhook_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionWebhookResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.createwebhook(
                revert_t_id="x-revert-t-id",
                webhook_url="webhookUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createwebhook(
            revert_t_id=revert_t_id, webhook_url=webhook_url, request_options=request_options
        )
        return _response.data

    async def deletewebhook(
        self, *, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteConnectionWebhookResponse:
        """
        Delete the connection webhook for a specific tenant.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteConnectionWebhookResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.deletewebhook(
                revert_t_id="x-revert-t-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletewebhook(revert_t_id=revert_t_id, request_options=request_options)
        return _response.data

    async def getintegrationstatus(
        self, revert_public_token: str, *, tenant_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectStatusResponse:
        """
        Get the OAuth connection event status. This endpoint responds with a `http.ServerResponse` instead of `json`.

        Parameters
        ----------
        revert_public_token : str

        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectStatusResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.getintegrationstatus(
                revert_public_token="revertPublicToken",
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getintegrationstatus(
            revert_public_token, tenant_id=tenant_id, request_options=request_options
        )
        return _response.data

    async def importconnections(
        self,
        *,
        revert_t_id: str,
        connections: typing.Sequence[ConnectionImport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportConnectionsResponse:
        """
        Import multiple connections for a specific environment. Use this to bulk import connections as a one-time exercise.

        Parameters
        ----------
        revert_t_id : str
            The unique customer id used when the customer linked their account.

        connections : typing.Sequence[ConnectionImport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportConnectionsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConnectionImport

        client = AsyncFernApi()


        async def main() -> None:
            await client.connection.importconnections(
                revert_t_id="x-revert-t-id",
                connections=[
                    ConnectionImport(
                        tp_id="hubspot",
                        tp_access_token="tp_access_token",
                        tp_refresh_token="tp_refresh_token",
                        tp_customer_id="tp_customer_id",
                        t_id="t_id",
                        app_client_id="app_client_id",
                        app_client_secret="app_client_secret",
                        app_id="app_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.importconnections(
            revert_t_id=revert_t_id, connections=connections, request_options=request_options
        )
        return _response.data
