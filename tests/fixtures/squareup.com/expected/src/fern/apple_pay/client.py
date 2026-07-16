

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.register_domain_response import RegisterDomainResponse
from .raw_client import AsyncRawApplePayClient, RawApplePayClient


OMIT = typing.cast(typing.Any, ...)


class ApplePayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplePayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplePayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplePayClient
        """
        return self._raw_client

    def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterDomainResponse:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        To learn more about Web Apple Pay, see
        [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterDomainResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.apple_pay.register_domain(
            domain_name="domain_name",
        )
        """
        _response = self._raw_client.register_domain(domain_name=domain_name, request_options=request_options)
        return _response.data


class AsyncApplePayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplePayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplePayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplePayClient
        """
        return self._raw_client

    async def register_domain(
        self, *, domain_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterDomainResponse:
        """
        Activates a domain for use with Apple Pay on the Web and Square. A validation
        is performed on this domain by Apple to ensure that it is properly set up as
        an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate
        Apple Pay on the Web with Square for merchants using their platform.

        To learn more about Web Apple Pay, see
        [Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).

        Parameters
        ----------
        domain_name : str
            A domain name as described in RFC-1034 that will be registered with ApplePay.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterDomainResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.apple_pay.register_domain(
                domain_name="domain_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_domain(domain_name=domain_name, request_options=request_options)
        return _response.data
