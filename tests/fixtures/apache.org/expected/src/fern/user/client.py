

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.role import Role
from ..types.user import User
from ..types.user_collection import UserCollection
from ..types.user_collection_item import UserCollectionItem
from ..types.user_collection_item_roles_item import UserCollectionItemRolesItem
from .raw_client import AsyncRawUserClient, RawUserClient


OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCollection:
        """
        Get a list of users.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.get_users()
        """
        _response = self._raw_client.get_users(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def post_user(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Create a new user with unique username and email.

        *New in version 2.2.0*

        Parameters
        ----------
        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.post_user()
        """
        _response = self._raw_client.post_user(
            password=password,
            active=active,
            changed_on=changed_on,
            created_on=created_on,
            email=email,
            failed_login_count=failed_login_count,
            first_name=first_name,
            last_login=last_login,
            last_name=last_name,
            login_count=login_count,
            roles=roles,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def get_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserCollectionItem:
        """
        Get a user with a specific username.

        *New in version 2.1.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCollectionItem
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.get_user(
            username="username",
        )
        """
        _response = self._raw_client.get_user(username, request_options=request_options)
        return _response.data

    def delete_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a user with a specific username.

        *New in version 2.2.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

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
        client.user.delete_user(
            username="username",
        )
        """
        _response = self._raw_client.delete_user(username, request_options=request_options)
        return _response.data

    def patch_user(
        self,
        username_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Update fields for a user.

        *New in version 2.2.0*

        Parameters
        ----------
        username_ : str
            The username of the user.

            *New in version 2.1.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.patch_user(
            username_="username",
        )
        """
        _response = self._raw_client.patch_user(
            username_,
            update_mask=update_mask,
            password=password,
            active=active,
            changed_on=changed_on,
            created_on=created_on,
            email=email,
            failed_login_count=failed_login_count,
            first_name=first_name,
            last_login=last_login,
            last_name=last_name,
            login_count=login_count,
            roles=roles,
            username=username,
            request_options=request_options,
        )
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserCollection:
        """
        Get a list of users.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def post_user(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Create a new user with unique username and email.

        *New in version 2.2.0*

        Parameters
        ----------
        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.post_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_user(
            password=password,
            active=active,
            changed_on=changed_on,
            created_on=created_on,
            email=email,
            failed_login_count=failed_login_count,
            first_name=first_name,
            last_login=last_login,
            last_name=last_name,
            login_count=login_count,
            roles=roles,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def get_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserCollectionItem:
        """
        Get a user with a specific username.

        *New in version 2.1.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserCollectionItem
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.get_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(username, request_options=request_options)
        return _response.data

    async def delete_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a user with a specific username.

        *New in version 2.2.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

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
            await client.user.delete_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(username, request_options=request_options)
        return _response.data

    async def patch_user(
        self,
        username_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """
        Update fields for a user.

        *New in version 2.2.0*

        Parameters
        ----------
        username_ : str
            The username of the user.

            *New in version 2.1.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.patch_user(
                username_="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_user(
            username_,
            update_mask=update_mask,
            password=password,
            active=active,
            changed_on=changed_on,
            created_on=created_on,
            email=email,
            failed_login_count=failed_login_count,
            first_name=first_name,
            last_login=last_login,
            last_name=last_name,
            login_count=login_count,
            roles=roles,
            username=username,
            request_options=request_options,
        )
        return _response.data
