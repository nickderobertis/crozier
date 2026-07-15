

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_journal_entry_response import CreateJournalEntryResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.currency_rate import CurrencyRate
from ..types.delete_journal_entry_response import DeleteJournalEntryResponse
from ..types.get_journal_entries_response import GetJournalEntriesResponse
from ..types.get_journal_entry_response import GetJournalEntryResponse
from ..types.id import Id
from ..types.journal_entry_line_item import JournalEntryLineItem
from ..types.pass_through_query import PassThroughQuery
from ..types.row_version import RowVersion
from ..types.update_journal_entry_response import UpdateJournalEntryResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawJournalEntriesClient, RawJournalEntriesClient


OMIT = typing.cast(typing.Any, ...)


class JournalEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJournalEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJournalEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJournalEntriesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJournalEntriesResponse:
        """
        List Journal Entries

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJournalEntriesResponse
            JournalEntry

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.journal_entries.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        id: typing.Optional[Id] = OMIT,
        journal_symbol: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[JournalEntryLineItem]] = OMIT,
        memo: typing.Optional[str] = OMIT,
        posted_at: typing.Optional[dt.datetime] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateJournalEntryResponse:
        """
        Create Journal Entry

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        id : typing.Optional[Id]

        journal_symbol : typing.Optional[str]
            Journal symbol of the entry. For example IND for indirect costs

        line_items : typing.Optional[typing.Sequence[JournalEntryLineItem]]
            Requires a minimum of 2 line items that sum to 0

        memo : typing.Optional[str]
            Reference for the journal entry.

        posted_at : typing.Optional[dt.datetime]
            This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.

        row_version : typing.Optional[RowVersion]

        title : typing.Optional[str]
            Journal entry title

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateJournalEntryResponse
            JournalEntries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.journal_entries.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            id=id,
            journal_symbol=journal_symbol,
            line_items=line_items,
            memo=memo,
            posted_at=posted_at,
            row_version=row_version,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJournalEntryResponse:
        """
        Get Journal Entry

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJournalEntryResponse
            JournalEntries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.journal_entries.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteJournalEntryResponse:
        """
        Delete Journal Entry

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteJournalEntryResponse
            JournalEntries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.journal_entries.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        id: typing.Optional[Id] = OMIT,
        journal_symbol: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[JournalEntryLineItem]] = OMIT,
        memo: typing.Optional[str] = OMIT,
        posted_at: typing.Optional[dt.datetime] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateJournalEntryResponse:
        """
        Update Journal Entry

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        id : typing.Optional[Id]

        journal_symbol : typing.Optional[str]
            Journal symbol of the entry. For example IND for indirect costs

        line_items : typing.Optional[typing.Sequence[JournalEntryLineItem]]
            Requires a minimum of 2 line items that sum to 0

        memo : typing.Optional[str]
            Reference for the journal entry.

        posted_at : typing.Optional[dt.datetime]
            This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.

        row_version : typing.Optional[RowVersion]

        title : typing.Optional[str]
            Journal entry title

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateJournalEntryResponse
            JournalEntries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.journal_entries.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            id=id,
            journal_symbol=journal_symbol,
            line_items=line_items,
            memo=memo,
            posted_at=posted_at,
            row_version=row_version,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncJournalEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJournalEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJournalEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJournalEntriesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJournalEntriesResponse:
        """
        List Journal Entries

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJournalEntriesResponse
            JournalEntry

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.journal_entries.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        id: typing.Optional[Id] = OMIT,
        journal_symbol: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[JournalEntryLineItem]] = OMIT,
        memo: typing.Optional[str] = OMIT,
        posted_at: typing.Optional[dt.datetime] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateJournalEntryResponse:
        """
        Create Journal Entry

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        id : typing.Optional[Id]

        journal_symbol : typing.Optional[str]
            Journal symbol of the entry. For example IND for indirect costs

        line_items : typing.Optional[typing.Sequence[JournalEntryLineItem]]
            Requires a minimum of 2 line items that sum to 0

        memo : typing.Optional[str]
            Reference for the journal entry.

        posted_at : typing.Optional[dt.datetime]
            This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.

        row_version : typing.Optional[RowVersion]

        title : typing.Optional[str]
            Journal entry title

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateJournalEntryResponse
            JournalEntries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.journal_entries.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            id=id,
            journal_symbol=journal_symbol,
            line_items=line_items,
            memo=memo,
            posted_at=posted_at,
            row_version=row_version,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJournalEntryResponse:
        """
        Get Journal Entry

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJournalEntryResponse
            JournalEntries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.journal_entries.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteJournalEntryResponse:
        """
        Delete Journal Entry

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteJournalEntryResponse
            JournalEntries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.journal_entries.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        currency_rate: typing.Optional[CurrencyRate] = OMIT,
        id: typing.Optional[Id] = OMIT,
        journal_symbol: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[JournalEntryLineItem]] = OMIT,
        memo: typing.Optional[str] = OMIT,
        posted_at: typing.Optional[dt.datetime] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateJournalEntryResponse:
        """
        Update Journal Entry

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        currency_rate : typing.Optional[CurrencyRate]

        id : typing.Optional[Id]

        journal_symbol : typing.Optional[str]
            Journal symbol of the entry. For example IND for indirect costs

        line_items : typing.Optional[typing.Sequence[JournalEntryLineItem]]
            Requires a minimum of 2 line items that sum to 0

        memo : typing.Optional[str]
            Reference for the journal entry.

        posted_at : typing.Optional[dt.datetime]
            This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.

        row_version : typing.Optional[RowVersion]

        title : typing.Optional[str]
            Journal entry title

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateJournalEntryResponse
            JournalEntries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.journal_entries.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            currency_rate=currency_rate,
            id=id,
            journal_symbol=journal_symbol,
            line_items=line_items,
            memo=memo,
            posted_at=posted_at,
            row_version=row_version,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
