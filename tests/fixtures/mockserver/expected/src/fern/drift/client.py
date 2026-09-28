

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDriftClient, RawDriftClient
from .types.get_mockserver_drift_response import GetMockserverDriftResponse
from .types.put_mockserver_drift_clear_response import PutMockserverDriftClearResponse


class DriftClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDriftClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDriftClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDriftClient
        """
        return self._raw_client

    def retrieve_recorded_mock_drift(
        self,
        *,
        expectation_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMockserverDriftResponse:
        """
        Returns recorded drift records (differences between expectations and observed responses), optionally filtered by expectation id and limited in count.

        Parameters
        ----------
        expectation_id : typing.Optional[str]
            only return drift records for the given expectation id

        limit : typing.Optional[int]
            maximum number of recent drift records to return (default 50, capped at 500), ignored when expectationId is supplied

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverDriftResponse
            drift records returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.drift.retrieve_recorded_mock_drift()
        """
        _response = self._raw_client.retrieve_recorded_mock_drift(
            expectation_id=expectation_id, limit=limit, request_options=request_options
        )
        return _response.data

    def clear_all_recorded_mock_drift(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverDriftClearResponse:
        """
        removes all recorded drift records

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverDriftClearResponse
            drift records cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.drift.clear_all_recorded_mock_drift()
        """
        _response = self._raw_client.clear_all_recorded_mock_drift(request_options=request_options)
        return _response.data


class AsyncDriftClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDriftClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDriftClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDriftClient
        """
        return self._raw_client

    async def retrieve_recorded_mock_drift(
        self,
        *,
        expectation_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMockserverDriftResponse:
        """
        Returns recorded drift records (differences between expectations and observed responses), optionally filtered by expectation id and limited in count.

        Parameters
        ----------
        expectation_id : typing.Optional[str]
            only return drift records for the given expectation id

        limit : typing.Optional[int]
            maximum number of recent drift records to return (default 50, capped at 500), ignored when expectationId is supplied

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverDriftResponse
            drift records returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.drift.retrieve_recorded_mock_drift()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_recorded_mock_drift(
            expectation_id=expectation_id, limit=limit, request_options=request_options
        )
        return _response.data

    async def clear_all_recorded_mock_drift(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverDriftClearResponse:
        """
        removes all recorded drift records

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverDriftClearResponse
            drift records cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.drift.clear_all_recorded_mock_drift()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_all_recorded_mock_drift(request_options=request_options)
        return _response.data
