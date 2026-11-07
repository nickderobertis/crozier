

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWatermarkClient, RawWatermarkClient
from .types.apply_watermark_request_prefer import ApplyWatermarkRequestPrefer
from .types.apply_watermark_response import ApplyWatermarkResponse
from .types.detect_watermark_request_prefer import DetectWatermarkRequestPrefer
from .types.detect_watermark_response import DetectWatermarkResponse
from .types.get_watermark_apply_result_response import GetWatermarkApplyResultResponse
from .types.get_watermark_detection_result_response import GetWatermarkDetectionResultResponse


OMIT = typing.cast(typing.Any, ...)


class WatermarkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWatermarkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWatermarkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWatermarkClient
        """
        return self._raw_client

    def apply_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[ApplyWatermarkRequestPrefer] = None,
        strength: typing.Optional[float] = OMIT,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplyWatermarkResponse:
        """
        Apply a watermark to an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.

        Parameters
        ----------
        url : str
            HTTPS URL to the media file (audio, image, or video).

        prefer : typing.Optional[ApplyWatermarkRequestPrefer]
            When set to "wait", the API processes synchronously and returns the completed result.

        strength : typing.Optional[float]
            Watermark strength for image/video. Ignored for audio.

        custom_message : typing.Optional[str]
            Custom message to embed for image/video. Ignored for audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplyWatermarkResponse
            Watermark job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watermark.apply_watermark(
            url="url",
        )
        """
        _response = self._raw_client.apply_watermark(
            url=url, prefer=prefer, strength=strength, custom_message=custom_message, request_options=request_options
        )
        return _response.data

    def get_watermark_apply_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatermarkApplyResultResponse:
        """
        Retrieve the result of a watermark apply job.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatermarkApplyResultResponse
            Apply result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watermark.get_watermark_apply_result(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_watermark_apply_result(uuid_, request_options=request_options)
        return _response.data

    def detect_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[DetectWatermarkRequestPrefer] = None,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DetectWatermarkResponse:
        """
        Detect a watermark in an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.

        Parameters
        ----------
        url : str
            HTTPS URL to the media file (audio, image, or video).

        prefer : typing.Optional[DetectWatermarkRequestPrefer]
            When set to "wait", the API processes synchronously and returns the completed result with metrics.

        custom_message : typing.Optional[str]
            Custom message used during encoding for image/video. Ignored for audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetectWatermarkResponse
            Detection job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watermark.detect_watermark(
            url="url",
        )
        """
        _response = self._raw_client.detect_watermark(
            url=url, prefer=prefer, custom_message=custom_message, request_options=request_options
        )
        return _response.data

    def get_watermark_detection_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatermarkDetectionResultResponse:
        """
        Retrieve the result of a watermark detection.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatermarkDetectionResultResponse
            Detection result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.watermark.get_watermark_detection_result(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_watermark_detection_result(uuid_, request_options=request_options)
        return _response.data


class AsyncWatermarkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWatermarkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWatermarkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWatermarkClient
        """
        return self._raw_client

    async def apply_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[ApplyWatermarkRequestPrefer] = None,
        strength: typing.Optional[float] = OMIT,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplyWatermarkResponse:
        """
        Apply a watermark to an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.

        Parameters
        ----------
        url : str
            HTTPS URL to the media file (audio, image, or video).

        prefer : typing.Optional[ApplyWatermarkRequestPrefer]
            When set to "wait", the API processes synchronously and returns the completed result.

        strength : typing.Optional[float]
            Watermark strength for image/video. Ignored for audio.

        custom_message : typing.Optional[str]
            Custom message to embed for image/video. Ignored for audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplyWatermarkResponse
            Watermark job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watermark.apply_watermark(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply_watermark(
            url=url, prefer=prefer, strength=strength, custom_message=custom_message, request_options=request_options
        )
        return _response.data

    async def get_watermark_apply_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatermarkApplyResultResponse:
        """
        Retrieve the result of a watermark apply job.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatermarkApplyResultResponse
            Apply result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watermark.get_watermark_apply_result(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_watermark_apply_result(uuid_, request_options=request_options)
        return _response.data

    async def detect_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[DetectWatermarkRequestPrefer] = None,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DetectWatermarkResponse:
        """
        Detect a watermark in an audio, image, or video file. The media type is automatically detected from the file content. Use the `Prefer: wait` header for synchronous processing.

        Parameters
        ----------
        url : str
            HTTPS URL to the media file (audio, image, or video).

        prefer : typing.Optional[DetectWatermarkRequestPrefer]
            When set to "wait", the API processes synchronously and returns the completed result with metrics.

        custom_message : typing.Optional[str]
            Custom message used during encoding for image/video. Ignored for audio.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetectWatermarkResponse
            Detection job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watermark.detect_watermark(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detect_watermark(
            url=url, prefer=prefer, custom_message=custom_message, request_options=request_options
        )
        return _response.data

    async def get_watermark_detection_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWatermarkDetectionResultResponse:
        """
        Retrieve the result of a watermark detection.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWatermarkDetectionResultResponse
            Detection result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.watermark.get_watermark_detection_result(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_watermark_detection_result(uuid_, request_options=request_options)
        return _response.data
