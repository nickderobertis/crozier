

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.age_restriction_update_dto import AgeRestrictionUpdateDto
from ..types.authentication_activity_dto import AuthenticationActivityDto
from ..types.page_authentication_activity_dto import PageAuthenticationActivityDto
from ..types.shared_libraries_update_dto import SharedLibrariesUpdateDto
from ..types.user_dto import UserDto
from .raw_client import AsyncRawUsersClient, RawUsersClient


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

    def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(request_options=request_options)
        return _response.data

    def add_user(
        self,
        *,
        email: str,
        password: str,
        roles: typing.Sequence[str],
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        email : str

        password : str

        roles : typing.Sequence[str]

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.add_user(
            email="email",
            password="password",
            roles=["roles"],
        )
        """
        _response = self._raw_client.add_user(
            email=email,
            password=password,
            roles=roles,
            age_restriction=age_restriction,
            labels_allow=labels_allow,
            labels_exclude=labels_exclude,
            shared_libraries=shared_libraries,
            request_options=request_options,
        )
        return _response.data

    def get_authentication_activity(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthenticationActivityDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageAuthenticationActivityDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.get_authentication_activity()
        """
        _response = self._raw_client.get_authentication_activity(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def delete_user_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        )
        client.users.delete_user_by_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_user_by_id(id, request_options=request_options)
        return _response.data

    def update_user_by_id(
        self,
        id: str,
        *,
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        roles : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

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
        )
        client.users.update_user_by_id(
            id="id",
        )
        """
        _response = self._raw_client.update_user_by_id(
            id,
            age_restriction=age_restriction,
            labels_allow=labels_allow,
            labels_exclude=labels_exclude,
            roles=roles,
            shared_libraries=shared_libraries,
            request_options=request_options,
        )
        return _response.data

    def get_latest_authentication_activity_by_user_id(
        self,
        id: str,
        *,
        apikey_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthenticationActivityDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        apikey_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationActivityDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.users.get_latest_authentication_activity_by_user_id(
            id="id",
        )
        """
        _response = self._raw_client.get_latest_authentication_activity_by_user_id(
            id, apikey_id=apikey_id, request_options=request_options
        )
        return _response.data

    def update_password_by_user_id(
        self, id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        password : str

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
        )
        client.users.update_password_by_user_id(
            id="id",
            password="password",
        )
        """
        _response = self._raw_client.update_password_by_user_id(id, password=password, request_options=request_options)
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

    async def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[UserDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(request_options=request_options)
        return _response.data

    async def add_user(
        self,
        *,
        email: str,
        password: str,
        roles: typing.Sequence[str],
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        email : str

        password : str

        roles : typing.Sequence[str]

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.add_user(
                email="email",
                password="password",
                roles=["roles"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user(
            email=email,
            password=password,
            roles=roles,
            age_restriction=age_restriction,
            labels_allow=labels_allow,
            labels_exclude=labels_exclude,
            shared_libraries=shared_libraries,
            request_options=request_options,
        )
        return _response.data

    async def get_authentication_activity(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthenticationActivityDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        unpaged : typing.Optional[bool]

        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageAuthenticationActivityDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.get_authentication_activity()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authentication_activity(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def delete_user_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

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
        )


        async def main() -> None:
            await client.users.delete_user_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_by_id(id, request_options=request_options)
        return _response.data

    async def update_user_by_id(
        self,
        id: str,
        *,
        age_restriction: typing.Optional[AgeRestrictionUpdateDto] = OMIT,
        labels_allow: typing.Optional[typing.Sequence[str]] = OMIT,
        labels_exclude: typing.Optional[typing.Sequence[str]] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        shared_libraries: typing.Optional[SharedLibrariesUpdateDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        age_restriction : typing.Optional[AgeRestrictionUpdateDto]

        labels_allow : typing.Optional[typing.Sequence[str]]

        labels_exclude : typing.Optional[typing.Sequence[str]]

        roles : typing.Optional[typing.Sequence[str]]

        shared_libraries : typing.Optional[SharedLibrariesUpdateDto]

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
        )


        async def main() -> None:
            await client.users.update_user_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_by_id(
            id,
            age_restriction=age_restriction,
            labels_allow=labels_allow,
            labels_exclude=labels_exclude,
            roles=roles,
            shared_libraries=shared_libraries,
            request_options=request_options,
        )
        return _response.data

    async def get_latest_authentication_activity_by_user_id(
        self,
        id: str,
        *,
        apikey_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthenticationActivityDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        apikey_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationActivityDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.users.get_latest_authentication_activity_by_user_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_authentication_activity_by_user_id(
            id, apikey_id=apikey_id, request_options=request_options
        )
        return _response.data

    async def update_password_by_user_id(
        self, id: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        id : str

        password : str

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
        )


        async def main() -> None:
            await client.users.update_password_by_user_id(
                id="id",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_password_by_user_id(
            id, password=password, request_options=request_options
        )
        return _response.data
