

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDeepfakeDetectionClient, RawDeepfakeDetectionClient
from .types.create_detection_request_model_types import CreateDetectionRequestModelTypes
from .types.create_detection_response import CreateDetectionResponse
from .types.get_detection_response import GetDetectionResponse
from .types.list_detections_response import ListDetectionsResponse


OMIT = typing.cast(typing.Any, ...)


class DeepfakeDetectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeepfakeDetectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeepfakeDetectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeepfakeDetectionClient
        """
        return self._raw_client

    def list_detections(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDetectionsResponse:
        """
        Retrieve a paginated list of all detect objects for the authenticated user's team

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
        ListDetectionsResponse
            List of detects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deepfake_detection.list_detections(
            page=1,
        )
        """
        _response = self._raw_client.list_detections(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def create_detection(
        self,
        *,
        url: str,
        callback_url: typing.Optional[str] = OMIT,
        visualize: typing.Optional[bool] = OMIT,
        frame_length: typing.Optional[int] = OMIT,
        start_region: typing.Optional[float] = OMIT,
        end_region: typing.Optional[float] = OMIT,
        max_video_fps: typing.Optional[float] = OMIT,
        max_video_secs: typing.Optional[float] = OMIT,
        model_types: typing.Optional[CreateDetectionRequestModelTypes] = OMIT,
        intelligence: typing.Optional[bool] = OMIT,
        audio_source_tracing: typing.Optional[bool] = OMIT,
        use_reverse_search: typing.Optional[bool] = OMIT,
        use_ood_detector: typing.Optional[bool] = OMIT,
        zero_retention_mode: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDetectionResponse:
        """
        Analyze audio, image, and video for deepfake detection

        Parameters
        ----------
        url : str
            HTTPS URL to audio, image, or video file

        callback_url : typing.Optional[str]
            POST destination when analysis completes

        visualize : typing.Optional[bool]
            Generate visualization artifacts

        frame_length : typing.Optional[int]
            Window size in seconds (audio/video)

        start_region : typing.Optional[float]
            Start of segment to analyze (seconds)

        end_region : typing.Optional[float]
            End of segment to analyze (seconds)

        max_video_fps : typing.Optional[float]
            Downsample high-frame-rate media

        max_video_secs : typing.Optional[float]
            Cap processed duration

        model_types : typing.Optional[CreateDetectionRequestModelTypes]
            Use talking_head for face-swaps

        intelligence : typing.Optional[bool]
            Run multimodal intelligence analysis on the media

        audio_source_tracing : typing.Optional[bool]
            Enable audio source tracing to identify synthetic audio origin

        use_reverse_search : typing.Optional[bool]
            Enable reverse image search to improve detection accuracy for image files. Searches the web for matching images and uses AI to classify whether the match indicates a known fake. Only applies to image detections.

        use_ood_detector : typing.Optional[bool]
            Enable out-of-distribution detection

        zero_retention_mode : typing.Optional[bool]
            Enable Zero Retention Mode to automatically delete submitted media after detection completes. When enabled, media URLs are redacted and the filename is tokenized.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDetectionResponse
            Detection job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deepfake_detection.create_detection(
            url="url",
        )
        """
        _response = self._raw_client.create_detection(
            url=url,
            callback_url=callback_url,
            visualize=visualize,
            frame_length=frame_length,
            start_region=start_region,
            end_region=end_region,
            max_video_fps=max_video_fps,
            max_video_secs=max_video_secs,
            model_types=model_types,
            intelligence=intelligence,
            audio_source_tracing=audio_source_tracing,
            use_reverse_search=use_reverse_search,
            use_ood_detector=use_ood_detector,
            zero_retention_mode=zero_retention_mode,
            request_options=request_options,
        )
        return _response.data

    def get_detection(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDetectionResponse:
        """
        Get deepfake detection result by UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the detect object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDetectionResponse
            Detection result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deepfake_detection.get_detection(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_detection(uuid_, request_options=request_options)
        return _response.data


class AsyncDeepfakeDetectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeepfakeDetectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeepfakeDetectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeepfakeDetectionClient
        """
        return self._raw_client

    async def list_detections(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListDetectionsResponse:
        """
        Retrieve a paginated list of all detect objects for the authenticated user's team

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
        ListDetectionsResponse
            List of detects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deepfake_detection.list_detections(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_detections(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_detection(
        self,
        *,
        url: str,
        callback_url: typing.Optional[str] = OMIT,
        visualize: typing.Optional[bool] = OMIT,
        frame_length: typing.Optional[int] = OMIT,
        start_region: typing.Optional[float] = OMIT,
        end_region: typing.Optional[float] = OMIT,
        max_video_fps: typing.Optional[float] = OMIT,
        max_video_secs: typing.Optional[float] = OMIT,
        model_types: typing.Optional[CreateDetectionRequestModelTypes] = OMIT,
        intelligence: typing.Optional[bool] = OMIT,
        audio_source_tracing: typing.Optional[bool] = OMIT,
        use_reverse_search: typing.Optional[bool] = OMIT,
        use_ood_detector: typing.Optional[bool] = OMIT,
        zero_retention_mode: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDetectionResponse:
        """
        Analyze audio, image, and video for deepfake detection

        Parameters
        ----------
        url : str
            HTTPS URL to audio, image, or video file

        callback_url : typing.Optional[str]
            POST destination when analysis completes

        visualize : typing.Optional[bool]
            Generate visualization artifacts

        frame_length : typing.Optional[int]
            Window size in seconds (audio/video)

        start_region : typing.Optional[float]
            Start of segment to analyze (seconds)

        end_region : typing.Optional[float]
            End of segment to analyze (seconds)

        max_video_fps : typing.Optional[float]
            Downsample high-frame-rate media

        max_video_secs : typing.Optional[float]
            Cap processed duration

        model_types : typing.Optional[CreateDetectionRequestModelTypes]
            Use talking_head for face-swaps

        intelligence : typing.Optional[bool]
            Run multimodal intelligence analysis on the media

        audio_source_tracing : typing.Optional[bool]
            Enable audio source tracing to identify synthetic audio origin

        use_reverse_search : typing.Optional[bool]
            Enable reverse image search to improve detection accuracy for image files. Searches the web for matching images and uses AI to classify whether the match indicates a known fake. Only applies to image detections.

        use_ood_detector : typing.Optional[bool]
            Enable out-of-distribution detection

        zero_retention_mode : typing.Optional[bool]
            Enable Zero Retention Mode to automatically delete submitted media after detection completes. When enabled, media URLs are redacted and the filename is tokenized.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDetectionResponse
            Detection job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deepfake_detection.create_detection(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_detection(
            url=url,
            callback_url=callback_url,
            visualize=visualize,
            frame_length=frame_length,
            start_region=start_region,
            end_region=end_region,
            max_video_fps=max_video_fps,
            max_video_secs=max_video_secs,
            model_types=model_types,
            intelligence=intelligence,
            audio_source_tracing=audio_source_tracing,
            use_reverse_search=use_reverse_search,
            use_ood_detector=use_ood_detector,
            zero_retention_mode=zero_retention_mode,
            request_options=request_options,
        )
        return _response.data

    async def get_detection(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDetectionResponse:
        """
        Get deepfake detection result by UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the detect object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDetectionResponse
            Detection result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deepfake_detection.get_detection(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_detection(uuid_, request_options=request_options)
        return _response.data
