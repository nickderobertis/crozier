

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.prompts_get_response import PromptsGetResponse
from ..types.prompts_prompt_name_post_response import PromptsPromptNamePostResponse
from ..types.prompts_refresh_post_response import PromptsRefreshPostResponse
from ..types.prompts_sources_post_error413 import PromptsSourcesPostError413
from ..types.prompts_sources_post_response import PromptsSourcesPostResponse
from .types.prompts_sources_post_request_files_item import PromptsSourcesPostRequestFilesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_available_prompts(
        self,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PromptsGetResponse]:
        """
        List all available prompts

        Parameters
        ----------
        source : typing.Optional[str]
            Enumerate a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). An unknown/evicted identifier returns 400 with re-upload guidance. Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PromptsGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/prompts",
            method="GET",
            params={
                "source": source,
                "repo": repo,
                "path": path,
                "branch": branch,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptsGetResponse,
                    parse_obj_as(
                        type_=PromptsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PromptsRefreshPostResponse]:
        """
        Force-refresh the prompts cache by pulling latest from the git repository

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PromptsRefreshPostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/prompts/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptsRefreshPostResponse,
                    parse_obj_as(
                        type_=PromptsRefreshPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
        self,
        *,
        source: str,
        files: typing.Sequence[PromptsSourcesPostRequestFilesItem],
        content_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PromptsSourcesPostResponse]:
        """
        Ingest (upload) a skill source the server caches and renders via POST /api/v1/prompts/:promptName?source=<identifier> with no git clone (PRD #647)

        Parameters
        ----------
        source : str
            Stable source identifier (e.g., "local:team-dev" or a git URL the server cannot reach)

        files : typing.Sequence[PromptsSourcesPostRequestFilesItem]
            Uploaded files with base64-encoded content

        content_hash : typing.Optional[str]
            CLI-computed content hash (enables future re-upload dedup)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PromptsSourcesPostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/prompts/sources",
            method="POST",
            json={
                "source": source,
                "contentHash": content_hash,
                "files": convert_and_respect_annotation_metadata(
                    object_=files, annotation=typing.Sequence[PromptsSourcesPostRequestFilesItem], direction="write"
                ),
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
                    PromptsSourcesPostResponse,
                    parse_obj_as(
                        type_=PromptsSourcesPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
                        PromptsSourcesPostError413,
                        parse_obj_as(
                            type_=PromptsSourcesPostError413,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_a_prompt_with_rendered_template_arguments(
        self,
        prompt_name: str,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        arguments: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PromptsPromptNamePostResponse]:
        """
        Get a prompt with rendered template arguments

        Parameters
        ----------
        prompt_name : str
            Name of the prompt

        source : typing.Optional[str]
            Render a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        arguments : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PromptsPromptNamePostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/prompts/{encode_path_param(prompt_name)}",
            method="POST",
            params={
                "source": source,
                "repo": repo,
                "path": path,
                "branch": branch,
            },
            json={
                "arguments": arguments,
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
                    PromptsPromptNamePostResponse,
                    parse_obj_as(
                        type_=PromptsPromptNamePostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_available_prompts(
        self,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PromptsGetResponse]:
        """
        List all available prompts

        Parameters
        ----------
        source : typing.Optional[str]
            Enumerate a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). An unknown/evicted identifier returns 400 with re-upload guidance. Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PromptsGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/prompts",
            method="GET",
            params={
                "source": source,
                "repo": repo,
                "path": path,
                "branch": branch,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptsGetResponse,
                    parse_obj_as(
                        type_=PromptsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PromptsRefreshPostResponse]:
        """
        Force-refresh the prompts cache by pulling latest from the git repository

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PromptsRefreshPostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/prompts/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PromptsRefreshPostResponse,
                    parse_obj_as(
                        type_=PromptsRefreshPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
        self,
        *,
        source: str,
        files: typing.Sequence[PromptsSourcesPostRequestFilesItem],
        content_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PromptsSourcesPostResponse]:
        """
        Ingest (upload) a skill source the server caches and renders via POST /api/v1/prompts/:promptName?source=<identifier> with no git clone (PRD #647)

        Parameters
        ----------
        source : str
            Stable source identifier (e.g., "local:team-dev" or a git URL the server cannot reach)

        files : typing.Sequence[PromptsSourcesPostRequestFilesItem]
            Uploaded files with base64-encoded content

        content_hash : typing.Optional[str]
            CLI-computed content hash (enables future re-upload dedup)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PromptsSourcesPostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/prompts/sources",
            method="POST",
            json={
                "source": source,
                "contentHash": content_hash,
                "files": convert_and_respect_annotation_metadata(
                    object_=files, annotation=typing.Sequence[PromptsSourcesPostRequestFilesItem], direction="write"
                ),
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
                    PromptsSourcesPostResponse,
                    parse_obj_as(
                        type_=PromptsSourcesPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
                        PromptsSourcesPostError413,
                        parse_obj_as(
                            type_=PromptsSourcesPostError413,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_a_prompt_with_rendered_template_arguments(
        self,
        prompt_name: str,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        arguments: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PromptsPromptNamePostResponse]:
        """
        Get a prompt with rendered template arguments

        Parameters
        ----------
        prompt_name : str
            Name of the prompt

        source : typing.Optional[str]
            Render a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        arguments : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PromptsPromptNamePostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/prompts/{encode_path_param(prompt_name)}",
            method="POST",
            params={
                "source": source,
                "repo": repo,
                "path": path,
                "branch": branch,
            },
            json={
                "arguments": arguments,
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
                    PromptsPromptNamePostResponse,
                    parse_obj_as(
                        type_=PromptsPromptNamePostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
