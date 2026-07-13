

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.payment_service_provider_draft_payment_create import PaymentServiceProviderDraftPaymentCreate
from ..types.payment_service_provider_draft_payment_listing import PaymentServiceProviderDraftPaymentListing
from ..types.payment_service_provider_draft_payment_read import PaymentServiceProviderDraftPaymentRead
from ..types.payment_service_provider_draft_payment_update import PaymentServiceProviderDraftPaymentUpdate
from .raw_client import AsyncRawPaymentServiceProviderDraftPaymentClient, RawPaymentServiceProviderDraftPaymentClient


OMIT = typing.cast(typing.Any, ...)


class PaymentServiceProviderDraftPaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentServiceProviderDraftPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentServiceProviderDraftPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentServiceProviderDraftPaymentClient
        """
        return self._raw_client

    def list_all_payment_service_provider_draft_payment_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentServiceProviderDraftPaymentListing]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentServiceProviderDraftPaymentListing]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_draft_payment.list_all_payment_service_provider_draft_payment_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_service_provider_draft_payment_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def create_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderDraftPaymentCreate:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentCreate
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_draft_payment.create_payment_service_provider_draft_payment_for_user(
            user_id=1,
            amount=Amount(),
            counterparty_iban="counterparty_iban",
            counterparty_name="counterparty_name",
            description="description",
            sender_iban="sender_iban",
        )
        """
        _response = self._raw_client.create_payment_service_provider_draft_payment_for_user(
            user_id,
            amount=amount,
            counterparty_iban=counterparty_iban,
            counterparty_name=counterparty_name,
            description=description,
            sender_iban=sender_iban,
            sender_name=sender_name,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def read_payment_service_provider_draft_payment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentServiceProviderDraftPaymentRead:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentRead
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_draft_payment.read_payment_service_provider_draft_payment_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_payment_service_provider_draft_payment_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderDraftPaymentUpdate:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentUpdate
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_draft_payment.update_payment_service_provider_draft_payment_for_user(
            user_id=1,
            item_id=1,
            amount=Amount(),
            counterparty_iban="counterparty_iban",
            counterparty_name="counterparty_name",
            description="description",
            sender_iban="sender_iban",
        )
        """
        _response = self._raw_client.update_payment_service_provider_draft_payment_for_user(
            user_id,
            item_id,
            amount=amount,
            counterparty_iban=counterparty_iban,
            counterparty_name=counterparty_name,
            description=description,
            sender_iban=sender_iban,
            sender_name=sender_name,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncPaymentServiceProviderDraftPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentServiceProviderDraftPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentServiceProviderDraftPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentServiceProviderDraftPaymentClient
        """
        return self._raw_client

    async def list_all_payment_service_provider_draft_payment_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentServiceProviderDraftPaymentListing]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentServiceProviderDraftPaymentListing]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_draft_payment.list_all_payment_service_provider_draft_payment_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_service_provider_draft_payment_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderDraftPaymentCreate:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentCreate
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_draft_payment.create_payment_service_provider_draft_payment_for_user(
                user_id=1,
                amount=Amount(),
                counterparty_iban="counterparty_iban",
                counterparty_name="counterparty_name",
                description="description",
                sender_iban="sender_iban",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_service_provider_draft_payment_for_user(
            user_id,
            amount=amount,
            counterparty_iban=counterparty_iban,
            counterparty_name=counterparty_name,
            description=description,
            sender_iban=sender_iban,
            sender_name=sender_name,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def read_payment_service_provider_draft_payment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentServiceProviderDraftPaymentRead:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentRead
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_draft_payment.read_payment_service_provider_draft_payment_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_payment_service_provider_draft_payment_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderDraftPaymentUpdate:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderDraftPaymentUpdate
            Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_draft_payment.update_payment_service_provider_draft_payment_for_user(
                user_id=1,
                item_id=1,
                amount=Amount(),
                counterparty_iban="counterparty_iban",
                counterparty_name="counterparty_name",
                description="description",
                sender_iban="sender_iban",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_payment_service_provider_draft_payment_for_user(
            user_id,
            item_id,
            amount=amount,
            counterparty_iban=counterparty_iban,
            counterparty_name=counterparty_name,
            description=description,
            sender_iban=sender_iban,
            sender_name=sender_name,
            status=status,
            request_options=request_options,
        )
        return _response.data
