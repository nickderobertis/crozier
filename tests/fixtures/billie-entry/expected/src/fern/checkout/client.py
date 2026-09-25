

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCheckoutClient, RawCheckoutClient


OMIT = typing.cast(typing.Any, ...)


class CheckoutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckoutClient
        """
        return self._raw_client

    def create_checkout_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Creates a new checkout session for buyer assessment and payment authorization.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Checkout session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkout.create_checkout_session(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.create_checkout_session(request=request, request_options=request_options)
        return _response.data

    def create_hosted_payment_page_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Creates a checkout session with a hosted payment page for the buyer.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            HPP session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkout.create_hosted_payment_page_session(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.create_hosted_payment_page_session(
            request=request, request_options=request_options
        )
        return _response.data

    def get_authorization(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Retrieves the authorization details for a checkout session.

        Parameters
        ----------
        id : str
            Checkout session ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Authorization details retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkout.get_authorization(
            id="id",
        )
        """
        _response = self._raw_client.get_authorization(id, request_options=request_options)
        return _response.data

    def confirm_checkout_session(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Confirms a checkout session after the buyer has completed payment.

        Parameters
        ----------
        id : str
            Checkout session ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Checkout session confirmed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkout.confirm_checkout_session(
            id="id",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.confirm_checkout_session(id, request=request, request_options=request_options)
        return _response.data


class AsyncCheckoutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckoutClient
        """
        return self._raw_client

    async def create_checkout_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Creates a new checkout session for buyer assessment and payment authorization.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Checkout session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout.create_checkout_session(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_checkout_session(request=request, request_options=request_options)
        return _response.data

    async def create_hosted_payment_page_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Creates a checkout session with a hosted payment page for the buyer.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            HPP session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout.create_hosted_payment_page_session(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_hosted_payment_page_session(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_authorization(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves the authorization details for a checkout session.

        Parameters
        ----------
        id : str
            Checkout session ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Authorization details retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout.get_authorization(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_authorization(id, request_options=request_options)
        return _response.data

    async def confirm_checkout_session(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Confirms a checkout session after the buyer has completed payment.

        Parameters
        ----------
        id : str
            Checkout session ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Checkout session confirmed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout.confirm_checkout_session(
                id="id",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.confirm_checkout_session(
            id, request=request, request_options=request_options
        )
        return _response.data
