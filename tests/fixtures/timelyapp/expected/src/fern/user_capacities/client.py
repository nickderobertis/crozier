

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1user_capacity import V1UserCapacity
from .raw_client import AsyncRawUserCapacitiesClient, RawUserCapacitiesClient
from .types.list_users_capacities_response_item import ListUsersCapacitiesResponseItem


class UserCapacitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserCapacitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserCapacitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserCapacitiesClient
        """
        return self._raw_client

    def list_user_capacities(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1UserCapacity]:
        """
        Retrieve capacity configurations for a specific user. Capacities define a user's working hours, working days, and daily/weekly hour limits.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1UserCapacity]
            User's capacities retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_capacities.list_user_capacities(
            account_id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.list_user_capacities(account_id, user_id, request_options=request_options)
        return _response.data

    def list_users_capacities(
        self,
        account_id: int,
        *,
        user_ids: typing.Optional[str] = None,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListUsersCapacitiesResponseItem]:
        """
        Retrieve capacity configurations for multiple users in the account. Supports filtering by user IDs and date range.

        Parameters
        ----------
        account_id : int
            Account ID

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        since : typing.Optional[dt.date]
            Fetch capacities after this date (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            Fetch capacities before this date (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListUsersCapacitiesResponseItem]
            Users capacities retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_capacities.list_users_capacities(
            account_id=1,
        )
        """
        _response = self._raw_client.list_users_capacities(
            account_id, user_ids=user_ids, since=since, until=until, request_options=request_options
        )
        return _response.data


class AsyncUserCapacitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserCapacitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserCapacitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserCapacitiesClient
        """
        return self._raw_client

    async def list_user_capacities(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1UserCapacity]:
        """
        Retrieve capacity configurations for a specific user. Capacities define a user's working hours, working days, and daily/weekly hour limits.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1UserCapacity]
            User's capacities retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_capacities.list_user_capacities(
                account_id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_capacities(account_id, user_id, request_options=request_options)
        return _response.data

    async def list_users_capacities(
        self,
        account_id: int,
        *,
        user_ids: typing.Optional[str] = None,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListUsersCapacitiesResponseItem]:
        """
        Retrieve capacity configurations for multiple users in the account. Supports filtering by user IDs and date range.

        Parameters
        ----------
        account_id : int
            Account ID

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        since : typing.Optional[dt.date]
            Fetch capacities after this date (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            Fetch capacities before this date (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListUsersCapacitiesResponseItem]
            Users capacities retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_capacities.list_users_capacities(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users_capacities(
            account_id, user_ids=user_ids, since=since, until=until, request_options=request_options
        )
        return _response.data
