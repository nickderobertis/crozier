

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
from ..types.chat_completion_message_param import ChatCompletionMessageParam
from ..types.create_function_function_schema import CreateFunctionFunctionSchema
from ..types.create_function_origin import CreateFunctionOrigin
from ..types.ending_before import EndingBefore
from ..types.function import Function
from ..types.function_data import FunctionData
from ..types.function_data_nullish import FunctionDataNullish
from ..types.function_id_param import FunctionIdParam
from ..types.function_name import FunctionName
from ..types.function_type_enum_nullish import FunctionTypeEnumNullish
from ..types.ids import Ids
from ..types.invoke_parent import InvokeParent
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.prompt_data_nullish import PromptDataNullish
from ..types.prompt_environment import PromptEnvironment
from ..types.prompt_version import PromptVersion
from ..types.slug import Slug
from ..types.starting_after import StartingAfter
from ..types.streaming_mode import StreamingMode
from .types.get_function_response import GetFunctionResponse
from .types.invoke_api_mcp_auth_value import InvokeApiMcpAuthValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_function(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        function_name: typing.Optional[FunctionName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetFunctionResponse]:
        """
        List out all functions. The functions are sorted by creation date, with the most recently-created functions coming first

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

        function_name : typing.Optional[FunctionName]
            Name of the function to search for

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
        HttpResponse[GetFunctionResponse]
            Returns a list of function objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/function",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "function_name": function_name,
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
                    GetFunctionResponse,
                    parse_obj_as(
                        type_=GetFunctionResponse,
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

    def post_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Create a new function. If there is an existing function in the project with the same slug as the one specified in the request, will return the existing function unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Returns the new function object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/function",
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
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=FunctionData, direction="write"
                ),
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=typing.Optional[CreateFunctionOrigin], direction="write"
                ),
                "function_schema": convert_and_respect_annotation_metadata(
                    object_=function_schema, annotation=typing.Optional[CreateFunctionFunctionSchema], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def put_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Returns the new function object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/function",
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
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=FunctionData, direction="write"
                ),
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=typing.Optional[CreateFunctionOrigin], direction="write"
                ),
                "function_schema": convert_and_respect_annotation_metadata(
                    object_=function_schema, annotation=typing.Optional[CreateFunctionFunctionSchema], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def get_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Get a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

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
        HttpResponse[Function]
            Returns the function object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def delete_function_id(
        self, function_id: FunctionIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Function]:
        """
        Delete a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Returns the deleted function object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def patch_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        function_data: typing.Optional[FunctionDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Partially update a function object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        name : typing.Optional[str]
            Name of the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        function_data : typing.Optional[FunctionDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Returns the function object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=typing.Optional[FunctionDataNullish], direction="write"
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def post_function_id_invoke(
        self,
        function_id: FunctionIdParam,
        *,
        input: typing.Optional[typing.Any] = OMIT,
        expected: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatCompletionMessageParam]] = OMIT,
        parent: typing.Optional[InvokeParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        mode: typing.Optional[StreamingMode] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]] = OMIT,
        overrides: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Invoke a function.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        input : typing.Optional[typing.Any]
            Argument to the function, which can be any JSON serializable value

        expected : typing.Optional[typing.Any]
            The expected output of the function

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Any relevant metadata. This will be logged and available as the `metadata` argument.

        tags : typing.Optional[typing.Sequence[str]]
            Any relevant tags to log on the span.

        messages : typing.Optional[typing.Sequence[ChatCompletionMessageParam]]
            If the function is an LLM, additional messages to pass along to it

        parent : typing.Optional[InvokeParent]

        stream : typing.Optional[bool]
            Whether to stream the response. If true, results will be returned in the Braintrust SSE format.

        mode : typing.Optional[StreamingMode]

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        mcp_auth : typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]]
            Map of MCP server URL to auth credentials

        overrides : typing.Optional[typing.Dict[str, typing.Any]]
            Partial function definition to merge with the function being invoked. Fields are validated against the function type's schema at runtime. For facets: { preprocessor?, prompt?, model? }. For prompts: { model?, ... }.

        version : typing.Optional[str]
            The version of the function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Function invocation response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}/invoke",
            method="POST",
            json={
                "input": input,
                "expected": expected,
                "metadata": metadata,
                "tags": tags,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatCompletionMessageParam], direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=InvokeParent, direction="write"
                ),
                "stream": stream,
                "mode": mode,
                "strict": strict,
                "mcp_auth": convert_and_respect_annotation_metadata(
                    object_=mcp_auth, annotation=typing.Dict[str, InvokeApiMcpAuthValue], direction="write"
                ),
                "overrides": overrides,
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
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


class AsyncRawFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_function(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        function_name: typing.Optional[FunctionName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        slug: typing.Optional[Slug] = None,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetFunctionResponse]:
        """
        List out all functions. The functions are sorted by creation date, with the most recently-created functions coming first

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

        function_name : typing.Optional[FunctionName]
            Name of the function to search for

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
        AsyncHttpResponse[GetFunctionResponse]
            Returns a list of function objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/function",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "function_name": function_name,
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
                    GetFunctionResponse,
                    parse_obj_as(
                        type_=GetFunctionResponse,
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

    async def post_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Create a new function. If there is an existing function in the project with the same slug as the one specified in the request, will return the existing function unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Returns the new function object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/function",
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
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=FunctionData, direction="write"
                ),
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=typing.Optional[CreateFunctionOrigin], direction="write"
                ),
                "function_schema": convert_and_respect_annotation_metadata(
                    object_=function_schema, annotation=typing.Optional[CreateFunctionFunctionSchema], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def put_function(
        self,
        *,
        project_id: str,
        name: str,
        slug: str,
        function_data: FunctionData,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        function_type: typing.Optional[FunctionTypeEnumNullish] = OMIT,
        origin: typing.Optional[CreateFunctionOrigin] = OMIT,
        function_schema: typing.Optional[CreateFunctionFunctionSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the prompt belongs under

        name : str
            Name of the prompt

        slug : str
            Unique identifier for the prompt

        function_data : FunctionData

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        function_type : typing.Optional[FunctionTypeEnumNullish]

        origin : typing.Optional[CreateFunctionOrigin]

        function_schema : typing.Optional[CreateFunctionFunctionSchema]
            JSON schema for the function's parameters and return type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Returns the new function object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/function",
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
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=FunctionData, direction="write"
                ),
                "origin": convert_and_respect_annotation_metadata(
                    object_=origin, annotation=typing.Optional[CreateFunctionOrigin], direction="write"
                ),
                "function_schema": convert_and_respect_annotation_metadata(
                    object_=function_schema, annotation=typing.Optional[CreateFunctionFunctionSchema], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def get_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        version: typing.Optional[PromptVersion] = None,
        environment: typing.Optional[PromptEnvironment] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Get a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

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
        AsyncHttpResponse[Function]
            Returns the function object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def delete_function_id(
        self, function_id: FunctionIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Function]:
        """
        Delete a function object by its id

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Returns the deleted function object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def patch_function_id(
        self,
        function_id: FunctionIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        prompt_data: typing.Optional[PromptDataNullish] = OMIT,
        function_data: typing.Optional[FunctionDataNullish] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Partially update a function object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        name : typing.Optional[str]
            Name of the prompt

        description : typing.Optional[str]
            Textual description of the prompt

        prompt_data : typing.Optional[PromptDataNullish]

        function_data : typing.Optional[FunctionDataNullish]

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Returns the function object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "prompt_data": convert_and_respect_annotation_metadata(
                    object_=prompt_data, annotation=typing.Optional[PromptDataNullish], direction="write"
                ),
                "function_data": convert_and_respect_annotation_metadata(
                    object_=function_data, annotation=typing.Optional[FunctionDataNullish], direction="write"
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def post_function_id_invoke(
        self,
        function_id: FunctionIdParam,
        *,
        input: typing.Optional[typing.Any] = OMIT,
        expected: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatCompletionMessageParam]] = OMIT,
        parent: typing.Optional[InvokeParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        mode: typing.Optional[StreamingMode] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]] = OMIT,
        overrides: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Invoke a function.

        Parameters
        ----------
        function_id : FunctionIdParam
            Function id

        input : typing.Optional[typing.Any]
            Argument to the function, which can be any JSON serializable value

        expected : typing.Optional[typing.Any]
            The expected output of the function

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Any relevant metadata. This will be logged and available as the `metadata` argument.

        tags : typing.Optional[typing.Sequence[str]]
            Any relevant tags to log on the span.

        messages : typing.Optional[typing.Sequence[ChatCompletionMessageParam]]
            If the function is an LLM, additional messages to pass along to it

        parent : typing.Optional[InvokeParent]

        stream : typing.Optional[bool]
            Whether to stream the response. If true, results will be returned in the Braintrust SSE format.

        mode : typing.Optional[StreamingMode]

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        mcp_auth : typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]]
            Map of MCP server URL to auth credentials

        overrides : typing.Optional[typing.Dict[str, typing.Any]]
            Partial function definition to merge with the function being invoked. Fields are validated against the function type's schema at runtime. For facets: { preprocessor?, prompt?, model? }. For prompts: { model?, ... }.

        version : typing.Optional[str]
            The version of the function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Function invocation response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/function/{encode_path_param(function_id)}/invoke",
            method="POST",
            json={
                "input": input,
                "expected": expected,
                "metadata": metadata,
                "tags": tags,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatCompletionMessageParam], direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=InvokeParent, direction="write"
                ),
                "stream": stream,
                "mode": mode,
                "strict": strict,
                "mcp_auth": convert_and_respect_annotation_metadata(
                    object_=mcp_auth, annotation=typing.Dict[str, InvokeApiMcpAuthValue], direction="write"
                ),
                "overrides": overrides,
                "version": version,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
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
