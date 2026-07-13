

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schedule_listing import ScheduleListing
from ..types.schedule_read import ScheduleRead
from ..types.schedule_user_listing import ScheduleUserListing
from .raw_client import AsyncRawScheduleClient, RawScheduleClient


class ScheduleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScheduleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScheduleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScheduleClient
        """
        return self._raw_client

    def list_all_schedule_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScheduleListing]:
        """
        Get a collection of scheduled definition for a given monetary account. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleListing]
            view for reading the scheduled definitions.

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
        client.schedule.list_all_schedule_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_schedule_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def read_schedule_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleRead:
        """
        Get a specific schedule definition for a given monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleRead
            view for reading the scheduled definitions.

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
        client.schedule.read_schedule_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_schedule_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_schedule_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScheduleUserListing]:
        """
        Get a collection of scheduled definition for all accessible monetary accounts of the user. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleUserListing]
            view for reading the scheduled definitions.

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
        client.schedule.list_all_schedule_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_schedule_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncScheduleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScheduleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScheduleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScheduleClient
        """
        return self._raw_client

    async def list_all_schedule_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScheduleListing]:
        """
        Get a collection of scheduled definition for a given monetary account. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleListing]
            view for reading the scheduled definitions.

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
            await client.schedule.list_all_schedule_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_schedule_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def read_schedule_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleRead:
        """
        Get a specific schedule definition for a given monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleRead
            view for reading the scheduled definitions.

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
            await client.schedule.read_schedule_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_schedule_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_schedule_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScheduleUserListing]:
        """
        Get a collection of scheduled definition for all accessible monetary accounts of the user. You can add the parameter type to filter the response. When type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is provided only schedule definition object that relate to these definitions are returned.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScheduleUserListing]
            view for reading the scheduled definitions.

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
            await client.schedule.list_all_schedule_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_schedule_for_user(user_id, request_options=request_options)
        return _response.data
