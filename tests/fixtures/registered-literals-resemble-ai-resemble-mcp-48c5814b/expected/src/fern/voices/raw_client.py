

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.build_voice_response import BuildVoiceResponse
from .types.create_voice_request_voice_type import CreateVoiceRequestVoiceType
from .types.create_voice_response import CreateVoiceResponse
from .types.delete_voice_response import DeleteVoiceResponse
from .types.get_voice_response import GetVoiceResponse
from .types.list_voices_response import ListVoicesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_voices(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListVoicesResponse]:
        """
        Retrieve voice metadata

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListVoicesResponse]
            List of voices
        """
        _response = self._client_wrapper.httpx_client.request(
            "voices",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVoicesResponse,
                    parse_obj_as(
                        type_=ListVoicesResponse,
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

    def create_voice(
        self,
        *,
        name: str,
        voice_type: typing.Optional[CreateVoiceRequestVoiceType] = OMIT,
        dataset_url: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateVoiceResponse]:
        """
        Create a new voice

        Parameters
        ----------
        name : str

        voice_type : typing.Optional[CreateVoiceRequestVoiceType]

        dataset_url : typing.Optional[str]

        callback_uri : typing.Optional[str]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateVoiceResponse]
            Voice created
        """
        _response = self._client_wrapper.httpx_client.request(
            "voices",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "voice_type": voice_type,
                "dataset_url": dataset_url,
                "callback_uri": callback_uri,
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
                _data = typing.cast(
                    CreateVoiceResponse,
                    parse_obj_as(
                        type_=CreateVoiceResponse,
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

    def get_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetVoiceResponse]:
        """
        Get voice details

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetVoiceResponse]
            Voice details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVoiceResponse,
                    parse_obj_as(
                        type_=GetVoiceResponse,
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

    def delete_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteVoiceResponse]:
        """
        Delete a voice

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteVoiceResponse]
            Voice deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteVoiceResponse,
                    parse_obj_as(
                        type_=DeleteVoiceResponse,
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

    def build_voice(
        self,
        voice_uuid: str,
        *,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildVoiceResponse]:
        """
        Start voice training

        Parameters
        ----------
        voice_uuid : str

        fill : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildVoiceResponse]
            Build started
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/build",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "fill": fill,
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
                    BuildVoiceResponse,
                    parse_obj_as(
                        type_=BuildVoiceResponse,
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


class AsyncRawVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_voices(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListVoicesResponse]:
        """
        Retrieve voice metadata

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListVoicesResponse]
            List of voices
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voices",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVoicesResponse,
                    parse_obj_as(
                        type_=ListVoicesResponse,
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

    async def create_voice(
        self,
        *,
        name: str,
        voice_type: typing.Optional[CreateVoiceRequestVoiceType] = OMIT,
        dataset_url: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateVoiceResponse]:
        """
        Create a new voice

        Parameters
        ----------
        name : str

        voice_type : typing.Optional[CreateVoiceRequestVoiceType]

        dataset_url : typing.Optional[str]

        callback_uri : typing.Optional[str]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateVoiceResponse]
            Voice created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voices",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "voice_type": voice_type,
                "dataset_url": dataset_url,
                "callback_uri": callback_uri,
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
                _data = typing.cast(
                    CreateVoiceResponse,
                    parse_obj_as(
                        type_=CreateVoiceResponse,
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

    async def get_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetVoiceResponse]:
        """
        Get voice details

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetVoiceResponse]
            Voice details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVoiceResponse,
                    parse_obj_as(
                        type_=GetVoiceResponse,
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

    async def delete_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteVoiceResponse]:
        """
        Delete a voice

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteVoiceResponse]
            Voice deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteVoiceResponse,
                    parse_obj_as(
                        type_=DeleteVoiceResponse,
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

    async def build_voice(
        self,
        voice_uuid: str,
        *,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildVoiceResponse]:
        """
        Start voice training

        Parameters
        ----------
        voice_uuid : str

        fill : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildVoiceResponse]
            Build started
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voices/{encode_path_param(voice_uuid)}/build",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "fill": fill,
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
                    BuildVoiceResponse,
                    parse_obj_as(
                        type_=BuildVoiceResponse,
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
