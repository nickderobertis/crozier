

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mutable_auth_client import MutableAuthClient
from .raw_client import AsyncRawAuthClientsClient, RawAuthClientsClient
from .types.create_client_response import CreateClientResponse
from .types.get_client_by_id_response import GetClientByIdResponse
from .types.get_clients_response import GetClientsResponse
from .types.start_platform_auth_flow_response import StartPlatformAuthFlowResponse
from .types.update_client_response import UpdateClientResponse


OMIT = typing.cast(typing.Any, ...)


class AuthClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClientsClient
        """
        return self._raw_client

    def get_clients(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetClientsResponse:
        """
        Retrieve all clients created by the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClientsResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_clients.get_clients()
        """
        _response = self._raw_client.get_clients(
            page_size=page_size, page_number=page_number, request_options=request_options
        )
        return _response.data

    def create_client(
        self, *, request: MutableAuthClient, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateClientResponse:
        """
        Create an client

        Parameters
        ----------
        request : MutableAuthClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClientResponse
            successful operation

        Examples
        --------
        from fern import (
            FernApi,
            MutableAuthClient_Oa1TwoLegged,
            MutableOa1TwoLeggedClientType,
            Owner,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_clients.create_client(
            request=MutableAuthClient_Oa1TwoLegged(
                name="name",
                owners=[
                    Owner(
                        id="617082258803c70031f85b26",
                        type="USER",
                    )
                ],
                type=MutableOa1TwoLeggedClientType.OA1TWO_LEGGED,
                consumer_key="consumerKey",
                consumer_secret="consumerSecret",
                nonce="nonce",
                signature="signature",
                signature_method="signatureMethod",
            ),
        )
        """
        _response = self._raw_client.create_client(request=request, request_options=request_options)
        return _response.data

    def get_client_by_id(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClientByIdResponse:
        """
        Returns a client with given ID

        Parameters
        ----------
        client_id : str
            ID of the client to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClientByIdResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_clients.get_client_by_id(
            client_id="61719514a477890012b804b9",
        )
        """
        _response = self._raw_client.get_client_by_id(client_id, request_options=request_options)
        return _response.data

    def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a client

        Parameters
        ----------
        client_id : str
            ID of the client to delete

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
        client.auth_clients.delete_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data

    def update_client(
        self, client_id: str, *, request: MutableAuthClient, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateClientResponse:
        """
        Update a client

        Parameters
        ----------
        client_id : str
            ID of the client to update

        request : MutableAuthClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateClientResponse
            successful operation

        Examples
        --------
        from fern import (
            FernApi,
            MutableAuthClient_Oa1TwoLegged,
            MutableOa1TwoLeggedClientType,
            Owner,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_clients.update_client(
            client_id="clientId",
            request=MutableAuthClient_Oa1TwoLegged(
                name="name",
                owners=[
                    Owner(
                        id="617082258803c70031f85b26",
                        type="USER",
                    )
                ],
                type=MutableOa1TwoLeggedClientType.OA1TWO_LEGGED,
                consumer_key="consumerKey",
                consumer_secret="consumerSecret",
                nonce="nonce",
                signature="signature",
                signature_method="signatureMethod",
            ),
        )
        """
        _response = self._raw_client.update_client(client_id, request=request, request_options=request_options)
        return _response.data

    def start_platform_auth_flow(
        self,
        client_id: str,
        *,
        scope: typing.Optional[str] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        success_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartPlatformAuthFlowResponse:
        """
        Can be done by any user

        Parameters
        ----------
        client_id : str
            ID of the client to return

        scope : typing.Optional[str]

        secret_name : typing.Optional[str]

        success_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartPlatformAuthFlowResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_clients.start_platform_auth_flow(
            client_id="6171ad81a477890012b804c0",
        )
        """
        _response = self._raw_client.start_platform_auth_flow(
            client_id, scope=scope, secret_name=secret_name, success_url=success_url, request_options=request_options
        )
        return _response.data


class AsyncAuthClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClientsClient
        """
        return self._raw_client

    async def get_clients(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetClientsResponse:
        """
        Retrieve all clients created by the current user.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of results to return per page

        page_number : typing.Optional[int]
            The page number to return (not zero indexed)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClientsResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_clients.get_clients()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_clients(
            page_size=page_size, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def create_client(
        self, *, request: MutableAuthClient, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateClientResponse:
        """
        Create an client

        Parameters
        ----------
        request : MutableAuthClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClientResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MutableAuthClient_Oa1TwoLegged,
            MutableOa1TwoLeggedClientType,
            Owner,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_clients.create_client(
                request=MutableAuthClient_Oa1TwoLegged(
                    name="name",
                    owners=[
                        Owner(
                            id="617082258803c70031f85b26",
                            type="USER",
                        )
                    ],
                    type=MutableOa1TwoLeggedClientType.OA1TWO_LEGGED,
                    consumer_key="consumerKey",
                    consumer_secret="consumerSecret",
                    nonce="nonce",
                    signature="signature",
                    signature_method="signatureMethod",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_client(request=request, request_options=request_options)
        return _response.data

    async def get_client_by_id(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetClientByIdResponse:
        """
        Returns a client with given ID

        Parameters
        ----------
        client_id : str
            ID of the client to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetClientByIdResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_clients.get_client_by_id(
                client_id="61719514a477890012b804b9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_client_by_id(client_id, request_options=request_options)
        return _response.data

    async def delete_client(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a client

        Parameters
        ----------
        client_id : str
            ID of the client to delete

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
            await client.auth_clients.delete_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_client(client_id, request_options=request_options)
        return _response.data

    async def update_client(
        self, client_id: str, *, request: MutableAuthClient, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateClientResponse:
        """
        Update a client

        Parameters
        ----------
        client_id : str
            ID of the client to update

        request : MutableAuthClient

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateClientResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MutableAuthClient_Oa1TwoLegged,
            MutableOa1TwoLeggedClientType,
            Owner,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_clients.update_client(
                client_id="clientId",
                request=MutableAuthClient_Oa1TwoLegged(
                    name="name",
                    owners=[
                        Owner(
                            id="617082258803c70031f85b26",
                            type="USER",
                        )
                    ],
                    type=MutableOa1TwoLeggedClientType.OA1TWO_LEGGED,
                    consumer_key="consumerKey",
                    consumer_secret="consumerSecret",
                    nonce="nonce",
                    signature="signature",
                    signature_method="signatureMethod",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_client(client_id, request=request, request_options=request_options)
        return _response.data

    async def start_platform_auth_flow(
        self,
        client_id: str,
        *,
        scope: typing.Optional[str] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        success_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartPlatformAuthFlowResponse:
        """
        Can be done by any user

        Parameters
        ----------
        client_id : str
            ID of the client to return

        scope : typing.Optional[str]

        secret_name : typing.Optional[str]

        success_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartPlatformAuthFlowResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_clients.start_platform_auth_flow(
                client_id="6171ad81a477890012b804c0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_platform_auth_flow(
            client_id, scope=scope, secret_name=secret_name, success_url=success_url, request_options=request_options
        )
        return _response.data
