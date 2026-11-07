

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.results_with_counts_dto import ResultsWithCountsDto
from .raw_client import AsyncRawLiveDataClient, RawLiveDataClient


class LiveDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLiveDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLiveDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLiveDataClient
        """
        return self._raw_client

    def get_api_livedata_scenarioname(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ResultsWithCountsDto]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.live_data.get_api_livedata_scenarioname(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_livedata_scenarioname(scenario_name, request_options=request_options)
        return _response.data


class AsyncLiveDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLiveDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLiveDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLiveDataClient
        """
        return self._raw_client

    async def get_api_livedata_scenarioname(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ResultsWithCountsDto]:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ResultsWithCountsDto]


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
            await client.live_data.get_api_livedata_scenarioname(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_livedata_scenarioname(scenario_name, request_options=request_options)
        return _response.data
