

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1company import V1Company
from .raw_client import AsyncRawClientsClient, RawClientsClient
from .types.get11account_id_clients_request_show import Get11AccountIdClientsRequestShow
from .types.v1companies_create_client import V1CompaniesCreateClient
from .types.v1companies_update_client import V1CompaniesUpdateClient


OMIT = typing.cast(typing.Any, ...)


class ClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientsClient
        """
        return self._raw_client

    def list_all_clients_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        show: typing.Optional[Get11AccountIdClientsRequestShow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Company]:
        """
        NOTE: By default, client list will return first 10000 clients in alphabetical order. You can also use optional parameters like “limit”, “offset”, “show” and “order” to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of clients

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve clients from offset

        show : typing.Optional[Get11AccountIdClientsRequestShow]
            Specifies which records to retrieve. Example: "show=all" or "show=active" or "show=archived"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Company]
            Client details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clients.list_all_clients_of_an_account(
            account_id=1,
        )
        """
        _response = self._raw_client.list_all_clients_of_an_account(
            account_id, limit=limit, order=order, offset=offset, show=show, request_options=request_options
        )
        return _response.data

    def create_client(
        self,
        account_id: int,
        *,
        client: V1CompaniesCreateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        This API lets you create a client for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to create

        client : V1CompaniesCreateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client

        Examples
        --------
        from fern.clients import V1CompaniesCreateClient

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clients.create_client(
            account_id=1,
            client=V1CompaniesCreateClient(
                name="New Client",
            ),
        )
        """
        _response = self._raw_client.create_client(account_id, client=client, request_options=request_options)
        return _response.data

    def client_details(
        self,
        account_id: int,
        id: int,
        *,
        project_counts: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        Client details and project counts

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to retrieve

        id : int
            Client ID to retrieve

        project_counts : typing.Optional[str]
            Specify to retrieve project counts. Example values: "true" or "false"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clients.client_details(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.client_details(
            account_id, id, project_counts=project_counts, request_options=request_options
        )
        return _response.data

    def client_update(
        self,
        account_id: int,
        id: int,
        *,
        client: V1CompaniesUpdateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        Update client details just by using a client ID.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to update

        id : int
            Client ID to update

        client : V1CompaniesUpdateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client details

        Examples
        --------
        from fern.clients import V1CompaniesUpdateClient

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clients.client_update(
            account_id=1,
            id=1,
            client=V1CompaniesUpdateClient(
                active=True,
            ),
        )
        """
        _response = self._raw_client.client_update(account_id, id, client=client, request_options=request_options)
        return _response.data


class AsyncClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientsClient
        """
        return self._raw_client

    async def list_all_clients_of_an_account(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        show: typing.Optional[Get11AccountIdClientsRequestShow] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Company]:
        """
        NOTE: By default, client list will return first 10000 clients in alphabetical order. You can also use optional parameters like “limit”, “offset”, “show” and “order” to change the results.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        limit : typing.Optional[int]
            Retrieve number of clients

        order : typing.Optional[str]
            "asc (default)" and "desc"

        offset : typing.Optional[int]
            Retrieve clients from offset

        show : typing.Optional[Get11AccountIdClientsRequestShow]
            Specifies which records to retrieve. Example: "show=all" or "show=active" or "show=archived"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Company]
            Client details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clients.list_all_clients_of_an_account(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_clients_of_an_account(
            account_id, limit=limit, order=order, offset=offset, show=show, request_options=request_options
        )
        return _response.data

    async def create_client(
        self,
        account_id: int,
        *,
        client: V1CompaniesCreateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        This API lets you create a client for an account.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to create

        client : V1CompaniesCreateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client

        Examples
        --------
        import asyncio

        from fern.clients import V1CompaniesCreateClient

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clients.create_client(
                account_id=1,
                client=V1CompaniesCreateClient(
                    name="New Client",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_client(account_id, client=client, request_options=request_options)
        return _response.data

    async def client_details(
        self,
        account_id: int,
        id: int,
        *,
        project_counts: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        Client details and project counts

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to retrieve

        id : int
            Client ID to retrieve

        project_counts : typing.Optional[str]
            Specify to retrieve project counts. Example values: "true" or "false"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clients.client_details(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.client_details(
            account_id, id, project_counts=project_counts, request_options=request_options
        )
        return _response.data

    async def client_update(
        self,
        account_id: int,
        id: int,
        *,
        client: V1CompaniesUpdateClient,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Company:
        """
        Update client details just by using a client ID.

        Parameters
        ----------
        account_id : int
            Account ID for the client you want to update

        id : int
            Client ID to update

        client : V1CompaniesUpdateClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Company
            Client details

        Examples
        --------
        import asyncio

        from fern.clients import V1CompaniesUpdateClient

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clients.client_update(
                account_id=1,
                id=1,
                client=V1CompaniesUpdateClient(
                    active=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.client_update(account_id, id, client=client, request_options=request_options)
        return _response.data
