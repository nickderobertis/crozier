

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection_files_paginated_list import ConnectionFilesPaginatedList
from .raw_client import AsyncRawLabAutomationClient, RawLabAutomationClient
from .types.list_connect_files_request_data_type import ListConnectFilesRequestDataType


class LabAutomationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLabAutomationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLabAutomationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLabAutomationClient
        """
        return self._raw_client

    def list_connect_files(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        filename_includes: typing.Optional[str] = None,
        connection_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        connection_schema_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_type: typing.Optional[ListConnectFilesRequestDataType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionFilesPaginatedList:
        """
        List Benchling Connect files

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        filename_includes : typing.Optional[str]
            Name substring of a file. Restricts results to those with names that include the provided substring.

        connection_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection IDs. Restricts results to those created by the given connections.

        connection_schema_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection schema IDs. Restricts results to those created by connections with the given connection schemas.

        data_type : typing.Optional[ListConnectFilesRequestDataType]
            File data type. Restricts results to those with the specified data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionFilesPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.lab_automation.list_connect_files()
        """
        _response = self._raw_client.list_connect_files(
            page_size=page_size,
            next_token=next_token,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_gte=created_at_gte,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            filename_includes=filename_includes,
            connection_ids=connection_ids,
            connection_schema_ids=connection_schema_ids,
            data_type=data_type,
            request_options=request_options,
        )
        return _response.data


class AsyncLabAutomationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLabAutomationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLabAutomationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLabAutomationClient
        """
        return self._raw_client

    async def list_connect_files(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        filename_includes: typing.Optional[str] = None,
        connection_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        connection_schema_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_type: typing.Optional[ListConnectFilesRequestDataType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionFilesPaginatedList:
        """
        List Benchling Connect files

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        filename_includes : typing.Optional[str]
            Name substring of a file. Restricts results to those with names that include the provided substring.

        connection_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection IDs. Restricts results to those created by the given connections.

        connection_schema_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection schema IDs. Restricts results to those created by connections with the given connection schemas.

        data_type : typing.Optional[ListConnectFilesRequestDataType]
            File data type. Restricts results to those with the specified data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionFilesPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.lab_automation.list_connect_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connect_files(
            page_size=page_size,
            next_token=next_token,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_gte=created_at_gte,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            filename_includes=filename_includes,
            connection_ids=connection_ids,
            connection_schema_ids=connection_schema_ids,
            data_type=data_type,
            request_options=request_options,
        )
        return _response.data
