

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.forbidden_error_body import ForbiddenErrorBody
from .types.create_audio_enhancement_request_enhancement_engine import CreateAudioEnhancementRequestEnhancementEngine
from .types.create_audio_enhancement_response import CreateAudioEnhancementResponse
from .types.get_audio_enhancement_response import GetAudioEnhancementResponse
from .types.list_audio_enhancements_response import ListAudioEnhancementsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAudioEnhancementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_audio_enhancements(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAudioEnhancementsResponse]:
        """
        Returns a paginated list of all audio enhancements for your team, ordered by most recent first.

        Parameters
        ----------
        page : int
            Page number (starting from 1).

        page_size : typing.Optional[int]
            Items per page (10 to 1000). Default 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAudioEnhancementsResponse]
            List of enhancements
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio_enhancements",
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
                    ListAudioEnhancementsResponse,
                    parse_obj_as(
                        type_=ListAudioEnhancementsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_audio_enhancement(
        self,
        *,
        audio_file: core.File,
        enhancement_engine: typing.Optional[CreateAudioEnhancementRequestEnhancementEngine] = OMIT,
        remove_noise: typing.Optional[bool] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        studio_sound: typing.Optional[bool] = OMIT,
        enhancement_level: typing.Optional[float] = OMIT,
        loudness_target_level: typing.Optional[int] = OMIT,
        loudness_peak_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAudioEnhancementResponse]:
        """
        Submit an audio file for enhancement. Processing happens asynchronously in the background.
        The API defaults to the v2 enhancement engine. The v1 engine is legacy and will be sunset in a future release.

        Parameters
        ----------
        audio_file : core.File
            See core.File for more documentation

        enhancement_engine : typing.Optional[CreateAudioEnhancementRequestEnhancementEngine]
            Enhancement engine to use. Default is v2.

        remove_noise : typing.Optional[bool]
            Remove background noise. Engine v2 only.

        normalize : typing.Optional[bool]
            Normalize audio levels. Engine v2 only.

        studio_sound : typing.Optional[bool]
            Apply studio-quality enhancement. Engine v2 only.

        enhancement_level : typing.Optional[float]
            Enhancement intensity (0.0 to 1.0). Engine v1 only (legacy).

        loudness_target_level : typing.Optional[int]
            Target loudness in LUFS. Engine v1 only (legacy).

        loudness_peak_limit : typing.Optional[int]
            Peak limit in dBTP. Engine v1 only (legacy).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAudioEnhancementResponse]
            Enhancement job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio_enhancements",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "enhancement_engine": enhancement_engine,
                "remove_noise": remove_noise,
                "normalize": normalize,
                "studio_sound": studio_sound,
                "enhancement_level": enhancement_level,
                "loudness_target_level": loudness_target_level,
                "loudness_peak_limit": loudness_peak_limit,
            },
            files={
                "audio_file": audio_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAudioEnhancementResponse,
                    parse_obj_as(
                        type_=CreateAudioEnhancementResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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

    def get_audio_enhancement(
        self, enhancement_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAudioEnhancementResponse]:
        """
        Poll this endpoint to check the status of an enhancement job and retrieve the download URL when complete.

        Parameters
        ----------
        enhancement_uuid : str
            The UUID returned from the create endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAudioEnhancementResponse]
            Enhancement details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audio_enhancements/{encode_path_param(enhancement_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioEnhancementResponse,
                    parse_obj_as(
                        type_=GetAudioEnhancementResponse,
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


class AsyncRawAudioEnhancementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_audio_enhancements(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAudioEnhancementsResponse]:
        """
        Returns a paginated list of all audio enhancements for your team, ordered by most recent first.

        Parameters
        ----------
        page : int
            Page number (starting from 1).

        page_size : typing.Optional[int]
            Items per page (10 to 1000). Default 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAudioEnhancementsResponse]
            List of enhancements
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio_enhancements",
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
                    ListAudioEnhancementsResponse,
                    parse_obj_as(
                        type_=ListAudioEnhancementsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_audio_enhancement(
        self,
        *,
        audio_file: core.File,
        enhancement_engine: typing.Optional[CreateAudioEnhancementRequestEnhancementEngine] = OMIT,
        remove_noise: typing.Optional[bool] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        studio_sound: typing.Optional[bool] = OMIT,
        enhancement_level: typing.Optional[float] = OMIT,
        loudness_target_level: typing.Optional[int] = OMIT,
        loudness_peak_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAudioEnhancementResponse]:
        """
        Submit an audio file for enhancement. Processing happens asynchronously in the background.
        The API defaults to the v2 enhancement engine. The v1 engine is legacy and will be sunset in a future release.

        Parameters
        ----------
        audio_file : core.File
            See core.File for more documentation

        enhancement_engine : typing.Optional[CreateAudioEnhancementRequestEnhancementEngine]
            Enhancement engine to use. Default is v2.

        remove_noise : typing.Optional[bool]
            Remove background noise. Engine v2 only.

        normalize : typing.Optional[bool]
            Normalize audio levels. Engine v2 only.

        studio_sound : typing.Optional[bool]
            Apply studio-quality enhancement. Engine v2 only.

        enhancement_level : typing.Optional[float]
            Enhancement intensity (0.0 to 1.0). Engine v1 only (legacy).

        loudness_target_level : typing.Optional[int]
            Target loudness in LUFS. Engine v1 only (legacy).

        loudness_peak_limit : typing.Optional[int]
            Peak limit in dBTP. Engine v1 only (legacy).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAudioEnhancementResponse]
            Enhancement job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio_enhancements",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "enhancement_engine": enhancement_engine,
                "remove_noise": remove_noise,
                "normalize": normalize,
                "studio_sound": studio_sound,
                "enhancement_level": enhancement_level,
                "loudness_target_level": loudness_target_level,
                "loudness_peak_limit": loudness_peak_limit,
            },
            files={
                "audio_file": audio_file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAudioEnhancementResponse,
                    parse_obj_as(
                        type_=CreateAudioEnhancementResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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

    async def get_audio_enhancement(
        self, enhancement_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAudioEnhancementResponse]:
        """
        Poll this endpoint to check the status of an enhancement job and retrieve the download URL when complete.

        Parameters
        ----------
        enhancement_uuid : str
            The UUID returned from the create endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAudioEnhancementResponse]
            Enhancement details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audio_enhancements/{encode_path_param(enhancement_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioEnhancementResponse,
                    parse_obj_as(
                        type_=GetAudioEnhancementResponse,
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
