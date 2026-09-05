

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
from ..types.acl import Acl
from ..types.acl_batch_update_response import AclBatchUpdateResponse
from ..types.acl_id_param import AclIdParam
from ..types.acl_item import AclItem
from ..types.acl_list_group_id import AclListGroupId
from ..types.acl_list_org_object_id import AclListOrgObjectId
from ..types.acl_list_org_object_type import AclListOrgObjectType
from ..types.acl_list_permission import AclListPermission
from ..types.acl_list_restrict_object_type import AclListRestrictObjectType
from ..types.acl_list_role_id import AclListRoleId
from ..types.acl_list_user_id import AclListUserId
from ..types.acl_object_id import AclObjectId
from ..types.acl_object_type import AclObjectType
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.permission import Permission
from ..types.starting_after import StartingAfter
from .types.get_acl_response import GetAclResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAclsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAclResponse]:
        """
        List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

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

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAclResponse]
            Returns a list of acl objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAclResponse,
                    parse_obj_as(
                        type_=GetAclResponse,
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

    def post_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Acl]:
        """
        Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Acl]
            Returns the new acl object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    def delete_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Acl]:
        """
        Delete a single acl

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Acl]
            Returns the deleted acl object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="DELETE",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    def get_acl_id(
        self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Acl]:
        """
        Get an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Acl]
            Returns the acl object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/acl/{encode_path_param(acl_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    def delete_acl_id(
        self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Acl]:
        """
        Delete an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Acl]
            Returns the deleted acl object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/acl/{encode_path_param(acl_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    def acl_batch_update(
        self,
        *,
        add_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        remove_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AclBatchUpdateResponse]:
        """
        Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.

        Parameters
        ----------
        add_acls : typing.Optional[typing.Sequence[AclItem]]

        remove_acls : typing.Optional[typing.Sequence[AclItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AclBatchUpdateResponse]
            A success status
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/acl/batch_update",
            method="POST",
            json={
                "add_acls": convert_and_respect_annotation_metadata(
                    object_=add_acls, annotation=typing.Optional[typing.Sequence[AclItem]], direction="write"
                ),
                "remove_acls": convert_and_respect_annotation_metadata(
                    object_=remove_acls, annotation=typing.Optional[typing.Sequence[AclItem]], direction="write"
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
                    AclBatchUpdateResponse,
                    parse_obj_as(
                        type_=AclBatchUpdateResponse,
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

    def acl_list_org(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        object_type: typing.Optional[AclListOrgObjectType] = None,
        object_id: typing.Optional[AclListOrgObjectId] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Acl]]:
        """
        List all acls in the org. This query requires the caller to have `read_acls` permission at the organization level

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        object_type : typing.Optional[AclListOrgObjectType]
            The object type that the ACL applies to

        object_id : typing.Optional[AclListOrgObjectId]
            The id of the object the ACL applies to

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Acl]]
            A list of acls
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/acl/list_org",
            method="GET",
            params={
                "limit": limit,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "starting_after": starting_after,
                "ending_before": ending_before,
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Acl],
                    parse_obj_as(
                        type_=typing.List[Acl],
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


class AsyncRawAclsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAclResponse]:
        """
        List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

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

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAclResponse]
            Returns a list of acl objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAclResponse,
                    parse_obj_as(
                        type_=GetAclResponse,
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

    async def post_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Acl]:
        """
        Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Acl]
            Returns the new acl object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    async def delete_acl(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        user_id: typing.Optional[str] = OMIT,
        group_id: typing.Optional[str] = OMIT,
        permission: typing.Optional[Permission] = OMIT,
        restrict_object_type: typing.Optional[AclObjectType] = OMIT,
        role_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Acl]:
        """
        Delete a single acl

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the ACL applies to

        user_id : typing.Optional[str]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[str]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[Permission]
            Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided

        restrict_object_type : typing.Optional[AclObjectType]
            When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.

        role_id : typing.Optional[str]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Acl]
            Returns the deleted acl object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/acl",
            method="DELETE",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    async def get_acl_id(
        self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Acl]:
        """
        Get an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Acl]
            Returns the acl object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/acl/{encode_path_param(acl_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    async def delete_acl_id(
        self, acl_id: AclIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Acl]:
        """
        Delete an acl object by its id

        Parameters
        ----------
        acl_id : AclIdParam
            Acl id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Acl]
            Returns the deleted acl object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/acl/{encode_path_param(acl_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Acl,
                    parse_obj_as(
                        type_=Acl,
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

    async def acl_batch_update(
        self,
        *,
        add_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        remove_acls: typing.Optional[typing.Sequence[AclItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AclBatchUpdateResponse]:
        """
        Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.

        Parameters
        ----------
        add_acls : typing.Optional[typing.Sequence[AclItem]]

        remove_acls : typing.Optional[typing.Sequence[AclItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AclBatchUpdateResponse]
            A success status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/acl/batch_update",
            method="POST",
            json={
                "add_acls": convert_and_respect_annotation_metadata(
                    object_=add_acls, annotation=typing.Optional[typing.Sequence[AclItem]], direction="write"
                ),
                "remove_acls": convert_and_respect_annotation_metadata(
                    object_=remove_acls, annotation=typing.Optional[typing.Sequence[AclItem]], direction="write"
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
                    AclBatchUpdateResponse,
                    parse_obj_as(
                        type_=AclBatchUpdateResponse,
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

    async def acl_list_org(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        ids: typing.Optional[Ids] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        object_type: typing.Optional[AclListOrgObjectType] = None,
        object_id: typing.Optional[AclListOrgObjectId] = None,
        user_id: typing.Optional[AclListUserId] = None,
        group_id: typing.Optional[AclListGroupId] = None,
        permission: typing.Optional[AclListPermission] = None,
        restrict_object_type: typing.Optional[AclListRestrictObjectType] = None,
        role_id: typing.Optional[AclListRoleId] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Acl]]:
        """
        List all acls in the org. This query requires the caller to have `read_acls` permission at the organization level

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        object_type : typing.Optional[AclListOrgObjectType]
            The object type that the ACL applies to

        object_id : typing.Optional[AclListOrgObjectId]
            The id of the object the ACL applies to

        user_id : typing.Optional[AclListUserId]
            Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        group_id : typing.Optional[AclListGroupId]
            Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided

        permission : typing.Optional[AclListPermission]
            Each permission permits a certain type of operation on an object in the system

            Permissions can be assigned to to objects on an individual basis, or grouped into roles

        restrict_object_type : typing.Optional[AclListRestrictObjectType]
            The object type that the ACL applies to

        role_id : typing.Optional[AclListRoleId]
            Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Acl]]
            A list of acls
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/acl/list_org",
            method="GET",
            params={
                "limit": limit,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "starting_after": starting_after,
                "ending_before": ending_before,
                "object_type": object_type,
                "object_id": object_id,
                "user_id": user_id,
                "group_id": group_id,
                "permission": permission,
                "restrict_object_type": restrict_object_type,
                "role_id": role_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Acl],
                    parse_obj_as(
                        type_=typing.List[Acl],
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
