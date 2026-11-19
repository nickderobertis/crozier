

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPubSubClient, RawPubSubClient


class PubSubClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPubSubClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPubSubClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPubSubClient
        """
        return self._raw_client

    def get_subscriptions(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
        client.pub_sub.get_subscriptions()
        """
        _response = self._raw_client.get_subscriptions(request_options=request_options)
        return _response.data


class AsyncPubSubClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPubSubClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPubSubClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPubSubClient
        """
        return self._raw_client

    async def get_subscriptions(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.pub_sub.get_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscriptions(request_options=request_options)
        return _response.data
