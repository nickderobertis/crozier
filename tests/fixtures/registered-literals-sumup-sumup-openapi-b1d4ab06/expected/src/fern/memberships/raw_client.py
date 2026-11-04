

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.membership_status import MembershipStatus
from ..types.resource_type import ResourceType
from .types.list_memberships_response import ListMembershipsResponse
from pydantic import ValidationError


class RawMembershipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_memberships(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        kind: typing.Optional[ResourceType] = None,
        status: typing.Optional[MembershipStatus] = None,
        resource_type: typing.Optional[ResourceType] = None,
        resource_attributes_sandbox: typing.Optional[bool] = None,
        resource_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_parent_id: typing.Optional[str] = None,
        resource_parent_type: typing.Optional[ResourceType] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMembershipsResponse]:
        """
        List memberships of the current user.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        kind : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        status : typing.Optional[MembershipStatus]
            Filter the returned memberships by the membership status.

        resource_type : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        resource_attributes_sandbox : typing.Optional[bool]
            Filter memberships by the sandbox status of the resource the membership is in.

        resource_name : typing.Optional[str]
            Filter memberships by the name of the resource the membership is in.

        resource_id : typing.Optional[str]
            Filter memberships by the ID of the resource the membership is in.

        resource_parent_id : typing.Optional[str]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        resource_parent_type : typing.Optional[ResourceType]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned memberships by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMembershipsResponse]
            Returns a list of Membership objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/memberships",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "kind": kind,
                "status": status,
                "resource.type": resource_type,
                "resource.attributes.sandbox": resource_attributes_sandbox,
                "resource.name": resource_name,
                "resource.id": resource_id,
                "resource.parent.id": resource_parent_id,
                "resource.parent.type": resource_parent_type,
                "roles": roles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMembershipsResponse,
                    parse_obj_as(
                        type_=ListMembershipsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMembershipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_memberships(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        kind: typing.Optional[ResourceType] = None,
        status: typing.Optional[MembershipStatus] = None,
        resource_type: typing.Optional[ResourceType] = None,
        resource_attributes_sandbox: typing.Optional[bool] = None,
        resource_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_parent_id: typing.Optional[str] = None,
        resource_parent_type: typing.Optional[ResourceType] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMembershipsResponse]:
        """
        List memberships of the current user.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        kind : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        status : typing.Optional[MembershipStatus]
            Filter the returned memberships by the membership status.

        resource_type : typing.Optional[ResourceType]
            Filter memberships by resource kind.

        resource_attributes_sandbox : typing.Optional[bool]
            Filter memberships by the sandbox status of the resource the membership is in.

        resource_name : typing.Optional[str]
            Filter memberships by the name of the resource the membership is in.

        resource_id : typing.Optional[str]
            Filter memberships by the ID of the resource the membership is in.

        resource_parent_id : typing.Optional[str]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        resource_parent_type : typing.Optional[ResourceType]
            Filter memberships by the parent of the resource the membership is in.
            Omit both `resource.parent.id` and `resource.parent.type` to skip parent filtering. When filtering by parent, both parameters must be present. To select resources without a parent, set each parameter to an empty value. Otherwise, both parameters must identify a parent.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned memberships by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMembershipsResponse]
            Returns a list of Membership objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/memberships",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "kind": kind,
                "status": status,
                "resource.type": resource_type,
                "resource.attributes.sandbox": resource_attributes_sandbox,
                "resource.name": resource_name,
                "resource.id": resource_id,
                "resource.parent.id": resource_parent_id,
                "resource.parent.type": resource_parent_type,
                "roles": roles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMembershipsResponse,
                    parse_obj_as(
                        type_=ListMembershipsResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
