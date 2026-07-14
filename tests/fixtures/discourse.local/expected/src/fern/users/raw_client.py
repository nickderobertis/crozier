

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.admin_get_user_response import AdminGetUserResponse
from .types.admin_list_users_request_asc import AdminListUsersRequestAsc
from .types.admin_list_users_request_flag import AdminListUsersRequestFlag
from .types.admin_list_users_request_order import AdminListUsersRequestOrder
from .types.admin_list_users_response_item import AdminListUsersResponseItem
from .types.anonymize_user_response import AnonymizeUserResponse
from .types.create_user_response import CreateUserResponse
from .types.delete_user_response import DeleteUserResponse
from .types.get_user_emails_response import GetUserEmailsResponse
from .types.get_user_external_id_response import GetUserExternalIdResponse
from .types.get_user_identiy_provider_external_id_response import GetUserIdentiyProviderExternalIdResponse
from .types.get_user_response import GetUserResponse
from .types.list_user_actions_response import ListUserActionsResponse
from .types.list_users_public_request_asc import ListUsersPublicRequestAsc
from .types.list_users_public_request_order import ListUsersPublicRequestOrder
from .types.list_users_public_request_period import ListUsersPublicRequestPeriod
from .types.list_users_public_response import ListUsersPublicResponse
from .types.log_out_user_response import LogOutUserResponse
from .types.refresh_gravatar_response import RefreshGravatarResponse
from .types.send_password_reset_email_response import SendPasswordResetEmailResponse
from .types.silence_user_response import SilenceUserResponse
from .types.suspend_user_response import SuspendUserResponse
from .types.update_avatar_request_type import UpdateAvatarRequestType
from .types.update_avatar_response import UpdateAvatarResponse
from .types.update_user_response import UpdateUserResponse


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def admin_list_users(
        self,
        flag: AdminListUsersRequestFlag,
        *,
        order: typing.Optional[AdminListUsersRequestOrder] = None,
        asc: typing.Optional[AdminListUsersRequestAsc] = None,
        page: typing.Optional[int] = None,
        show_emails: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AdminListUsersResponseItem]]:
        """
        Parameters
        ----------
        flag : AdminListUsersRequestFlag

        order : typing.Optional[AdminListUsersRequestOrder]

        asc : typing.Optional[AdminListUsersRequestAsc]

        page : typing.Optional[int]

        show_emails : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AdminListUsersResponseItem]]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/list/{jsonable_encoder(flag)}.json",
            method="GET",
            params={
                "order": order,
                "asc": asc,
                "page": page,
                "show_emails": show_emails,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AdminListUsersResponseItem],
                    parse_obj_as(
                        type_=typing.List[AdminListUsersResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def admin_get_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AdminGetUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AdminGetUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminGetUserResponse,
                    parse_obj_as(
                        type_=AdminGetUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_user(
        self,
        id: int,
        *,
        block_email: typing.Optional[bool] = OMIT,
        block_ip: typing.Optional[bool] = OMIT,
        block_urls: typing.Optional[bool] = OMIT,
        delete_posts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteUserResponse]:
        """
        Parameters
        ----------
        id : int

        block_email : typing.Optional[bool]

        block_ip : typing.Optional[bool]

        block_urls : typing.Optional[bool]

        delete_posts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}.json",
            method="DELETE",
            json={
                "block_email": block_email,
                "block_ip": block_ip,
                "block_urls": block_urls,
                "delete_posts": delete_posts,
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
                    DeleteUserResponse,
                    parse_obj_as(
                        type_=DeleteUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def anonymize_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AnonymizeUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnonymizeUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/anonymize.json",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnonymizeUserResponse,
                    parse_obj_as(
                        type_=AnonymizeUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def log_out_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LogOutUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogOutUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/log_out.json",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogOutUserResponse,
                    parse_obj_as(
                        type_=LogOutUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def silence_user(
        self,
        id: int,
        *,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        silenced_till: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SilenceUserResponse]:
        """
        Parameters
        ----------
        id : int

        message : typing.Optional[str]
            Will send an email with this message when present

        post_action : typing.Optional[str]

        reason : typing.Optional[str]

        silenced_till : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SilenceUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/silence.json",
            method="PUT",
            json={
                "message": message,
                "post_action": post_action,
                "reason": reason,
                "silenced_till": silenced_till,
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
                    SilenceUserResponse,
                    parse_obj_as(
                        type_=SilenceUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def suspend_user(
        self,
        id: int,
        *,
        reason: str,
        suspend_until: str,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuspendUserResponse]:
        """
        Parameters
        ----------
        id : int

        reason : str

        suspend_until : str

        message : typing.Optional[str]
            Will send an email with this message when present

        post_action : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuspendUserResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/suspend.json",
            method="PUT",
            json={
                "message": message,
                "post_action": post_action,
                "reason": reason,
                "suspend_until": suspend_until,
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
                    SuspendUserResponse,
                    parse_obj_as(
                        type_=SuspendUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_users_public(
        self,
        *,
        period: ListUsersPublicRequestPeriod,
        order: ListUsersPublicRequestOrder,
        asc: typing.Optional[ListUsersPublicRequestAsc] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListUsersPublicResponse]:
        """
        Parameters
        ----------
        period : ListUsersPublicRequestPeriod

        order : ListUsersPublicRequestOrder

        asc : typing.Optional[ListUsersPublicRequestAsc]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUsersPublicResponse]
            directory items response
        """
        _response = self._client_wrapper.httpx_client.request(
            "directory_items.json",
            method="GET",
            params={
                "period": period,
                "order": order,
                "asc": asc,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUsersPublicResponse,
                    parse_obj_as(
                        type_=ListUsersPublicResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def send_password_reset_email(
        self, *, login: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SendPasswordResetEmailResponse]:
        """
        Parameters
        ----------
        login : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendPasswordResetEmailResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "session/forgot_password.json",
            method="POST",
            json={
                "login": login,
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
                    SendPasswordResetEmailResponse,
                    parse_obj_as(
                        type_=SendPasswordResetEmailResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_user_external_id(
        self,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetUserExternalIdResponse]:
        """
        Parameters
        ----------
        external_id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserExternalIdResponse]
            user response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/by-external/{jsonable_encoder(external_id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserExternalIdResponse,
                    parse_obj_as(
                        type_=GetUserExternalIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetUserIdentiyProviderExternalIdResponse]:
        """
        Parameters
        ----------
        provider : str
            Authentication provider name. Can be found in the provider callback
            URL: `/auth/{provider}/callback`

        external_id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserIdentiyProviderExternalIdResponse]
            user response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/by-external/{jsonable_encoder(provider)}/{jsonable_encoder(external_id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserIdentiyProviderExternalIdResponse,
                    parse_obj_as(
                        type_=GetUserIdentiyProviderExternalIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_user(
        self, username: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserResponse]:
        """
        Parameters
        ----------
        username : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserResponse]
            user response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserResponse,
                    parse_obj_as(
                        type_=GetUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_user(
        self,
        username: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        external_ids: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateUserResponse]:
        """
        Parameters
        ----------
        username : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        external_ids : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        name : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateUserResponse]
            user updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}.json",
            method="PUT",
            json={
                "email": email,
                "external_ids": external_ids,
                "name": name,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_user_emails(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserEmailsResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserEmailsResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/emails.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserEmailsResponse,
                    parse_obj_as(
                        type_=GetUserEmailsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_avatar(
        self,
        username: str,
        *,
        type: UpdateAvatarRequestType,
        upload_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAvatarResponse]:
        """
        Parameters
        ----------
        username : str

        type : UpdateAvatarRequestType

        upload_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateAvatarResponse]
            avatar updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/avatar/pick.json",
            method="PUT",
            json={
                "type": type,
                "upload_id": upload_id,
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
                    UpdateAvatarResponse,
                    parse_obj_as(
                        type_=UpdateAvatarResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_email(
        self, username: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        username : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/email.json",
            method="PUT",
            json={
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_username(
        self, username: str, *, new_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        username : str

        new_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/username.json",
            method="PUT",
            json={
                "new_username": new_username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_actions(
        self, *, offset: int, username: str, filter: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListUserActionsResponse]:
        """
        Parameters
        ----------
        offset : int

        username : str

        filter : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUserActionsResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            "user_actions.json",
            method="GET",
            params={
                "offset": offset,
                "username": username,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserActionsResponse,
                    parse_obj_as(
                        type_=ListUserActionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def refresh_gravatar(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RefreshGravatarResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RefreshGravatarResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user_avatar/{jsonable_encoder(username)}/refresh_gravatar.json",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshGravatarResponse,
                    parse_obj_as(
                        type_=RefreshGravatarResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_user(
        self,
        *,
        api_key: str,
        api_username: str,
        email: str,
        name: str,
        password: str,
        username: str,
        active: typing.Optional[bool] = OMIT,
        approved: typing.Optional[bool] = OMIT,
        external_ids: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        user_fields1: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateUserResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        email : str

        name : str

        password : str

        username : str

        active : typing.Optional[bool]
            This param requires an api key in the request header
            or it will be ignored

        approved : typing.Optional[bool]

        external_ids : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        user_fields1 : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateUserResponse]
            user created
        """
        _response = self._client_wrapper.httpx_client.request(
            "users.json",
            method="POST",
            json={
                "active": active,
                "approved": approved,
                "email": email,
                "external_ids": external_ids,
                "name": name,
                "password": password,
                "user_fields[1]": user_fields1,
                "username": username,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def change_password(
        self, token: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        password : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/password-reset/{jsonable_encoder(token)}.json",
            method="PUT",
            json={
                "password": password,
                "username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def admin_list_users(
        self,
        flag: AdminListUsersRequestFlag,
        *,
        order: typing.Optional[AdminListUsersRequestOrder] = None,
        asc: typing.Optional[AdminListUsersRequestAsc] = None,
        page: typing.Optional[int] = None,
        show_emails: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AdminListUsersResponseItem]]:
        """
        Parameters
        ----------
        flag : AdminListUsersRequestFlag

        order : typing.Optional[AdminListUsersRequestOrder]

        asc : typing.Optional[AdminListUsersRequestAsc]

        page : typing.Optional[int]

        show_emails : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AdminListUsersResponseItem]]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/list/{jsonable_encoder(flag)}.json",
            method="GET",
            params={
                "order": order,
                "asc": asc,
                "page": page,
                "show_emails": show_emails,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AdminListUsersResponseItem],
                    parse_obj_as(
                        type_=typing.List[AdminListUsersResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def admin_get_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AdminGetUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AdminGetUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminGetUserResponse,
                    parse_obj_as(
                        type_=AdminGetUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_user(
        self,
        id: int,
        *,
        block_email: typing.Optional[bool] = OMIT,
        block_ip: typing.Optional[bool] = OMIT,
        block_urls: typing.Optional[bool] = OMIT,
        delete_posts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteUserResponse]:
        """
        Parameters
        ----------
        id : int

        block_email : typing.Optional[bool]

        block_ip : typing.Optional[bool]

        block_urls : typing.Optional[bool]

        delete_posts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}.json",
            method="DELETE",
            json={
                "block_email": block_email,
                "block_ip": block_ip,
                "block_urls": block_urls,
                "delete_posts": delete_posts,
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
                    DeleteUserResponse,
                    parse_obj_as(
                        type_=DeleteUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def anonymize_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AnonymizeUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnonymizeUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/anonymize.json",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnonymizeUserResponse,
                    parse_obj_as(
                        type_=AnonymizeUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def log_out_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LogOutUserResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogOutUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/log_out.json",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogOutUserResponse,
                    parse_obj_as(
                        type_=LogOutUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def silence_user(
        self,
        id: int,
        *,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        silenced_till: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SilenceUserResponse]:
        """
        Parameters
        ----------
        id : int

        message : typing.Optional[str]
            Will send an email with this message when present

        post_action : typing.Optional[str]

        reason : typing.Optional[str]

        silenced_till : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SilenceUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/silence.json",
            method="PUT",
            json={
                "message": message,
                "post_action": post_action,
                "reason": reason,
                "silenced_till": silenced_till,
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
                    SilenceUserResponse,
                    parse_obj_as(
                        type_=SilenceUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def suspend_user(
        self,
        id: int,
        *,
        reason: str,
        suspend_until: str,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuspendUserResponse]:
        """
        Parameters
        ----------
        id : int

        reason : str

        suspend_until : str

        message : typing.Optional[str]
            Will send an email with this message when present

        post_action : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuspendUserResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/users/{jsonable_encoder(id)}/suspend.json",
            method="PUT",
            json={
                "message": message,
                "post_action": post_action,
                "reason": reason,
                "suspend_until": suspend_until,
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
                    SuspendUserResponse,
                    parse_obj_as(
                        type_=SuspendUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_users_public(
        self,
        *,
        period: ListUsersPublicRequestPeriod,
        order: ListUsersPublicRequestOrder,
        asc: typing.Optional[ListUsersPublicRequestAsc] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListUsersPublicResponse]:
        """
        Parameters
        ----------
        period : ListUsersPublicRequestPeriod

        order : ListUsersPublicRequestOrder

        asc : typing.Optional[ListUsersPublicRequestAsc]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUsersPublicResponse]
            directory items response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "directory_items.json",
            method="GET",
            params={
                "period": period,
                "order": order,
                "asc": asc,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUsersPublicResponse,
                    parse_obj_as(
                        type_=ListUsersPublicResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def send_password_reset_email(
        self, *, login: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SendPasswordResetEmailResponse]:
        """
        Parameters
        ----------
        login : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendPasswordResetEmailResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session/forgot_password.json",
            method="POST",
            json={
                "login": login,
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
                    SendPasswordResetEmailResponse,
                    parse_obj_as(
                        type_=SendPasswordResetEmailResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_user_external_id(
        self,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetUserExternalIdResponse]:
        """
        Parameters
        ----------
        external_id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserExternalIdResponse]
            user response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/by-external/{jsonable_encoder(external_id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserExternalIdResponse,
                    parse_obj_as(
                        type_=GetUserExternalIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetUserIdentiyProviderExternalIdResponse]:
        """
        Parameters
        ----------
        provider : str
            Authentication provider name. Can be found in the provider callback
            URL: `/auth/{provider}/callback`

        external_id : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserIdentiyProviderExternalIdResponse]
            user response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/by-external/{jsonable_encoder(provider)}/{jsonable_encoder(external_id)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserIdentiyProviderExternalIdResponse,
                    parse_obj_as(
                        type_=GetUserIdentiyProviderExternalIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_user(
        self, username: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserResponse]:
        """
        Parameters
        ----------
        username : str

        api_key : str

        api_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserResponse]
            user response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}.json",
            method="GET",
            headers={
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserResponse,
                    parse_obj_as(
                        type_=GetUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_user(
        self,
        username: str,
        *,
        api_key: str,
        api_username: str,
        email: typing.Optional[str] = OMIT,
        external_ids: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateUserResponse]:
        """
        Parameters
        ----------
        username : str

        api_key : str

        api_username : str

        email : typing.Optional[str]

        external_ids : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        name : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateUserResponse]
            user updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}.json",
            method="PUT",
            json={
                "email": email,
                "external_ids": external_ids,
                "name": name,
                "password": password,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateUserResponse,
                    parse_obj_as(
                        type_=UpdateUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_user_emails(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserEmailsResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserEmailsResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/emails.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserEmailsResponse,
                    parse_obj_as(
                        type_=GetUserEmailsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_avatar(
        self,
        username: str,
        *,
        type: UpdateAvatarRequestType,
        upload_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAvatarResponse]:
        """
        Parameters
        ----------
        username : str

        type : UpdateAvatarRequestType

        upload_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateAvatarResponse]
            avatar updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/avatar/pick.json",
            method="PUT",
            json={
                "type": type,
                "upload_id": upload_id,
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
                    UpdateAvatarResponse,
                    parse_obj_as(
                        type_=UpdateAvatarResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_email(
        self, username: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        username : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/email.json",
            method="PUT",
            json={
                "email": email,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_username(
        self, username: str, *, new_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        username : str

        new_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"u/{jsonable_encoder(username)}/preferences/username.json",
            method="PUT",
            json={
                "new_username": new_username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_actions(
        self, *, offset: int, username: str, filter: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListUserActionsResponse]:
        """
        Parameters
        ----------
        offset : int

        username : str

        filter : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUserActionsResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "user_actions.json",
            method="GET",
            params={
                "offset": offset,
                "username": username,
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserActionsResponse,
                    parse_obj_as(
                        type_=ListUserActionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def refresh_gravatar(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RefreshGravatarResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RefreshGravatarResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user_avatar/{jsonable_encoder(username)}/refresh_gravatar.json",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshGravatarResponse,
                    parse_obj_as(
                        type_=RefreshGravatarResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_user(
        self,
        *,
        api_key: str,
        api_username: str,
        email: str,
        name: str,
        password: str,
        username: str,
        active: typing.Optional[bool] = OMIT,
        approved: typing.Optional[bool] = OMIT,
        external_ids: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        user_fields1: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateUserResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        email : str

        name : str

        password : str

        username : str

        active : typing.Optional[bool]
            This param requires an api key in the request header
            or it will be ignored

        approved : typing.Optional[bool]

        external_ids : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        user_fields1 : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateUserResponse]
            user created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users.json",
            method="POST",
            json={
                "active": active,
                "approved": approved,
                "email": email,
                "external_ids": external_ids,
                "name": name,
                "password": password,
                "user_fields[1]": user_fields1,
                "username": username,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUserResponse,
                    parse_obj_as(
                        type_=CreateUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def change_password(
        self, token: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        password : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/password-reset/{jsonable_encoder(token)}.json",
            method="PUT",
            json={
                "password": password,
                "username": username,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
