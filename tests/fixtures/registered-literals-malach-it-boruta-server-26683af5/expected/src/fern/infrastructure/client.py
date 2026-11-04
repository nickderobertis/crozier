

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInfrastructureClient, RawInfrastructureClient


class InfrastructureClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfrastructureClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfrastructureClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfrastructureClient
        """
        return self._raw_client

    def retrieve_an_acme_http01challenge_response(
        self, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        token : str
            ACME challenge token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            ACME challenge key authorization

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.infrastructure.retrieve_an_acme_http01challenge_response(
            token="token",
        )
        """
        _response = self._raw_client.retrieve_an_acme_http01challenge_response(token, request_options=request_options)
        return _response.data

    def check_service_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.infrastructure.check_service_health()
        """
        _response = self._raw_client.check_service_health(request_options=request_options)
        return _response.data


class AsyncInfrastructureClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfrastructureClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfrastructureClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfrastructureClient
        """
        return self._raw_client

    async def retrieve_an_acme_http01challenge_response(
        self, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        token : str
            ACME challenge token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            ACME challenge key authorization

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.infrastructure.retrieve_an_acme_http01challenge_response(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_acme_http01challenge_response(
            token, request_options=request_options
        )
        return _response.data

    async def check_service_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.infrastructure.check_service_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_service_health(request_options=request_options)
        return _response.data
