

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.error import Error
from ..types.request_inquiry_reference import RequestInquiryReference
from ..types.schedule_anchor_object import ScheduleAnchorObject
from ..types.schedule_instance_anchor_object import ScheduleInstanceAnchorObject
from ..types.schedule_instance_listing import ScheduleInstanceListing
from ..types.schedule_instance_read import ScheduleInstanceRead
from ..types.schedule_instance_update import ScheduleInstanceUpdate
from .raw_client import AsyncRawScheduleInstanceClient, RawScheduleInstanceClient


OMIT = typing.cast(typing.Any, ...)


class ScheduleInstanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScheduleInstanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScheduleInstanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScheduleInstanceClient
        """
        return self._raw_client

    def list_all_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ScheduleInstanceListing]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleInstanceListing]
            view for reading, updating and listing the scheduled instance.

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
        client.schedule_instance.list_all_schedule_instance_for_user_monetary_account_schedule(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
        )
        """
        _response = self._raw_client.list_all_schedule_instance_for_user_monetary_account_schedule(
            user_id, monetary_account_id, schedule_id, request_options=request_options
        )
        return _response.data

    def read_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleInstanceRead:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleInstanceRead
            view for reading, updating and listing the scheduled instance.

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
        client.schedule_instance.read_schedule_instance_for_user_monetary_account_schedule(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_schedule_instance_for_user_monetary_account_schedule(
            user_id, monetary_account_id, schedule_id, item_id, request_options=request_options
        )
        return _response.data

    def update_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        error_message: typing.Optional[typing.Sequence[Error]] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        result_object: typing.Optional[ScheduleInstanceAnchorObject] = OMIT,
        scheduled_object: typing.Optional[ScheduleAnchorObject] = OMIT,
        state: typing.Optional[str] = OMIT,
        time_end: typing.Optional[str] = OMIT,
        time_start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleInstanceUpdate:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        error_message : typing.Optional[typing.Sequence[Error]]
            The message when the scheduled instance has run and failed due to user error.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        result_object : typing.Optional[ScheduleInstanceAnchorObject]
            The result object of this schedule instance. (Payment, PaymentBatch)

        scheduled_object : typing.Optional[ScheduleAnchorObject]
            The scheduled object. (Payment, PaymentBatch)

        state : typing.Optional[str]
            The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)

        time_end : typing.Optional[str]
            The schedule end time (UTC).

        time_start : typing.Optional[str]
            The schedule start time (UTC).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleInstanceUpdate
            view for reading, updating and listing the scheduled instance.

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
        client.schedule_instance.update_schedule_instance_for_user_monetary_account_schedule(
            user_id=1,
            monetary_account_id=1,
            schedule_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_schedule_instance_for_user_monetary_account_schedule(
            user_id,
            monetary_account_id,
            schedule_id,
            item_id,
            error_message=error_message,
            request_reference_split_the_bill=request_reference_split_the_bill,
            result_object=result_object,
            scheduled_object=scheduled_object,
            state=state,
            time_end=time_end,
            time_start=time_start,
            request_options=request_options,
        )
        return _response.data


class AsyncScheduleInstanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScheduleInstanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScheduleInstanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScheduleInstanceClient
        """
        return self._raw_client

    async def list_all_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ScheduleInstanceListing]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleInstanceListing]
            view for reading, updating and listing the scheduled instance.

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
            await client.schedule_instance.list_all_schedule_instance_for_user_monetary_account_schedule(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_schedule_instance_for_user_monetary_account_schedule(
            user_id, monetary_account_id, schedule_id, request_options=request_options
        )
        return _response.data

    async def read_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleInstanceRead:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleInstanceRead
            view for reading, updating and listing the scheduled instance.

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
            await client.schedule_instance.read_schedule_instance_for_user_monetary_account_schedule(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_schedule_instance_for_user_monetary_account_schedule(
            user_id, monetary_account_id, schedule_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        error_message: typing.Optional[typing.Sequence[Error]] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        result_object: typing.Optional[ScheduleInstanceAnchorObject] = OMIT,
        scheduled_object: typing.Optional[ScheduleAnchorObject] = OMIT,
        state: typing.Optional[str] = OMIT,
        time_end: typing.Optional[str] = OMIT,
        time_start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleInstanceUpdate:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        error_message : typing.Optional[typing.Sequence[Error]]
            The message when the scheduled instance has run and failed due to user error.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        result_object : typing.Optional[ScheduleInstanceAnchorObject]
            The result object of this schedule instance. (Payment, PaymentBatch)

        scheduled_object : typing.Optional[ScheduleAnchorObject]
            The scheduled object. (Payment, PaymentBatch)

        state : typing.Optional[str]
            The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)

        time_end : typing.Optional[str]
            The schedule end time (UTC).

        time_start : typing.Optional[str]
            The schedule start time (UTC).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleInstanceUpdate
            view for reading, updating and listing the scheduled instance.

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
            await client.schedule_instance.update_schedule_instance_for_user_monetary_account_schedule(
                user_id=1,
                monetary_account_id=1,
                schedule_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_schedule_instance_for_user_monetary_account_schedule(
            user_id,
            monetary_account_id,
            schedule_id,
            item_id,
            error_message=error_message,
            request_reference_split_the_bill=request_reference_split_the_bill,
            result_object=result_object,
            scheduled_object=scheduled_object,
            state=state,
            time_end=time_end,
            time_start=time_start,
            request_options=request_options,
        )
        return _response.data
