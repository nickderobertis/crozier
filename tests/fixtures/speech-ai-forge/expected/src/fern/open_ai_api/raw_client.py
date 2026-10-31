

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.audio_format import AudioFormat
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOpenAiApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def openai_speech_api(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[AudioFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        style: typing.Optional[str] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[float] = OMIT,
        eos: typing.Optional[str] = OMIT,
        enhance: typing.Optional[bool] = OMIT,
        denoise: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        bitrate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        openai api document:
        [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

        以下属性为本系统自定义属性，不在openai文档中：
        - batch_size: 是否开启batch合成，小于等于1表示不使用batch （不推荐）
        - spliter_threshold: 开启batch合成时，句子分割的阈值
        - style: 风格

        > model 可填任意值

        Parameters
        ----------
        input : str

        model : typing.Optional[str]

        voice : typing.Optional[str]

        response_format : typing.Optional[AudioFormat]

        speed : typing.Optional[float]
            Speed of the audio

        seed : typing.Optional[int]

        temperature : typing.Optional[float]

        top_k : typing.Optional[int]

        top_p : typing.Optional[float]

        style : typing.Optional[str]

        batch_size : typing.Optional[int]
            Batch size

        spliter_threshold : typing.Optional[float]
            Threshold for sentence spliter

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        stream : typing.Optional[bool]

        bitrate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/audio/speech",
            method="POST",
            json={
                "input": input,
                "model": model,
                "voice": voice,
                "response_format": response_format,
                "speed": speed,
                "seed": seed,
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p,
                "style": style,
                "batch_size": batch_size,
                "spliter_threshold": spliter_threshold,
                "eos": eos,
                "enhance": enhance,
                "denoise": denoise,
                "stream": stream,
                "bitrate": bitrate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        language : typing.Optional[str]

        prompt : typing.Optional[str]

        response_format : typing.Optional[str]

        temperature : typing.Optional[float]

        timestamp_granularities : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/audio/transcriptions",
            method="POST",
            data={
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamp_granularities": jsonable_encoder(timestamp_granularities)
                if timestamp_granularities is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawOpenAiApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def openai_speech_api(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[AudioFormat] = OMIT,
        speed: typing.Optional[float] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        style: typing.Optional[str] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[float] = OMIT,
        eos: typing.Optional[str] = OMIT,
        enhance: typing.Optional[bool] = OMIT,
        denoise: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        bitrate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        openai api document:
        [https://platform.openai.com/docs/guides/text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

        以下属性为本系统自定义属性，不在openai文档中：
        - batch_size: 是否开启batch合成，小于等于1表示不使用batch （不推荐）
        - spliter_threshold: 开启batch合成时，句子分割的阈值
        - style: 风格

        > model 可填任意值

        Parameters
        ----------
        input : str

        model : typing.Optional[str]

        voice : typing.Optional[str]

        response_format : typing.Optional[AudioFormat]

        speed : typing.Optional[float]
            Speed of the audio

        seed : typing.Optional[int]

        temperature : typing.Optional[float]

        top_k : typing.Optional[int]

        top_p : typing.Optional[float]

        style : typing.Optional[str]

        batch_size : typing.Optional[int]
            Batch size

        spliter_threshold : typing.Optional[float]
            Threshold for sentence spliter

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        stream : typing.Optional[bool]

        bitrate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/audio/speech",
            method="POST",
            json={
                "input": input,
                "model": model,
                "voice": voice,
                "response_format": response_format,
                "speed": speed,
                "seed": seed,
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p,
                "style": style,
                "batch_size": batch_size,
                "spliter_threshold": spliter_threshold,
                "eos": eos,
                "enhance": enhance,
                "denoise": denoise,
                "stream": stream,
                "bitrate": bitrate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        language : typing.Optional[str]

        prompt : typing.Optional[str]

        response_format : typing.Optional[str]

        temperature : typing.Optional[float]

        timestamp_granularities : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/audio/transcriptions",
            method="POST",
            data={
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamp_granularities": jsonable_encoder(timestamp_granularities)
                if timestamp_granularities is not OMIT
                else OMIT,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
