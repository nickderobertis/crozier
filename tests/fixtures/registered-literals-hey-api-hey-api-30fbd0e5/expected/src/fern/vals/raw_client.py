

import contextlib
import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.precondition_failed_error import PreconditionFailedError
from ..types.branch import Branch
from ..types.file_revision_metadata_v2 import FileRevisionMetadataV2
from ..types.t_environment_variable import TEnvironmentVariable
from ..types.val import Val
from .types.branches_list2response import BranchesList2Response
from .types.file_content_update2request_type import FileContentUpdate2RequestType
from .types.files_create2request_body import FilesCreate2RequestBody
from .types.val_environment_variable_groups_list_response import ValEnvironmentVariableGroupsListResponse
from .types.val_environment_variables_list_response import ValEnvironmentVariablesListResponse
from .types.val_files_get2response import ValFilesGet2Response
from .types.vals_create2request_privacy import ValsCreate2RequestPrivacy
from .types.vals_list2request_privacy import ValsList2RequestPrivacy
from .types.vals_list2response import ValsList2Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawValsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def val_environment_variables_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ValEnvironmentVariablesListResponse]:
        """
        List environment variables defined in this project. This only includes names, not values.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValEnvironmentVariablesListResponse]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValEnvironmentVariablesListResponse,
                    parse_obj_as(
                        type_=ValEnvironmentVariablesListResponse,
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

    def val_environment_variables_create(
        self,
        val_id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TEnvironmentVariable]:
        """
        Create a new environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/",
            method="POST",
            json={
                "value": value,
                "description": description,
                "key": key,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def val_environment_variables_update(
        self,
        val_id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TEnvironmentVariable]:
        """
        Update a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/{encode_path_param(key)}",
            method="PUT",
            json={
                "value": value,
                "description": description,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
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

    def val_environment_variables_delete(
        self, val_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def val_environment_variable_groups_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ValEnvironmentVariableGroupsListResponse]:
        """
        List the environment variable groups attached to this val. This only includes the groups, not the variables in them.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValEnvironmentVariableGroupsListResponse]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValEnvironmentVariableGroupsListResponse,
                    parse_obj_as(
                        type_=ValEnvironmentVariableGroupsListResponse,
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

    def val_environment_variable_groups_attach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Attach an environment variable group to this val. Every variable in the group is injected into the val's environment. Variables defined on the val itself take precedence over variables with the same key in a group. Attaching a group that is already attached succeeds without doing anything.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/{encode_path_param(group_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def val_environment_variable_groups_detach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Detach an environment variable group from this val. The group itself, and the variables in it, are left alone.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def vals_get2(self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Val]:
        """
        Get a val by id

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Val]
            A Val
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Val,
                    parse_obj_as(
                        type_=Val,
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

    def projects_delete2(
        self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a project

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def vals_list2(
        self,
        *,
        limit: int,
        privacy: typing.Optional[ValsList2RequestPrivacy] = None,
        user_id: typing.Optional[str] = None,
        cursor: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ValsList2Response]:
        """
        Lists all vals including all public vals and your unlisted and private vals

        Parameters
        ----------
        limit : int
            Maximum items to return in each paginated response

        privacy : typing.Optional[ValsList2RequestPrivacy]
            This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.

        user_id : typing.Optional[str]
            User ID to filter by

        cursor : typing.Optional[dt.datetime]
            Cursor to start the pagination from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValsList2Response]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vals",
            method="GET",
            params={
                "privacy": privacy,
                "user_id": user_id,
                "cursor": serialize_datetime(cursor) if cursor is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValsList2Response,
                    parse_obj_as(
                        type_=ValsList2Response,
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

    def vals_create2(
        self,
        *,
        name: str,
        privacy: ValsCreate2RequestPrivacy,
        description: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Val]:
        """
        Create a new val

        Parameters
        ----------
        name : str

        privacy : ValsCreate2RequestPrivacy

        description : typing.Optional[str]

        org_id : typing.Optional[str]
            ID of the org to create the val in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Val]
            A Val
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vals",
            method="POST",
            json={
                "name": name,
                "description": description,
                "privacy": privacy,
                "orgId": org_id,
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
                    Val,
                    parse_obj_as(
                        type_=Val,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def branches_get2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Branch]:
        """
        Get a branch by id

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Branch]
            A Branch
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches/{encode_path_param(branch_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Branch,
                    parse_obj_as(
                        type_=Branch,
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

    def branches_delete2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a branch

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches/{encode_path_param(branch_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def branches_list2(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BranchesList2Response]:
        """
        List all branches for a val

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BranchesList2Response]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchesList2Response,
                    parse_obj_as(
                        type_=BranchesList2Response,
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

    def branches_create2(
        self,
        val_id: str,
        *,
        name: str,
        branch_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Branch]:
        """
        Create a new branch

        Parameters
        ----------
        val_id : str
            Id of a val

        name : str

        branch_id : typing.Optional[str]
            The branch ID to fork from. If this is not specified, the new branch will be forked from main.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Branch]
            A Branch
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches",
            method="POST",
            json={
                "name": name,
                "branchId": branch_id,
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
                    Branch,
                    parse_obj_as(
                        type_=Branch,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def val_files_get2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        offset: int,
        limit: int,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ValFilesGet2Response]:
        """
        Get metadata for files and directories in a val. If path is an empty string, returns files at the root directory.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ValFilesGet2Response]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="GET",
            params={
                "version": version,
                "branch_id": branch_id,
                "path": path,
                "recursive": recursive,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValFilesGet2Response,
                    parse_obj_as(
                        type_=ValFilesGet2Response,
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

    def files_create2(
        self,
        val_id: str,
        *,
        path: str,
        request: FilesCreate2RequestBody,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileRevisionMetadataV2]:
        """
        Create a new file, project val or directory

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        request : FilesCreate2RequestBody

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="POST",
            params={
                "branch_id": branch_id,
                "path": path,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=FilesCreate2RequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    def file_content_update2(
        self,
        val_id: str,
        *,
        path: str,
        branch_id: typing.Optional[str] = None,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[FileContentUpdate2RequestType] = OMIT,
        parent_path: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileRevisionMetadataV2]:
        """
        Update a file's content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        content : typing.Optional[str]
            File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.

        type : typing.Optional[FileContentUpdate2RequestType]

        parent_path : typing.Optional[str]
            Path to the directory you'd like to move this file to (e.g. 'folder1/folder2')

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="PUT",
            params={
                "branch_id": branch_id,
                "path": path,
            },
            json={
                "content": content,
                "type": type,
                "parent_path": parent_path,
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
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
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

    def files_delete2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a file or a directory. To delete a directory and all of its children, use the recursive flag. To delete all files, pass in an empty path and the recursive flag.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="DELETE",
            params={
                "branch_id": branch_id,
                "path": path,
                "recursive": recursive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def files_content_get2(
        self,
        val_id: str,
        *,
        path: str,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        if_unmodified_since: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        if_modified_since: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Download file content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        if_match : typing.Optional[str]

        if_unmodified_since : typing.Optional[str]

        if_none_match : typing.Optional[str]

        if_modified_since : typing.Optional[str]

        cache_control : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Contents of the file
        """
        with self._client_wrapper.httpx_client.stream(
            f"v2/vals/{encode_path_param(val_id)}/files/content",
            method="GET",
            params={
                "version": version,
                "branch_id": branch_id,
                "path": path,
            },
            headers={
                "If-Match": str(if_match) if if_match is not None else None,
                "If-Unmodified-Since": str(if_unmodified_since) if if_unmodified_since is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
                "Cache-Control": str(cache_control) if cache_control is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 412:
                        raise PreconditionFailedError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawValsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def val_environment_variables_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ValEnvironmentVariablesListResponse]:
        """
        List environment variables defined in this project. This only includes names, not values.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValEnvironmentVariablesListResponse]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValEnvironmentVariablesListResponse,
                    parse_obj_as(
                        type_=ValEnvironmentVariablesListResponse,
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

    async def val_environment_variables_create(
        self,
        val_id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TEnvironmentVariable]:
        """
        Create a new environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/",
            method="POST",
            json={
                "value": value,
                "description": description,
                "key": key,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def val_environment_variables_update(
        self,
        val_id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TEnvironmentVariable]:
        """
        Update a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TEnvironmentVariable]
            An environment variable
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/{encode_path_param(key)}",
            method="PUT",
            json={
                "value": value,
                "description": description,
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
                    TEnvironmentVariable,
                    parse_obj_as(
                        type_=TEnvironmentVariable,
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

    async def val_environment_variables_delete(
        self, val_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def val_environment_variable_groups_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ValEnvironmentVariableGroupsListResponse]:
        """
        List the environment variable groups attached to this val. This only includes the groups, not the variables in them.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValEnvironmentVariableGroupsListResponse]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValEnvironmentVariableGroupsListResponse,
                    parse_obj_as(
                        type_=ValEnvironmentVariableGroupsListResponse,
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

    async def val_environment_variable_groups_attach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Attach an environment variable group to this val. Every variable in the group is injected into the val's environment. Variables defined on the val itself take precedence over variables with the same key in a group. Attaching a group that is already attached succeeds without doing anything.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/{encode_path_param(group_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def val_environment_variable_groups_detach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Detach an environment variable group from this val. The group itself, and the variables in it, are left alone.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/environment_variable_groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def vals_get2(
        self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Val]:
        """
        Get a val by id

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Val]
            A Val
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Val,
                    parse_obj_as(
                        type_=Val,
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

    async def projects_delete2(
        self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a project

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def vals_list2(
        self,
        *,
        limit: int,
        privacy: typing.Optional[ValsList2RequestPrivacy] = None,
        user_id: typing.Optional[str] = None,
        cursor: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ValsList2Response]:
        """
        Lists all vals including all public vals and your unlisted and private vals

        Parameters
        ----------
        limit : int
            Maximum items to return in each paginated response

        privacy : typing.Optional[ValsList2RequestPrivacy]
            This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.

        user_id : typing.Optional[str]
            User ID to filter by

        cursor : typing.Optional[dt.datetime]
            Cursor to start the pagination from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValsList2Response]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vals",
            method="GET",
            params={
                "privacy": privacy,
                "user_id": user_id,
                "cursor": serialize_datetime(cursor) if cursor is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValsList2Response,
                    parse_obj_as(
                        type_=ValsList2Response,
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

    async def vals_create2(
        self,
        *,
        name: str,
        privacy: ValsCreate2RequestPrivacy,
        description: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Val]:
        """
        Create a new val

        Parameters
        ----------
        name : str

        privacy : ValsCreate2RequestPrivacy

        description : typing.Optional[str]

        org_id : typing.Optional[str]
            ID of the org to create the val in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Val]
            A Val
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vals",
            method="POST",
            json={
                "name": name,
                "description": description,
                "privacy": privacy,
                "orgId": org_id,
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
                    Val,
                    parse_obj_as(
                        type_=Val,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def branches_get2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Branch]:
        """
        Get a branch by id

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Branch]
            A Branch
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches/{encode_path_param(branch_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Branch,
                    parse_obj_as(
                        type_=Branch,
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

    async def branches_delete2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a branch

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches/{encode_path_param(branch_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def branches_list2(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BranchesList2Response]:
        """
        List all branches for a val

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BranchesList2Response]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BranchesList2Response,
                    parse_obj_as(
                        type_=BranchesList2Response,
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

    async def branches_create2(
        self,
        val_id: str,
        *,
        name: str,
        branch_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Branch]:
        """
        Create a new branch

        Parameters
        ----------
        val_id : str
            Id of a val

        name : str

        branch_id : typing.Optional[str]
            The branch ID to fork from. If this is not specified, the new branch will be forked from main.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Branch]
            A Branch
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/branches",
            method="POST",
            json={
                "name": name,
                "branchId": branch_id,
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
                    Branch,
                    parse_obj_as(
                        type_=Branch,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def val_files_get2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        offset: int,
        limit: int,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ValFilesGet2Response]:
        """
        Get metadata for files and directories in a val. If path is an empty string, returns files at the root directory.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ValFilesGet2Response]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="GET",
            params={
                "version": version,
                "branch_id": branch_id,
                "path": path,
                "recursive": recursive,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ValFilesGet2Response,
                    parse_obj_as(
                        type_=ValFilesGet2Response,
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

    async def files_create2(
        self,
        val_id: str,
        *,
        path: str,
        request: FilesCreate2RequestBody,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileRevisionMetadataV2]:
        """
        Create a new file, project val or directory

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        request : FilesCreate2RequestBody

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="POST",
            params={
                "branch_id": branch_id,
                "path": path,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=FilesCreate2RequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
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

    async def file_content_update2(
        self,
        val_id: str,
        *,
        path: str,
        branch_id: typing.Optional[str] = None,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[FileContentUpdate2RequestType] = OMIT,
        parent_path: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileRevisionMetadataV2]:
        """
        Update a file's content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        content : typing.Optional[str]
            File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.

        type : typing.Optional[FileContentUpdate2RequestType]

        parent_path : typing.Optional[str]
            Path to the directory you'd like to move this file to (e.g. 'folder1/folder2')

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="PUT",
            params={
                "branch_id": branch_id,
                "path": path,
            },
            json={
                "content": content,
                "type": type,
                "parent_path": parent_path,
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
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
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

    async def files_delete2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a file or a directory. To delete a directory and all of its children, use the recursive flag. To delete all files, pass in an empty path and the recursive flag.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/vals/{encode_path_param(val_id)}/files",
            method="DELETE",
            params={
                "branch_id": branch_id,
                "path": path,
                "recursive": recursive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def files_content_get2(
        self,
        val_id: str,
        *,
        path: str,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        if_unmodified_since: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        if_modified_since: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Download file content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        if_match : typing.Optional[str]

        if_unmodified_since : typing.Optional[str]

        if_none_match : typing.Optional[str]

        if_modified_since : typing.Optional[str]

        cache_control : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Contents of the file
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v2/vals/{encode_path_param(val_id)}/files/content",
            method="GET",
            params={
                "version": version,
                "branch_id": branch_id,
                "path": path,
            },
            headers={
                "If-Match": str(if_match) if if_match is not None else None,
                "If-Unmodified-Since": str(if_unmodified_since) if if_unmodified_since is not None else None,
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
                "Cache-Control": str(cache_control) if cache_control is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 412:
                        raise PreconditionFailedError(
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
