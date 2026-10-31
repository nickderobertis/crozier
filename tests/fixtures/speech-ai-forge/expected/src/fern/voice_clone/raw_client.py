

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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVoiceCloneClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def voice_clone(
        self,
        *,
        src_audio: core.File,
        ref_spk: typing.Optional[str] = None,
        spk_emotion: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        tau: typing.Optional[float] = None,
        format: typing.Optional[str] = None,
        ref_audio: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Voice cloning API

        **Deprecated**
        This API is deprecated and will be removed in the future.
        Please use the `TTS API` instead.

        Parameters
        ----------
        src_audio : core.File
            See core.File for more documentation

        ref_spk : typing.Optional[str]

        spk_emotion : typing.Optional[str]

        model : typing.Optional[str]

        tau : typing.Optional[float]

        format : typing.Optional[str]

        ref_audio : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vc",
            method="POST",
            params={
                "ref_spk": ref_spk,
                "spk_emotion": spk_emotion,
                "model": model,
                "tau": tau,
                "format": format,
            },
            data={},
            files={
                "src_audio": src_audio,
                **({"ref_audio": ref_audio} if ref_audio is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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


class AsyncRawVoiceCloneClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def voice_clone(
        self,
        *,
        src_audio: core.File,
        ref_spk: typing.Optional[str] = None,
        spk_emotion: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        tau: typing.Optional[float] = None,
        format: typing.Optional[str] = None,
        ref_audio: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Voice cloning API

        **Deprecated**
        This API is deprecated and will be removed in the future.
        Please use the `TTS API` instead.

        Parameters
        ----------
        src_audio : core.File
            See core.File for more documentation

        ref_spk : typing.Optional[str]

        spk_emotion : typing.Optional[str]

        model : typing.Optional[str]

        tau : typing.Optional[float]

        format : typing.Optional[str]

        ref_audio : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vc",
            method="POST",
            params={
                "ref_spk": ref_spk,
                "spk_emotion": spk_emotion,
                "model": model,
                "tau": tau,
                "format": format,
            },
            data={},
            files={
                "src_audio": src_audio,
                **({"ref_audio": ref_audio} if ref_audio is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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
