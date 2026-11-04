

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_voice_from_candidate_response import CreateVoiceFromCandidateResponse
from .types.generate_voice_design_response import GenerateVoiceDesignResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVoiceDesignClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate_voice_design(
        self, *, user_prompt: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GenerateVoiceDesignResponse]:
        """
        Generate three voice candidates from a text prompt

        Parameters
        ----------
        user_prompt : str
            Description of desired voice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GenerateVoiceDesignResponse]
            Voice candidates generated
        """
        _response = self._client_wrapper.httpx_client.request(
            "voice-design",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "user_prompt": user_prompt,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GenerateVoiceDesignResponse,
                    parse_obj_as(
                        type_=GenerateVoiceDesignResponse,
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

    def create_voice_from_candidate(
        self, *, uuid_: str, voice_sample_index: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateVoiceFromCandidateResponse]:
        """
        Create a voice from a voice design candidate

        Parameters
        ----------
        uuid_ : str

        voice_sample_index : int

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateVoiceFromCandidateResponse]
            Voice created
        """
        _response = self._client_wrapper.httpx_client.request(
            "voice-design/create",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "uuid": uuid_,
                "voice_sample_index": voice_sample_index,
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
                    CreateVoiceFromCandidateResponse,
                    parse_obj_as(
                        type_=CreateVoiceFromCandidateResponse,
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


class AsyncRawVoiceDesignClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate_voice_design(
        self, *, user_prompt: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GenerateVoiceDesignResponse]:
        """
        Generate three voice candidates from a text prompt

        Parameters
        ----------
        user_prompt : str
            Description of desired voice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GenerateVoiceDesignResponse]
            Voice candidates generated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voice-design",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            data={
                "user_prompt": user_prompt,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GenerateVoiceDesignResponse,
                    parse_obj_as(
                        type_=GenerateVoiceDesignResponse,
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

    async def create_voice_from_candidate(
        self, *, uuid_: str, voice_sample_index: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateVoiceFromCandidateResponse]:
        """
        Create a voice from a voice design candidate

        Parameters
        ----------
        uuid_ : str

        voice_sample_index : int

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateVoiceFromCandidateResponse]
            Voice created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voice-design/create",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "uuid": uuid_,
                "voice_sample_index": voice_sample_index,
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
                    CreateVoiceFromCandidateResponse,
                    parse_obj_as(
                        type_=CreateVoiceFromCandidateResponse,
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
