

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_response_of_change_log_entry import PaginatedResponseOfChangeLogEntry
from .raw_client import AsyncRawAuditingClient, RawAuditingClient


class AuditingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuditingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuditingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuditingClient
        """
        return self._raw_client

    def list_organization_change_log(
        self,
        organization_id: str,
        *,
        message_mime_type: typing.Optional[str] = None,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfChangeLogEntry:
        """
        Listing change log entries of the specified organization id.

        Parameters
        ----------
        organization_id : str
            The namespace identifying the organization whose change log entries are to be listed

        message_mime_type : typing.Optional[str]
            The Mime-type for the message format that should be returned. e.g. 'text/plain' or 'text/mustache'

        from_date : typing.Optional[dt.datetime]
            From date time as UTC Date-Time format

        to_date : typing.Optional[dt.datetime]
            To date time as UTC Date-Time format

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfChangeLogEntry
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.auditing.list_organization_change_log(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.list_organization_change_log(
            organization_id,
            message_mime_type=message_mime_type,
            from_date=from_date,
            to_date=to_date,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data


class AsyncAuditingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuditingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuditingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuditingClient
        """
        return self._raw_client

    async def list_organization_change_log(
        self,
        organization_id: str,
        *,
        message_mime_type: typing.Optional[str] = None,
        from_date: typing.Optional[dt.datetime] = None,
        to_date: typing.Optional[dt.datetime] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfChangeLogEntry:
        """
        Listing change log entries of the specified organization id.

        Parameters
        ----------
        organization_id : str
            The namespace identifying the organization whose change log entries are to be listed

        message_mime_type : typing.Optional[str]
            The Mime-type for the message format that should be returned. e.g. 'text/plain' or 'text/mustache'

        from_date : typing.Optional[dt.datetime]
            From date time as UTC Date-Time format

        to_date : typing.Optional[dt.datetime]
            To date time as UTC Date-Time format

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfChangeLogEntry
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.auditing.list_organization_change_log(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_organization_change_log(
            organization_id,
            message_mime_type=message_mime_type,
            from_date=from_date,
            to_date=to_date,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data
