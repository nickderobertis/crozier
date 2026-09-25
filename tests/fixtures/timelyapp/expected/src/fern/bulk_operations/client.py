

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1bulk_hours_import_create_item import V1BulkHoursImportCreateItem
from ..types.v1bulk_hours_import_update_item import V1BulkHoursImportUpdateItem
from ..types.v1bulk_import_response import V1BulkImportResponse
from .raw_client import AsyncRawBulkOperationsClient, RawBulkOperationsClient


OMIT = typing.cast(typing.Any, ...)


class BulkOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBulkOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBulkOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBulkOperationsClient
        """
        return self._raw_client

    def bulk_import_hours(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1BulkImportResponse:
        """
        Create, update, or delete multiple time entries in a single request. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BulkImportResponse
            Time entries imported successfully (synchronous)

        Examples
        --------
        from fern import FernApi, V1BulkHoursImportCreateItem

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bulk_operations.bulk_import_hours(
            account_id=1,
            create=[
                V1BulkHoursImportCreateItem(
                    user_id=1,
                    project_id=1,
                    hours=3,
                    minutes=30,
                    seconds=0,
                    day="2024-01-15",
                    note="Test entry",
                )
            ],
        )
        """
        _response = self._raw_client.bulk_import_hours(
            account_id, create=create, update=update, delete=delete, request_options=request_options
        )
        return _response.data

    def bulk_import_events(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1BulkImportResponse:
        """
        Create, update, or delete multiple events in a single request. Events are the same as time entries - this is an alias endpoint. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BulkImportResponse
            Events imported successfully (synchronous)

        Examples
        --------
        from fern import FernApi, V1BulkHoursImportCreateItem

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bulk_operations.bulk_import_events(
            account_id=1,
            create=[
                V1BulkHoursImportCreateItem(
                    user_id=1,
                    project_id=1,
                    hours=2,
                    minutes=0,
                    seconds=0,
                    day="2024-01-15",
                    note="Test event",
                )
            ],
        )
        """
        _response = self._raw_client.bulk_import_events(
            account_id, create=create, update=update, delete=delete, request_options=request_options
        )
        return _response.data


class AsyncBulkOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBulkOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBulkOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBulkOperationsClient
        """
        return self._raw_client

    async def bulk_import_hours(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1BulkImportResponse:
        """
        Create, update, or delete multiple time entries in a single request. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BulkImportResponse
            Time entries imported successfully (synchronous)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1BulkHoursImportCreateItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_operations.bulk_import_hours(
                account_id=1,
                create=[
                    V1BulkHoursImportCreateItem(
                        user_id=1,
                        project_id=1,
                        hours=3,
                        minutes=30,
                        seconds=0,
                        day="2024-01-15",
                        note="Test entry",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_import_hours(
            account_id, create=create, update=update, delete=delete, request_options=request_options
        )
        return _response.data

    async def bulk_import_events(
        self,
        account_id: int,
        *,
        create: typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]] = OMIT,
        update: typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]] = OMIT,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1BulkImportResponse:
        """
        Create, update, or delete multiple events in a single request. Events are the same as time entries - this is an alias endpoint. For large operations (100+ records), the operation runs asynchronously and returns a job ID.

        Parameters
        ----------
        account_id : int
            Workspace id

        create : typing.Optional[typing.Sequence[V1BulkHoursImportCreateItem]]
            Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.

        update : typing.Optional[typing.Sequence[V1BulkHoursImportUpdateItem]]
            Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.

        delete : typing.Optional[typing.Sequence[int]]
            Array of time entry IDs to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BulkImportResponse
            Events imported successfully (synchronous)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, V1BulkHoursImportCreateItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_operations.bulk_import_events(
                account_id=1,
                create=[
                    V1BulkHoursImportCreateItem(
                        user_id=1,
                        project_id=1,
                        hours=2,
                        minutes=0,
                        seconds=0,
                        day="2024-01-15",
                        note="Test event",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_import_events(
            account_id, create=create, update=update, delete=delete, request_options=request_options
        )
        return _response.data
