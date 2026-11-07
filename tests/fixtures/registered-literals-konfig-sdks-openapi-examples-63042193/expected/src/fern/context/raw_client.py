

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
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.context_create_new_context_response import ContextCreateNewContextResponse
from ..types.context_create_restriction409response import ContextCreateRestriction409Response
from ..types.context_get_information_response import ContextGetInformationResponse
from ..types.context_get_restrictions429response import ContextGetRestrictions429Response
from ..types.context_list_environment_variables_response import ContextListEnvironmentVariablesResponse
from ..types.context_list_owner_contexts_response import ContextListOwnerContextsResponse
from ..types.context_project_restrictions_list import ContextProjectRestrictionsList
from ..types.context_remove_context_response import ContextRemoveContextResponse
from ..types.context_remove_environment_variable_response import ContextRemoveEnvironmentVariableResponse
from ..types.context_update_environment_variable_response import ContextUpdateEnvironmentVariableResponse
from ..types.restriction_created import RestrictionCreated
from ..types.restriction_deleted import RestrictionDeleted
from .types.context_create_new_context_request_owner import ContextCreateNewContextRequestOwner
from .types.context_list_owner_contexts_request_owner_type import ContextListOwnerContextsRequestOwnerType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listownercontexts(
        self,
        *,
        owner_id: typing.Optional[str] = None,
        owner_slug: typing.Optional[str] = None,
        owner_type: typing.Optional[ContextListOwnerContextsRequestOwnerType] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContextListOwnerContextsResponse]:
        """
        List all contexts for an owner.

        Parameters
        ----------
        owner_id : typing.Optional[str]
            The unique ID of the owner of the context. Specify either this or owner-slug.

        owner_slug : typing.Optional[str]
            A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.

        owner_type : typing.Optional[ContextListOwnerContextsRequestOwnerType]
            The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextListOwnerContextsResponse]
            A paginated list of contexts
        """
        _response = self._client_wrapper.httpx_client.request(
            "context",
            method="GET",
            params={
                "owner-id": owner_id,
                "owner-slug": owner_slug,
                "owner-type": owner_type,
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextListOwnerContextsResponse,
                    parse_obj_as(
                        type_=ContextListOwnerContextsResponse,
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

    def createnewcontext(
        self,
        *,
        name: str,
        owner: ContextCreateNewContextRequestOwner,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContextCreateNewContextResponse]:
        """
        Creates a new context.

        Parameters
        ----------
        name : str
            The user defined name of the context.

        owner : ContextCreateNewContextRequestOwner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextCreateNewContextResponse]
            The new context
        """
        _response = self._client_wrapper.httpx_client.request(
            "context",
            method="POST",
            json={
                "name": name,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=ContextCreateNewContextRequestOwner, direction="write"
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
                    ContextCreateNewContextResponse,
                    parse_obj_as(
                        type_=ContextCreateNewContextResponse,
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

    def getinformation(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextGetInformationResponse]:
        """
        Returns basic information about a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextGetInformationResponse]
            The context
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextGetInformationResponse,
                    parse_obj_as(
                        type_=ContextGetInformationResponse,
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

    def removecontext(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextRemoveContextResponse]:
        """
        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextRemoveContextResponse]
            A confirmation message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextRemoveContextResponse,
                    parse_obj_as(
                        type_=ContextRemoveContextResponse,
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

    def listenvironmentvariables(
        self,
        context_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContextListEnvironmentVariablesResponse]:
        """
        List information about environment variables in a context, not including their values.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextListEnvironmentVariablesResponse]
            A paginated list of environment variables
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextListEnvironmentVariablesResponse,
                    parse_obj_as(
                        type_=ContextListEnvironmentVariablesResponse,
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

    def updateenvironmentvariable(
        self, context_id: str, env_var_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextUpdateEnvironmentVariableResponse]:
        """
        Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        value : str
            The value of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextUpdateEnvironmentVariableResponse]
            The new environment variable
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable/{encode_path_param(env_var_name)}",
            method="PUT",
            json={
                "value": value,
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
                    ContextUpdateEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ContextUpdateEnvironmentVariableResponse,
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

    def removeenvironmentvariable(
        self, context_id: str, env_var_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextRemoveEnvironmentVariableResponse]:
        """
        Delete an environment variable from a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextRemoveEnvironmentVariableResponse]
            A confirmation message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable/{encode_path_param(env_var_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextRemoveEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ContextRemoveEnvironmentVariableResponse,
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

    def getrestrictions(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextProjectRestrictionsList]:
        """
        [__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextProjectRestrictionsList]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextProjectRestrictionsList,
                    parse_obj_as(
                        type_=ContextProjectRestrictionsList,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    def createrestriction(
        self,
        context_id: str,
        *,
        project_id: typing.Optional[str] = OMIT,
        restriction_type: typing.Optional[str] = OMIT,
        restriction_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RestrictionCreated]:
        """
        [__EXPERIMENTAL__] Creates project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        project_id : typing.Optional[str]
            Deprecated - Use "restriction_type" and "restriction_value"
            instead.

            The project ID to use for a project restriction. This is
            mutually exclusive with restriction_type and restriction_value
            and implies restriction_type is "project".

        restriction_type : typing.Optional[str]

        restriction_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RestrictionCreated]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions",
            method="POST",
            json={
                "project_id": project_id,
                "restriction_type": restriction_type,
                "restriction_value": restriction_value,
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
                    RestrictionCreated,
                    parse_obj_as(
                        type_=RestrictionCreated,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextCreateRestriction409Response,
                        parse_obj_as(
                            type_=ContextCreateRestriction409Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    def deleterestriction(
        self, context_id: str, restriction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RestrictionDeleted]:
        """
        [__EXPERIMENTAL__] Deletes a project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        restriction_id : str
            An opaque identifier of a context restriction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RestrictionDeleted]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions/{encode_path_param(restriction_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RestrictionDeleted,
                    parse_obj_as(
                        type_=RestrictionDeleted,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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


class AsyncRawContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listownercontexts(
        self,
        *,
        owner_id: typing.Optional[str] = None,
        owner_slug: typing.Optional[str] = None,
        owner_type: typing.Optional[ContextListOwnerContextsRequestOwnerType] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContextListOwnerContextsResponse]:
        """
        List all contexts for an owner.

        Parameters
        ----------
        owner_id : typing.Optional[str]
            The unique ID of the owner of the context. Specify either this or owner-slug.

        owner_slug : typing.Optional[str]
            A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.

        owner_type : typing.Optional[ContextListOwnerContextsRequestOwnerType]
            The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextListOwnerContextsResponse]
            A paginated list of contexts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "context",
            method="GET",
            params={
                "owner-id": owner_id,
                "owner-slug": owner_slug,
                "owner-type": owner_type,
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextListOwnerContextsResponse,
                    parse_obj_as(
                        type_=ContextListOwnerContextsResponse,
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

    async def createnewcontext(
        self,
        *,
        name: str,
        owner: ContextCreateNewContextRequestOwner,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContextCreateNewContextResponse]:
        """
        Creates a new context.

        Parameters
        ----------
        name : str
            The user defined name of the context.

        owner : ContextCreateNewContextRequestOwner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextCreateNewContextResponse]
            The new context
        """
        _response = await self._client_wrapper.httpx_client.request(
            "context",
            method="POST",
            json={
                "name": name,
                "owner": convert_and_respect_annotation_metadata(
                    object_=owner, annotation=ContextCreateNewContextRequestOwner, direction="write"
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
                    ContextCreateNewContextResponse,
                    parse_obj_as(
                        type_=ContextCreateNewContextResponse,
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

    async def getinformation(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextGetInformationResponse]:
        """
        Returns basic information about a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextGetInformationResponse]
            The context
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextGetInformationResponse,
                    parse_obj_as(
                        type_=ContextGetInformationResponse,
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

    async def removecontext(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextRemoveContextResponse]:
        """
        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextRemoveContextResponse]
            A confirmation message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextRemoveContextResponse,
                    parse_obj_as(
                        type_=ContextRemoveContextResponse,
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

    async def listenvironmentvariables(
        self,
        context_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContextListEnvironmentVariablesResponse]:
        """
        List information about environment variables in a context, not including their values.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextListEnvironmentVariablesResponse]
            A paginated list of environment variables
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable",
            method="GET",
            params={
                "page-token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextListEnvironmentVariablesResponse,
                    parse_obj_as(
                        type_=ContextListEnvironmentVariablesResponse,
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

    async def updateenvironmentvariable(
        self, context_id: str, env_var_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextUpdateEnvironmentVariableResponse]:
        """
        Create or update an environment variable within a context. Returns information about the environment variable, not including its value.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        value : str
            The value of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextUpdateEnvironmentVariableResponse]
            The new environment variable
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable/{encode_path_param(env_var_name)}",
            method="PUT",
            json={
                "value": value,
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
                    ContextUpdateEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ContextUpdateEnvironmentVariableResponse,
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

    async def removeenvironmentvariable(
        self, context_id: str, env_var_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextRemoveEnvironmentVariableResponse]:
        """
        Delete an environment variable from a context.

        Parameters
        ----------
        context_id : str
            ID of the context (UUID)

        env_var_name : str
            The name of the environment variable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextRemoveEnvironmentVariableResponse]
            A confirmation message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/environment-variable/{encode_path_param(env_var_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextRemoveEnvironmentVariableResponse,
                    parse_obj_as(
                        type_=ContextRemoveEnvironmentVariableResponse,
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

    async def getrestrictions(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextProjectRestrictionsList]:
        """
        [__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextProjectRestrictionsList]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextProjectRestrictionsList,
                    parse_obj_as(
                        type_=ContextProjectRestrictionsList,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    async def createrestriction(
        self,
        context_id: str,
        *,
        project_id: typing.Optional[str] = OMIT,
        restriction_type: typing.Optional[str] = OMIT,
        restriction_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RestrictionCreated]:
        """
        [__EXPERIMENTAL__] Creates project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        project_id : typing.Optional[str]
            Deprecated - Use "restriction_type" and "restriction_value"
            instead.

            The project ID to use for a project restriction. This is
            mutually exclusive with restriction_type and restriction_value
            and implies restriction_type is "project".

        restriction_type : typing.Optional[str]

        restriction_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RestrictionCreated]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions",
            method="POST",
            json={
                "project_id": project_id,
                "restriction_type": restriction_type,
                "restriction_value": restriction_value,
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
                    RestrictionCreated,
                    parse_obj_as(
                        type_=RestrictionCreated,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextCreateRestriction409Response,
                        parse_obj_as(
                            type_=ContextCreateRestriction409Response,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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

    async def deleterestriction(
        self, context_id: str, restriction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RestrictionDeleted]:
        """
        [__EXPERIMENTAL__] Deletes a project restriction on a context.

        Parameters
        ----------
        context_id : str
            An opaque identifier of a context.

        restriction_id : str
            An opaque identifier of a context restriction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RestrictionDeleted]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"context/{encode_path_param(context_id)}/restrictions/{encode_path_param(restriction_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RestrictionDeleted,
                    parse_obj_as(
                        type_=RestrictionDeleted,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ContextGetRestrictions429Response,
                        parse_obj_as(
                            type_=ContextGetRestrictions429Response,
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
