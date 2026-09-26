

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.metrics_response import MetricsResponse
from ..types.metrics_v60response import MetricsV60Response
from .raw_client import AsyncRawAccountClient, RawAccountClient


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get_account_metrics(
        self, *, key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricsResponse:
        """
        Returns usage metrics for the authenticated account

        Parameters
        ----------
        key : typing.Optional[str]
            API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.account.get_account_metrics()
        """
        _response = self._raw_client.get_account_metrics(key=key, request_options=request_options)
        return _response.data

    def get_account_metrics_v60(
        self, *, key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricsV60Response:
        """
        Returns usage metrics for the authenticated account in the simplified v6.0 format. In v6.0 all keys are geo keys, so the counters reflect geo usage.

        Parameters
        ----------
        key : typing.Optional[str]
            API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsV60Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.account.get_account_metrics_v60()
        """
        _response = self._raw_client.get_account_metrics_v60(key=key, request_options=request_options)
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get_account_metrics(
        self, *, key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricsResponse:
        """
        Returns usage metrics for the authenticated account

        Parameters
        ----------
        key : typing.Optional[str]
            API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_account_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_metrics(key=key, request_options=request_options)
        return _response.data

    async def get_account_metrics_v60(
        self, *, key: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MetricsV60Response:
        """
        Returns usage metrics for the authenticated account in the simplified v6.0 format. In v6.0 all keys are geo keys, so the counters reflect geo usage.

        Parameters
        ----------
        key : typing.Optional[str]
            API key identifying the account whose usage metrics are returned. May be supplied as this query parameter or the X-API-KEY header.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsV60Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.account.get_account_metrics_v60()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_metrics_v60(key=key, request_options=request_options)
        return _response.data
