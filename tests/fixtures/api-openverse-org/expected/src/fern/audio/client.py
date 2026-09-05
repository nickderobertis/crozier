

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.audio import Audio
from ..types.paginated_audio_results import PaginatedAudioResults
from ..types.report_request_reason import ReportRequestReason
from ..types.source_stats import SourceStats
from .raw_client import AsyncRawAudioClient, RawAudioClient
from .types.get_audio_waveform_response import GetAudioWaveformResponse
from .types.search_audio_request_category import SearchAudioRequestCategory
from .types.search_audio_request_length import SearchAudioRequestLength


OMIT = typing.cast(typing.Any, ...)


class AudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioClient
        """
        return self._raw_client

    def search_audio(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        category: typing.Optional[SearchAudioRequestCategory] = None,
        length: typing.Optional[SearchAudioRequestLength] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAudioResults:
        """
        Search for openly-licensed audio files with filtering and pagination.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        category : typing.Optional[SearchAudioRequestCategory]
            Filter by audio category

        length : typing.Optional[SearchAudioRequestLength]
            Filter by audio duration

        extension : typing.Optional[str]
            Filter by file extension (e.g., mp3, ogg, flac)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAudioResults
            Successful audio search results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.search_audio()
        """
        _response = self._raw_client.search_audio(
            q=q,
            page=page,
            page_size=page_size,
            license=license,
            license_type=license_type,
            source=source,
            excluded_source=excluded_source,
            creator=creator,
            tags=tags,
            title=title,
            mature=mature,
            filter_dead=filter_dead,
            category=category,
            length=length,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    def get_audio(self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None) -> Audio:
        """
        Retrieve detailed information about a specific audio file by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Audio
            Audio details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.get_audio(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_audio(identifier, request_options=request_options)
        return _response.data

    def get_related_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedAudioResults:
        """
        Find audio files related to a specified audio.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAudioResults
            Related audio

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.get_related_audio(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_related_audio(identifier, request_options=request_options)
        return _response.data

    def report_audio(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Report an audio file for issues such as DMCA violations or mature content.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ReportRequestReason

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.report_audio(
            identifier="identifier",
            reason=ReportRequestReason.MATURE,
        )
        """
        _response = self._raw_client.report_audio(
            identifier, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    def get_audio_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Retrieve a thumbnail for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Thumbnail image

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.get_audio_thumbnail(
            identifier="identifier",
        )
        """
        with self._raw_client.get_audio_thumbnail(identifier, request_options=request_options) as r:
            yield from r.data

    def get_audio_waveform(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioWaveformResponse:
        """
        Retrieve waveform peak data for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioWaveformResponse
            Waveform data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.get_audio_waveform(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_audio_waveform(identifier, request_options=request_options)
        return _response.data

    def get_audio_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[SourceStats]:
        """
        List all content sources for audio and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceStats]
            Audio source statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio.get_audio_stats()
        """
        _response = self._raw_client.get_audio_stats(request_options=request_options)
        return _response.data


class AsyncAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioClient
        """
        return self._raw_client

    async def search_audio(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        category: typing.Optional[SearchAudioRequestCategory] = None,
        length: typing.Optional[SearchAudioRequestLength] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAudioResults:
        """
        Search for openly-licensed audio files with filtering and pagination.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        category : typing.Optional[SearchAudioRequestCategory]
            Filter by audio category

        length : typing.Optional[SearchAudioRequestLength]
            Filter by audio duration

        extension : typing.Optional[str]
            Filter by file extension (e.g., mp3, ogg, flac)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAudioResults
            Successful audio search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.search_audio()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_audio(
            q=q,
            page=page,
            page_size=page_size,
            license=license,
            license_type=license_type,
            source=source,
            excluded_source=excluded_source,
            creator=creator,
            tags=tags,
            title=title,
            mature=mature,
            filter_dead=filter_dead,
            category=category,
            length=length,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    async def get_audio(self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None) -> Audio:
        """
        Retrieve detailed information about a specific audio file by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Audio
            Audio details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.get_audio(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio(identifier, request_options=request_options)
        return _response.data

    async def get_related_audio(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedAudioResults:
        """
        Find audio files related to a specified audio.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAudioResults
            Related audio

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.get_related_audio(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_related_audio(identifier, request_options=request_options)
        return _response.data

    async def report_audio(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Report an audio file for issues such as DMCA violations or mature content.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ReportRequestReason

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.report_audio(
                identifier="identifier",
                reason=ReportRequestReason.MATURE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_audio(
            identifier, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    async def get_audio_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Retrieve a thumbnail for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Thumbnail image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.get_audio_thumbnail(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_audio_thumbnail(identifier, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_audio_waveform(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioWaveformResponse:
        """
        Retrieve waveform peak data for the specified audio file.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioWaveformResponse
            Waveform data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.get_audio_waveform(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_waveform(identifier, request_options=request_options)
        return _response.data

    async def get_audio_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceStats]:
        """
        List all content sources for audio and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceStats]
            Audio source statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio.get_audio_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_stats(request_options=request_options)
        return _response.data
