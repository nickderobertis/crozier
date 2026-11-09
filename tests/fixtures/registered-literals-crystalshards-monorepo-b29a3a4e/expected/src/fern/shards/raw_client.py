

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
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.conflict_error_body import ConflictErrorBody
from ..types.content_too_large_error_body import ContentTooLargeErrorBody
from ..types.error import Error
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.shard_detail import ShardDetail
from ..types.validation_error import ValidationError as types_validation_error_ValidationError
from .types.get_api_shards_response import GetApiShardsResponse
from .types.post_api_shards_response import PostApiShardsResponse
from .types.post_api_shards_upload_response import PostApiShardsUploadResponse
from pydantic import ValidationError as pydantic_ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawShardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_shards(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetApiShardsResponse]:
        """
        Get a paginated list of all Crystal shards

        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Number of items per page

        query : typing.Optional[str]
            Search query to filter shards by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiShardsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/shards",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsResponse,
                    parse_obj_as(
                        type_=GetApiShardsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_a_new_shard(
        self,
        *,
        name: str,
        repository_url: str,
        version: str,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiShardsResponse]:
        """
        Publish a new Crystal shard to the registry

        Parameters
        ----------
        name : str

        repository_url : str

        version : str

        description : typing.Optional[str]

        homepage_url : typing.Optional[str]

        documentation_url : typing.Optional[str]

        license : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiShardsResponse]
            Shard created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/shards",
            method="POST",
            json={
                "name": name,
                "description": description,
                "repository_url": repository_url,
                "homepage_url": homepage_url,
                "documentation_url": documentation_url,
                "license": license,
                "version": version,
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
                    PostApiShardsResponse,
                    parse_obj_as(
                        type_=PostApiShardsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upload_shard_package(
        self,
        *,
        name: str,
        version: str,
        repository_url: str,
        package: core.File,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiShardsUploadResponse]:
        """
        Upload a Crystal shard package via multipart form data.
        This endpoint accepts a .tar.gz file along with shard metadata.
        The package is uploaded directly to MinIO storage and a ShardVersion is created.

        **Authentication required:** Include auth_token in Authorization header or as query parameter.
        **Size limit:** Maximum 50 MB per package.

        Parameters
        ----------
        name : str
            Unique shard name (lowercase, alphanumeric with hyphens)

        version : str
            Semantic version number

        repository_url : str
            Git repository URL

        package : core.File
            See core.File for more documentation

        description : typing.Optional[str]
            Brief description of the shard

        homepage_url : typing.Optional[str]
            Project homepage URL

        documentation_url : typing.Optional[str]
            Documentation URL

        license : typing.Optional[str]
            SPDX license identifier

        checksum : typing.Optional[str]
            Optional SHA256 checksum for verification (computed if not provided)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiShardsUploadResponse]
            Package uploaded successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/shards/upload",
            method="POST",
            data={
                "name": name,
                "version": version,
                "description": description,
                "repository_url": repository_url,
                "homepage_url": homepage_url,
                "documentation_url": documentation_url,
                "license": license,
                "checksum": checksum,
            },
            files={
                "package": package,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiShardsUploadResponse,
                    parse_obj_as(
                        type_=PostApiShardsUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContentTooLargeErrorBody,
                        parse_obj_as(
                            type_=ContentTooLargeErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_shard_details_by_name_deprecated(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Superseded by /api/shards/{host}/{owner}/{repo}. A shard is identified by
        the repository it comes from, because two shards may share a name on
        different hosts.

        When exactly one shard carries the name, this responds 301 with the
        canonical path in Location. When more than one does, it responds 409
        with the candidate paths rather than guessing which was meant.

        Parameters
        ----------
        name : str
            Shard display name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_shard_details(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ShardDetail]:
        """
        Get a shard by the repository that identifies it, for example
        /api/shards/github.com/kemalcr/kemal.

        Nested namespace paths (host/group/subgroup/repo) are not addressable:
        identity is host/owner/repo.

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShardDetail]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShardDetail,
                    parse_obj_as(
                        type_=ShardDetail,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawShardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_shards(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetApiShardsResponse]:
        """
        Get a paginated list of all Crystal shards

        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Number of items per page

        query : typing.Optional[str]
            Search query to filter shards by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiShardsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/shards",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsResponse,
                    parse_obj_as(
                        type_=GetApiShardsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_a_new_shard(
        self,
        *,
        name: str,
        repository_url: str,
        version: str,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiShardsResponse]:
        """
        Publish a new Crystal shard to the registry

        Parameters
        ----------
        name : str

        repository_url : str

        version : str

        description : typing.Optional[str]

        homepage_url : typing.Optional[str]

        documentation_url : typing.Optional[str]

        license : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiShardsResponse]
            Shard created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/shards",
            method="POST",
            json={
                "name": name,
                "description": description,
                "repository_url": repository_url,
                "homepage_url": homepage_url,
                "documentation_url": documentation_url,
                "license": license,
                "version": version,
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
                    PostApiShardsResponse,
                    parse_obj_as(
                        type_=PostApiShardsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upload_shard_package(
        self,
        *,
        name: str,
        version: str,
        repository_url: str,
        package: core.File,
        description: typing.Optional[str] = OMIT,
        homepage_url: typing.Optional[str] = OMIT,
        documentation_url: typing.Optional[str] = OMIT,
        license: typing.Optional[str] = OMIT,
        checksum: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiShardsUploadResponse]:
        """
        Upload a Crystal shard package via multipart form data.
        This endpoint accepts a .tar.gz file along with shard metadata.
        The package is uploaded directly to MinIO storage and a ShardVersion is created.

        **Authentication required:** Include auth_token in Authorization header or as query parameter.
        **Size limit:** Maximum 50 MB per package.

        Parameters
        ----------
        name : str
            Unique shard name (lowercase, alphanumeric with hyphens)

        version : str
            Semantic version number

        repository_url : str
            Git repository URL

        package : core.File
            See core.File for more documentation

        description : typing.Optional[str]
            Brief description of the shard

        homepage_url : typing.Optional[str]
            Project homepage URL

        documentation_url : typing.Optional[str]
            Documentation URL

        license : typing.Optional[str]
            SPDX license identifier

        checksum : typing.Optional[str]
            Optional SHA256 checksum for verification (computed if not provided)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiShardsUploadResponse]
            Package uploaded successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/shards/upload",
            method="POST",
            data={
                "name": name,
                "version": version,
                "description": description,
                "repository_url": repository_url,
                "homepage_url": homepage_url,
                "documentation_url": documentation_url,
                "license": license,
                "checksum": checksum,
            },
            files={
                "package": package,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiShardsUploadResponse,
                    parse_obj_as(
                        type_=PostApiShardsUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContentTooLargeErrorBody,
                        parse_obj_as(
                            type_=ContentTooLargeErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_shard_details_by_name_deprecated(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Superseded by /api/shards/{host}/{owner}/{repo}. A shard is identified by
        the repository it comes from, because two shards may share a name on
        different hosts.

        When exactly one shard carries the name, this responds 301 with the
        canonical path in Location. When more than one does, it responds 409
        with the candidate paths rather than guessing which was meant.

        Parameters
        ----------
        name : str
            Shard display name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_shard_details(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ShardDetail]:
        """
        Get a shard by the repository that identifies it, for example
        /api/shards/github.com/kemalcr/kemal.

        Nested namespace paths (host/group/subgroup/repo) are not addressable:
        identity is host/owner/repo.

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShardDetail]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShardDetail,
                    parse_obj_as(
                        type_=ShardDetail,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
