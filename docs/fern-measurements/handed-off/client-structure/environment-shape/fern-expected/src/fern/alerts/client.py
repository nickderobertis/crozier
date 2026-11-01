

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAlertsClient, RawAlertsClient


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

    def list_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Transient alerts.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alerts.list_alerts()
        """
        _response = self._raw_client.list_alerts(request_options=request_options)
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

    async def list_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Transient alerts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alerts.list_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_alerts(request_options=request_options)
        return _response.data
