

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNewsletterClient, RawNewsletterClient


OMIT = typing.cast(typing.Any, ...)


class NewsletterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNewsletterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNewsletterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNewsletterClient
        """
        return self._raw_client

    def signs_an_email_address_up_to_the_newsletter(
        self, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str
            The email of the user to subscribe.

        token : str
            The recaptcha token used to verify the caller is not a bot.

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
        client.newsletter.signs_an_email_address_up_to_the_newsletter(
            email="email",
            token="token",
        )
        """
        _response = self._raw_client.signs_an_email_address_up_to_the_newsletter(
            email=email, token=token, request_options=request_options
        )
        return _response.data

    def removes_an_email_address_from_the_newsletter(
        self, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str
            The email of the user to unsubscribe.

        token : str
            The recaptcha token used to verify the caller is not a bot.

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
        client.newsletter.removes_an_email_address_from_the_newsletter(
            email="email",
            token="token",
        )
        """
        _response = self._raw_client.removes_an_email_address_from_the_newsletter(
            email=email, token=token, request_options=request_options
        )
        return _response.data


class AsyncNewsletterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNewsletterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNewsletterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNewsletterClient
        """
        return self._raw_client

    async def signs_an_email_address_up_to_the_newsletter(
        self, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str
            The email of the user to subscribe.

        token : str
            The recaptcha token used to verify the caller is not a bot.

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
            await client.newsletter.signs_an_email_address_up_to_the_newsletter(
                email="email",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signs_an_email_address_up_to_the_newsletter(
            email=email, token=token, request_options=request_options
        )
        return _response.data

    async def removes_an_email_address_from_the_newsletter(
        self, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : str
            The email of the user to unsubscribe.

        token : str
            The recaptcha token used to verify the caller is not a bot.

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
            await client.newsletter.removes_an_email_address_from_the_newsletter(
                email="email",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removes_an_email_address_from_the_newsletter(
            email=email, token=token, request_options=request_options
        )
        return _response.data
