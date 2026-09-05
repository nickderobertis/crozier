

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_credit_price_get import EnvelopeCreditPriceGet
from ..types.envelope_invitation_generated import EnvelopeInvitationGenerated
from ..types.envelope_product_get import EnvelopeProductGet
from ..types.envelope_product_ui_get import EnvelopeProductUiGet
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.trial_account_annotated import TrialAccountAnnotated
from ..types.welcome_credits_annotated import WelcomeCreditsAnnotated
from .raw_client import AsyncRawProductsClient, RawProductsClient
from .types.get_product_request_product_name import GetProductRequestProductName


OMIT = typing.cast(typing.Any, ...)


class ProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsClient
        """
        return self._raw_client

    def get_current_product_price(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeCreditPriceGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCreditPriceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.get_current_product_price()
        """
        _response = self._raw_client.get_current_product_price(request_options=request_options)
        return _response.data

    def get_product(
        self, product_name: GetProductRequestProductName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProductGet:
        """
        NOTE: `/products/current` is used to define current project w/o naming it

        Parameters
        ----------
        product_name : GetProductRequestProductName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProductGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.get_product(
            product_name="current",
        )
        """
        _response = self._raw_client.get_product(product_name, request_options=request_options)
        return _response.data

    def get_current_product_ui(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProductUiGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProductUiGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.get_current_product_ui()
        """
        _response = self._raw_client.get_current_product_ui(request_options=request_options)
        return _response.data

    def generate_invitation(
        self,
        *,
        guest: LowerCaseEmailStr,
        trial_account_days: typing.Optional[TrialAccountAnnotated] = OMIT,
        extra_credits_in_usd: typing.Optional[WelcomeCreditsAnnotated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeInvitationGenerated:
        """
        Parameters
        ----------
        guest : LowerCaseEmailStr

        trial_account_days : typing.Optional[TrialAccountAnnotated]

        extra_credits_in_usd : typing.Optional[WelcomeCreditsAnnotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeInvitationGenerated
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.generate_invitation(
            guest="guest",
        )
        """
        _response = self._raw_client.generate_invitation(
            guest=guest,
            trial_account_days=trial_account_days,
            extra_credits_in_usd=extra_credits_in_usd,
            request_options=request_options,
        )
        return _response.data


class AsyncProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsClient
        """
        return self._raw_client

    async def get_current_product_price(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeCreditPriceGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCreditPriceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.get_current_product_price()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_product_price(request_options=request_options)
        return _response.data

    async def get_product(
        self, product_name: GetProductRequestProductName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProductGet:
        """
        NOTE: `/products/current` is used to define current project w/o naming it

        Parameters
        ----------
        product_name : GetProductRequestProductName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProductGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.get_product(
                product_name="current",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product(product_name, request_options=request_options)
        return _response.data

    async def get_current_product_ui(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeProductUiGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeProductUiGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.get_current_product_ui()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_product_ui(request_options=request_options)
        return _response.data

    async def generate_invitation(
        self,
        *,
        guest: LowerCaseEmailStr,
        trial_account_days: typing.Optional[TrialAccountAnnotated] = OMIT,
        extra_credits_in_usd: typing.Optional[WelcomeCreditsAnnotated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeInvitationGenerated:
        """
        Parameters
        ----------
        guest : LowerCaseEmailStr

        trial_account_days : typing.Optional[TrialAccountAnnotated]

        extra_credits_in_usd : typing.Optional[WelcomeCreditsAnnotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeInvitationGenerated
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.generate_invitation(
                guest="guest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_invitation(
            guest=guest,
            trial_account_days=trial_account_days,
            extra_credits_in_usd=extra_credits_in_usd,
            request_options=request_options,
        )
        return _response.data
