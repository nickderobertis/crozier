

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
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_duet_voice_pair_response import CreateDuetVoicePairResponse
from .types.create_duet_voice_response import CreateDuetVoiceResponse
from .types.delete_duet_voice_response import DeleteDuetVoiceResponse
from .types.generate_duet_request_script_item import GenerateDuetRequestScriptItem
from .types.generate_duet_response import GenerateDuetResponse
from .types.list_duet_voice_pairs_response import ListDuetVoicePairsResponse
from .types.list_duet_voices_response import ListDuetVoicesResponse
from .types.update_duet_voice_response import UpdateDuetVoiceResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDuetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_duet_voices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListDuetVoicesResponse]:
        """
        Returns default and custom duet voices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDuetVoicesResponse]
            List of duet voices
        """
        _response = self._client_wrapper.httpx_client.request(
            "duet_voices",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDuetVoicesResponse,
                    parse_obj_as(
                        type_=ListDuetVoicesResponse,
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

    def create_duet_voice(
        self,
        *,
        name: str,
        audio: core.File,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDuetVoiceResponse]:
        """
        Create a custom voice for duet generation

        Parameters
        ----------
        name : str
            Voice name

        audio : core.File
            See core.File for more documentation

        style_prompt : typing.Optional[str]
            Optional style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDuetVoiceResponse]
            Duet voice created
        """
        _response = self._client_wrapper.httpx_client.request(
            "duet_voices",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "name": name,
                "style_prompt": style_prompt,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDuetVoiceResponse,
                    parse_obj_as(
                        type_=CreateDuetVoiceResponse,
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

    def update_duet_voice(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateDuetVoiceResponse]:
        """
        Update a custom duet voice (default voices cannot be modified)

        Parameters
        ----------
        id : int

        name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateDuetVoiceResponse]
            Duet voice updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"duet_voices/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "name": name,
                "style_prompt": style_prompt,
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
                    UpdateDuetVoiceResponse,
                    parse_obj_as(
                        type_=UpdateDuetVoiceResponse,
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

    def delete_duet_voice(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDuetVoiceResponse]:
        """
        Delete a custom duet voice (default voices cannot be deleted)

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDuetVoiceResponse]
            Duet voice deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"duet_voices/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDuetVoiceResponse,
                    parse_obj_as(
                        type_=DeleteDuetVoiceResponse,
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

    def list_duet_voice_pairs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListDuetVoicePairsResponse]:
        """
        List all voice pairs for duet generation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDuetVoicePairsResponse]
            List of voice pairs
        """
        _response = self._client_wrapper.httpx_client.request(
            "duet_voice_pairs",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDuetVoicePairsResponse,
                    parse_obj_as(
                        type_=ListDuetVoicePairsResponse,
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

    def create_duet_voice_pair(
        self,
        *,
        voice1id: int,
        voice2id: int,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDuetVoicePairResponse]:
        """
        Create a voice pair for duet generation

        Parameters
        ----------
        voice1id : int
            ID of first voice

        voice2id : int
            ID of second voice

        name : typing.Optional[str]
            Optional pair name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDuetVoicePairResponse]
            Voice pair created
        """
        _response = self._client_wrapper.httpx_client.request(
            "duet_voice_pairs",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "voice_1_id": voice1id,
                "voice_2_id": voice2id,
                "name": name,
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
                    CreateDuetVoicePairResponse,
                    parse_obj_as(
                        type_=CreateDuetVoicePairResponse,
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

    def generate_duet(
        self,
        *,
        voice_pair_id: int,
        script: typing.Sequence[GenerateDuetRequestScriptItem],
        title: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GenerateDuetResponse]:
        """
        Generate conversational audio with two speakers

        Parameters
        ----------
        voice_pair_id : int
            Voice pair ID to use

        script : typing.Sequence[GenerateDuetRequestScriptItem]

        title : typing.Optional[str]
            Optional title for the duet

        callback_uri : typing.Optional[str]
            Webhook URL for completion notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GenerateDuetResponse]
            Duet generation job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "duet",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "voice_pair_id": voice_pair_id,
                "script": convert_and_respect_annotation_metadata(
                    object_=script, annotation=typing.Sequence[GenerateDuetRequestScriptItem], direction="write"
                ),
                "title": title,
                "callback_uri": callback_uri,
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
                    GenerateDuetResponse,
                    parse_obj_as(
                        type_=GenerateDuetResponse,
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


class AsyncRawDuetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_duet_voices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListDuetVoicesResponse]:
        """
        Returns default and custom duet voices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDuetVoicesResponse]
            List of duet voices
        """
        _response = await self._client_wrapper.httpx_client.request(
            "duet_voices",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDuetVoicesResponse,
                    parse_obj_as(
                        type_=ListDuetVoicesResponse,
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

    async def create_duet_voice(
        self,
        *,
        name: str,
        audio: core.File,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDuetVoiceResponse]:
        """
        Create a custom voice for duet generation

        Parameters
        ----------
        name : str
            Voice name

        audio : core.File
            See core.File for more documentation

        style_prompt : typing.Optional[str]
            Optional style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDuetVoiceResponse]
            Duet voice created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "duet_voices",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "name": name,
                "style_prompt": style_prompt,
            },
            files={
                "audio": audio,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDuetVoiceResponse,
                    parse_obj_as(
                        type_=CreateDuetVoiceResponse,
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

    async def update_duet_voice(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateDuetVoiceResponse]:
        """
        Update a custom duet voice (default voices cannot be modified)

        Parameters
        ----------
        id : int

        name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateDuetVoiceResponse]
            Duet voice updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"duet_voices/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "name": name,
                "style_prompt": style_prompt,
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
                    UpdateDuetVoiceResponse,
                    parse_obj_as(
                        type_=UpdateDuetVoiceResponse,
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

    async def delete_duet_voice(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteDuetVoiceResponse]:
        """
        Delete a custom duet voice (default voices cannot be deleted)

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDuetVoiceResponse]
            Duet voice deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"duet_voices/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDuetVoiceResponse,
                    parse_obj_as(
                        type_=DeleteDuetVoiceResponse,
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

    async def list_duet_voice_pairs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListDuetVoicePairsResponse]:
        """
        List all voice pairs for duet generation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDuetVoicePairsResponse]
            List of voice pairs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "duet_voice_pairs",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDuetVoicePairsResponse,
                    parse_obj_as(
                        type_=ListDuetVoicePairsResponse,
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

    async def create_duet_voice_pair(
        self,
        *,
        voice1id: int,
        voice2id: int,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDuetVoicePairResponse]:
        """
        Create a voice pair for duet generation

        Parameters
        ----------
        voice1id : int
            ID of first voice

        voice2id : int
            ID of second voice

        name : typing.Optional[str]
            Optional pair name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDuetVoicePairResponse]
            Voice pair created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "duet_voice_pairs",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "voice_1_id": voice1id,
                "voice_2_id": voice2id,
                "name": name,
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
                    CreateDuetVoicePairResponse,
                    parse_obj_as(
                        type_=CreateDuetVoicePairResponse,
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

    async def generate_duet(
        self,
        *,
        voice_pair_id: int,
        script: typing.Sequence[GenerateDuetRequestScriptItem],
        title: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GenerateDuetResponse]:
        """
        Generate conversational audio with two speakers

        Parameters
        ----------
        voice_pair_id : int
            Voice pair ID to use

        script : typing.Sequence[GenerateDuetRequestScriptItem]

        title : typing.Optional[str]
            Optional title for the duet

        callback_uri : typing.Optional[str]
            Webhook URL for completion notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GenerateDuetResponse]
            Duet generation job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "duet",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "voice_pair_id": voice_pair_id,
                "script": convert_and_respect_annotation_metadata(
                    object_=script, annotation=typing.Sequence[GenerateDuetRequestScriptItem], direction="write"
                ),
                "title": title,
                "callback_uri": callback_uri,
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
                    GenerateDuetResponse,
                    parse_obj_as(
                        type_=GenerateDuetResponse,
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
