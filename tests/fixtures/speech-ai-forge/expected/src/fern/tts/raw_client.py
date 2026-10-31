

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
from ..types.synthesize_tts_v1tts_get_request_no_cache import SynthesizeTtsV1TtsGetRequestNoCache
from pydantic import ValidationError


class RawTtsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def synthesize_tts(
        self,
        *,
        text: str,
        spk: typing.Optional[str] = None,
        style: typing.Optional[str] = None,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        seed: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        bitrate: typing.Optional[str] = None,
        prompt: typing.Optional[str] = None,
        prompt1: typing.Optional[str] = None,
        prompt2: typing.Optional[str] = None,
        prefix: typing.Optional[str] = None,
        bs: typing.Optional[str] = None,
        thr: typing.Optional[str] = None,
        eos: typing.Optional[str] = None,
        enhance: typing.Optional[bool] = None,
        denoise: typing.Optional[bool] = None,
        speed: typing.Optional[float] = None,
        pitch: typing.Optional[float] = None,
        volume_gain: typing.Optional[float] = None,
        stream: typing.Optional[bool] = None,
        chunk_size: typing.Optional[int] = None,
        no_cache: typing.Optional[SynthesizeTtsV1TtsGetRequestNoCache] = None,
        model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        **Text-to-Speech Synthesis API (v1 - GET)**

        This endpoint converts text into speech using GET request parameters.
        It offers various options for customizing the voice, style, audio output, and processing.

        **Mandatory Parameter**:
        *   `text`: The text string to be synthesized.

        **Speaker and Style Customization**:
        *   `spk`: Specify the speaker by name or seed (e.g., "female2").
        *   `style`: Define the speaking style (e.g., "chat").

        **Generation Control**:
        *   `temperature`: Sampling temperature (0.0-1.0, e.g., 0.3). Controls randomness.
        *   `top_p`: Nucleus sampling probability (0.0-1.0, e.g., 0.5).
        *   `top_k`: Limits sampling to the K most likely next tokens (e.g., 20).
        *   `seed`: Seed for reproducible generation (e.g., 42).
        *   `prompt`, `prompt1`, `prompt2`: Optional text prompts to guide inference.
        *   `prefix`: Optional text prefix for inference.
        *   `bs` (batch_size): Batch size for processing (e.g., "8").
        *   `thr` (threshold): Sentence splitter threshold (e.g., "100").
        *   `eos`: End-of-sentence marker (e.g., "[uv_break]").

        **Output Audio Configuration**:
        *   `format`: Desired audio output format. Supported: "mp3", "wav", "raw" (default).
        *   `bitrate`: Audio bitrate for compressed formats (e.g., "64k").

        **Audio Adjustments**:
        *   `speed`: Playback speed multiplier (e.g., 1.0 for normal).
        *   `pitch`: Pitch adjustment (e.g., 0 for no change).
        *   `volume_gain`: Volume gain in dB (e.g., 0 for no change).

        **Enhancements**:
        *   `enhance`: Boolean to enable audio enhancement (default: false).
        *   `denoise`: Boolean to enable audio denoising (default: false).

        **Streaming Output**:
        *   `stream`: Boolean to enable streaming audio generation (default: false).
        *   `chunk_size`: Size of chunks for streaming (e.g., 64, if stream is true).

        **Caching**:
        *   `no_cache`: Boolean or "on"/"off" to disable caching (default: false).

        **Model Selection**:
        *   `model`: Specify the TTS model ID to use (e.g., "chat-tts", "cosy-voice").

        **Response**:
        *   **Success**: An audio file stream (`FileResponse`).
        *   **Failure**: A JSON object detailing the error (e.g., validation errors, internal server error).

        **Note**: This v1 endpoint does *not* support voice cloning via reference audio. For voice cloning, please refer to the v2 API. Parameters like temperature, top_p, top_k, seed, prompts, and prefix might be overridden by specific speaker (`spk`) or style (`style`) configurations.

        Parameters
        ----------
        text : str

        spk : typing.Optional[str]

        style : typing.Optional[str]

        temperature : typing.Optional[float]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        seed : typing.Optional[int]

        format : typing.Optional[str]

        bitrate : typing.Optional[str]

        prompt : typing.Optional[str]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        bs : typing.Optional[str]

        thr : typing.Optional[str]

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        speed : typing.Optional[float]

        pitch : typing.Optional[float]

        volume_gain : typing.Optional[float]

        stream : typing.Optional[bool]

        chunk_size : typing.Optional[int]

        no_cache : typing.Optional[SynthesizeTtsV1TtsGetRequestNoCache]

        model : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tts",
            method="GET",
            params={
                "text": text,
                "spk": spk,
                "style": style,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "seed": seed,
                "format": format,
                "bitrate": bitrate,
                "prompt": prompt,
                "prompt1": prompt1,
                "prompt2": prompt2,
                "prefix": prefix,
                "bs": bs,
                "thr": thr,
                "eos": eos,
                "enhance": enhance,
                "denoise": denoise,
                "speed": speed,
                "pitch": pitch,
                "volume_gain": volume_gain,
                "stream": stream,
                "chunk_size": chunk_size,
                "no_cache": no_cache,
                "model": model,
            },
            request_options=request_options,
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


class AsyncRawTtsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def synthesize_tts(
        self,
        *,
        text: str,
        spk: typing.Optional[str] = None,
        style: typing.Optional[str] = None,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        seed: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        bitrate: typing.Optional[str] = None,
        prompt: typing.Optional[str] = None,
        prompt1: typing.Optional[str] = None,
        prompt2: typing.Optional[str] = None,
        prefix: typing.Optional[str] = None,
        bs: typing.Optional[str] = None,
        thr: typing.Optional[str] = None,
        eos: typing.Optional[str] = None,
        enhance: typing.Optional[bool] = None,
        denoise: typing.Optional[bool] = None,
        speed: typing.Optional[float] = None,
        pitch: typing.Optional[float] = None,
        volume_gain: typing.Optional[float] = None,
        stream: typing.Optional[bool] = None,
        chunk_size: typing.Optional[int] = None,
        no_cache: typing.Optional[SynthesizeTtsV1TtsGetRequestNoCache] = None,
        model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        **Text-to-Speech Synthesis API (v1 - GET)**

        This endpoint converts text into speech using GET request parameters.
        It offers various options for customizing the voice, style, audio output, and processing.

        **Mandatory Parameter**:
        *   `text`: The text string to be synthesized.

        **Speaker and Style Customization**:
        *   `spk`: Specify the speaker by name or seed (e.g., "female2").
        *   `style`: Define the speaking style (e.g., "chat").

        **Generation Control**:
        *   `temperature`: Sampling temperature (0.0-1.0, e.g., 0.3). Controls randomness.
        *   `top_p`: Nucleus sampling probability (0.0-1.0, e.g., 0.5).
        *   `top_k`: Limits sampling to the K most likely next tokens (e.g., 20).
        *   `seed`: Seed for reproducible generation (e.g., 42).
        *   `prompt`, `prompt1`, `prompt2`: Optional text prompts to guide inference.
        *   `prefix`: Optional text prefix for inference.
        *   `bs` (batch_size): Batch size for processing (e.g., "8").
        *   `thr` (threshold): Sentence splitter threshold (e.g., "100").
        *   `eos`: End-of-sentence marker (e.g., "[uv_break]").

        **Output Audio Configuration**:
        *   `format`: Desired audio output format. Supported: "mp3", "wav", "raw" (default).
        *   `bitrate`: Audio bitrate for compressed formats (e.g., "64k").

        **Audio Adjustments**:
        *   `speed`: Playback speed multiplier (e.g., 1.0 for normal).
        *   `pitch`: Pitch adjustment (e.g., 0 for no change).
        *   `volume_gain`: Volume gain in dB (e.g., 0 for no change).

        **Enhancements**:
        *   `enhance`: Boolean to enable audio enhancement (default: false).
        *   `denoise`: Boolean to enable audio denoising (default: false).

        **Streaming Output**:
        *   `stream`: Boolean to enable streaming audio generation (default: false).
        *   `chunk_size`: Size of chunks for streaming (e.g., 64, if stream is true).

        **Caching**:
        *   `no_cache`: Boolean or "on"/"off" to disable caching (default: false).

        **Model Selection**:
        *   `model`: Specify the TTS model ID to use (e.g., "chat-tts", "cosy-voice").

        **Response**:
        *   **Success**: An audio file stream (`FileResponse`).
        *   **Failure**: A JSON object detailing the error (e.g., validation errors, internal server error).

        **Note**: This v1 endpoint does *not* support voice cloning via reference audio. For voice cloning, please refer to the v2 API. Parameters like temperature, top_p, top_k, seed, prompts, and prefix might be overridden by specific speaker (`spk`) or style (`style`) configurations.

        Parameters
        ----------
        text : str

        spk : typing.Optional[str]

        style : typing.Optional[str]

        temperature : typing.Optional[float]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        seed : typing.Optional[int]

        format : typing.Optional[str]

        bitrate : typing.Optional[str]

        prompt : typing.Optional[str]

        prompt1 : typing.Optional[str]

        prompt2 : typing.Optional[str]

        prefix : typing.Optional[str]

        bs : typing.Optional[str]

        thr : typing.Optional[str]

        eos : typing.Optional[str]

        enhance : typing.Optional[bool]

        denoise : typing.Optional[bool]

        speed : typing.Optional[float]

        pitch : typing.Optional[float]

        volume_gain : typing.Optional[float]

        stream : typing.Optional[bool]

        chunk_size : typing.Optional[int]

        no_cache : typing.Optional[SynthesizeTtsV1TtsGetRequestNoCache]

        model : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tts",
            method="GET",
            params={
                "text": text,
                "spk": spk,
                "style": style,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "seed": seed,
                "format": format,
                "bitrate": bitrate,
                "prompt": prompt,
                "prompt1": prompt1,
                "prompt2": prompt2,
                "prefix": prefix,
                "bs": bs,
                "thr": thr,
                "eos": eos,
                "enhance": enhance,
                "denoise": denoise,
                "speed": speed,
                "pitch": pitch,
                "volume_gain": volume_gain,
                "stream": stream,
                "chunk_size": chunk_size,
                "no_cache": no_cache,
                "model": model,
            },
            request_options=request_options,
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
