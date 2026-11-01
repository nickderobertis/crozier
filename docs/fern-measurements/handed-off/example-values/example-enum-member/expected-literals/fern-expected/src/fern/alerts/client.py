

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alert_kind import AlertKind
from .raw_client import AsyncRawAlertsClient, RawAlertsClient
from .types.subscribe_alerts_response import SubscribeAlertsResponse


OMIT = typing.cast(typing.Any, ...)


class AlertsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlertsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlertsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlertsClient
        """
        return self._raw_client

    def subscribe_alerts(
        self,
        *,
        kinds: typing.Sequence[AlertKind],
        callback: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeAlertsResponse:
        """
        Parameters
        ----------
        kinds : typing.Sequence[AlertKind]

        callback : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeAlertsResponse
            Subscribed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.alerts.subscribe_alerts(
            kinds=["*"],
            callback="callback",
        )
        """
        _response = self._raw_client.subscribe_alerts(kinds=kinds, callback=callback, request_options=request_options)
        return _response.data


class AsyncAlertsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlertsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlertsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlertsClient
        """
        return self._raw_client

    async def subscribe_alerts(
        self,
        *,
        kinds: typing.Sequence[AlertKind],
        callback: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeAlertsResponse:
        """
        Parameters
        ----------
        kinds : typing.Sequence[AlertKind]

        callback : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeAlertsResponse
            Subscribed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alerts.subscribe_alerts(
                kinds=["*"],
                callback="callback",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe_alerts(
            kinds=kinds, callback=callback, request_options=request_options
        )
        return _response.data
