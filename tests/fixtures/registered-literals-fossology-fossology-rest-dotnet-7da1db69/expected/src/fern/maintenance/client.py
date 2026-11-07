

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.info import Info
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient
from .types.create_maintenance_options_item import CreateMaintenanceOptionsItem


OMIT = typing.cast(typing.Any, ...)


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    def initiate_maintenance(
        self,
        *,
        options: typing.Optional[typing.Sequence[CreateMaintenanceOptionsItem]] = OMIT,
        logs_date: typing.Optional[str] = OMIT,
        gold_date: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Perform maintenance operations corresponding to the user options.

        Parameters
        ----------
        options : typing.Optional[typing.Sequence[CreateMaintenanceOptionsItem]]
            options list

        logs_date : typing.Optional[str]
            Date from which to remove older gold files from repository.

        gold_date : typing.Optional[str]
            Date from which to remove older log files from repository.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Maintenance Initiated Successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.maintenance.initiate_maintenance()
        """
        _response = self._raw_client.initiate_maintenance(
            options=options, logs_date=logs_date, gold_date=gold_date, request_options=request_options
        )
        return _response.data


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    async def initiate_maintenance(
        self,
        *,
        options: typing.Optional[typing.Sequence[CreateMaintenanceOptionsItem]] = OMIT,
        logs_date: typing.Optional[str] = OMIT,
        gold_date: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Perform maintenance operations corresponding to the user options.

        Parameters
        ----------
        options : typing.Optional[typing.Sequence[CreateMaintenanceOptionsItem]]
            options list

        logs_date : typing.Optional[str]
            Date from which to remove older gold files from repository.

        gold_date : typing.Optional[str]
            Date from which to remove older log files from repository.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Maintenance Initiated Successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.maintenance.initiate_maintenance()


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_maintenance(
            options=options, logs_date=logs_date, gold_date=gold_date, request_options=request_options
        )
        return _response.data
