

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from .types.create_detection_request_model_types import CreateDetectionRequestModelTypes
from .types.create_detection_response import CreateDetectionResponse
from .types.get_detection_response import GetDetectionResponse
from .types.list_detections_response import ListDetectionsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeepfakeDetectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_detections(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDetectionsResponse]:
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
        HttpResponse[ListDetectionsResponse]
            List of detects
        """
        _response = self._client_wrapper.httpx_client.request(
            "detect",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDetectionsResponse,
                    parse_obj_as(
                        type_=ListDetectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CreateDetectionResponse]:
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
        HttpResponse[CreateDetectionResponse]
            Detection job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "detect",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "callback_url": callback_url,
                "visualize": visualize,
                "frame_length": frame_length,
                "start_region": start_region,
                "end_region": end_region,
                "max_video_fps": max_video_fps,
                "max_video_secs": max_video_secs,
                "model_types": model_types,
                "intelligence": intelligence,
                "audio_source_tracing": audio_source_tracing,
                "use_reverse_search": use_reverse_search,
                "use_ood_detector": use_ood_detector,
                "zero_retention_mode": zero_retention_mode,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDetectionResponse,
                    parse_obj_as(
                        type_=CreateDetectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_detection(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDetectionResponse]:
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
        HttpResponse[GetDetectionResponse]
            Detection result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"detect/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDetectionResponse,
                    parse_obj_as(
                        type_=GetDetectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDeepfakeDetectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_detections(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDetectionsResponse]:
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
        AsyncHttpResponse[ListDetectionsResponse]
            List of detects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "detect",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDetectionsResponse,
                    parse_obj_as(
                        type_=ListDetectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CreateDetectionResponse]:
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
        AsyncHttpResponse[CreateDetectionResponse]
            Detection job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "detect",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "callback_url": callback_url,
                "visualize": visualize,
                "frame_length": frame_length,
                "start_region": start_region,
                "end_region": end_region,
                "max_video_fps": max_video_fps,
                "max_video_secs": max_video_secs,
                "model_types": model_types,
                "intelligence": intelligence,
                "audio_source_tracing": audio_source_tracing,
                "use_reverse_search": use_reverse_search,
                "use_ood_detector": use_ood_detector,
                "zero_retention_mode": zero_retention_mode,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDetectionResponse,
                    parse_obj_as(
                        type_=CreateDetectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_detection(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDetectionResponse]:
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
        AsyncHttpResponse[GetDetectionResponse]
            Detection result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"detect/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDetectionResponse,
                    parse_obj_as(
                        type_=GetDetectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
