

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
from .types.create_recording_response import CreateRecordingResponse
from .types.delete_recording_response import DeleteRecordingResponse
from .types.get_recording_response import GetRecordingResponse
from .types.list_recordings_response import ListRecordingsResponse
from .types.update_recording_response import UpdateRecordingResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRecordingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_recordings(
        self,
        voice_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListRecordingsResponse]:
        """
        List all recordings for a voice

        Parameters
        ----------
        voice_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRecordingsResponse]
            List of recordings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings",
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
                    ListRecordingsResponse,
                    parse_obj_as(
                        type_=ListRecordingsResponse,
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

    def create_recording(
        self,
        voice_uuid: str,
        *,
        file: core.File,
        name: str,
        text: str,
        emotion: str,
        is_active: bool,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateRecordingResponse]:
        """
        Upload a new recording for voice training

        Parameters
        ----------
        voice_uuid : str

        file : core.File
            See core.File for more documentation

        name : str
            Display name

        text : str
            Transcript of the clip

        emotion : str
            Emotion label

        is_active : bool
            Include in training

        fill : typing.Optional[bool]
            Include for Resemble Fill

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateRecordingResponse]
            Recording created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "name": name,
                "text": text,
                "emotion": emotion,
                "is_active": is_active,
                "fill": fill,
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
                    CreateRecordingResponse,
                    parse_obj_as(
                        type_=CreateRecordingResponse,
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

    def get_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRecordingResponse]:
        """
        Get recording details

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRecordingResponse]
            Recording details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRecordingResponse,
                    parse_obj_as(
                        type_=GetRecordingResponse,
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

    def delete_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteRecordingResponse]:
        """
        Delete a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteRecordingResponse]
            Recording deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteRecordingResponse,
                    parse_obj_as(
                        type_=DeleteRecordingResponse,
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

    def update_recording(
        self,
        voice_uuid: str,
        recording_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        emotion: typing.Optional[str] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateRecordingResponse]:
        """
        Update a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        name : typing.Optional[str]

        text : typing.Optional[str]

        emotion : typing.Optional[str]

        is_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateRecordingResponse]
            Recording updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "text": text,
                "emotion": emotion,
                "is_active": is_active,
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
                    UpdateRecordingResponse,
                    parse_obj_as(
                        type_=UpdateRecordingResponse,
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


class AsyncRawRecordingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_recordings(
        self,
        voice_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListRecordingsResponse]:
        """
        List all recordings for a voice

        Parameters
        ----------
        voice_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRecordingsResponse]
            List of recordings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings",
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
                    ListRecordingsResponse,
                    parse_obj_as(
                        type_=ListRecordingsResponse,
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

    async def create_recording(
        self,
        voice_uuid: str,
        *,
        file: core.File,
        name: str,
        text: str,
        emotion: str,
        is_active: bool,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateRecordingResponse]:
        """
        Upload a new recording for voice training

        Parameters
        ----------
        voice_uuid : str

        file : core.File
            See core.File for more documentation

        name : str
            Display name

        text : str
            Transcript of the clip

        emotion : str
            Emotion label

        is_active : bool
            Include in training

        fill : typing.Optional[bool]
            Include for Resemble Fill

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateRecordingResponse]
            Recording created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "name": name,
                "text": text,
                "emotion": emotion,
                "is_active": is_active,
                "fill": fill,
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
                    CreateRecordingResponse,
                    parse_obj_as(
                        type_=CreateRecordingResponse,
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

    async def get_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRecordingResponse]:
        """
        Get recording details

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRecordingResponse]
            Recording details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRecordingResponse,
                    parse_obj_as(
                        type_=GetRecordingResponse,
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

    async def delete_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteRecordingResponse]:
        """
        Delete a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteRecordingResponse]
            Recording deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteRecordingResponse,
                    parse_obj_as(
                        type_=DeleteRecordingResponse,
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

    async def update_recording(
        self,
        voice_uuid: str,
        recording_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        emotion: typing.Optional[str] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateRecordingResponse]:
        """
        Update a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        name : typing.Optional[str]

        text : typing.Optional[str]

        emotion : typing.Optional[str]

        is_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateRecordingResponse]
            Recording updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/recordings/{encode_path_param(recording_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "text": text,
                "emotion": emotion,
                "is_active": is_active,
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
                    UpdateRecordingResponse,
                    parse_obj_as(
                        type_=UpdateRecordingResponse,
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
