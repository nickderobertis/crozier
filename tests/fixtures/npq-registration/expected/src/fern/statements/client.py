

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id_attribute import IdAttribute
from ..types.list_statements_filter import ListStatementsFilter
from ..types.pagination_filter import PaginationFilter
from ..types.statement_response import StatementResponse
from ..types.statements_response import StatementsResponse
from .raw_client import AsyncRawStatementsClient, RawStatementsClient


class StatementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatementsClient
        """
        return self._raw_client

    def retrieve_financial_statements(
        self,
        *,
        filter: typing.Optional[ListStatementsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatementsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListStatementsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatementsResponse
            A list of statements as part of which the DfE will make output payments for participants

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.statements.retrieve_financial_statements()
        """
        _response = self._raw_client.retrieve_financial_statements(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    def retrieve_a_specific_financial_statement(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatementResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatementResponse
            A specific financial statement

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.statements.retrieve_a_specific_financial_statement(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.retrieve_a_specific_financial_statement(id, request_options=request_options)
        return _response.data


class AsyncStatementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatementsClient
        """
        return self._raw_client

    async def retrieve_financial_statements(
        self,
        *,
        filter: typing.Optional[ListStatementsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatementsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListStatementsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatementsResponse
            A list of statements as part of which the DfE will make output payments for participants

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.statements.retrieve_financial_statements()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_financial_statements(
            filter=filter, page=page, request_options=request_options
        )
        return _response.data

    async def retrieve_a_specific_financial_statement(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatementResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatementResponse
            A specific financial statement

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.statements.retrieve_a_specific_financial_statement(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_specific_financial_statement(id, request_options=request_options)
        return _response.data
