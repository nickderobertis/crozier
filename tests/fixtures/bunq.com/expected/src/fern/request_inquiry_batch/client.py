

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.request_inquiry import RequestInquiry
from ..types.request_inquiry_batch_create import RequestInquiryBatchCreate
from ..types.request_inquiry_batch_listing import RequestInquiryBatchListing
from ..types.request_inquiry_batch_read import RequestInquiryBatchRead
from ..types.request_inquiry_batch_update import RequestInquiryBatchUpdate
from ..types.request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject
from .raw_client import AsyncRawRequestInquiryBatchClient, RawRequestInquiryBatchClient


OMIT = typing.cast(typing.Any, ...)


class RequestInquiryBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRequestInquiryBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRequestInquiryBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRequestInquiryBatchClient
        """
        return self._raw_client

    def list_all_request_inquiry_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestInquiryBatchListing]:
        """
        Return all the request batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestInquiryBatchListing]
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
        client.request_inquiry_batch.list_all_request_inquiry_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_request_inquiry_batch_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchCreate:
        """
        Create a request batch by sending an array of single request objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchCreate
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
        client.request_inquiry_batch.create_request_inquiry_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.create_request_inquiry_batch_for_user_monetary_account(
            user_id,
            monetary_account_id,
            event_id=event_id,
            reference_split_the_bill=reference_split_the_bill,
            request_inquiries=request_inquiries,
            status=status,
            total_amount_inquired=total_amount_inquired,
            request_options=request_options,
        )
        return _response.data

    def read_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchRead:
        """
        Return the details of a specific request batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchRead
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
        client.request_inquiry_batch.read_request_inquiry_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_request_inquiry_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchUpdate:
        """
        Revoke a request batch. The status of all the requests will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchUpdate
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
        client.request_inquiry_batch.update_request_inquiry_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_request_inquiry_batch_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            event_id=event_id,
            reference_split_the_bill=reference_split_the_bill,
            request_inquiries=request_inquiries,
            status=status,
            total_amount_inquired=total_amount_inquired,
            request_options=request_options,
        )
        return _response.data


class AsyncRequestInquiryBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRequestInquiryBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRequestInquiryBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRequestInquiryBatchClient
        """
        return self._raw_client

    async def list_all_request_inquiry_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RequestInquiryBatchListing]:
        """
        Return all the request batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RequestInquiryBatchListing]
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
            await client.request_inquiry_batch.list_all_request_inquiry_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_request_inquiry_batch_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchCreate:
        """
        Create a request batch by sending an array of single request objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchCreate
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
            await client.request_inquiry_batch.create_request_inquiry_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_request_inquiry_batch_for_user_monetary_account(
            user_id,
            monetary_account_id,
            event_id=event_id,
            reference_split_the_bill=reference_split_the_bill,
            request_inquiries=request_inquiries,
            status=status,
            total_amount_inquired=total_amount_inquired,
            request_options=request_options,
        )
        return _response.data

    async def read_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchRead:
        """
        Return the details of a specific request batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchRead
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
            await client.request_inquiry_batch.read_request_inquiry_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_request_inquiry_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestInquiryBatchUpdate:
        """
        Revoke a request batch. The status of all the requests will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInquiryBatchUpdate
            Create a batch of requests for payment, or show the request batches of a monetary account.

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
            await client.request_inquiry_batch.update_request_inquiry_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_request_inquiry_batch_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            event_id=event_id,
            reference_split_the_bill=reference_split_the_bill,
            request_inquiries=request_inquiries,
            status=status,
            total_amount_inquired=total_amount_inquired,
            request_options=request_options,
        )
        return _response.data
