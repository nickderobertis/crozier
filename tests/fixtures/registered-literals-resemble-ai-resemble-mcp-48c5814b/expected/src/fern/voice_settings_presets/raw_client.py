

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_voice_settings_preset_response import CreateVoiceSettingsPresetResponse
from .types.delete_voice_settings_preset_response import DeleteVoiceSettingsPresetResponse
from .types.get_voice_settings_preset_response import GetVoiceSettingsPresetResponse
from .types.list_voice_settings_presets_response import ListVoiceSettingsPresetsResponse
from .types.update_voice_settings_preset_response import UpdateVoiceSettingsPresetResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVoiceSettingsPresetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_voice_settings_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListVoiceSettingsPresetsResponse]:
        """
        List all voice settings presets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListVoiceSettingsPresetsResponse]
            List of presets
        """
        _response = self._client_wrapper.httpx_client.request(
            "voice_settings_presets",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVoiceSettingsPresetsResponse,
                    parse_obj_as(
                        type_=ListVoiceSettingsPresetsResponse,
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

    def create_voice_settings_preset(
        self,
        *,
        name: str,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateVoiceSettingsPresetResponse]:
        """
        Create a new voice settings preset (max 5 per user)

        Parameters
        ----------
        name : str
            Preset name (unique, max 30 characters)

        pace : typing.Optional[float]
            Speech pace/speed

        temperature : typing.Optional[float]
            Voice variation

        pitch : typing.Optional[float]
            Voice pitch adjustment

        use_hd : typing.Optional[bool]
            Use HD quality

        exaggeration : typing.Optional[float]
            Emotional exaggeration

        description : typing.Optional[str]
            Voice style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateVoiceSettingsPresetResponse]
            Preset created
        """
        _response = self._client_wrapper.httpx_client.request(
            "voice_settings_presets",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "pace": pace,
                "temperature": temperature,
                "pitch": pitch,
                "useHd": use_hd,
                "exaggeration": exaggeration,
                "description": description,
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
                    CreateVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=CreateVoiceSettingsPresetResponse,
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

    def get_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetVoiceSettingsPresetResponse]:
        """
        Get preset details

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetVoiceSettingsPresetResponse]
            Preset details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=GetVoiceSettingsPresetResponse,
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

    def delete_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteVoiceSettingsPresetResponse]:
        """
        Delete a preset

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteVoiceSettingsPresetResponse]
            Preset deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=DeleteVoiceSettingsPresetResponse,
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

    def update_voice_settings_preset(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateVoiceSettingsPresetResponse]:
        """
        Update a preset

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        pace : typing.Optional[float]

        temperature : typing.Optional[float]

        pitch : typing.Optional[float]

        use_hd : typing.Optional[bool]

        exaggeration : typing.Optional[float]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateVoiceSettingsPresetResponse]
            Preset updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "pace": pace,
                "temperature": temperature,
                "pitch": pitch,
                "useHd": use_hd,
                "exaggeration": exaggeration,
                "description": description,
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
                    UpdateVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=UpdateVoiceSettingsPresetResponse,
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


class AsyncRawVoiceSettingsPresetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_voice_settings_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListVoiceSettingsPresetsResponse]:
        """
        List all voice settings presets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListVoiceSettingsPresetsResponse]
            List of presets
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voice_settings_presets",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVoiceSettingsPresetsResponse,
                    parse_obj_as(
                        type_=ListVoiceSettingsPresetsResponse,
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

    async def create_voice_settings_preset(
        self,
        *,
        name: str,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateVoiceSettingsPresetResponse]:
        """
        Create a new voice settings preset (max 5 per user)

        Parameters
        ----------
        name : str
            Preset name (unique, max 30 characters)

        pace : typing.Optional[float]
            Speech pace/speed

        temperature : typing.Optional[float]
            Voice variation

        pitch : typing.Optional[float]
            Voice pitch adjustment

        use_hd : typing.Optional[bool]
            Use HD quality

        exaggeration : typing.Optional[float]
            Emotional exaggeration

        description : typing.Optional[str]
            Voice style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateVoiceSettingsPresetResponse]
            Preset created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voice_settings_presets",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "pace": pace,
                "temperature": temperature,
                "pitch": pitch,
                "useHd": use_hd,
                "exaggeration": exaggeration,
                "description": description,
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
                    CreateVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=CreateVoiceSettingsPresetResponse,
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

    async def get_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetVoiceSettingsPresetResponse]:
        """
        Get preset details

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetVoiceSettingsPresetResponse]
            Preset details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=GetVoiceSettingsPresetResponse,
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

    async def delete_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteVoiceSettingsPresetResponse]:
        """
        Delete a preset

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteVoiceSettingsPresetResponse]
            Preset deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=DeleteVoiceSettingsPresetResponse,
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

    async def update_voice_settings_preset(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateVoiceSettingsPresetResponse]:
        """
        Update a preset

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        pace : typing.Optional[float]

        temperature : typing.Optional[float]

        pitch : typing.Optional[float]

        use_hd : typing.Optional[bool]

        exaggeration : typing.Optional[float]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateVoiceSettingsPresetResponse]
            Preset updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voice_settings_presets/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "pace": pace,
                "temperature": temperature,
                "pitch": pitch,
                "useHd": use_hd,
                "exaggeration": exaggeration,
                "description": description,
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
                    UpdateVoiceSettingsPresetResponse,
                    parse_obj_as(
                        type_=UpdateVoiceSettingsPresetResponse,
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
