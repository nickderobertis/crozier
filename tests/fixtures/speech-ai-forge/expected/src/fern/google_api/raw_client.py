

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.audio_config import AudioConfig
from ..types.enhancer_config import EnhancerConfig
from ..types.google_text_synthesize_response import GoogleTextSynthesizeResponse
from ..types.http_validation_error import HttpValidationError
from ..types.synthesis_input import SynthesisInput
from ..types.voice_selection_params import VoiceSelectionParams
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGoogleApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def google_text_synthesize(
        self,
        *,
        input: SynthesisInput,
        voice: VoiceSelectionParams,
        audio_config: AudioConfig,
        enhancer_config: typing.Optional[EnhancerConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GoogleTextSynthesizeResponse]:
        """
        google api document: <br/>
        [https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize)

        - 多个属性在本系统中无用仅仅是为了兼容google api
        - voice 中的 topP, topK, temperature 为本系统中的参数
        - voice.name 即 speaker name （或者speaker seed）
        - voice.seed 为 infer seed （可在webui中测试具体作用）

        - 编码格式影响的是 audioContent 的二进制格式，所以所有format都是返回带有base64数据的json

        Parameters
        ----------
        input : SynthesisInput

        voice : VoiceSelectionParams

        audio_config : AudioConfig

        enhancer_config : typing.Optional[EnhancerConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GoogleTextSynthesizeResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/text:synthesize",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=SynthesisInput, direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=VoiceSelectionParams, direction="write"
                ),
                "audioConfig": convert_and_respect_annotation_metadata(
                    object_=audio_config, annotation=AudioConfig, direction="write"
                ),
                "enhancerConfig": convert_and_respect_annotation_metadata(
                    object_=enhancer_config, annotation=EnhancerConfig, direction="write"
                ),
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
                    GoogleTextSynthesizeResponse,
                    parse_obj_as(
                        type_=GoogleTextSynthesizeResponse,
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

    def speech_recognize(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        Performs synchronous speech recognition: receive results after all audio has been sent and processed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speech:recognize",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def long_running_recognize(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/speech:longrunningrecognize",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGoogleApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def google_text_synthesize(
        self,
        *,
        input: SynthesisInput,
        voice: VoiceSelectionParams,
        audio_config: AudioConfig,
        enhancer_config: typing.Optional[EnhancerConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GoogleTextSynthesizeResponse]:
        """
        google api document: <br/>
        [https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize)

        - 多个属性在本系统中无用仅仅是为了兼容google api
        - voice 中的 topP, topK, temperature 为本系统中的参数
        - voice.name 即 speaker name （或者speaker seed）
        - voice.seed 为 infer seed （可在webui中测试具体作用）

        - 编码格式影响的是 audioContent 的二进制格式，所以所有format都是返回带有base64数据的json

        Parameters
        ----------
        input : SynthesisInput

        voice : VoiceSelectionParams

        audio_config : AudioConfig

        enhancer_config : typing.Optional[EnhancerConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GoogleTextSynthesizeResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/text:synthesize",
            method="POST",
            json={
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=SynthesisInput, direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=VoiceSelectionParams, direction="write"
                ),
                "audioConfig": convert_and_respect_annotation_metadata(
                    object_=audio_config, annotation=AudioConfig, direction="write"
                ),
                "enhancerConfig": convert_and_respect_annotation_metadata(
                    object_=enhancer_config, annotation=EnhancerConfig, direction="write"
                ),
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
                    GoogleTextSynthesizeResponse,
                    parse_obj_as(
                        type_=GoogleTextSynthesizeResponse,
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

    async def speech_recognize(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Performs synchronous speech recognition: receive results after all audio has been sent and processed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speech:recognize",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def long_running_recognize(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/speech:longrunningrecognize",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
