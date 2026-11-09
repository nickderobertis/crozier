

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_trace_response import DeleteTraceResponse
from ..types.trace_with_full_details import TraceWithFullDetails
from ..types.traces import Traces
from .raw_client import AsyncRawTraceClient, RawTraceClient


OMIT = typing.cast(typing.Any, ...)


class TraceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTraceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTraceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTraceClient
        """
        return self._raw_client

    def get(self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TraceWithFullDetails:
        """
        Get a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of a trace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceWithFullDetails


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.get(
            trace_id="traceId",
        )
        """
        _response = self._raw_client.get(trace_id, request_options=request_options)
        return _response.data

    def delete(self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteTraceResponse:
        """
        Delete a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of the trace to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTraceResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.delete(
            trace_id="traceId",
        )
        """
        _response = self._raw_client.delete(trace_id, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        version: typing.Optional[str] = None,
        release: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Traces:
        """
        Get list of traces

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]

        name : typing.Optional[str]

        session_id : typing.Optional[str]

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp before a certain datetime (ISO 8601)

        order_by : typing.Optional[str]
            Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only traces that include all of these tags will be returned.

        version : typing.Optional[str]
            Optional filter to only include traces with a certain version.

        release : typing.Optional[str]
            Optional filter to only include traces with a certain release.

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for traces where the environment is one of the provided values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Traces


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.list()
        """
        _response = self._raw_client.list(
            page=page,
            limit=limit,
            user_id=user_id,
            name=name,
            session_id=session_id,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            order_by=order_by,
            tags=tags,
            version=version,
            release=release,
            environment=environment,
            request_options=request_options,
        )
        return _response.data

    def deletemultiple(
        self, *, trace_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTraceResponse:
        """
        Delete multiple traces

        Parameters
        ----------
        trace_ids : typing.Sequence[str]
            List of trace IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTraceResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trace.deletemultiple(
            trace_ids=["traceIds"],
        )
        """
        _response = self._raw_client.deletemultiple(trace_ids=trace_ids, request_options=request_options)
        return _response.data


class AsyncTraceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTraceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTraceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTraceClient
        """
        return self._raw_client

    async def get(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TraceWithFullDetails:
        """
        Get a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of a trace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceWithFullDetails


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
            await client.trace.get(
                trace_id="traceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(trace_id, request_options=request_options)
        return _response.data

    async def delete(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTraceResponse:
        """
        Delete a specific trace

        Parameters
        ----------
        trace_id : str
            The unique langfuse identifier of the trace to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTraceResponse


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
            await client.trace.delete(
                trace_id="traceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(trace_id, request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        version: typing.Optional[str] = None,
        release: typing.Optional[str] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Traces:
        """
        Get list of traces

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]

        name : typing.Optional[str]

        session_id : typing.Optional[str]

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces with a trace.timestamp before a certain datetime (ISO 8601)

        order_by : typing.Optional[str]
            Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only traces that include all of these tags will be returned.

        version : typing.Optional[str]
            Optional filter to only include traces with a certain version.

        release : typing.Optional[str]
            Optional filter to only include traces with a certain release.

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for traces where the environment is one of the provided values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Traces


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
            await client.trace.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page=page,
            limit=limit,
            user_id=user_id,
            name=name,
            session_id=session_id,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            order_by=order_by,
            tags=tags,
            version=version,
            release=release,
            environment=environment,
            request_options=request_options,
        )
        return _response.data

    async def deletemultiple(
        self, *, trace_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTraceResponse:
        """
        Delete multiple traces

        Parameters
        ----------
        trace_ids : typing.Sequence[str]
            List of trace IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTraceResponse


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
            await client.trace.deletemultiple(
                trace_ids=["traceIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletemultiple(trace_ids=trace_ids, request_options=request_options)
        return _response.data
