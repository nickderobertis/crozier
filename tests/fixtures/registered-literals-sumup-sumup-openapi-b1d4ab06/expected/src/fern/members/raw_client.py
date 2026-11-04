

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
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.attributes import Attributes
from ..types.member import Member
from ..types.membership_status import MembershipStatus
from ..types.metadata import Metadata
from ..types.problem import Problem
from .types.list_merchant_members_response import ListMerchantMembersResponse
from .types.update_merchant_member_request_user import UpdateMerchantMemberRequestUser
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_merchant_members(
        self,
        merchant_code: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        scroll: typing.Optional[bool] = None,
        email: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        status: typing.Optional[MembershipStatus] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMerchantMembersResponse]:
        """
        Lists merchant members.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        scroll : typing.Optional[bool]
            Indicates to skip count query.

        email : typing.Optional[str]
            Filter the returned members by email address prefix.

        user_id : typing.Optional[str]
            Search for a member by user id.

        status : typing.Optional[MembershipStatus]
            Filter the returned members by the membership status.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned members by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMerchantMembersResponse]
            Returns a list of Member objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "scroll": scroll,
                "email": email,
                "user.id": user_id,
                "status": status,
                "roles": roles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMerchantMembersResponse,
                    parse_obj_as(
                        type_=ListMerchantMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def create_merchant_member(
        self,
        merchant_code: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        is_managed_user: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Member]:
        """
        Adds a member to the merchant account with the specified roles.

        By default, sends an invitation email to the provided address. The recipient must accept the invitation to join the account.
        When `is_managed_user` is `true`, creates a managed user with the provided password and optional nickname and assigns the roles directly, without sending an invitation.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        email : str
            Email address of the member to add.

        roles : typing.Sequence[str]
            List of roles to assign to the new member.

        is_managed_user : typing.Optional[bool]
            True if the user is managed by the merchant. In this case, we'll created a virtual user with the provided password and nickname.

        password : typing.Optional[str]
            Password of the member to add. Only used if `is_managed_user` is true. In the case of service accounts, the password is not used and can not be defined by the caller.

        nickname : typing.Optional[str]
            Nickname of the member to add. Only used if `is_managed_user` is true. Used for display purposes only.

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Member]
            Returns the Member object if the creation succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members",
            method="POST",
            json={
                "is_managed_user": is_managed_user,
                "email": email,
                "password": password,
                "nickname": nickname,
                "roles": roles,
                "metadata": metadata,
                "attributes": attributes,
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
                    Member,
                    parse_obj_as(
                        type_=Member,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    def get_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Member]:
        """
        Retrieve a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Member]
            Returns the Member object for a valid identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Member,
                    parse_obj_as(
                        type_=Member,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def update_merchant_member(
        self,
        merchant_code: str,
        member_id: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        user: typing.Optional[UpdateMerchantMemberRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Member]:
        """
        Updates a merchant member and returns the updated member.

        Providing `roles` replaces the member's assigned roles and can grant or revoke access. Providing `metadata` replaces the entire metadata object.
        For managed users, `user.nickname` changes the display name and `user.password` replaces the password. Updating the password also enables the managed user account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        roles : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        user : typing.Optional[UpdateMerchantMemberRequestUser]
            Allows you to update user data of managed users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Member]
            Returns the updated Member object if the update succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="PUT",
            json={
                "roles": roles,
                "metadata": metadata,
                "attributes": attributes,
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=UpdateMerchantMemberRequestUser, direction="write"
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
                    Member,
                    parse_obj_as(
                        type_=Member,
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

    def delete_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_merchant_members(
        self,
        merchant_code: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        scroll: typing.Optional[bool] = None,
        email: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        status: typing.Optional[MembershipStatus] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMerchantMembersResponse]:
        """
        Lists merchant members.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        scroll : typing.Optional[bool]
            Indicates to skip count query.

        email : typing.Optional[str]
            Filter the returned members by email address prefix.

        user_id : typing.Optional[str]
            Search for a member by user id.

        status : typing.Optional[MembershipStatus]
            Filter the returned members by the membership status.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned members by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMerchantMembersResponse]
            Returns a list of Member objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "scroll": scroll,
                "email": email,
                "user.id": user_id,
                "status": status,
                "roles": roles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMerchantMembersResponse,
                    parse_obj_as(
                        type_=ListMerchantMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def create_merchant_member(
        self,
        merchant_code: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        is_managed_user: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Member]:
        """
        Adds a member to the merchant account with the specified roles.

        By default, sends an invitation email to the provided address. The recipient must accept the invitation to join the account.
        When `is_managed_user` is `true`, creates a managed user with the provided password and optional nickname and assigns the roles directly, without sending an invitation.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        email : str
            Email address of the member to add.

        roles : typing.Sequence[str]
            List of roles to assign to the new member.

        is_managed_user : typing.Optional[bool]
            True if the user is managed by the merchant. In this case, we'll created a virtual user with the provided password and nickname.

        password : typing.Optional[str]
            Password of the member to add. Only used if `is_managed_user` is true. In the case of service accounts, the password is not used and can not be defined by the caller.

        nickname : typing.Optional[str]
            Nickname of the member to add. Only used if `is_managed_user` is true. Used for display purposes only.

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Member]
            Returns the Member object if the creation succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members",
            method="POST",
            json={
                "is_managed_user": is_managed_user,
                "email": email,
                "password": password,
                "nickname": nickname,
                "roles": roles,
                "metadata": metadata,
                "attributes": attributes,
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
                    Member,
                    parse_obj_as(
                        type_=Member,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    async def get_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Member]:
        """
        Retrieve a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Member]
            Returns the Member object for a valid identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Member,
                    parse_obj_as(
                        type_=Member,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def update_merchant_member(
        self,
        merchant_code: str,
        member_id: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        user: typing.Optional[UpdateMerchantMemberRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Member]:
        """
        Updates a merchant member and returns the updated member.

        Providing `roles` replaces the member's assigned roles and can grant or revoke access. Providing `metadata` replaces the entire metadata object.
        For managed users, `user.nickname` changes the display name and `user.password` replaces the password. Updating the password also enables the managed user account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        roles : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        user : typing.Optional[UpdateMerchantMemberRequestUser]
            Allows you to update user data of managed users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Member]
            Returns the updated Member object if the update succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="PUT",
            json={
                "roles": roles,
                "metadata": metadata,
                "attributes": attributes,
                "user": convert_and_respect_annotation_metadata(
                    object_=user, annotation=UpdateMerchantMemberRequestUser, direction="write"
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
                    Member,
                    parse_obj_as(
                        type_=Member,
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

    async def delete_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/members/{encode_path_param(member_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
