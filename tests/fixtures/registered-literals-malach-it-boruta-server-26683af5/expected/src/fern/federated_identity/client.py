

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFederatedIdentityClient, RawFederatedIdentityClient


class FederatedIdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFederatedIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFederatedIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFederatedIdentityClient
        """
        return self._raw_client

    def start_federated_authentication(
        self,
        id: str,
        federated_server_name: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        federated_server_name : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
        client.federated_identity.start_federated_authentication(
            id="id",
            federated_server_name="federated_server_name",
        )
        """
        _response = self._raw_client.start_federated_authentication(
            id, federated_server_name, request=request, request_options=request_options
        )
        return _response.data

    def complete_federated_authentication(
        self,
        id: str,
        federated_server_name: str,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        federated_server_name : str

        code : typing.Optional[str]

        state : typing.Optional[str]

        error : typing.Optional[str]

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
        client.federated_identity.complete_federated_authentication(
            id="id",
            federated_server_name="federated_server_name",
        )
        """
        _response = self._raw_client.complete_federated_authentication(
            id, federated_server_name, code=code, state=state, error=error, request_options=request_options
        )
        return _response.data


class AsyncFederatedIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFederatedIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFederatedIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFederatedIdentityClient
        """
        return self._raw_client

    async def start_federated_authentication(
        self,
        id: str,
        federated_server_name: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        federated_server_name : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
            await client.federated_identity.start_federated_authentication(
                id="id",
                federated_server_name="federated_server_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_federated_authentication(
            id, federated_server_name, request=request, request_options=request_options
        )
        return _response.data

    async def complete_federated_authentication(
        self,
        id: str,
        federated_server_name: str,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        federated_server_name : str

        code : typing.Optional[str]

        state : typing.Optional[str]

        error : typing.Optional[str]

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
            await client.federated_identity.complete_federated_authentication(
                id="id",
                federated_server_name="federated_server_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_federated_authentication(
            id, federated_server_name, code=code, state=state, error=error, request_options=request_options
        )
        return _response.data
