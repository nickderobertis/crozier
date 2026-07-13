

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_statement_create import ExportStatementCreate
from ..types.export_statement_delete import ExportStatementDelete
from ..types.export_statement_listing import ExportStatementListing
from ..types.export_statement_read import ExportStatementRead
from .raw_client import AsyncRawCustomerStatementClient, RawCustomerStatementClient


OMIT = typing.cast(typing.Any, ...)


class CustomerStatementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerStatementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerStatementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerStatementClient
        """
        return self._raw_client

    def list_all_customer_statement_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementListing]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementListing]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
        client.customer_statement.list_all_customer_statement_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        date_end: str,
        date_start: str,
        statement_format: str,
        include_attachment: typing.Optional[bool] = OMIT,
        regional_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCreate:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        statement_format : str
            The format type of statement. Allowed values: MT940, CSV, PDF.

        include_attachment : typing.Optional[bool]
            Only for PDF exports. Includes attachments to mutations in the export, such as scanned receipts.

        regional_format : typing.Optional[str]
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCreate
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
        client.customer_statement.create_customer_statement_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            date_end="date_end",
            date_start="date_start",
            statement_format="statement_format",
        )
        """
        _response = self._raw_client.create_customer_statement_for_user_monetary_account(
            user_id,
            monetary_account_id,
            date_end=date_end,
            date_start=date_start,
            statement_format=statement_format,
            include_attachment=include_attachment,
            regional_format=regional_format,
            request_options=request_options,
        )
        return _response.data

    def read_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementRead:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementRead
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
        client.customer_statement.read_customer_statement_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def delete_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementDelete:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementDelete
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
        client.customer_statement.delete_customer_statement_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncCustomerStatementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerStatementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerStatementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerStatementClient
        """
        return self._raw_client

    async def list_all_customer_statement_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementListing]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementListing]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
            await client.customer_statement.list_all_customer_statement_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        date_end: str,
        date_start: str,
        statement_format: str,
        include_attachment: typing.Optional[bool] = OMIT,
        regional_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCreate:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        statement_format : str
            The format type of statement. Allowed values: MT940, CSV, PDF.

        include_attachment : typing.Optional[bool]
            Only for PDF exports. Includes attachments to mutations in the export, such as scanned receipts.

        regional_format : typing.Optional[str]
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCreate
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
            await client.customer_statement.create_customer_statement_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                date_end="date_end",
                date_start="date_start",
                statement_format="statement_format",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer_statement_for_user_monetary_account(
            user_id,
            monetary_account_id,
            date_end=date_end,
            date_start=date_start,
            statement_format=statement_format,
            include_attachment=include_attachment,
            regional_format=regional_format,
            request_options=request_options,
        )
        return _response.data

    async def read_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementRead:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementRead
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
            await client.customer_statement.read_customer_statement_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementDelete:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementDelete
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

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
            await client.customer_statement.delete_customer_statement_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customer_statement_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
