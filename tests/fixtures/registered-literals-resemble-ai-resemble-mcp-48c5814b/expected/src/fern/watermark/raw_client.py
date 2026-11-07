

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.apply_watermark_request_prefer import ApplyWatermarkRequestPrefer
from .types.apply_watermark_response import ApplyWatermarkResponse
from .types.detect_watermark_request_prefer import DetectWatermarkRequestPrefer
from .types.detect_watermark_response import DetectWatermarkResponse
from .types.get_watermark_apply_result_response import GetWatermarkApplyResultResponse
from .types.get_watermark_detection_result_response import GetWatermarkDetectionResultResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWatermarkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def apply_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[ApplyWatermarkRequestPrefer] = None,
        strength: typing.Optional[float] = OMIT,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplyWatermarkResponse]:
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
        HttpResponse[ApplyWatermarkResponse]
            Watermark job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "watermark/apply",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "strength": strength,
                "custom_message": custom_message,
            },
            headers={
                "content-type": "application/json",
                "Prefer": prefer.value if prefer is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplyWatermarkResponse,
                    parse_obj_as(
                        type_=ApplyWatermarkResponse,
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

    def get_watermark_apply_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWatermarkApplyResultResponse]:
        """
        Retrieve the result of a watermark apply job.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWatermarkApplyResultResponse]
            Apply result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"watermark/apply/{encode_path_param(uuid_)}/result",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWatermarkApplyResultResponse,
                    parse_obj_as(
                        type_=GetWatermarkApplyResultResponse,
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

    def detect_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[DetectWatermarkRequestPrefer] = None,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DetectWatermarkResponse]:
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
        HttpResponse[DetectWatermarkResponse]
            Detection job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "watermark/detect",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "custom_message": custom_message,
            },
            headers={
                "content-type": "application/json",
                "Prefer": prefer.value if prefer is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetectWatermarkResponse,
                    parse_obj_as(
                        type_=DetectWatermarkResponse,
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

    def get_watermark_detection_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWatermarkDetectionResultResponse]:
        """
        Retrieve the result of a watermark detection.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWatermarkDetectionResultResponse]
            Detection result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"watermark/detect/{encode_path_param(uuid_)}/result",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWatermarkDetectionResultResponse,
                    parse_obj_as(
                        type_=GetWatermarkDetectionResultResponse,
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


class AsyncRawWatermarkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def apply_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[ApplyWatermarkRequestPrefer] = None,
        strength: typing.Optional[float] = OMIT,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplyWatermarkResponse]:
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
        AsyncHttpResponse[ApplyWatermarkResponse]
            Watermark job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "watermark/apply",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "strength": strength,
                "custom_message": custom_message,
            },
            headers={
                "content-type": "application/json",
                "Prefer": prefer.value if prefer is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplyWatermarkResponse,
                    parse_obj_as(
                        type_=ApplyWatermarkResponse,
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

    async def get_watermark_apply_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWatermarkApplyResultResponse]:
        """
        Retrieve the result of a watermark apply job.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWatermarkApplyResultResponse]
            Apply result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"watermark/apply/{encode_path_param(uuid_)}/result",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWatermarkApplyResultResponse,
                    parse_obj_as(
                        type_=GetWatermarkApplyResultResponse,
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

    async def detect_watermark(
        self,
        *,
        url: str,
        prefer: typing.Optional[DetectWatermarkRequestPrefer] = None,
        custom_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DetectWatermarkResponse]:
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
        AsyncHttpResponse[DetectWatermarkResponse]
            Detection job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "watermark/detect",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "url": url,
                "custom_message": custom_message,
            },
            headers={
                "content-type": "application/json",
                "Prefer": prefer.value if prefer is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetectWatermarkResponse,
                    parse_obj_as(
                        type_=DetectWatermarkResponse,
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

    async def get_watermark_detection_result(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWatermarkDetectionResultResponse]:
        """
        Retrieve the result of a watermark detection.

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWatermarkDetectionResultResponse]
            Detection result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"watermark/detect/{encode_path_param(uuid_)}/result",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWatermarkDetectionResultResponse,
                    parse_obj_as(
                        type_=GetWatermarkDetectionResultResponse,
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
