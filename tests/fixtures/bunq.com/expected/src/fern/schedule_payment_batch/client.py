

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schedule import Schedule
from ..types.schedule_payment_batch_create import SchedulePaymentBatchCreate
from ..types.schedule_payment_batch_delete import SchedulePaymentBatchDelete
from ..types.schedule_payment_batch_read import SchedulePaymentBatchRead
from ..types.schedule_payment_batch_update import SchedulePaymentBatchUpdate
from ..types.schedule_payment_entry import SchedulePaymentEntry
from .raw_client import AsyncRawSchedulePaymentBatchClient, RawSchedulePaymentBatchClient


OMIT = typing.cast(typing.Any, ...)


class SchedulePaymentBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchedulePaymentBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchedulePaymentBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchedulePaymentBatchClient
        """
        return self._raw_client

    def create_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchCreate:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchCreate
            Endpoint for schedule payment batches.

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
        client.schedule_payment_batch.create_schedule_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.create_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, payments=payments, schedule=schedule, request_options=request_options
        )
        return _response.data

    def read_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchRead:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchRead
            Endpoint for schedule payment batches.

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
        client.schedule_payment_batch.read_schedule_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchUpdate:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchUpdate
            Endpoint for schedule payment batches.

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
        client.schedule_payment_batch.update_schedule_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, payments=payments, schedule=schedule, request_options=request_options
        )
        return _response.data

    def delete_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchDelete:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchDelete
            Endpoint for schedule payment batches.

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
        client.schedule_payment_batch.delete_schedule_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncSchedulePaymentBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchedulePaymentBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchedulePaymentBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchedulePaymentBatchClient
        """
        return self._raw_client

    async def create_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchCreate:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchCreate
            Endpoint for schedule payment batches.

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
            await client.schedule_payment_batch.create_schedule_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, payments=payments, schedule=schedule, request_options=request_options
        )
        return _response.data

    async def read_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchRead:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchRead
            Endpoint for schedule payment batches.

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
            await client.schedule_payment_batch.read_schedule_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchUpdate:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchUpdate
            Endpoint for schedule payment batches.

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
            await client.schedule_payment_batch.update_schedule_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, payments=payments, schedule=schedule, request_options=request_options
        )
        return _response.data

    async def delete_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentBatchDelete:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentBatchDelete
            Endpoint for schedule payment batches.

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
            await client.schedule_payment_batch.delete_schedule_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schedule_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
