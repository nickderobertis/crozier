

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuthClient, RawAuthClient


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def register_a_user(
        self,
        *,
        password: str,
        name: str,
        email: str,
        last_name: str,
        location: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        password : str

        name : str

        email : str

        last_name : str

        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.register_a_user(
            name="name",
            email="email",
            last_name="lastName",
            location="location",
            password="password",
        )
        """
        _response = self._raw_client.register_a_user(
            password=password,
            name=name,
            email=email,
            last_name=last_name,
            location=location,
            request_options=request_options,
        )
        return _response.data

    def log_in_and_receive_a_jwt(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str

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
            token="YOUR_TOKEN",
        )
        client.auth.log_in_and_receive_a_jwt(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.log_in_and_receive_a_jwt(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    def update_the_authenticated_users_profile(
        self,
        *,
        name: str,
        email: str,
        last_name: str,
        location: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        email : str

        last_name : str

        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.update_the_authenticated_users_profile(
            name="name",
            email="email",
            last_name="lastName",
            location="location",
        )
        """
        _response = self._raw_client.update_the_authenticated_users_profile(
            name=name, email=email, last_name=last_name, location=location, request_options=request_options
        )
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def register_a_user(
        self,
        *,
        password: str,
        name: str,
        email: str,
        last_name: str,
        location: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        password : str

        name : str

        email : str

        last_name : str

        location : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.register_a_user(
                name="name",
                email="email",
                last_name="lastName",
                location="location",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_user(
            password=password,
            name=name,
            email=email,
            last_name=last_name,
            location=location,
            request_options=request_options,
        )
        return _response.data

    async def log_in_and_receive_a_jwt(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.log_in_and_receive_a_jwt(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_in_and_receive_a_jwt(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    async def update_the_authenticated_users_profile(
        self,
        *,
        name: str,
        email: str,
        last_name: str,
        location: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        email : str

        last_name : str

        location : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.update_the_authenticated_users_profile(
                name="name",
                email="email",
                last_name="lastName",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_the_authenticated_users_profile(
            name=name, email=email, last_name=last_name, location=location, request_options=request_options
        )
        return _response.data
