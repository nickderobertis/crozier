

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_authentication_activity_dto import PageAuthenticationActivityDto
from ..types.user_dto import UserDto
from .raw_client import AsyncRawCurrentUserClient, RawCurrentUserClient


OMIT = typing.cast(typing.Any, ...)


class CurrentUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurrentUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurrentUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurrentUserClient
        """
        return self._raw_client

    def get_current_user(
        self, *, remember_me: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> UserDto:
        """
        Parameters
        ----------
        remember_me : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.current_user.get_current_user()
        """
        _response = self._raw_client.get_current_user(remember_me=remember_me, request_options=request_options)
        return _response.data

    def get_authentication_activity_for_current_user(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthenticationActivityDto:
        """
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
        client.current_user.get_authentication_activity_for_current_user()
        """
        _response = self._raw_client.get_authentication_activity_for_current_user(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def update_password_for_current_user(
        self, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.current_user.update_password_for_current_user(
            password="password",
        )
        """
        _response = self._raw_client.update_password_for_current_user(
            password=password, request_options=request_options
        )
        return _response.data


class AsyncCurrentUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurrentUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurrentUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurrentUserClient
        """
        return self._raw_client

    async def get_current_user(
        self, *, remember_me: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> UserDto:
        """
        Parameters
        ----------
        remember_me : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.current_user.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(remember_me=remember_me, request_options=request_options)
        return _response.data

    async def get_authentication_activity_for_current_user(
        self,
        *,
        unpaged: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageAuthenticationActivityDto:
        """
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
            await client.current_user.get_authentication_activity_for_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authentication_activity_for_current_user(
            unpaged=unpaged, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def update_password_for_current_user(
        self, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.current_user.update_password_for_current_user(
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_password_for_current_user(
            password=password, request_options=request_options
        )
        return _response.data
