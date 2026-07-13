

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.amount import Amount
from ..types.attachment import Attachment
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.request_inquiry_reference import RequestInquiryReference
from ..types.request_response_listing import RequestResponseListing
from ..types.request_response_read import RequestResponseRead
from ..types.request_response_update import RequestResponseUpdate
from .raw_client import AsyncRawRequestResponseClient, RawRequestResponseClient


OMIT = typing.cast(typing.Any, ...)


class RequestResponseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRequestResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRequestResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRequestResponseClient
        """
        return self._raw_client

    def list_all_request_response_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestResponseListing]:
        """
        Get all RequestResponses for a MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestResponseListing]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
        client.request_response.list_all_request_response_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_request_response_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def read_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponseRead:
        """
        Get the details for a specific existing RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponseRead
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
        client.request_response.read_request_response_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_request_response_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        credit_scheme_identifier: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        eligible_whitelist_id: typing.Optional[int] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        mandate_identifier: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_refund_requested: typing.Optional[str] = OMIT,
        time_refunded: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_refund_requested: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponseUpdate:
        """
        Update the status to accept or reject the RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.

        amount_inquired : typing.Optional[Amount]
            The requested Amount.

        amount_responded : typing.Optional[Amount]
            The Amount the RequestResponse was accepted with.

        attachment : typing.Optional[typing.Sequence[Attachment]]
            The Attachments attached to the RequestResponse.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.

        created : typing.Optional[str]
            The timestamp when the Request Response was created.

        credit_scheme_identifier : typing.Optional[str]
            The credit scheme id provided by the counterparty for DIRECT_DEBIT inquiries.

        description : typing.Optional[str]
            The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.

        eligible_whitelist_id : typing.Optional[int]
            The whitelist id for this action or null.

        event_id : typing.Optional[int]
            The ID of the latest event for the request.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the RequestResponse was created.

        id : typing.Optional[int]
            The id of the Request Response.

        mandate_identifier : typing.Optional[str]
            The mandate id provided by the counterparty for DIRECT_DEBIT inquiries.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestResponse must have.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the RequestResponse was received on.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        status : typing.Optional[str]
            The status of the RequestResponse. Can be ACCEPTED, PENDING, REJECTED, REFUND_REQUESTED, REFUNDED or REVOKED.

        sub_type : typing.Optional[str]
            The subtype of the RequestInquiry. Can be ONCE or RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.

        time_expiry : typing.Optional[str]
            The timestamp of when the RequestResponse expired or will expire.

        time_refund_requested : typing.Optional[str]
            The timestamp of when a refund request for the RequestResponse was claimed.

        time_refunded : typing.Optional[str]
            The timestamp of when the RequestResponse was refunded.

        time_responded : typing.Optional[str]
            The timestamp of when the RequestResponse was responded to.

        type : typing.Optional[str]
            The type of the RequestInquiry. Can be DIRECT_DEBIT, DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.

        updated : typing.Optional[str]
            The timestamp when the Request Response was last updated (will be updated when chat messages are received).

        user_refund_requested : typing.Optional[LabelUser]
            The label of the user that requested the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponseUpdate
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
        client.request_response.update_request_response_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_request_response_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            address_billing=address_billing,
            address_shipping=address_shipping,
            alias=alias,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            counterparty_alias=counterparty_alias,
            created=created,
            credit_scheme_identifier=credit_scheme_identifier,
            description=description,
            eligible_whitelist_id=eligible_whitelist_id,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            mandate_identifier=mandate_identifier,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            request_reference_split_the_bill=request_reference_split_the_bill,
            require_address=require_address,
            status=status,
            sub_type=sub_type,
            time_expiry=time_expiry,
            time_refund_requested=time_refund_requested,
            time_refunded=time_refunded,
            time_responded=time_responded,
            type=type,
            updated=updated,
            user_refund_requested=user_refund_requested,
            request_options=request_options,
        )
        return _response.data


class AsyncRequestResponseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRequestResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRequestResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRequestResponseClient
        """
        return self._raw_client

    async def list_all_request_response_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestResponseListing]:
        """
        Get all RequestResponses for a MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestResponseListing]
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
            await client.request_response.list_all_request_response_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_request_response_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def read_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponseRead:
        """
        Get the details for a specific existing RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponseRead
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
            await client.request_response.read_request_response_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_request_response_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_request_response_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        credit_scheme_identifier: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        eligible_whitelist_id: typing.Optional[int] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        mandate_identifier: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_refund_requested: typing.Optional[str] = OMIT,
        time_refunded: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_refund_requested: typing.Optional[LabelUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponseUpdate:
        """
        Update the status to accept or reject the RequestResponse.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.

        amount_inquired : typing.Optional[Amount]
            The requested Amount.

        amount_responded : typing.Optional[Amount]
            The Amount the RequestResponse was accepted with.

        attachment : typing.Optional[typing.Sequence[Attachment]]
            The Attachments attached to the RequestResponse.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.

        created : typing.Optional[str]
            The timestamp when the Request Response was created.

        credit_scheme_identifier : typing.Optional[str]
            The credit scheme id provided by the counterparty for DIRECT_DEBIT inquiries.

        description : typing.Optional[str]
            The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.

        eligible_whitelist_id : typing.Optional[int]
            The whitelist id for this action or null.

        event_id : typing.Optional[int]
            The ID of the latest event for the request.

        geolocation : typing.Optional[Geolocation]
            The Geolocation where the RequestResponse was created.

        id : typing.Optional[int]
            The id of the Request Response.

        mandate_identifier : typing.Optional[str]
            The mandate id provided by the counterparty for DIRECT_DEBIT inquiries.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestResponse must have.

        monetary_account_id : typing.Optional[int]
            The id of the MonetaryAccount the RequestResponse was received on.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        status : typing.Optional[str]
            The status of the RequestResponse. Can be ACCEPTED, PENDING, REJECTED, REFUND_REQUESTED, REFUNDED or REVOKED.

        sub_type : typing.Optional[str]
            The subtype of the RequestInquiry. Can be ONCE or RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.

        time_expiry : typing.Optional[str]
            The timestamp of when the RequestResponse expired or will expire.

        time_refund_requested : typing.Optional[str]
            The timestamp of when a refund request for the RequestResponse was claimed.

        time_refunded : typing.Optional[str]
            The timestamp of when the RequestResponse was refunded.

        time_responded : typing.Optional[str]
            The timestamp of when the RequestResponse was responded to.

        type : typing.Optional[str]
            The type of the RequestInquiry. Can be DIRECT_DEBIT, DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.

        updated : typing.Optional[str]
            The timestamp when the Request Response was last updated (will be updated when chat messages are received).

        user_refund_requested : typing.Optional[LabelUser]
            The label of the user that requested the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponseUpdate
            A RequestResponse is what a user on the other side of a RequestInquiry gets when he is sent one. So a RequestInquiry is the initiator and visible for the user that sent it and that wants to receive the money. A RequestResponse is what the other side sees, i.e. the user that pays the money to accept the request. The content is almost identical.

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
            await client.request_response.update_request_response_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_request_response_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            address_billing=address_billing,
            address_shipping=address_shipping,
            alias=alias,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            counterparty_alias=counterparty_alias,
            created=created,
            credit_scheme_identifier=credit_scheme_identifier,
            description=description,
            eligible_whitelist_id=eligible_whitelist_id,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            mandate_identifier=mandate_identifier,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            request_reference_split_the_bill=request_reference_split_the_bill,
            require_address=require_address,
            status=status,
            sub_type=sub_type,
            time_expiry=time_expiry,
            time_refund_requested=time_refund_requested,
            time_refunded=time_refunded,
            time_responded=time_responded,
            type=type,
            updated=updated,
            user_refund_requested=user_refund_requested,
            request_options=request_options,
        )
        return _response.data
