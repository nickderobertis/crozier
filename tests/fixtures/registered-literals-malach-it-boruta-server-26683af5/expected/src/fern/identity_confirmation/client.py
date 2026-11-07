

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityConfirmationClient, RawIdentityConfirmationClient


OMIT = typing.cast(typing.Any, ...)


class IdentityConfirmationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityConfirmationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityConfirmationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityConfirmationClient
        """
        return self._raw_client

    def display_the_confirmation_instructions_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
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
        client.identity_confirmation.display_the_confirmation_instructions_form()
        """
        _response = self._raw_client.display_the_confirmation_instructions_form(request_options=request_options)
        return _response.data

    def resend_account_confirmation_instructions(
        self, *, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

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
        client.identity_confirmation.resend_account_confirmation_instructions(
            user_email="user[email]",
        )
        """
        _response = self._raw_client.resend_account_confirmation_instructions(
            user_email=user_email, request_options=request_options
        )
        return _response.data

    def confirm_an_account(
        self,
        token: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
        client.identity_confirmation.confirm_an_account(
            token="token",
        )
        """
        _response = self._raw_client.confirm_an_account(token, request=request, request_options=request_options)
        return _response.data


class AsyncIdentityConfirmationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityConfirmationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityConfirmationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityConfirmationClient
        """
        return self._raw_client

    async def display_the_confirmation_instructions_form(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
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
            await client.identity_confirmation.display_the_confirmation_instructions_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_confirmation_instructions_form(request_options=request_options)
        return _response.data

    async def resend_account_confirmation_instructions(
        self, *, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        user_email : str

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
            await client.identity_confirmation.resend_account_confirmation_instructions(
                user_email="user[email]",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend_account_confirmation_instructions(
            user_email=user_email, request_options=request_options
        )
        return _response.data

    async def confirm_an_account(
        self,
        token: str,
        *,
        request: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        request : typing.Optional[str]
            Encoded authorization request retained across the identity flow

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
            await client.identity_confirmation.confirm_an_account(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.confirm_an_account(token, request=request, request_options=request_options)
        return _response.data
