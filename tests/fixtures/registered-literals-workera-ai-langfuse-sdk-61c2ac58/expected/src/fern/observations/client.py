

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.observations_view import ObservationsView
from ..types.observations_views import ObservationsViews
from .raw_client import AsyncRawObservationsClient, RawObservationsClient


class ObservationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObservationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObservationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObservationsClient
        """
        return self._raw_client

    def get(self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ObservationsView:
        """
        Get a observation

        Parameters
        ----------
        observation_id : str
            The unique langfuse identifier of an observation, can be an event, span or generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsView


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observations.get(
            observation_id="observationId",
        )
        """
        _response = self._raw_client.get(observation_id, request_options=request_options)
        return _response.data

    def getmany(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        parent_observation_id: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_start_time: typing.Optional[dt.datetime] = None,
        to_start_time: typing.Optional[dt.datetime] = None,
        version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObservationsViews:
        """
        Get a list of observations

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        name : typing.Optional[str]

        user_id : typing.Optional[str]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        parent_observation_id : typing.Optional[str]

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for observations where the environment is one of the provided values.

        from_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time or or after this datetime (ISO 8601).

        to_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time before this datetime (ISO 8601).

        version : typing.Optional[str]
            Optional filter to only include observations with a certain version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsViews


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observations.getmany()
        """
        _response = self._raw_client.getmany(
            page=page,
            limit=limit,
            name=name,
            user_id=user_id,
            type=type,
            trace_id=trace_id,
            parent_observation_id=parent_observation_id,
            environment=environment,
            from_start_time=from_start_time,
            to_start_time=to_start_time,
            version=version,
            request_options=request_options,
        )
        return _response.data


class AsyncObservationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObservationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObservationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObservationsClient
        """
        return self._raw_client

    async def get(
        self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObservationsView:
        """
        Get a observation

        Parameters
        ----------
        observation_id : str
            The unique langfuse identifier of an observation, can be an event, span or generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsView


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observations.get(
                observation_id="observationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(observation_id, request_options=request_options)
        return _response.data

    async def getmany(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        parent_observation_id: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_start_time: typing.Optional[dt.datetime] = None,
        to_start_time: typing.Optional[dt.datetime] = None,
        version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObservationsViews:
        """
        Get a list of observations

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        name : typing.Optional[str]

        user_id : typing.Optional[str]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        parent_observation_id : typing.Optional[str]

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for observations where the environment is one of the provided values.

        from_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time or or after this datetime (ISO 8601).

        to_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time before this datetime (ISO 8601).

        version : typing.Optional[str]
            Optional filter to only include observations with a certain version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsViews


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observations.getmany()


        asyncio.run(main())
        """
        _response = await self._raw_client.getmany(
            page=page,
            limit=limit,
            name=name,
            user_id=user_id,
            type=type,
            trace_id=trace_id,
            parent_observation_id=parent_observation_id,
            environment=environment,
            from_start_time=from_start_time,
            to_start_time=to_start_time,
            version=version,
            request_options=request_options,
        )
        return _response.data
