

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
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

    def create_user(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        user_status: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        id : typing.Optional[int]

        username : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        email : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        user_status : typing.Optional[int]
            User Status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.create_user()
        """
        _response = self._raw_client.create_user(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        )
        return _response.data

    def create_users_with_list_input(
        self, *, request: typing.Sequence[User], request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Creates list of users with given input array.

        Parameters
        ----------
        request : typing.Sequence[User]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful operation

        Examples
        --------
        from fern import FernApi, User

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.create_users_with_list_input(
            request=[User()],
        )
        """
        _response = self._raw_client.create_users_with_list_input(request=request, request_options=request_options)
        return _response.data

    def login_user(
        self,
        *,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Log into the system.

        Parameters
        ----------
        username : typing.Optional[str]
            The user name for login

        password : typing.Optional[str]
            The password for login in clear text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.login_user()
        """
        _response = self._raw_client.login_user(username=username, password=password, request_options=request_options)
        return _response.data

    def logout_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Log user out of the system.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.logout_user()
        """
        _response = self._raw_client.logout_user(request_options=request_options)
        return _response.data

    def get_user_by_name(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get user detail based on username.

        Parameters
        ----------
        username : str
            The name that needs to be fetched. Use user1 for testing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.get_user_by_name(
            username="username",
        )
        """
        _response = self._raw_client.get_user_by_name(username, request_options=request_options)
        return _response.data

    def update_user(
        self,
        username_: str,
        *,
        id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        user_status: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        username_ : str
            name that need to be deleted

        id : typing.Optional[int]

        username : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        email : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        user_status : typing.Optional[int]
            User Status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.update_user(
            username_="username",
        )
        """
        _response = self._raw_client.update_user(
            username_,
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        )
        return _response.data

    def delete_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        username : str
            The name that needs to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.user.delete_user(
            username="username",
        )
        """
        _response = self._raw_client.delete_user(username, request_options=request_options)
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

    async def create_user(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        user_status: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        id : typing.Optional[int]

        username : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        email : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        user_status : typing.Optional[int]
            User Status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.create_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        )
        return _response.data

    async def create_users_with_list_input(
        self, *, request: typing.Sequence[User], request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Creates list of users with given input array.

        Parameters
        ----------
        request : typing.Sequence[User]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, User

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.create_users_with_list_input(
                request=[User()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_users_with_list_input(
            request=request, request_options=request_options
        )
        return _response.data

    async def login_user(
        self,
        *,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Log into the system.

        Parameters
        ----------
        username : typing.Optional[str]
            The user name for login

        password : typing.Optional[str]
            The password for login in clear text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.login_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.login_user(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def logout_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Log user out of the system.

        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.logout_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout_user(request_options=request_options)
        return _response.data

    async def get_user_by_name(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get user detail based on username.

        Parameters
        ----------
        username : str
            The name that needs to be fetched. Use user1 for testing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_user_by_name(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_by_name(username, request_options=request_options)
        return _response.data

    async def update_user(
        self,
        username_: str,
        *,
        id: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        user_status: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        username_ : str
            name that need to be deleted

        id : typing.Optional[int]

        username : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        email : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        user_status : typing.Optional[int]
            User Status

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.update_user(
                username_="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            username_,
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
            request_options=request_options,
        )
        return _response.data

    async def delete_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        This can only be done by the logged in user.

        Parameters
        ----------
        username : str
            The name that needs to be deleted

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.delete_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(username, request_options=request_options)
        return _response.data
