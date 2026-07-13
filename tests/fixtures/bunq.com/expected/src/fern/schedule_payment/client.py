

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schedule import Schedule
from ..types.schedule_payment_create import SchedulePaymentCreate
from ..types.schedule_payment_delete import SchedulePaymentDelete
from ..types.schedule_payment_entry import SchedulePaymentEntry
from ..types.schedule_payment_listing import SchedulePaymentListing
from ..types.schedule_payment_read import SchedulePaymentRead
from ..types.schedule_payment_update import SchedulePaymentUpdate
from .raw_client import AsyncRawSchedulePaymentClient, RawSchedulePaymentClient


OMIT = typing.cast(typing.Any, ...)


class SchedulePaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchedulePaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchedulePaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchedulePaymentClient
        """
        return self._raw_client

    def list_all_schedule_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SchedulePaymentListing]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchedulePaymentListing]
            Endpoint for schedule payments.

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
        client.schedule_payment.list_all_schedule_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentCreate:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentCreate
            Endpoint for schedule payments.

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
        client.schedule_payment.create_schedule_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.create_schedule_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            payment=payment,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def read_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentRead:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentRead
            Endpoint for schedule payments.

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
        client.schedule_payment.read_schedule_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentUpdate:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentUpdate
            Endpoint for schedule payments.

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
        client.schedule_payment.update_schedule_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_schedule_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            payment=payment,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def delete_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentDelete:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentDelete
            Endpoint for schedule payments.

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
        client.schedule_payment.delete_schedule_payment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncSchedulePaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchedulePaymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchedulePaymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchedulePaymentClient
        """
        return self._raw_client

    async def list_all_schedule_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SchedulePaymentListing]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchedulePaymentListing]
            Endpoint for schedule payments.

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
            await client.schedule_payment.list_all_schedule_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentCreate:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentCreate
            Endpoint for schedule payments.

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
            await client.schedule_payment.create_schedule_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_schedule_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            payment=payment,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def read_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentRead:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentRead
            Endpoint for schedule payments.

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
            await client.schedule_payment.read_schedule_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentUpdate:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentUpdate
            Endpoint for schedule payments.

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
            await client.schedule_payment.update_schedule_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_schedule_payment_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            payment=payment,
            schedule=schedule,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def delete_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePaymentDelete:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePaymentDelete
            Endpoint for schedule payments.

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
            await client.schedule_payment.delete_schedule_payment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schedule_payment_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
