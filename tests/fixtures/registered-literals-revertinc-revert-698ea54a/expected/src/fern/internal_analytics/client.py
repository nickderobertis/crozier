

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.internal_get_analytics_response import InternalGetAnalyticsResponse
from .raw_client import AsyncRawInternalAnalyticsClient, RawInternalAnalyticsClient


OMIT = typing.cast(typing.Any, ...)


class InternalAnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalAnalyticsClient
        """
        return self._raw_client

    def internal_analytics_get_analytics(
        self, *, user_id: str, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalGetAnalyticsResponse:
        """
        Get Analytics of your revert account

        Parameters
        ----------
        user_id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAnalyticsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_analytics.internal_analytics_get_analytics(
            user_id="userId",
            environment="environment",
        )
        """
        _response = self._raw_client.internal_analytics_get_analytics(
            user_id=user_id, environment=environment, request_options=request_options
        )
        return _response.data


class AsyncInternalAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalAnalyticsClient
        """
        return self._raw_client

    async def internal_analytics_get_analytics(
        self, *, user_id: str, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalGetAnalyticsResponse:
        """
        Get Analytics of your revert account

        Parameters
        ----------
        user_id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAnalyticsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_analytics.internal_analytics_get_analytics(
                user_id="userId",
                environment="environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_analytics_get_analytics(
            user_id=user_id, environment=environment, request_options=request_options
        )
        return _response.data
