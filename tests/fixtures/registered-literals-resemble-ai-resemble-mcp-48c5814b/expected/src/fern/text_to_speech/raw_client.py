

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from .types.stream_synthesize_request_precision import StreamSynthesizeRequestPrecision
from .types.synthesize_request_output_format import SynthesizeRequestOutputFormat
from .types.synthesize_request_precision import SynthesizeRequestPrecision
from .types.synthesize_response import SynthesizeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTextToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[SynthesizeRequestPrecision] = OMIT,
        output_format: typing.Optional[SynthesizeRequestOutputFormat] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SynthesizeResponse]:
        """
        Generate speech synchronously from text or SSML. Returns complete audio as base64.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 3,000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        title : typing.Optional[str]
            Optional title for the generated clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[SynthesizeRequestPrecision]
            Audio precision for WAV output

        output_format : typing.Optional[SynthesizeRequestOutputFormat]
            Audio output format

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SynthesizeResponse]
            Successful synthesis
        """
        _response = self._client_wrapper.httpx_client.request(
            "synthesize",
            base_url=self._client_wrapper.get_environment().synthesis,
            method="POST",
            json={
                "voice_uuid": voice_uuid,
                "project_uuid": project_uuid,
                "title": title,
                "data": data,
                "model": model,
                "precision": precision,
                "output_format": output_format,
                "sample_rate": sample_rate,
                "use_hd": use_hd,
                "apply_custom_pronunciations": apply_custom_pronunciations,
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
                    SynthesizeResponse,
                    parse_obj_as(
                        type_=SynthesizeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    @contextlib.contextmanager
    def stream_synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[StreamSynthesizeRequestPrecision] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Stream audio as it's generated. Returns chunked WAV data for progressive playback.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 2000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[StreamSynthesizeRequestPrecision]
            Audio precision

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Streaming audio response (chunked WAV)
        """
        with self._client_wrapper.httpx_client.stream(
            "stream",
            base_url=self._client_wrapper.get_environment().synthesis,
            method="POST",
            json={
                "voice_uuid": voice_uuid,
                "data": data,
                "project_uuid": project_uuid,
                "model": model,
                "precision": precision,
                "sample_rate": sample_rate,
                "use_hd": use_hd,
                "apply_custom_pronunciations": apply_custom_pronunciations,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawTextToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[SynthesizeRequestPrecision] = OMIT,
        output_format: typing.Optional[SynthesizeRequestOutputFormat] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SynthesizeResponse]:
        """
        Generate speech synchronously from text or SSML. Returns complete audio as base64.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 3,000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        title : typing.Optional[str]
            Optional title for the generated clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[SynthesizeRequestPrecision]
            Audio precision for WAV output

        output_format : typing.Optional[SynthesizeRequestOutputFormat]
            Audio output format

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SynthesizeResponse]
            Successful synthesis
        """
        _response = await self._client_wrapper.httpx_client.request(
            "synthesize",
            base_url=self._client_wrapper.get_environment().synthesis,
            method="POST",
            json={
                "voice_uuid": voice_uuid,
                "project_uuid": project_uuid,
                "title": title,
                "data": data,
                "model": model,
                "precision": precision,
                "output_format": output_format,
                "sample_rate": sample_rate,
                "use_hd": use_hd,
                "apply_custom_pronunciations": apply_custom_pronunciations,
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
                    SynthesizeResponse,
                    parse_obj_as(
                        type_=SynthesizeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    @contextlib.asynccontextmanager
    async def stream_synthesize(
        self,
        *,
        voice_uuid: str,
        data: str,
        project_uuid: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        precision: typing.Optional[StreamSynthesizeRequestPrecision] = OMIT,
        sample_rate: typing.Optional[int] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        apply_custom_pronunciations: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Stream audio as it's generated. Returns chunked WAV data for progressive playback.

        Parameters
        ----------
        voice_uuid : str
            Voice UUID to use for synthesis

        data : str
            Text or SSML to synthesize (max 2000 characters)

        project_uuid : typing.Optional[str]
            Optional project UUID to store the clip

        model : typing.Optional[str]
            Model to use for synthesis. Pass `chatterbox-turbo` to use the Turbo model for lower latency and paralinguistic tag support. If not specified, defaults to Chatterbox or Chatterbox Multilingual based on the voice. Note - Chatterbox-Turbo is supported by all Rapid English voices and Pre Built Library voices.

        precision : typing.Optional[StreamSynthesizeRequestPrecision]
            Audio precision

        sample_rate : typing.Optional[int]
            Audio sample rate in Hz

        use_hd : typing.Optional[bool]
            Enable HD synthesis with small latency trade-off

        apply_custom_pronunciations : typing.Optional[bool]
            When true, automatically applies your team's custom pronunciations to matching words in the input text. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Streaming audio response (chunked WAV)
        """
        async with self._client_wrapper.httpx_client.stream(
            "stream",
            base_url=self._client_wrapper.get_environment().synthesis,
            method="POST",
            json={
                "voice_uuid": voice_uuid,
                "data": data,
                "project_uuid": project_uuid,
                "model": model,
                "precision": precision,
                "sample_rate": sample_rate,
                "use_hd": use_hd,
                "apply_custom_pronunciations": apply_custom_pronunciations,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
