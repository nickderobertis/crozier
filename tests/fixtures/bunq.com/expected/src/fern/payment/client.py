

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.amount import Amount
from ..types.attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.master_card_payment_listing import MasterCardPaymentListing
from ..types.payment_auto_allocate_instance import PaymentAutoAllocateInstance
from ..types.payment_create import PaymentCreate
from ..types.payment_listing import PaymentListing
from ..types.payment_read import PaymentRead
from ..types.request_inquiry_reference import RequestInquiryReference
from .raw_client import AsyncRawPaymentClient, RawPaymentClient


OMIT = typing.cast(typing.Any, ...)


class PaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentClient
        """
        return self._raw_client

    def list_all_payment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MasterCardPaymentListing]:
        """
        MasterCard transaction view.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MasterCardPaymentListing]
            MasterCard transaction view.

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
        client.payment.list_all_payment_for_user_monetary_account_mastercard_action(
            user_id=1,
            monetary_account_id=1,
            mastercard_action_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    def list_all_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentListing]:
        """
        Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing).

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentListing]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
        client.payment.list_all_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        allow_bunqto: typing.Optional[bool] = OMIT,
        amount: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]] = OMIT,
        balance_after_mutation: typing.Optional[Amount] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqto_expiry: typing.Optional[str] = OMIT,
        bunqto_share_url: typing.Optional[str] = OMIT,
        bunqto_status: typing.Optional[str] = OMIT,
        bunqto_sub_status: typing.Optional[str] = OMIT,
        bunqto_time_responded: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        payment_auto_allocate_instance: typing.Optional[PaymentAutoAllocateInstance] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentCreate:
        """
        Create a new Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        address_billing : typing.Optional[Address]
            A billing Address provided with the Payment, currently unused.

        address_shipping : typing.Optional[Address]
            A shipping Address provided with the Payment, currently unused.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        allow_bunqto : typing.Optional[bool]
            Whether or not sending a bunq.to payment is allowed.

        amount : typing.Optional[Amount]
            The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).

        attachment : typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]]
            The Attachments attached to the Payment.

        balance_after_mutation : typing.Optional[Amount]
            The new balance of the monetary account after the mutation.

        batch_id : typing.Optional[int]
            The id of the PaymentBatch if this Payment was part of one.

        bunqto_expiry : typing.Optional[str]
            When bunq.to payment is about to expire.

        bunqto_share_url : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_status : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_sub_status : typing.Optional[str]
            The sub status of the bunq.to payment.

        bunqto_time_responded : typing.Optional[str]
            The timestamp of when the bunq.to payment was responded to.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        created : typing.Optional[str]
            The timestamp when the Payment was done.

        description : typing.Optional[str]
            The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the Payment was done from.

        id : typing.Optional[int]
            The id of the created Payment.

        merchant_reference : typing.Optional[str]
            Optional data included with the Payment specific to the merchant.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).

        payment_auto_allocate_instance : typing.Optional[PaymentAutoAllocateInstance]
            A reference to the PaymentAutoAllocateInstance if it exists.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        scheduled_id : typing.Optional[int]
            The id of the JobScheduled if the Payment was scheduled.

        sub_type : typing.Optional[str]
            The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.

        type : typing.Optional[str]
            The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).

        updated : typing.Optional[str]
            The timestamp when the Payment was last updated (will be updated when chat messages are received).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentCreate
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
        client.payment.create_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
        )
        """
        _response = self._raw_client.create_payment_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            address_billing=address_billing,
            address_shipping=address_shipping,
            alias=alias,
            allow_bunqto=allow_bunqto,
            amount=amount,
            attachment=attachment,
            balance_after_mutation=balance_after_mutation,
            batch_id=batch_id,
            bunqto_expiry=bunqto_expiry,
            bunqto_share_url=bunqto_share_url,
            bunqto_status=bunqto_status,
            bunqto_sub_status=bunqto_sub_status,
            bunqto_time_responded=bunqto_time_responded,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            monetary_account_id=monetary_account_id,
            payment_auto_allocate_instance=payment_auto_allocate_instance,
            request_reference_split_the_bill=request_reference_split_the_bill,
            scheduled_id=scheduled_id,
            sub_type=sub_type,
            type=type,
            updated=updated,
            request_options=request_options,
        )
        return _response.data

    def read_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRead:
        """
        Get a specific previous Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRead
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
        client.payment.read_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentClient
        """
        return self._raw_client

    async def list_all_payment_for_user_monetary_account_mastercard_action(
        self,
        user_id: int,
        monetary_account_id: int,
        mastercard_action_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MasterCardPaymentListing]:
        """
        MasterCard transaction view.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        mastercard_action_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MasterCardPaymentListing]
            MasterCard transaction view.

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
            await client.payment.list_all_payment_for_user_monetary_account_mastercard_action(
                user_id=1,
                monetary_account_id=1,
                mastercard_action_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_for_user_monetary_account_mastercard_action(
            user_id, monetary_account_id, mastercard_action_id, request_options=request_options
        )
        return _response.data

    async def list_all_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentListing]:
        """
        Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing).

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentListing]
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
            await client.payment.list_all_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        allow_bunqto: typing.Optional[bool] = OMIT,
        amount: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]] = OMIT,
        balance_after_mutation: typing.Optional[Amount] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqto_expiry: typing.Optional[str] = OMIT,
        bunqto_share_url: typing.Optional[str] = OMIT,
        bunqto_status: typing.Optional[str] = OMIT,
        bunqto_sub_status: typing.Optional[str] = OMIT,
        bunqto_time_responded: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        payment_auto_allocate_instance: typing.Optional[PaymentAutoAllocateInstance] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentCreate:
        """
        Create a new Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        address_billing : typing.Optional[Address]
            A billing Address provided with the Payment, currently unused.

        address_shipping : typing.Optional[Address]
            A shipping Address provided with the Payment, currently unused.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.

        allow_bunqto : typing.Optional[bool]
            Whether or not sending a bunq.to payment is allowed.

        amount : typing.Optional[Amount]
            The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).

        attachment : typing.Optional[typing.Sequence[AttachmentMonetaryAccountPayment]]
            The Attachments attached to the Payment.

        balance_after_mutation : typing.Optional[Amount]
            The new balance of the monetary account after the mutation.

        batch_id : typing.Optional[int]
            The id of the PaymentBatch if this Payment was part of one.

        bunqto_expiry : typing.Optional[str]
            When bunq.to payment is about to expire.

        bunqto_share_url : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_status : typing.Optional[str]
            The status of the bunq.to payment.

        bunqto_sub_status : typing.Optional[str]
            The sub status of the bunq.to payment.

        bunqto_time_responded : typing.Optional[str]
            The timestamp of when the bunq.to payment was responded to.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.

        created : typing.Optional[str]
            The timestamp when the Payment was done.

        description : typing.Optional[str]
            The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the Payment was done from.

        id : typing.Optional[int]
            The id of the created Payment.

        merchant_reference : typing.Optional[str]
            Optional data included with the Payment specific to the merchant.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).

        payment_auto_allocate_instance : typing.Optional[PaymentAutoAllocateInstance]
            A reference to the PaymentAutoAllocateInstance if it exists.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        scheduled_id : typing.Optional[int]
            The id of the JobScheduled if the Payment was scheduled.

        sub_type : typing.Optional[str]
            The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.

        type : typing.Optional[str]
            The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).

        updated : typing.Optional[str]
            The timestamp when the Payment was last updated (will be updated when chat messages are received).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentCreate
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
            await client.payment.create_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            address_billing=address_billing,
            address_shipping=address_shipping,
            alias=alias,
            allow_bunqto=allow_bunqto,
            amount=amount,
            attachment=attachment,
            balance_after_mutation=balance_after_mutation,
            batch_id=batch_id,
            bunqto_expiry=bunqto_expiry,
            bunqto_share_url=bunqto_share_url,
            bunqto_status=bunqto_status,
            bunqto_sub_status=bunqto_sub_status,
            bunqto_time_responded=bunqto_time_responded,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            monetary_account_id=monetary_account_id,
            payment_auto_allocate_instance=payment_auto_allocate_instance,
            request_reference_split_the_bill=request_reference_split_the_bill,
            scheduled_id=scheduled_id,
            sub_type=sub_type,
            type=type,
            updated=updated,
            request_options=request_options,
        )
        return _response.data

    async def read_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentRead:
        """
        Get a specific previous Payment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentRead
            Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account.

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
            await client.payment.read_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
