

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.function_type_enum_nullish import FunctionTypeEnumNullish
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.prompt import Prompt
from ..types.prompt_data_nullish import PromptDataNullish
from ..types.prompt_environment import PromptEnvironment
from ..types.prompt_id_param import PromptIdParam
from ..types.prompt_name import PromptName
from ..types.prompt_version import PromptVersion
from ..types.slug import Slug
from ..types.starting_after import StartingAfter
from .types.get_prompt_response import GetPromptResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_prompt(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        prompt_name: typing.Optional[PromptName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPromptResponse]:
        """
        List out all prompts. The prompts are sorted by creation date, with the most recently-created prompts coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        prompt_name : typing.Optional[PromptName]
            Name of the prompt to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        slug : typing.Optional[Slug]
            Retrieve prompt with a specific slug

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPromptResponse]
            Returns a list of prompt objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "prompt_name": prompt_name,
                "project_name": project_name,
                "project_id": project_id,
                "slug": slug,
                "version": version,
                "environment": environment,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPromptResponse,
                    parse_obj_as(
                        type_=GetPromptResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Create a new prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will return the existing prompt unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Returns the new prompt object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
                "function_type": function_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def put_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Create or replace prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will replace the existing prompt with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Returns the new prompt object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="PUT",
            json={
                "project_id": project_id,
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
                "function_type": function_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def get_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Get a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Returns the prompt object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="GET",
            params={
                "version": version,
                "environment": environment,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def delete_prompt_id(
        self, prompt_id: PromptIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Prompt]:
        """
        Delete a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Returns the deleted prompt object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def patch_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
        """
        Partially update a prompt object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        name : typing.Optional[str]
            Name of the prompt

        slug : typing.Optional[str]
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Prompt]
            Returns the prompt object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="PATCH",
            json={
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_prompt(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        prompt_name: typing.Optional[PromptName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPromptResponse]:
        """
        List out all prompts. The prompts are sorted by creation date, with the most recently-created prompts coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        prompt_name : typing.Optional[PromptName]
            Name of the prompt to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        slug : typing.Optional[Slug]
            Retrieve prompt with a specific slug

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPromptResponse]
            Returns a list of prompt objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "prompt_name": prompt_name,
                "project_name": project_name,
                "project_id": project_id,
                "slug": slug,
                "version": version,
                "environment": environment,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPromptResponse,
                    parse_obj_as(
                        type_=GetPromptResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Create a new prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will return the existing prompt unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Returns the new prompt object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
                "function_type": function_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def put_prompt(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Create or replace prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will replace the existing prompt with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Returns the new prompt object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/prompt",
            method="PUT",
            json={
                "project_id": project_id,
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
                "function_type": function_type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Get a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        version : typing.Optional[PromptVersion]
            Retrieve prompt at a specific version.

            The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').

        environment : typing.Optional[PromptEnvironment]
            Filter by environment slug. Cannot be used together with `version`.

            For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Returns the prompt object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="GET",
            params={
                "version": version,
                "environment": environment,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def delete_prompt_id(
        self, prompt_id: PromptIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Prompt]:
        """
        Delete a prompt object by its id

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Returns the deleted prompt object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def patch_prompt_id(
        self,
        prompt_id: PromptIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
        """
        Partially update a prompt object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        prompt_id : PromptIdParam
            Prompt id

        name : typing.Optional[str]
            Name of the prompt

        slug : typing.Optional[str]
            Unique identifier for the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Prompt]
            Returns the prompt object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/prompt/{encode_path_param(prompt_id)}",
            method="PATCH",
            json={
                "name": name,
                "slug": slug,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "tags": tags,
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
