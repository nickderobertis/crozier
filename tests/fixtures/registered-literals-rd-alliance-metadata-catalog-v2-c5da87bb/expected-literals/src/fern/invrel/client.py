

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.patch_inv_relation import PatchInvRelation
from ..types.response_item_inv_relation import ResponseItemInvRelation
from ..types.response_page_inv_relation import ResponsePageInvRelation
from ..types.response_success_inv_relation import ResponseSuccessInvRelation
from .raw_client import AsyncRawInvrelClient, RawInvrelClient
from .types.get_api2invrel_table_int_request_table import GetApi2InvrelTableIntRequestTable
from .types.patch_api2invrel_table_int_request_table import PatchApi2InvrelTableIntRequestTable


OMIT = typing.cast(typing.Any, ...)


class InvrelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvrelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvrelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvrelClient
        """
        return self._raw_client

    def list_virtual_records_of_inverse_entity_relations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageInvRelation:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageInvRelation
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invrel.list_virtual_records_of_inverse_entity_relations()
        """
        _response = self._raw_client.list_virtual_records_of_inverse_entity_relations(
            q=q, request_options=request_options
        )
        return _response.data

    def retrieve_a_virtual_record_of_inverse_entity_relations(
        self,
        table: GetApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemInvRelation:
        """
        Parameters
        ----------
        table : GetApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemInvRelation
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invrel.retrieve_a_virtual_record_of_inverse_entity_relations(
            table="m",
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_a_virtual_record_of_inverse_entity_relations(
            table, int_, request_options=request_options
        )
        return _response.data

    def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request: PatchInvRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessInvRelation:
        """
        Parameters
        ----------
        table : PatchApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchInvRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessInvRelation
            Success

        Examples
        --------
        from fern import FernApi, PatchInvRelationItemZero

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invrel.add_or_remove_an_individual_entity_relation(
            table="m",
            int_=1,
            request=[PatchInvRelationItemZero()],
        )
        """
        _response = self._raw_client.add_or_remove_an_individual_entity_relation(
            table, int_, request=request, request_options=request_options
        )
        return _response.data


class AsyncInvrelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvrelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvrelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvrelClient
        """
        return self._raw_client

    async def list_virtual_records_of_inverse_entity_relations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageInvRelation:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageInvRelation
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.invrel.list_virtual_records_of_inverse_entity_relations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_virtual_records_of_inverse_entity_relations(
            q=q, request_options=request_options
        )
        return _response.data

    async def retrieve_a_virtual_record_of_inverse_entity_relations(
        self,
        table: GetApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemInvRelation:
        """
        Parameters
        ----------
        table : GetApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemInvRelation
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.invrel.retrieve_a_virtual_record_of_inverse_entity_relations(
                table="m",
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_virtual_record_of_inverse_entity_relations(
            table, int_, request_options=request_options
        )
        return _response.data

    async def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request: PatchInvRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessInvRelation:
        """
        Parameters
        ----------
        table : PatchApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchInvRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessInvRelation
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchInvRelationItemZero

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.invrel.add_or_remove_an_individual_entity_relation(
                table="m",
                int_=1,
                request=[PatchInvRelationItemZero()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_or_remove_an_individual_entity_relation(
            table, int_, request=request, request_options=request_options
        )
        return _response.data
