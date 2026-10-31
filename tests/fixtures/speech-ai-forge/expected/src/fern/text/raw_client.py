

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
from ..types.base_response import BaseResponse
from ..types.http_validation_error import HttpValidationError
from ..types.tn_config import TnConfig
from .types.text_normalize_request_pipe_id import TextNormalizeRequestPipeId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def refiner_prompt_post(
        self,
        *,
        text: str,
        prompt: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        max_new_token: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        **DeprecationWarning**

        This endpoint is deprecated and will be removed in the future.

        Requirements:
        - `chattts` model

        Parameters
        ----------
        text : str

        prompt : typing.Optional[str]

        seed : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        temperature : typing.Optional[float]

        repetition_penalty : typing.Optional[float]

        max_new_token : typing.Optional[int]

        spliter_threshold : typing.Optional[int]

        normalize : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompt/refine",
            method="POST",
            json={
                "text": text,
                "prompt": prompt,
                "seed": seed,
                "top_P": top_p,
                "top_K": top_k,
                "temperature": temperature,
                "repetition_penalty": repetition_penalty,
                "max_new_token": max_new_token,
                "spliter_threshold": spliter_threshold,
                "normalize": normalize,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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

    def text_normalize_post(
        self,
        *,
        text: str,
        pipe_id: typing.Optional[TextNormalizeRequestPipeId] = OMIT,
        config: typing.Optional[TnConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaseResponse]:
        """
        Normalize raw input text using a selected Text Normalization (TN) pipeline.

        This endpoint supports different TN implementations to perform text normalization
        (e.g., expanding numbers, abbreviations, adding pauses or prosodic markers for TTS, etc.).

        ### Parameters

        - `text` (str): The raw text to normalize.
        - `pipe_id` (str): The TN pipeline to use. Available options:
          - `base`
          - `chat-tts`
          - `cosy-voice`
          - `fish-speech`
          - `f5-tts`
          - `index-tts`
          - `spark-tts`
        - `config` (TNConfig, optional): Optional configuration to customize TN behavior for specific pipelines.

        ### Returns

        A normalized version of the input text, suitable for use in speech synthesis or downstream NLP tasks.

        Parameters
        ----------
        text : str

        pipe_id : typing.Optional[TextNormalizeRequestPipeId]

        config : typing.Optional[TnConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BaseResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/text/normalize",
            method="POST",
            json={
                "text": text,
                "pipe_id": pipe_id,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=typing.Optional[TnConfig], direction="write"
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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


class AsyncRawTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def refiner_prompt_post(
        self,
        *,
        text: str,
        prompt: typing.Optional[str] = OMIT,
        seed: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        max_new_token: typing.Optional[int] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        **DeprecationWarning**

        This endpoint is deprecated and will be removed in the future.

        Requirements:
        - `chattts` model

        Parameters
        ----------
        text : str

        prompt : typing.Optional[str]

        seed : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        temperature : typing.Optional[float]

        repetition_penalty : typing.Optional[float]

        max_new_token : typing.Optional[int]

        spliter_threshold : typing.Optional[int]

        normalize : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompt/refine",
            method="POST",
            json={
                "text": text,
                "prompt": prompt,
                "seed": seed,
                "top_P": top_p,
                "top_K": top_k,
                "temperature": temperature,
                "repetition_penalty": repetition_penalty,
                "max_new_token": max_new_token,
                "spliter_threshold": spliter_threshold,
                "normalize": normalize,
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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

    async def text_normalize_post(
        self,
        *,
        text: str,
        pipe_id: typing.Optional[TextNormalizeRequestPipeId] = OMIT,
        config: typing.Optional[TnConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaseResponse]:
        """
        Normalize raw input text using a selected Text Normalization (TN) pipeline.

        This endpoint supports different TN implementations to perform text normalization
        (e.g., expanding numbers, abbreviations, adding pauses or prosodic markers for TTS, etc.).

        ### Parameters

        - `text` (str): The raw text to normalize.
        - `pipe_id` (str): The TN pipeline to use. Available options:
          - `base`
          - `chat-tts`
          - `cosy-voice`
          - `fish-speech`
          - `f5-tts`
          - `index-tts`
          - `spark-tts`
        - `config` (TNConfig, optional): Optional configuration to customize TN behavior for specific pipelines.

        ### Returns

        A normalized version of the input text, suitable for use in speech synthesis or downstream NLP tasks.

        Parameters
        ----------
        text : str

        pipe_id : typing.Optional[TextNormalizeRequestPipeId]

        config : typing.Optional[TnConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BaseResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/text/normalize",
            method="POST",
            json={
                "text": text,
                "pipe_id": pipe_id,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=typing.Optional[TnConfig], direction="write"
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
                    BaseResponse,
                    parse_obj_as(
                        type_=BaseResponse,
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
