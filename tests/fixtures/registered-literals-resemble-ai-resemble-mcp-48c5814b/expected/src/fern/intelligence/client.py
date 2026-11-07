

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIntelligenceClient, RawIntelligenceClient
from .types.get_intelligence_response import GetIntelligenceResponse
from .types.list_intelligences_response import ListIntelligencesResponse
from .types.run_intelligence_request_media_type import RunIntelligenceRequestMediaType
from .types.run_intelligence_response import RunIntelligenceResponse


OMIT = typing.cast(typing.Any, ...)


class IntelligenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntelligenceClient
        """
        return self._raw_client

    def run_intelligence(
        self,
        *,
        media_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        detect_id: typing.Optional[str] = OMIT,
        media_type: typing.Optional[RunIntelligenceRequestMediaType] = OMIT,
        json: typing.Optional[bool] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunIntelligenceResponse:
        """
        Analyze audio, image, or video for comprehensive insights. Optionally reference an existing detect to associate.

        Parameters
        ----------
        media_token : typing.Optional[str]
            Token for uploaded media file (from secure upload)

        url : typing.Optional[str]
            HTTPS URL to audio, image, or video file

        detect_id : typing.Optional[str]
            UUID of an existing detect to associate

        media_type : typing.Optional[RunIntelligenceRequestMediaType]
            Explicit media type (auto-detected if not provided)

        json : typing.Optional[bool]
            Return structured fields instead of prose. Default false for audio/video, true for images.

        callback_url : typing.Optional[str]
            URL that receives the final intelligence payload via HTTP POST. When present, the request runs asynchronously and returns 202 Accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunIntelligenceResponse
            Intelligence analysis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.intelligence.run_intelligence()
        """
        _response = self._raw_client.run_intelligence(
            media_token=media_token,
            url=url,
            detect_id=detect_id,
            media_type=media_type,
            json=json,
            callback_url=callback_url,
            request_options=request_options,
        )
        return _response.data

    def list_intelligences(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIntelligencesResponse:
        """
        Retrieve a paginated list of all intelligence reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIntelligencesResponse
            List of intelligence reports

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.intelligence.list_intelligences(
            page=1,
        )
        """
        _response = self._raw_client.list_intelligences(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def get_intelligence(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetIntelligenceResponse:
        """
        Retrieve a single intelligence report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the intelligence report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIntelligenceResponse
            Intelligence report

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.intelligence.get_intelligence(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_intelligence(uuid_, request_options=request_options)
        return _response.data


class AsyncIntelligenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntelligenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntelligenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntelligenceClient
        """
        return self._raw_client

    async def run_intelligence(
        self,
        *,
        media_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        detect_id: typing.Optional[str] = OMIT,
        media_type: typing.Optional[RunIntelligenceRequestMediaType] = OMIT,
        json: typing.Optional[bool] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunIntelligenceResponse:
        """
        Analyze audio, image, or video for comprehensive insights. Optionally reference an existing detect to associate.

        Parameters
        ----------
        media_token : typing.Optional[str]
            Token for uploaded media file (from secure upload)

        url : typing.Optional[str]
            HTTPS URL to audio, image, or video file

        detect_id : typing.Optional[str]
            UUID of an existing detect to associate

        media_type : typing.Optional[RunIntelligenceRequestMediaType]
            Explicit media type (auto-detected if not provided)

        json : typing.Optional[bool]
            Return structured fields instead of prose. Default false for audio/video, true for images.

        callback_url : typing.Optional[str]
            URL that receives the final intelligence payload via HTTP POST. When present, the request runs asynchronously and returns 202 Accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunIntelligenceResponse
            Intelligence analysis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.intelligence.run_intelligence()


        asyncio.run(main())
        """
        _response = await self._raw_client.run_intelligence(
            media_token=media_token,
            url=url,
            detect_id=detect_id,
            media_type=media_type,
            json=json,
            callback_url=callback_url,
            request_options=request_options,
        )
        return _response.data

    async def list_intelligences(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIntelligencesResponse:
        """
        Retrieve a paginated list of all intelligence reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIntelligencesResponse
            List of intelligence reports

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.intelligence.list_intelligences(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_intelligences(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_intelligence(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetIntelligenceResponse:
        """
        Retrieve a single intelligence report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the intelligence report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIntelligenceResponse
            Intelligence report

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.intelligence.get_intelligence(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_intelligence(uuid_, request_options=request_options)
        return _response.data
