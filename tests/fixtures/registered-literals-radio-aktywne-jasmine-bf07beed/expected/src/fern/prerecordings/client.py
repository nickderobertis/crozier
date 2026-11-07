

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_request_event import DeleteRequestEvent
from ..types.delete_request_start import DeleteRequestStart
from ..types.download_request_event import DownloadRequestEvent
from ..types.download_request_start import DownloadRequestStart
from ..types.head_download_request_event import HeadDownloadRequestEvent
from ..types.head_download_request_start import HeadDownloadRequestStart
from ..types.list_request_event import ListRequestEvent
from ..types.list_response_results import ListResponseResults
from ..types.upload_request_event import UploadRequestEvent
from ..types.upload_request_start import UploadRequestStart
from .raw_client import AsyncRawPrerecordingsClient, RawPrerecordingsClient
from .types.prerecordings_event_list_request_after import PrerecordingsEventListRequestAfter
from .types.prerecordings_event_list_request_before import PrerecordingsEventListRequestBefore
from .types.prerecordings_event_list_request_limit import PrerecordingsEventListRequestLimit
from .types.prerecordings_event_list_request_offset import PrerecordingsEventListRequestOffset
from .types.prerecordings_event_list_request_order import PrerecordingsEventListRequestOrder


OMIT = typing.cast(typing.Any, ...)


class PrerecordingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrerecordingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrerecordingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrerecordingsClient
        """
        return self._raw_client

    def prerecordings_event_start_download(
        self,
        event: DownloadRequestEvent,
        start: DownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Download a prerecording.

        Parameters
        ----------
        event : DownloadRequestEvent

        start : DownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Stream Response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prerecordings.prerecordings_event_start_download(
            event="event",
            start=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        with self._raw_client.prerecordings_event_start_download(event, start, request_options=request_options) as r:
            yield from r.data

    def prerecordings_event_start_upload(
        self,
        event: UploadRequestEvent,
        start: UploadRequestStart,
        *,
        request: bytes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload a prerecording.

        Parameters
        ----------
        event : UploadRequestEvent

        start : UploadRequestStart
            Datetime without timezone.

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prerecordings.prerecordings_event_start_upload(
            event="event",
            start=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            request="string",
        )
        """
        _response = self._raw_client.prerecordings_event_start_upload(
            event, start, request=request, request_options=request_options
        )
        return _response.data

    def prerecordings_event_start_delete(
        self,
        event: DeleteRequestEvent,
        start: DeleteRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a prerecording.

        Parameters
        ----------
        event : DeleteRequestEvent

        start : DeleteRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prerecordings.prerecordings_event_start_delete(
            event="event",
            start=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.prerecordings_event_start_delete(event, start, request_options=request_options)
        return _response.data

    def prerecordings_event_start_headdownload(
        self,
        event: HeadDownloadRequestEvent,
        start: HeadDownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Download prerecording headers.

        Parameters
        ----------
        event : HeadDownloadRequestEvent

        start : HeadDownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prerecordings.prerecordings_event_start_headdownload(
            event="event",
            start=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.prerecordings_event_start_headdownload(
            event, start, request_options=request_options
        )
        return _response.headers

    def prerecordings_event_list(
        self,
        event: ListRequestEvent,
        *,
        after: typing.Optional[PrerecordingsEventListRequestAfter] = None,
        before: typing.Optional[PrerecordingsEventListRequestBefore] = None,
        limit: typing.Optional[PrerecordingsEventListRequestLimit] = None,
        offset: typing.Optional[PrerecordingsEventListRequestOffset] = None,
        order: typing.Optional[PrerecordingsEventListRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseResults:
        """
        List prerecordings.

        Parameters
        ----------
        event : ListRequestEvent

        after : typing.Optional[PrerecordingsEventListRequestAfter]
            Only list prerecordings after this datetime (in event timezone).

        before : typing.Optional[PrerecordingsEventListRequestBefore]
            Only list prerecordings before this datetime (in event timezone).

        limit : typing.Optional[PrerecordingsEventListRequestLimit]
            Maximum number of prerecordings to return. Default is 10.

        offset : typing.Optional[PrerecordingsEventListRequestOffset]
            Number of prerecordings to skip.

        order : typing.Optional[PrerecordingsEventListRequestOrder]
            Order to apply to the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseResults
            Request fulfilled, document follows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prerecordings.prerecordings_event_list(
            event="event",
        )
        """
        _response = self._raw_client.prerecordings_event_list(
            event, after=after, before=before, limit=limit, offset=offset, order=order, request_options=request_options
        )
        return _response.data


class AsyncPrerecordingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrerecordingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrerecordingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrerecordingsClient
        """
        return self._raw_client

    async def prerecordings_event_start_download(
        self,
        event: DownloadRequestEvent,
        start: DownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Download a prerecording.

        Parameters
        ----------
        event : DownloadRequestEvent

        start : DownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Stream Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prerecordings.prerecordings_event_start_download(
                event="event",
                start=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        async with self._raw_client.prerecordings_event_start_download(
            event, start, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def prerecordings_event_start_upload(
        self,
        event: UploadRequestEvent,
        start: UploadRequestStart,
        *,
        request: bytes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Upload a prerecording.

        Parameters
        ----------
        event : UploadRequestEvent

        start : UploadRequestStart
            Datetime without timezone.

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prerecordings.prerecordings_event_start_upload(
                event="event",
                start=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prerecordings_event_start_upload(
            event, start, request=request, request_options=request_options
        )
        return _response.data

    async def prerecordings_event_start_delete(
        self,
        event: DeleteRequestEvent,
        start: DeleteRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a prerecording.

        Parameters
        ----------
        event : DeleteRequestEvent

        start : DeleteRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prerecordings.prerecordings_event_start_delete(
                event="event",
                start=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prerecordings_event_start_delete(
            event, start, request_options=request_options
        )
        return _response.data

    async def prerecordings_event_start_headdownload(
        self,
        event: HeadDownloadRequestEvent,
        start: HeadDownloadRequestStart,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Download prerecording headers.

        Parameters
        ----------
        event : HeadDownloadRequestEvent

        start : HeadDownloadRequestStart
            Datetime without timezone.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prerecordings.prerecordings_event_start_headdownload(
                event="event",
                start=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prerecordings_event_start_headdownload(
            event, start, request_options=request_options
        )
        return _response.headers

    async def prerecordings_event_list(
        self,
        event: ListRequestEvent,
        *,
        after: typing.Optional[PrerecordingsEventListRequestAfter] = None,
        before: typing.Optional[PrerecordingsEventListRequestBefore] = None,
        limit: typing.Optional[PrerecordingsEventListRequestLimit] = None,
        offset: typing.Optional[PrerecordingsEventListRequestOffset] = None,
        order: typing.Optional[PrerecordingsEventListRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseResults:
        """
        List prerecordings.

        Parameters
        ----------
        event : ListRequestEvent

        after : typing.Optional[PrerecordingsEventListRequestAfter]
            Only list prerecordings after this datetime (in event timezone).

        before : typing.Optional[PrerecordingsEventListRequestBefore]
            Only list prerecordings before this datetime (in event timezone).

        limit : typing.Optional[PrerecordingsEventListRequestLimit]
            Maximum number of prerecordings to return. Default is 10.

        offset : typing.Optional[PrerecordingsEventListRequestOffset]
            Number of prerecordings to skip.

        order : typing.Optional[PrerecordingsEventListRequestOrder]
            Order to apply to the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseResults
            Request fulfilled, document follows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prerecordings.prerecordings_event_list(
                event="event",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prerecordings_event_list(
            event, after=after, before=before, limit=limit, offset=offset, order=order, request_options=request_options
        )
        return _response.data
