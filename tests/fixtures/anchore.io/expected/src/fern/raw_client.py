

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import jsonable_encoder
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .types.file_content_search_list import FileContentSearchList
from .types.retrieved_file_list import RetrievedFileList
from .types.secret_search_list import SecretSearchList
from .types.service_version import ServiceVersion
from .types.token_response import TokenResponse


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Simple status check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Version check response, returns the api version prefix (e.g. 'v1')
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Health check, returns 200 and no body if service is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_file_content_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileContentSearchList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileContentSearchList]
            List of file metadata objects
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/file_content_search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileContentSearchList,
                    parse_obj_as(
                        type_=FileContentSearchList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_retrieved_files(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrievedFileList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrievedFileList]
            List of file metadata objects
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/retrieved_files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrievedFileList,
                    parse_obj_as(
                        type_=RetrievedFileList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_secret_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SecretSearchList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SecretSearchList]
            List of file metadata objects
        """
        _response = self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/secret_search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SecretSearchList,
                    parse_obj_as(
                        type_=SecretSearchList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_oauth_token(
        self,
        *,
        client_id: typing.Optional[str] = OMIT,
        grant_type: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponse]:
        """
        Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

        Parameters
        ----------
        client_id : typing.Optional[str]
            The type of client used for the OAuth token

        grant_type : typing.Optional[str]
            OAuth Grant type for token

        password : typing.Optional[str]
            Password for corresponding user

        username : typing.Optional[str]
            User to assign OAuth token to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponse]
            Resulting JWT token
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "client_id": client_id,
                "grant_type": grant_type,
                "password": password,
                "username": username,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def version_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ServiceVersion]:
        """
        Returns the version object for the service, including db schema version info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ServiceVersion]
            Version object describing version state
        """
        _response = self._client_wrapper.httpx_client.request(
            "version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServiceVersion,
                    parse_obj_as(
                        type_=ServiceVersion,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        Simple status check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Version check response, returns the api version prefix (e.g. 'v1')
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Health check, returns 200 and no body if service is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_file_content_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileContentSearchList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileContentSearchList]
            List of file metadata objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/file_content_search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileContentSearchList,
                    parse_obj_as(
                        type_=FileContentSearchList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_retrieved_files(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrievedFileList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrievedFileList]
            List of file metadata objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/retrieved_files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrievedFileList,
                    parse_obj_as(
                        type_=RetrievedFileList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_secret_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SecretSearchList]:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SecretSearchList]
            List of file metadata objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"images/{jsonable_encoder(image_digest)}/artifacts/secret_search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SecretSearchList,
                    parse_obj_as(
                        type_=SecretSearchList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_oauth_token(
        self,
        *,
        client_id: typing.Optional[str] = OMIT,
        grant_type: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokenResponse]:
        """
        Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

        Parameters
        ----------
        client_id : typing.Optional[str]
            The type of client used for the OAuth token

        grant_type : typing.Optional[str]
            OAuth Grant type for token

        password : typing.Optional[str]
            Password for corresponding user

        username : typing.Optional[str]
            User to assign OAuth token to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponse]
            Resulting JWT token
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "client_id": client_id,
                "grant_type": grant_type,
                "password": password,
                "username": username,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def version_check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ServiceVersion]:
        """
        Returns the version object for the service, including db schema version info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ServiceVersion]
            Version object describing version state
        """
        _response = await self._client_wrapper.httpx_client.request(
            "version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServiceVersion,
                    parse_obj_as(
                        type_=ServiceVersion,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
