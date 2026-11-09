

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ingestion_event import IngestionEvent
from .raw_client import AsyncRawIngestionClient, RawIngestionClient


OMIT = typing.cast(typing.Any, ...)


class IngestionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIngestionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIngestionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIngestionClient
        """
        return self._raw_client

    def batch(
        self,
        *,
        batch: typing.Sequence[IngestionEvent],
        metadata: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batched ingestion for Langfuse Tracing.
        If you want to use tracing via the API, such as to build your own Langfuse client implementation, this is the only API route you need to implement.

        Within each batch, there can be multiple events.
        Each event has a type, an id, a timestamp, metadata and a body.
        Internally, we refer to this as the "event envelope" as it tells us something about the event but not the trace.
        We use the event id within this envelope to deduplicate messages to avoid processing the same event twice, i.e. the event id should be unique per request.
        The event.body.id is the ID of the actual trace and will be used for updates and will be visible within the Langfuse App.
        I.e. if you want to update a trace, you'd use the same body id, but separate event IDs.

        Notes:
        - Introduction to data model: https://langfuse.com/docs/tracing-data-model
        - Batch sizes are limited to 3.5 MB in total. You need to adjust the number of events per batch accordingly.
        - The API does not return a 4xx status code for input errors. Instead, it responds with a 207 status code, which includes a list of the encountered errors.

        Parameters
        ----------
        batch : typing.Sequence[IngestionEvent]
            Batch of tracing events to be ingested. Discriminated by attribute `type`.

        metadata : typing.Optional[typing.Any]
            Optional. Metadata field used by the Langfuse SDKs for debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi, IngestionEventZero, IngestionEventZeroType, TraceBody

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.batch(
            batch=[
                IngestionEventZero(
                    id="abcdef-1234-5678-90ab",
                    timestamp="2022-01-01T00:00:00.000Z",
                    body=TraceBody(
                        id="abcdef-1234-5678-90ab",
                        timestamp=datetime.datetime.fromisoformat(
                            "2022-01-01 00:00:00+00:00",
                        ),
                        name="My Trace",
                        user_id="1234-5678-90ab-cdef",
                        input="My input",
                        output="My output",
                        session_id="1234-5678-90ab-cdef",
                        release="1.0.0",
                        version="1.0.0",
                        metadata="My metadata",
                        tags=["tag1", "tag2"],
                        environment="production",
                        public=True,
                    ),
                    type=IngestionEventZeroType.TRACE_CREATE,
                )
            ],
        )
        """
        _response = self._raw_client.batch(batch=batch, metadata=metadata, request_options=request_options)
        return _response.data


class AsyncIngestionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIngestionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIngestionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIngestionClient
        """
        return self._raw_client

    async def batch(
        self,
        *,
        batch: typing.Sequence[IngestionEvent],
        metadata: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batched ingestion for Langfuse Tracing.
        If you want to use tracing via the API, such as to build your own Langfuse client implementation, this is the only API route you need to implement.

        Within each batch, there can be multiple events.
        Each event has a type, an id, a timestamp, metadata and a body.
        Internally, we refer to this as the "event envelope" as it tells us something about the event but not the trace.
        We use the event id within this envelope to deduplicate messages to avoid processing the same event twice, i.e. the event id should be unique per request.
        The event.body.id is the ID of the actual trace and will be used for updates and will be visible within the Langfuse App.
        I.e. if you want to update a trace, you'd use the same body id, but separate event IDs.

        Notes:
        - Introduction to data model: https://langfuse.com/docs/tracing-data-model
        - Batch sizes are limited to 3.5 MB in total. You need to adjust the number of events per batch accordingly.
        - The API does not return a 4xx status code for input errors. Instead, it responds with a 207 status code, which includes a list of the encountered errors.

        Parameters
        ----------
        batch : typing.Sequence[IngestionEvent]
            Batch of tracing events to be ingested. Discriminated by attribute `type`.

        metadata : typing.Optional[typing.Any]
            Optional. Metadata field used by the Langfuse SDKs for debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            IngestionEventZero,
            IngestionEventZeroType,
            TraceBody,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.batch(
                batch=[
                    IngestionEventZero(
                        id="abcdef-1234-5678-90ab",
                        timestamp="2022-01-01T00:00:00.000Z",
                        body=TraceBody(
                            id="abcdef-1234-5678-90ab",
                            timestamp=datetime.datetime.fromisoformat(
                                "2022-01-01 00:00:00+00:00",
                            ),
                            name="My Trace",
                            user_id="1234-5678-90ab-cdef",
                            input="My input",
                            output="My output",
                            session_id="1234-5678-90ab-cdef",
                            release="1.0.0",
                            version="1.0.0",
                            metadata="My metadata",
                            tags=["tag1", "tag2"],
                            environment="production",
                            public=True,
                        ),
                        type=IngestionEventZeroType.TRACE_CREATE,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch(batch=batch, metadata=metadata, request_options=request_options)
        return _response.data
