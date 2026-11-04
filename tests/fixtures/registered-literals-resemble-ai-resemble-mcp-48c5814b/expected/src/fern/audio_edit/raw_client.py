

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
from .types.create_audio_edit_response import CreateAudioEditResponse
from .types.get_audio_edit_response import GetAudioEditResponse
from .types.list_audio_edits_response import ListAudioEditsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAudioEditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_audio_edits(
        self, *, page: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAudioEditsResponse]:
        """
        Retrieve paginated list of audio edits

        Parameters
        ----------
        page : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAudioEditsResponse]
            List of audio edits
        """
        _response = self._client_wrapper.httpx_client.request(
            "edit",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAudioEditsResponse,
                    parse_obj_as(
                        type_=ListAudioEditsResponse,
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

    def create_audio_edit(
        self,
        *,
        input_audio: core.File,
        original_transcript: str,
        target_transcript: str,
        voice_uuid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAudioEditResponse]:
        """
        Edit audio segments using voice synthesis

        Parameters
        ----------
        input_audio : core.File
            See core.File for more documentation

        original_transcript : str
            Accurate transcript of the uploaded audio

        target_transcript : str
            Desired replacement text

        voice_uuid : str
            Voice used to render the edited segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAudioEditResponse]
            Edit job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "edit",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "original_transcript": original_transcript,
                "target_transcript": target_transcript,
                "voice_uuid": voice_uuid,
            },
            files={
                "input_audio": input_audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAudioEditResponse,
                    parse_obj_as(
                        type_=CreateAudioEditResponse,
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

    def get_audio_edit(
        self, audio_edit_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAudioEditResponse]:
        """
        Get status and result of an audio edit

        Parameters
        ----------
        audio_edit_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAudioEditResponse]
            Audio edit details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"edit/{encode_path_param(audio_edit_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioEditResponse,
                    parse_obj_as(
                        type_=GetAudioEditResponse,
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


class AsyncRawAudioEditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_audio_edits(
        self, *, page: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAudioEditsResponse]:
        """
        Retrieve paginated list of audio edits

        Parameters
        ----------
        page : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAudioEditsResponse]
            List of audio edits
        """
        _response = await self._client_wrapper.httpx_client.request(
            "edit",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAudioEditsResponse,
                    parse_obj_as(
                        type_=ListAudioEditsResponse,
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

    async def create_audio_edit(
        self,
        *,
        input_audio: core.File,
        original_transcript: str,
        target_transcript: str,
        voice_uuid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAudioEditResponse]:
        """
        Edit audio segments using voice synthesis

        Parameters
        ----------
        input_audio : core.File
            See core.File for more documentation

        original_transcript : str
            Accurate transcript of the uploaded audio

        target_transcript : str
            Desired replacement text

        voice_uuid : str
            Voice used to render the edited segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAudioEditResponse]
            Edit job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "edit",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "original_transcript": original_transcript,
                "target_transcript": target_transcript,
                "voice_uuid": voice_uuid,
            },
            files={
                "input_audio": input_audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAudioEditResponse,
                    parse_obj_as(
                        type_=CreateAudioEditResponse,
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

    async def get_audio_edit(
        self, audio_edit_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAudioEditResponse]:
        """
        Get status and result of an audio edit

        Parameters
        ----------
        audio_edit_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAudioEditResponse]
            Audio edit details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"edit/{encode_path_param(audio_edit_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAudioEditResponse,
                    parse_obj_as(
                        type_=GetAudioEditResponse,
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
