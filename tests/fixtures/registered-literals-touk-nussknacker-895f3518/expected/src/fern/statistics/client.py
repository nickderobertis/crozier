

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.statistic_dto import StatisticDto
from ..types.statistic_url_response_dto import StatisticUrlResponseDto
from .raw_client import AsyncRawStatisticsClient, RawStatisticsClient


OMIT = typing.cast(typing.Any, ...)


class StatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatisticsClient
        """
        return self._raw_client

    def post_api_statistic(
        self,
        *,
        statistics: typing.Optional[typing.Sequence[StatisticDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        statistics : typing.Optional[typing.Sequence[StatisticDto]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.statistics.post_api_statistic()
        """
        _response = self._raw_client.post_api_statistic(statistics=statistics, request_options=request_options)
        return _response.data

    def get_api_statistic_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatisticUrlResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatisticUrlResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.statistics.get_api_statistic_usage()
        """
        _response = self._raw_client.get_api_statistic_usage(request_options=request_options)
        return _response.data


class AsyncStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatisticsClient
        """
        return self._raw_client

    async def post_api_statistic(
        self,
        *,
        statistics: typing.Optional[typing.Sequence[StatisticDto]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        statistics : typing.Optional[typing.Sequence[StatisticDto]]

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
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.statistics.post_api_statistic()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_statistic(statistics=statistics, request_options=request_options)
        return _response.data

    async def get_api_statistic_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatisticUrlResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatisticUrlResponseDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.statistics.get_api_statistic_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_statistic_usage(request_options=request_options)
        return _response.data
