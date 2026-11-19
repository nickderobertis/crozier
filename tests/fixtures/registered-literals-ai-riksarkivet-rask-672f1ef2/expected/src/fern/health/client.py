

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.liveness import Liveness
from ..types.readiness import Readiness
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def livez(self, *, request_options: typing.Optional[RequestOptions] = None) -> Liveness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Liveness
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.livez()
        """
        _response = self._raw_client.livez(request_options=request_options)
        return _response.data

    def readyz(self, *, request_options: typing.Optional[RequestOptions] = None) -> Readiness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readiness
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.readyz()
        """
        _response = self._raw_client.readyz(request_options=request_options)
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def livez(self, *, request_options: typing.Optional[RequestOptions] = None) -> Liveness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Liveness
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.livez()


        asyncio.run(main())
        """
        _response = await self._raw_client.livez(request_options=request_options)
        return _response.data

    async def readyz(self, *, request_options: typing.Optional[RequestOptions] = None) -> Readiness:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readiness
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.readyz()


        asyncio.run(main())
        """
        _response = await self._raw_client.readyz(request_options=request_options)
        return _response.data
