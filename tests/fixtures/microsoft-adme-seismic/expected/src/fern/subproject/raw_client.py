

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.sub_project import SubProject
from .types.sub_project_create_body_access_policy import SubProjectCreateBodyAccessPolicy
from .types.sub_project_create_body_acls import SubProjectCreateBodyAcls
from .types.sub_project_patch_body_acls import SubProjectPatchBodyAcls
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubprojectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubProject]:
        """
        <ul><li>Return the metadata for a requested sub-project.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubProject]
            Retrieved subproject metadata successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="GET",
            params={
                "translate-user-info": translate_user_info,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: typing.Optional[str] = None,
        admin: typing.Optional[str] = OMIT,
        storage_class: typing.Optional[str] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        access_policy: typing.Optional[SubProjectCreateBodyAccessPolicy] = OMIT,
        acls: typing.Optional[SubProjectCreateBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubProject]:
        """
        <ul>
        <li>Creates a new subproject resource in seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant name - In OSDU this match the data-partition-id

        subprojectid : str
            The subproject name. It must match the regex <b>^[a-z][a-z\\d\\-]*[a-z\\d]$</b>

        ltag : typing.Optional[str]
            A valid compliance legal tag. It can be generated and managed via core-compliance-service.

        admin : typing.Optional[str]
            An optional user to set as admin. The user will be added in the first admins acl group

        storage_class : typing.Optional[str]
            Storage class for the bucket (Google Required Only)

        storage_location : typing.Optional[str]
            Storage location for the bucket (Google Required Only)

        access_policy : typing.Optional[SubProjectCreateBodyAccessPolicy]
            The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)

        acls : typing.Optional[SubProjectCreateBodyAcls]
            The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubProject]
            The registered subproject.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="POST",
            json={
                "admin": admin,
                "storage_class": storage_class,
                "storage_location": storage_location,
                "access_policy": access_policy,
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=SubProjectCreateBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def delete(
        self, tenantid: str, subprojectid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        <ul><li>Delete a subproject in seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: str,
        recursive: typing.Optional[bool] = None,
        access_policy: typing.Optional[str] = OMIT,
        acls: typing.Optional[SubProjectPatchBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubProject]:
        """
        <ul>
          <li>Patch a subproject metadata in seismic store.</li>
          <li>Required roles: subproject.admin</li>
          <li>Possible actions:</li>
          <ul>
            <li>legal tag and/or ACLs groups can be patched by providing new values</li>
            <li>access policy can be changed from <i>uniform</i> to <i>dataset</i></li>
            <li><b>NOTE:</b> It is not possible to change subproject access policy from <i>dataset</i> to <i>uniform</i></li>
            <li><b>NOTE:</b> This operation is eventual consistent and it can take up to 5s before it gets completely applied</li>
          </ul>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        ltag : str
            Legal tag of the subproject.

        recursive : typing.Optional[bool]
            True if the legal tags of all datasets in a subproject needs to be updated.

        access_policy : typing.Optional[str]
            Access Policy for the subproject.

        acls : typing.Optional[SubProjectPatchBodyAcls]
            ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubProject]
            Updated subproject metadata successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="PATCH",
            params={
                "recursive": recursive,
            },
            json={
                "access_policy": access_policy,
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=SubProjectPatchBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSubprojectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubProject]:
        """
        <ul><li>Return the metadata for a requested sub-project.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubProject]
            Retrieved subproject metadata successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="GET",
            params={
                "translate-user-info": translate_user_info,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: typing.Optional[str] = None,
        admin: typing.Optional[str] = OMIT,
        storage_class: typing.Optional[str] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        access_policy: typing.Optional[SubProjectCreateBodyAccessPolicy] = OMIT,
        acls: typing.Optional[SubProjectCreateBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubProject]:
        """
        <ul>
        <li>Creates a new subproject resource in seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant name - In OSDU this match the data-partition-id

        subprojectid : str
            The subproject name. It must match the regex <b>^[a-z][a-z\\d\\-]*[a-z\\d]$</b>

        ltag : typing.Optional[str]
            A valid compliance legal tag. It can be generated and managed via core-compliance-service.

        admin : typing.Optional[str]
            An optional user to set as admin. The user will be added in the first admins acl group

        storage_class : typing.Optional[str]
            Storage class for the bucket (Google Required Only)

        storage_location : typing.Optional[str]
            Storage location for the bucket (Google Required Only)

        access_policy : typing.Optional[SubProjectCreateBodyAccessPolicy]
            The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)

        acls : typing.Optional[SubProjectCreateBodyAcls]
            The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubProject]
            The registered subproject.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="POST",
            json={
                "admin": admin,
                "storage_class": storage_class,
                "storage_location": storage_location,
                "access_policy": access_policy,
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=SubProjectCreateBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def delete(
        self, tenantid: str, subprojectid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        <ul><li>Delete a subproject in seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: str,
        recursive: typing.Optional[bool] = None,
        access_policy: typing.Optional[str] = OMIT,
        acls: typing.Optional[SubProjectPatchBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubProject]:
        """
        <ul>
          <li>Patch a subproject metadata in seismic store.</li>
          <li>Required roles: subproject.admin</li>
          <li>Possible actions:</li>
          <ul>
            <li>legal tag and/or ACLs groups can be patched by providing new values</li>
            <li>access policy can be changed from <i>uniform</i> to <i>dataset</i></li>
            <li><b>NOTE:</b> It is not possible to change subproject access policy from <i>dataset</i> to <i>uniform</i></li>
            <li><b>NOTE:</b> This operation is eventual consistent and it can take up to 5s before it gets completely applied</li>
          </ul>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        ltag : str
            Legal tag of the subproject.

        recursive : typing.Optional[bool]
            True if the legal tags of all datasets in a subproject needs to be updated.

        access_policy : typing.Optional[str]
            Access Policy for the subproject.

        acls : typing.Optional[SubProjectPatchBodyAcls]
            ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubProject]
            Updated subproject metadata successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subproject/tenant/{encode_path_param(tenantid)}/subproject/{encode_path_param(subprojectid)}",
            method="PATCH",
            params={
                "recursive": recursive,
            },
            json={
                "access_policy": access_policy,
                "acls": convert_and_respect_annotation_metadata(
                    object_=acls, annotation=SubProjectPatchBodyAcls, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "ltag": str(ltag) if ltag is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubProject,
                    parse_obj_as(
                        type_=SubProject,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
