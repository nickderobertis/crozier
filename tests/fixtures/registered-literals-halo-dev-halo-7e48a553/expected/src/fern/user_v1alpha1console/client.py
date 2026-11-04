

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.detailed_user import DetailedUser
from ..types.metadata import Metadata
from ..types.user import User
from ..types.user_endpoint_listed_user_list import UserEndpointListedUserList
from ..types.user_permission import UserPermission
from ..types.user_spec import UserSpec
from ..types.user_status import UserStatus
from .raw_client import AsyncRawUserV1Alpha1ConsoleClient, RawUserV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class UserV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_users(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserEndpointListedUserList:
        """
        List users

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword to search

        role : typing.Optional[str]
            Role metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEndpointListedUserList
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.list_users()
        """
        _response = self._raw_client.list_users(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def create_user(
        self,
        *,
        email: str,
        name: str,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        bio: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Creates a new user.

        Parameters
        ----------
        email : str
            email address of the user

        name : str
            user <code>metadata.name</code>, which also serves as the login name

        annotations : typing.Optional[typing.Dict[str, str]]
            metadata annotations to set on the user

        avatar : typing.Optional[str]
            avatar URL of the user

        bio : typing.Optional[str]
            biography or profile text of the user

        display_name : typing.Optional[str]
            display name shown in the console and theme

        password : typing.Optional[str]
            raw password to set for the user

        phone : typing.Optional[str]
            phone number of the user

        roles : typing.Optional[typing.Sequence[str]]
            role <code>metadata.name</code> values to grant to the user after creation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.create_user(
            email="email",
            name="name",
        )
        """
        _response = self._raw_client.create_user(
            email=email,
            name=name,
            annotations=annotations,
            avatar=avatar,
            bio=bio,
            display_name=display_name,
            password=password,
            phone=phone,
            roles=roles,
            request_options=request_options,
        )
        return _response.data

    def get_current_user_detail(self, *, request_options: typing.Optional[RequestOptions] = None) -> DetailedUser:
        """
        Get current user detail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetailedUser
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.get_current_user_detail()
        """
        _response = self._raw_client.get_current_user_detail(request_options=request_options)
        return _response.data

    def update_current_user(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: UserSpec,
        status: typing.Optional[UserStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update current user profile, but password.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : UserSpec

        status : typing.Optional[UserStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi, Metadata, UserSpec

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.update_current_user(
            api_version="apiVersion",
            kind="kind",
            metadata=Metadata(
                name="name",
            ),
            spec=UserSpec(
                display_name="displayName",
            ),
        )
        """
        _response = self._raw_client.update_current_user(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def change_own_password(
        self, *, old_password: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Change own password of user.

        Parameters
        ----------
        old_password : str
            old password

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.change_own_password(
            old_password="oldPassword",
            password="password",
        )
        """
        _response = self._raw_client.change_own_password(
            old_password=old_password, password=password, request_options=request_options
        )
        return _response.data

    def send_email_verification_code(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Send email verification code for user

        Parameters
        ----------
        email : str
            email address to verify

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.send_email_verification_code(
            email="email",
        )
        """
        _response = self._raw_client.send_email_verification_code(email=email, request_options=request_options)
        return _response.data

    def verify_email(
        self, *, code: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verify email for user by code.

        Parameters
        ----------
        code : str
            email verification code

        password : str
            current password of the authenticated user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.verify_email(
            code="code",
            password="password",
        )
        """
        _response = self._raw_client.verify_email(code=code, password=password, request_options=request_options)
        return _response.data

    def get_user_detail(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> DetailedUser:
        """
        Get user detail by metadata.name

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetailedUser
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.get_user_detail(
            name="name",
        )
        """
        _response = self._raw_client.get_user_detail(name, request_options=request_options)
        return _response.data

    def upload_user_avatar(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        upload user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.upload_user_avatar(
            name="name",
        )
        """
        _response = self._raw_client.upload_user_avatar(name, file=file, request_options=request_options)
        return _response.data

    def delete_user_avatar(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        delete user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.delete_user_avatar(
            name="name",
        )
        """
        _response = self._raw_client.delete_user_avatar(name, request_options=request_options)
        return _response.data

    def change_anyone_password(
        self, name: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Change anyone password of user for admin.

        Parameters
        ----------
        name : str
            User metadata.name. If the name is equal to '-', it will change the password of current user.

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.change_anyone_password(
            name="name",
            password="password",
        )
        """
        _response = self._raw_client.change_anyone_password(name, password=password, request_options=request_options)
        return _response.data

    def get_permissions(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserPermission:
        """
        Get permissions of user

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPermission
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.get_permissions(
            name="name",
        )
        """
        _response = self._raw_client.get_permissions(name, request_options=request_options)
        return _response.data

    def grant_permission(
        self, name: str, *, roles: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Grant permissions to user

        Parameters
        ----------
        name : str
            User metadata.name

        roles : typing.Sequence[str]
            role <code>metadata.name</code> values to grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.grant_permission(
            name="name",
            roles=["roles"],
        )
        """
        _response = self._raw_client.grant_permission(name, roles=roles, request_options=request_options)
        return _response.data

    def disable_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Disable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user has been disabled.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.disable_user(
            username="username",
        )
        """
        _response = self._raw_client.disable_user(username, request_options=request_options)
        return _response.data

    def enable_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Enable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user has been enabled.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_v1alpha1console.enable_user(
            username="username",
        )
        """
        _response = self._raw_client.enable_user(username, request_options=request_options)
        return _response.data


class AsyncUserV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_users(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserEndpointListedUserList:
        """
        List users

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword to search

        role : typing.Optional[str]
            Role metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserEndpointListedUserList
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(
            page=page,
            size=size,
            label_selector=label_selector,
            field_selector=field_selector,
            sort=sort,
            keyword=keyword,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def create_user(
        self,
        *,
        email: str,
        name: str,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        bio: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Creates a new user.

        Parameters
        ----------
        email : str
            email address of the user

        name : str
            user <code>metadata.name</code>, which also serves as the login name

        annotations : typing.Optional[typing.Dict[str, str]]
            metadata annotations to set on the user

        avatar : typing.Optional[str]
            avatar URL of the user

        bio : typing.Optional[str]
            biography or profile text of the user

        display_name : typing.Optional[str]
            display name shown in the console and theme

        password : typing.Optional[str]
            raw password to set for the user

        phone : typing.Optional[str]
            phone number of the user

        roles : typing.Optional[typing.Sequence[str]]
            role <code>metadata.name</code> values to grant to the user after creation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.create_user(
                email="email",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            email=email,
            name=name,
            annotations=annotations,
            avatar=avatar,
            bio=bio,
            display_name=display_name,
            password=password,
            phone=phone,
            roles=roles,
            request_options=request_options,
        )
        return _response.data

    async def get_current_user_detail(self, *, request_options: typing.Optional[RequestOptions] = None) -> DetailedUser:
        """
        Get current user detail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetailedUser
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.get_current_user_detail()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_detail(request_options=request_options)
        return _response.data

    async def update_current_user(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: UserSpec,
        status: typing.Optional[UserStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Update current user profile, but password.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : UserSpec

        status : typing.Optional[UserStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Metadata, UserSpec

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.update_current_user(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
                spec=UserSpec(
                    display_name="displayName",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_current_user(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def change_own_password(
        self, *, old_password: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Change own password of user.

        Parameters
        ----------
        old_password : str
            old password

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.change_own_password(
                old_password="oldPassword",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_own_password(
            old_password=old_password, password=password, request_options=request_options
        )
        return _response.data

    async def send_email_verification_code(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Send email verification code for user

        Parameters
        ----------
        email : str
            email address to verify

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.send_email_verification_code(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_email_verification_code(email=email, request_options=request_options)
        return _response.data

    async def verify_email(
        self, *, code: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verify email for user by code.

        Parameters
        ----------
        code : str
            email verification code

        password : str
            current password of the authenticated user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.verify_email(
                code="code",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_email(code=code, password=password, request_options=request_options)
        return _response.data

    async def get_user_detail(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DetailedUser:
        """
        Get user detail by metadata.name

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetailedUser
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.get_user_detail(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_detail(name, request_options=request_options)
        return _response.data

    async def upload_user_avatar(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        upload user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.upload_user_avatar(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_user_avatar(name, file=file, request_options=request_options)
        return _response.data

    async def delete_user_avatar(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        delete user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.delete_user_avatar(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_avatar(name, request_options=request_options)
        return _response.data

    async def change_anyone_password(
        self, name: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Change anyone password of user for admin.

        Parameters
        ----------
        name : str
            User metadata.name. If the name is equal to '-', it will change the password of current user.

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.change_anyone_password(
                name="name",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_anyone_password(
            name, password=password, request_options=request_options
        )
        return _response.data

    async def get_permissions(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserPermission:
        """
        Get permissions of user

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPermission
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.get_permissions(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_permissions(name, request_options=request_options)
        return _response.data

    async def grant_permission(
        self, name: str, *, roles: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Grant permissions to user

        Parameters
        ----------
        name : str
            User metadata.name

        roles : typing.Sequence[str]
            role <code>metadata.name</code> values to grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.grant_permission(
                name="name",
                roles=["roles"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grant_permission(name, roles=roles, request_options=request_options)
        return _response.data

    async def disable_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Disable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user has been disabled.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.disable_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_user(username, request_options=request_options)
        return _response.data

    async def enable_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Enable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            The user has been enabled.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_v1alpha1console.enable_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_user(username, request_options=request_options)
        return _response.data
