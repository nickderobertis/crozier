

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.error import Error
from .types.get_api_shards_host_owner_repo_version_response import GetApiShardsHostOwnerRepoVersionResponse
from .types.get_api_shards_host_owner_repo_versions_response import GetApiShardsHostOwnerRepoVersionsResponse
from pydantic import ValidationError


class RawVersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_shard_versions(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiShardsHostOwnerRepoVersionsResponse]:
        """
        Get all versions of a specific shard

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
        HttpResponse[GetApiShardsHostOwnerRepoVersionsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsHostOwnerRepoVersionsResponse,
                    parse_obj_as(
                        type_=GetApiShardsHostOwnerRepoVersionsResponse,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_specific_version(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiShardsHostOwnerRepoVersionResponse]:
        """
        Get detailed information about a specific version of a shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        version : str
            Version string (e.g., 1.0.0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiShardsHostOwnerRepoVersionResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}/{encode_path_param(version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsHostOwnerRepoVersionResponse,
                    parse_obj_as(
                        type_=GetApiShardsHostOwnerRepoVersionResponse,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_shard_versions(
        self, host: str, owner: str, repo: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiShardsHostOwnerRepoVersionsResponse]:
        """
        Get all versions of a specific shard

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
        AsyncHttpResponse[GetApiShardsHostOwnerRepoVersionsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsHostOwnerRepoVersionsResponse,
                    parse_obj_as(
                        type_=GetApiShardsHostOwnerRepoVersionsResponse,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_specific_version(
        self, host: str, owner: str, repo: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiShardsHostOwnerRepoVersionResponse]:
        """
        Get detailed information about a specific version of a shard

        Parameters
        ----------
        host : str
            Repository host

        owner : str
            Owner or organisation on that host

        repo : str
            Repository name on that host

        version : str
            Version string (e.g., 1.0.0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiShardsHostOwnerRepoVersionResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/shards/{encode_path_param(host)}/{encode_path_param(owner)}/{encode_path_param(repo)}/{encode_path_param(version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiShardsHostOwnerRepoVersionResponse,
                    parse_obj_as(
                        type_=GetApiShardsHostOwnerRepoVersionResponse,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
