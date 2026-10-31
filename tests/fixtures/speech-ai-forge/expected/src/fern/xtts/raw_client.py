

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawXttsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def speakers(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

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
            "v1/xtts_v2/speakers",
            method="GET",
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

    def tts_to_audio(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/tts_to_audio",
            method="POST",
            json={
                "text": text,
                "speaker_wav": speaker_wav,
                "language": language,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def tts_stream(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = None,
        no_cache: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        no_cache : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/tts_stream",
            method="GET",
            params={
                "text": text,
                "speaker_wav": speaker_wav,
                "language": language,
                "no_cache": no_cache,
            },
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

    def set_tts_settings(
        self,
        *,
        stream_chunk_size: int,
        temperature: float,
        speed: float,
        length_penalty: float,
        repetition_penalty: float,
        top_p: float,
        top_k: int,
        enable_text_splitting: bool,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        infer_seed: typing.Optional[int] = OMIT,
        use_decoder: typing.Optional[bool] = OMIT,
        prompt1: typing.Optional[str] = OMIT,
        prompt2: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        style: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        stream_chunk_size : int

        temperature : float

        speed : float

        length_penalty : float

        repetition_penalty : float

        top_p : float

        top_k : int

        enable_text_splitting : bool

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        infer_seed : typing.Optional[int]

        use_decoder : typing.Optional[bool]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        spliter_threshold : typing.Optional[int]

        style : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/set_tts_settings",
            method="POST",
            json={
                "stream_chunk_size": stream_chunk_size,
                "temperature": temperature,
                "speed": speed,
                "length_penalty": length_penalty,
                "repetition_penalty": repetition_penalty,
                "top_p": top_p,
                "top_k": top_k,
                "enable_text_splitting": enable_text_splitting,
                "batch_size": batch_size,
                "eos": eos,
                "infer_seed": infer_seed,
                "use_decoder": use_decoder,
                "prompt1": prompt1,
                "prompt2": prompt2,
                "prefix": prefix,
                "spliter_threshold": spliter_threshold,
                "style": style,
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


class AsyncRawXttsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def speakers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

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
            "v1/xtts_v2/speakers",
            method="GET",
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

    async def tts_to_audio(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/tts_to_audio",
            method="POST",
            json={
                "text": text,
                "speaker_wav": speaker_wav,
                "language": language,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def tts_stream(
        self,
        *,
        text: str,
        speaker_wav: str,
        language: typing.Optional[str] = None,
        no_cache: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        text : str

        speaker_wav : str

        language : typing.Optional[str]

        no_cache : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/tts_stream",
            method="GET",
            params={
                "text": text,
                "speaker_wav": speaker_wav,
                "language": language,
                "no_cache": no_cache,
            },
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

    async def set_tts_settings(
        self,
        *,
        stream_chunk_size: int,
        temperature: float,
        speed: float,
        length_penalty: float,
        repetition_penalty: float,
        top_p: float,
        top_k: int,
        enable_text_splitting: bool,
        batch_size: typing.Optional[int] = OMIT,
        eos: typing.Optional[str] = OMIT,
        infer_seed: typing.Optional[int] = OMIT,
        use_decoder: typing.Optional[bool] = OMIT,
        prompt1: typing.Optional[str] = OMIT,
        prompt2: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        spliter_threshold: typing.Optional[int] = OMIT,
        style: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        [[Click To XTTS_V2 API Document]](https://github.com/lenML/Speech-AI-Forge/blob/main/docs/api_xtts.md)

        [[Learn More About Documents]](https://github.com/lenML/Speech-AI-Forge/issues/240)

        Parameters
        ----------
        stream_chunk_size : int

        temperature : float

        speed : float

        length_penalty : float

        repetition_penalty : float

        top_p : float

        top_k : int

        enable_text_splitting : bool

        batch_size : typing.Optional[int]

        eos : typing.Optional[str]

        infer_seed : typing.Optional[int]

        use_decoder : typing.Optional[bool]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        spliter_threshold : typing.Optional[int]

        style : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/xtts_v2/set_tts_settings",
            method="POST",
            json={
                "stream_chunk_size": stream_chunk_size,
                "temperature": temperature,
                "speed": speed,
                "length_penalty": length_penalty,
                "repetition_penalty": repetition_penalty,
                "top_p": top_p,
                "top_k": top_k,
                "enable_text_splitting": enable_text_splitting,
                "batch_size": batch_size,
                "eos": eos,
                "infer_seed": infer_seed,
                "use_decoder": use_decoder,
                "prompt1": prompt1,
                "prompt2": prompt2,
                "prefix": prefix,
                "spliter_threshold": spliter_threshold,
                "style": style,
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
