

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.stt_output_format import SttOutputFormat
from ..types.transcriptions_response import TranscriptionsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSttClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TranscriptionsResponse]:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TranscriptionsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/stt/transcribe",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "prefix": prefix,
                "language": language,
                "temperature": temperature,
                "sample_len": sample_len,
                "best_of": best_of,
                "beam_size": beam_size,
                "patience": patience,
                "length_penalty": length_penalty,
                "format": format,
                "highlight_words": highlight_words,
                "max_line_count": max_line_count,
                "max_line_width": max_line_width,
                "max_words_per_line": max_words_per_line,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranscriptionsResponse,
                    parse_obj_as(
                        type_=TranscriptionsResponse,
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

    def transcribe_stream(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Transcribes audio into the input language in real-time.

        * Not implemented yet (WIP)

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/stt/stream",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "prefix": prefix,
                "language": language,
                "temperature": temperature,
                "sample_len": sample_len,
                "best_of": best_of,
                "beam_size": beam_size,
                "patience": patience,
                "length_penalty": length_penalty,
                "format": format,
                "highlight_words": highlight_words,
                "max_line_count": max_line_count,
                "max_line_width": max_line_width,
                "max_words_per_line": max_words_per_line,
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


class AsyncRawSttClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def transcribe(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TranscriptionsResponse]:
        """
        Transcribes audio into the input language.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TranscriptionsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/stt/transcribe",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "prefix": prefix,
                "language": language,
                "temperature": temperature,
                "sample_len": sample_len,
                "best_of": best_of,
                "beam_size": beam_size,
                "patience": patience,
                "length_penalty": length_penalty,
                "format": format,
                "highlight_words": highlight_words,
                "max_line_count": max_line_count,
                "max_line_width": max_line_width,
                "max_words_per_line": max_words_per_line,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TranscriptionsResponse,
                    parse_obj_as(
                        type_=TranscriptionsResponse,
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

    async def transcribe_stream(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[int] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Transcribes audio into the input language in real-time.

        * Not implemented yet (WIP)

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        model : typing.Optional[str]

        prompt : typing.Optional[str]

        prefix : typing.Optional[str]

        language : typing.Optional[str]

        temperature : typing.Optional[float]

        sample_len : typing.Optional[int]

        best_of : typing.Optional[int]

        beam_size : typing.Optional[int]

        patience : typing.Optional[int]

        length_penalty : typing.Optional[float]

        format : typing.Optional[SttOutputFormat]

        highlight_words : typing.Optional[bool]

        max_line_count : typing.Optional[int]

        max_line_width : typing.Optional[int]

        max_words_per_line : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/stt/stream",
            method="POST",
            data={
                "model": model,
                "prompt": prompt,
                "prefix": prefix,
                "language": language,
                "temperature": temperature,
                "sample_len": sample_len,
                "best_of": best_of,
                "beam_size": beam_size,
                "patience": patience,
                "length_penalty": length_penalty,
                "format": format,
                "highlight_words": highlight_words,
                "max_line_count": max_line_count,
                "max_line_width": max_line_width,
                "max_words_per_line": max_words_per_line,
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
