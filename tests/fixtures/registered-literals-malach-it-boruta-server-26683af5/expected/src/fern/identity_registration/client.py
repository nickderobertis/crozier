

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityRegistrationClient, RawIdentityRegistrationClient


OMIT = typing.cast(typing.Any, ...)


class IdentityRegistrationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityRegistrationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityRegistrationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityRegistrationClient
        """
        return self._raw_client

    def display_the_registration_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_registration.display_the_registration_form()
        """
        _response = self._raw_client.display_the_registration_form(request=request, request_options=request_options)
        return _response.data

    def register_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_registration.register_a_user(
            user_email="user[email]",
            user_password="user[password]",
        )
        """
        _response = self._raw_client.register_a_user(
            user_email=user_email,
            user_password=user_password,
            request=request,
            user_metadata=user_metadata,
            request_options=request_options,
        )
        return _response.data


class AsyncIdentityRegistrationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityRegistrationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityRegistrationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityRegistrationClient
        """
        return self._raw_client

    async def display_the_registration_form(
        self, *, request: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_registration.display_the_registration_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_registration_form(
            request=request, request_options=request_options
        )
        return _response.data

    async def register_a_user(
        self,
        *,
        user_email: str,
        user_password: str,
        request: typing.Optional[str] = None,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        user_email : str

        user_password : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_registration.register_a_user(
                user_email="user[email]",
                user_password="user[password]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_user(
            user_email=user_email,
            user_password=user_password,
            request=request,
            user_metadata=user_metadata,
            request_options=request_options,
        )
        return _response.data
