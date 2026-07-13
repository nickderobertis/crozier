

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.amount import Amount
from ..types.bunq_id import BunqId
from ..types.geolocation import Geolocation
from ..types.label_monetary_account import LabelMonetaryAccount
from ..types.label_user import LabelUser
from ..types.request_inquiry_create import RequestInquiryCreate
from ..types.request_inquiry_listing import RequestInquiryListing
from ..types.request_inquiry_read import RequestInquiryRead
from ..types.request_inquiry_update import RequestInquiryUpdate
from ..types.request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject
from .raw_client import AsyncRawRequestInquiryClient, RawRequestInquiryClient


OMIT = typing.cast(typing.Any, ...)


class RequestInquiryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRequestInquiryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRequestInquiryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRequestInquiryClient
        """
        return self._raw_client

    def list_all_request_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestInquiryListing]:
        """
        Get all payment requests for a user's monetary account. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestInquiryListing]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
        client.request_inquiry.list_all_request_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_request_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryCreate:
        """
        Create a new payment request.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryCreate
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
        client.request_inquiry.create_request_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
            allow_bunqme=True,
        )
        """
        _response = self._raw_client.create_request_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            allow_bunqme=allow_bunqme,
            address_billing=address_billing,
            address_shipping=address_shipping,
            allow_amount_higher=allow_amount_higher,
            allow_amount_lower=allow_amount_lower,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            batch_id=batch_id,
            bunqme_share_url=bunqme_share_url,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            reference_split_the_bill=reference_split_the_bill,
            require_address=require_address,
            scheduled_id=scheduled_id,
            status=status,
            time_expiry=time_expiry,
            time_responded=time_responded,
            updated=updated,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            want_tip=want_tip,
            request_options=request_options,
        )
        return _response.data

    def read_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryRead:
        """
        Get the details of a specific payment request, including its status. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryRead
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
        client.request_inquiry.read_request_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_request_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryUpdate:
        """
        Revoke a request for payment, by updating the status to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryUpdate
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
        client.request_inquiry.update_request_inquiry_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
            item_id=1,
            allow_bunqme=True,
        )
        """
        _response = self._raw_client.update_request_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            allow_bunqme=allow_bunqme,
            address_billing=address_billing,
            address_shipping=address_shipping,
            allow_amount_higher=allow_amount_higher,
            allow_amount_lower=allow_amount_lower,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            batch_id=batch_id,
            bunqme_share_url=bunqme_share_url,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            reference_split_the_bill=reference_split_the_bill,
            require_address=require_address,
            scheduled_id=scheduled_id,
            status=status,
            time_expiry=time_expiry,
            time_responded=time_responded,
            updated=updated,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            want_tip=want_tip,
            request_options=request_options,
        )
        return _response.data


class AsyncRequestInquiryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRequestInquiryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRequestInquiryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRequestInquiryClient
        """
        return self._raw_client

    async def list_all_request_inquiry_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestInquiryListing]:
        """
        Get all payment requests for a user's monetary account. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestInquiryListing]
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
            await client.request_inquiry.list_all_request_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_request_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryCreate:
        """
        Create a new payment request.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryCreate
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
            await client.request_inquiry.create_request_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
                allow_bunqme=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_request_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            allow_bunqme=allow_bunqme,
            address_billing=address_billing,
            address_shipping=address_shipping,
            allow_amount_higher=allow_amount_higher,
            allow_amount_lower=allow_amount_lower,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            batch_id=batch_id,
            bunqme_share_url=bunqme_share_url,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            reference_split_the_bill=reference_split_the_bill,
            require_address=require_address,
            scheduled_id=scheduled_id,
            status=status,
            time_expiry=time_expiry,
            time_responded=time_responded,
            updated=updated,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            want_tip=want_tip,
            request_options=request_options,
        )
        return _response.data

    async def read_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryRead:
        """
        Get the details of a specific payment request, including its status. bunqme_share_url is always null if the counterparty is a bunq user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryRead
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
            await client.request_inquiry.read_request_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_request_inquiry_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_request_inquiry_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        item_id: int,
        *,
        allow_bunqme: bool,
        address_billing: typing.Optional[Address] = OMIT,
        address_shipping: typing.Optional[Address] = OMIT,
        allow_amount_higher: typing.Optional[bool] = OMIT,
        allow_amount_lower: typing.Optional[bool] = OMIT,
        amount_inquired: typing.Optional[Amount] = OMIT,
        amount_responded: typing.Optional[Amount] = OMIT,
        attachment: typing.Optional[typing.Sequence[BunqId]] = OMIT,
        batch_id: typing.Optional[int] = OMIT,
        bunqme_share_url: typing.Optional[str] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        created: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        event_id: typing.Optional[int] = OMIT,
        geolocation: typing.Optional[Geolocation] = OMIT,
        id: typing.Optional[int] = OMIT,
        merchant_reference: typing.Optional[str] = OMIT,
        minimum_age: typing.Optional[int] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        require_address: typing.Optional[str] = OMIT,
        scheduled_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        time_expiry: typing.Optional[str] = OMIT,
        time_responded: typing.Optional[str] = OMIT,
        updated: typing.Optional[str] = OMIT,
        user_alias_created: typing.Optional[LabelUser] = OMIT,
        user_alias_revoked: typing.Optional[LabelUser] = OMIT,
        want_tip: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryUpdate:
        """
        Revoke a request for payment, by updating the status to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        item_id : int


        allow_bunqme : bool
            Whether or not sending a bunq.me request is allowed.

        address_billing : typing.Optional[Address]
            The billing address provided by the accepting user if an address was requested.

        address_shipping : typing.Optional[Address]
            The shipping address provided by the accepting user if an address was requested.

        allow_amount_higher : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a higher amount than requested. Defaults to false.

        allow_amount_lower : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can choose to accept with a lower amount than requested. Defaults to false.

        amount_inquired : typing.Optional[Amount]
            The requested amount.

        amount_responded : typing.Optional[Amount]
            The responded amount.

        attachment : typing.Optional[typing.Sequence[BunqId]]
            The attachments attached to the payment.

        batch_id : typing.Optional[int]
            The id of the batch if the request was part of a batch.

        bunqme_share_url : typing.Optional[str]
            The url that points to the bunq.me request.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.

        created : typing.Optional[str]
            The timestamp of the payment request's creation.

        description : typing.Optional[str]
            The description of the inquiry.

        event_id : typing.Optional[int]
            The ID of the associated event if the request was made using 'split the bill'.

        geolocation : typing.Optional[Geolocation]
            The geolocation where the payment was done.

        id : typing.Optional[int]
            The id of the created RequestInquiry.

        merchant_reference : typing.Optional[str]
            The client's custom reference that was attached to the request and the mutation.

        minimum_age : typing.Optional[int]
            The minimum age the user accepting the RequestInquiry must have.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account the request response applies to.

        redirect_url : typing.Optional[str]
            The URL which the user is sent to after accepting or rejecting the Request.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        require_address : typing.Optional[str]
            Whether or not an address must be provided on accept.

        scheduled_id : typing.Optional[int]
            The id of the scheduled job if the request was scheduled.

        status : typing.Optional[str]
            The status of the request.

        time_expiry : typing.Optional[str]
            The timestamp of when the payment request expired.

        time_responded : typing.Optional[str]
            The timestamp of when the payment request was responded to.

        updated : typing.Optional[str]
            The timestamp of the payment request's last update.

        user_alias_created : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        user_alias_revoked : typing.Optional[LabelUser]
            The label that's displayed to the counterparty with the mutation. Includes user.

        want_tip : typing.Optional[bool]
            [DEPRECATED] Whether or not the accepting user can give an extra tip on top of the requested Amount. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryUpdate
            RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative features that bunq offers. To request payment from another bunq account a new Request Inquiry is created. As with payments you can add attachments to a RFP. Requests for Payment are the foundation for a number of consumer features like 'Split the bill' and 'Request forwarding'. We invite you to invent your own based on the bunq api!

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
            await client.request_inquiry.update_request_inquiry_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
                item_id=1,
                allow_bunqme=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_request_inquiry_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            item_id,
            allow_bunqme=allow_bunqme,
            address_billing=address_billing,
            address_shipping=address_shipping,
            allow_amount_higher=allow_amount_higher,
            allow_amount_lower=allow_amount_lower,
            amount_inquired=amount_inquired,
            amount_responded=amount_responded,
            attachment=attachment,
            batch_id=batch_id,
            bunqme_share_url=bunqme_share_url,
            counterparty_alias=counterparty_alias,
            created=created,
            description=description,
            event_id=event_id,
            geolocation=geolocation,
            id=id,
            merchant_reference=merchant_reference,
            minimum_age=minimum_age,
            monetary_account_id=monetary_account_id,
            redirect_url=redirect_url,
            reference_split_the_bill=reference_split_the_bill,
            require_address=require_address,
            scheduled_id=scheduled_id,
            status=status,
            time_expiry=time_expiry,
            time_responded=time_responded,
            updated=updated,
            user_alias_created=user_alias_created,
            user_alias_revoked=user_alias_revoked,
            want_tip=want_tip,
            request_options=request_options,
        )
        return _response.data
