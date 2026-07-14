

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUsersClient, RawUsersClient
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


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def admin_list_users(
        self,
        flag: AdminListUsersRequestFlag,
        *,
        order: typing.Optional[AdminListUsersRequestOrder] = None,
        asc: typing.Optional[AdminListUsersRequestAsc] = None,
        page: typing.Optional[int] = None,
        show_emails: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AdminListUsersResponseItem]:
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
        typing.List[AdminListUsersResponseItem]
            response

        Examples
        --------
        from fern.users import AdminListUsersRequestFlag

        from fern import FernApi

        client = FernApi()
        client.users.admin_list_users(
            flag=AdminListUsersRequestFlag.ACTIVE,
        )
        """
        _response = self._raw_client.admin_list_users(
            flag, order=order, asc=asc, page=page, show_emails=show_emails, request_options=request_options
        )
        return _response.data

    def admin_get_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AdminGetUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminGetUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.admin_get_user(
            id=1,
        )
        """
        _response = self._raw_client.admin_get_user(id, request_options=request_options)
        return _response.data

    def delete_user(
        self,
        id: int,
        *,
        block_email: typing.Optional[bool] = OMIT,
        block_ip: typing.Optional[bool] = OMIT,
        block_urls: typing.Optional[bool] = OMIT,
        delete_posts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUserResponse:
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
        DeleteUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.delete_user(
            id=1,
        )
        """
        _response = self._raw_client.delete_user(
            id,
            block_email=block_email,
            block_ip=block_ip,
            block_urls=block_urls,
            delete_posts=delete_posts,
            request_options=request_options,
        )
        return _response.data

    def anonymize_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnonymizeUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnonymizeUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.anonymize_user(
            id=1,
        )
        """
        _response = self._raw_client.anonymize_user(id, request_options=request_options)
        return _response.data

    def log_out_user(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> LogOutUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogOutUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.log_out_user(
            id=1,
        )
        """
        _response = self._raw_client.log_out_user(id, request_options=request_options)
        return _response.data

    def silence_user(
        self,
        id: int,
        *,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        silenced_till: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SilenceUserResponse:
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
        SilenceUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.silence_user(
            id=1,
        )
        """
        _response = self._raw_client.silence_user(
            id,
            message=message,
            post_action=post_action,
            reason=reason,
            silenced_till=silenced_till,
            request_options=request_options,
        )
        return _response.data

    def suspend_user(
        self,
        id: int,
        *,
        reason: str,
        suspend_until: str,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuspendUserResponse:
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
        SuspendUserResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.suspend_user(
            id=1,
            reason="reason",
            suspend_until="2121-02-22",
        )
        """
        _response = self._raw_client.suspend_user(
            id,
            reason=reason,
            suspend_until=suspend_until,
            message=message,
            post_action=post_action,
            request_options=request_options,
        )
        return _response.data

    def list_users_public(
        self,
        *,
        period: ListUsersPublicRequestPeriod,
        order: ListUsersPublicRequestOrder,
        asc: typing.Optional[ListUsersPublicRequestAsc] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUsersPublicResponse:
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
        ListUsersPublicResponse
            directory items response

        Examples
        --------
        from fern.users import ListUsersPublicRequestOrder, ListUsersPublicRequestPeriod

        from fern import FernApi

        client = FernApi()
        client.users.list_users_public(
            period=ListUsersPublicRequestPeriod.DAILY,
            order=ListUsersPublicRequestOrder.LIKES_RECEIVED,
        )
        """
        _response = self._raw_client.list_users_public(
            period=period, order=order, asc=asc, page=page, request_options=request_options
        )
        return _response.data

    def send_password_reset_email(
        self, *, login: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SendPasswordResetEmailResponse:
        """
        Parameters
        ----------
        login : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendPasswordResetEmailResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.send_password_reset_email(
            login="login",
        )
        """
        _response = self._raw_client.send_password_reset_email(login=login, request_options=request_options)
        return _response.data

    def get_user_external_id(
        self,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserExternalIdResponse:
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
        GetUserExternalIdResponse
            user response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_user_external_id(
            external_id="external_id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_user_external_id(
            external_id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserIdentiyProviderExternalIdResponse:
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
        GetUserIdentiyProviderExternalIdResponse
            user response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_user_identiy_provider_external_id(
            provider="provider",
            external_id="external_id",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_user_identiy_provider_external_id(
            provider, external_id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    def get_user(
        self, username: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserResponse:
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
        GetUserResponse
            user response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_user(
            username="username",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.get_user(
            username, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

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
    ) -> UpdateUserResponse:
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
        UpdateUserResponse
            user updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.update_user(
            username="username",
            api_key="Api-Key",
            api_username="Api-Username",
        )
        """
        _response = self._raw_client.update_user(
            username,
            api_key=api_key,
            api_username=api_username,
            email=email,
            external_ids=external_ids,
            name=name,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def get_user_emails(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserEmailsResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserEmailsResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_user_emails(
            username="username",
        )
        """
        _response = self._raw_client.get_user_emails(username, request_options=request_options)
        return _response.data

    def update_avatar(
        self,
        username: str,
        *,
        type: UpdateAvatarRequestType,
        upload_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAvatarResponse:
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
        UpdateAvatarResponse
            avatar updated

        Examples
        --------
        from fern.users import UpdateAvatarRequestType

        from fern import FernApi

        client = FernApi()
        client.users.update_avatar(
            username="username",
            type=UpdateAvatarRequestType.UPLOADED,
            upload_id=1,
        )
        """
        _response = self._raw_client.update_avatar(
            username, type=type, upload_id=upload_id, request_options=request_options
        )
        return _response.data

    def update_email(
        self, username: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        username : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.update_email(
            username="username",
            email="email",
        )
        """
        _response = self._raw_client.update_email(username, email=email, request_options=request_options)
        return _response.data

    def update_username(
        self, username: str, *, new_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        username : str

        new_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.update_username(
            username="username",
            new_username="new_username",
        )
        """
        _response = self._raw_client.update_username(
            username, new_username=new_username, request_options=request_options
        )
        return _response.data

    def list_user_actions(
        self, *, offset: int, username: str, filter: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserActionsResponse:
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
        ListUserActionsResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.list_user_actions(
            offset=1,
            username="username",
            filter="filter",
        )
        """
        _response = self._raw_client.list_user_actions(
            offset=offset, username=username, filter=filter, request_options=request_options
        )
        return _response.data

    def refresh_gravatar(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshGravatarResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshGravatarResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.refresh_gravatar(
            username="username",
        )
        """
        _response = self._raw_client.refresh_gravatar(username, request_options=request_options)
        return _response.data

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
    ) -> CreateUserResponse:
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
        CreateUserResponse
            user created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.create_user(
            api_key="Api-Key",
            api_username="Api-Username",
            email="email",
            name="name",
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.create_user(
            api_key=api_key,
            api_username=api_username,
            email=email,
            name=name,
            password=password,
            username=username,
            active=active,
            approved=approved,
            external_ids=external_ids,
            user_fields1=user_fields1,
            request_options=request_options,
        )
        return _response.data

    def change_password(
        self, token: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.change_password(
            token="token",
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.change_password(
            token, password=password, username=username, request_options=request_options
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def admin_list_users(
        self,
        flag: AdminListUsersRequestFlag,
        *,
        order: typing.Optional[AdminListUsersRequestOrder] = None,
        asc: typing.Optional[AdminListUsersRequestAsc] = None,
        page: typing.Optional[int] = None,
        show_emails: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AdminListUsersResponseItem]:
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
        typing.List[AdminListUsersResponseItem]
            response

        Examples
        --------
        import asyncio

        from fern.users import AdminListUsersRequestFlag

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.admin_list_users(
                flag=AdminListUsersRequestFlag.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.admin_list_users(
            flag, order=order, asc=asc, page=page, show_emails=show_emails, request_options=request_options
        )
        return _response.data

    async def admin_get_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AdminGetUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminGetUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.admin_get_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.admin_get_user(id, request_options=request_options)
        return _response.data

    async def delete_user(
        self,
        id: int,
        *,
        block_email: typing.Optional[bool] = OMIT,
        block_ip: typing.Optional[bool] = OMIT,
        block_urls: typing.Optional[bool] = OMIT,
        delete_posts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteUserResponse:
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
        DeleteUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.delete_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(
            id,
            block_email=block_email,
            block_ip=block_ip,
            block_urls=block_urls,
            delete_posts=delete_posts,
            request_options=request_options,
        )
        return _response.data

    async def anonymize_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnonymizeUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnonymizeUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.anonymize_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.anonymize_user(id, request_options=request_options)
        return _response.data

    async def log_out_user(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LogOutUserResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogOutUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.log_out_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_out_user(id, request_options=request_options)
        return _response.data

    async def silence_user(
        self,
        id: int,
        *,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        silenced_till: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SilenceUserResponse:
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
        SilenceUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.silence_user(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.silence_user(
            id,
            message=message,
            post_action=post_action,
            reason=reason,
            silenced_till=silenced_till,
            request_options=request_options,
        )
        return _response.data

    async def suspend_user(
        self,
        id: int,
        *,
        reason: str,
        suspend_until: str,
        message: typing.Optional[str] = OMIT,
        post_action: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuspendUserResponse:
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
        SuspendUserResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.suspend_user(
                id=1,
                reason="reason",
                suspend_until="2121-02-22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suspend_user(
            id,
            reason=reason,
            suspend_until=suspend_until,
            message=message,
            post_action=post_action,
            request_options=request_options,
        )
        return _response.data

    async def list_users_public(
        self,
        *,
        period: ListUsersPublicRequestPeriod,
        order: ListUsersPublicRequestOrder,
        asc: typing.Optional[ListUsersPublicRequestAsc] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUsersPublicResponse:
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
        ListUsersPublicResponse
            directory items response

        Examples
        --------
        import asyncio

        from fern.users import ListUsersPublicRequestOrder, ListUsersPublicRequestPeriod

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_users_public(
                period=ListUsersPublicRequestPeriod.DAILY,
                order=ListUsersPublicRequestOrder.LIKES_RECEIVED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users_public(
            period=period, order=order, asc=asc, page=page, request_options=request_options
        )
        return _response.data

    async def send_password_reset_email(
        self, *, login: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SendPasswordResetEmailResponse:
        """
        Parameters
        ----------
        login : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendPasswordResetEmailResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.send_password_reset_email(
                login="login",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_password_reset_email(login=login, request_options=request_options)
        return _response.data

    async def get_user_external_id(
        self,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserExternalIdResponse:
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
        GetUserExternalIdResponse
            user response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_user_external_id(
                external_id="external_id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_external_id(
            external_id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def get_user_identiy_provider_external_id(
        self,
        provider: str,
        external_id: str,
        *,
        api_key: str,
        api_username: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserIdentiyProviderExternalIdResponse:
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
        GetUserIdentiyProviderExternalIdResponse
            user response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_user_identiy_provider_external_id(
                provider="provider",
                external_id="external_id",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_identiy_provider_external_id(
            provider, external_id, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

    async def get_user(
        self, username: str, *, api_key: str, api_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserResponse:
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
        GetUserResponse
            user response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_user(
                username="username",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(
            username, api_key=api_key, api_username=api_username, request_options=request_options
        )
        return _response.data

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
    ) -> UpdateUserResponse:
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
        UpdateUserResponse
            user updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.update_user(
                username="username",
                api_key="Api-Key",
                api_username="Api-Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            username,
            api_key=api_key,
            api_username=api_username,
            email=email,
            external_ids=external_ids,
            name=name,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def get_user_emails(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserEmailsResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserEmailsResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_user_emails(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_emails(username, request_options=request_options)
        return _response.data

    async def update_avatar(
        self,
        username: str,
        *,
        type: UpdateAvatarRequestType,
        upload_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAvatarResponse:
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
        UpdateAvatarResponse
            avatar updated

        Examples
        --------
        import asyncio

        from fern.users import UpdateAvatarRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.update_avatar(
                username="username",
                type=UpdateAvatarRequestType.UPLOADED,
                upload_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_avatar(
            username, type=type, upload_id=upload_id, request_options=request_options
        )
        return _response.data

    async def update_email(
        self, username: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        username : str

        email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.update_email(
                username="username",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_email(username, email=email, request_options=request_options)
        return _response.data

    async def update_username(
        self, username: str, *, new_username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        username : str

        new_username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.update_username(
                username="username",
                new_username="new_username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_username(
            username, new_username=new_username, request_options=request_options
        )
        return _response.data

    async def list_user_actions(
        self, *, offset: int, username: str, filter: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserActionsResponse:
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
        ListUserActionsResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.list_user_actions(
                offset=1,
                username="username",
                filter="filter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_actions(
            offset=offset, username=username, filter=filter, request_options=request_options
        )
        return _response.data

    async def refresh_gravatar(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshGravatarResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshGravatarResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.refresh_gravatar(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_gravatar(username, request_options=request_options)
        return _response.data

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
    ) -> CreateUserResponse:
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
        CreateUserResponse
            user created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.create_user(
                api_key="Api-Key",
                api_username="Api-Username",
                email="email",
                name="name",
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            api_key=api_key,
            api_username=api_username,
            email=email,
            name=name,
            password=password,
            username=username,
            active=active,
            approved=approved,
            external_ids=external_ids,
            user_fields1=user_fields1,
            request_options=request_options,
        )
        return _response.data

    async def change_password(
        self, token: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.change_password(
                token="token",
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_password(
            token, password=password, username=username, request_options=request_options
        )
        return _response.data
