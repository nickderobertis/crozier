

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_identity_response import CreateIdentityResponse
from .types.list_identities_response import ListIdentitiesResponse
from .types.search_identities_response import SearchIdentitiesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_identities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListIdentitiesResponse]:
        """
        List all speaker identities

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListIdentitiesResponse]
            List of identities
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIdentitiesResponse,
                    parse_obj_as(
                        type_=ListIdentitiesResponse,
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

    def create_identity(
        self,
        *,
        audio_url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateIdentityResponse]:
        """
        Create a new speaker identity

        Parameters
        ----------
        audio_url : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateIdentityResponse]
            Identity created
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_url": audio_url,
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
                    CreateIdentityResponse,
                    parse_obj_as(
                        type_=CreateIdentityResponse,
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

    def search_identities(
        self, *, audio_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SearchIdentitiesResponse]:
        """
        Search for matching speaker identities

        Parameters
        ----------
        audio_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchIdentitiesResponse]
            Search results
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity/search",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_url": audio_url,
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
                    SearchIdentitiesResponse,
                    parse_obj_as(
                        type_=SearchIdentitiesResponse,
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


class AsyncRawIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_identities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListIdentitiesResponse]:
        """
        List all speaker identities

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListIdentitiesResponse]
            List of identities
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIdentitiesResponse,
                    parse_obj_as(
                        type_=ListIdentitiesResponse,
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

    async def create_identity(
        self,
        *,
        audio_url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateIdentityResponse]:
        """
        Create a new speaker identity

        Parameters
        ----------
        audio_url : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateIdentityResponse]
            Identity created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_url": audio_url,
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
                    CreateIdentityResponse,
                    parse_obj_as(
                        type_=CreateIdentityResponse,
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

    async def search_identities(
        self, *, audio_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SearchIdentitiesResponse]:
        """
        Search for matching speaker identities

        Parameters
        ----------
        audio_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchIdentitiesResponse]
            Search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity/search",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "audio_url": audio_url,
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
                    SearchIdentitiesResponse,
                    parse_obj_as(
                        type_=SearchIdentitiesResponse,
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
