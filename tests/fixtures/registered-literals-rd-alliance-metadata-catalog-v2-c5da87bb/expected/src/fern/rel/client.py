

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mscid import Mscid
from ..types.patch_relation import PatchRelation
from ..types.response_item_relation import ResponseItemRelation
from ..types.response_page_relation import ResponsePageRelation
from ..types.response_success_relation import ResponseSuccessRelation
from .raw_client import AsyncRawRelClient, RawRelClient
from .types.delete_api2rel_table_int_request_table import DeleteApi2RelTableIntRequestTable
from .types.get_api2rel_table_int_request_table import GetApi2RelTableIntRequestTable
from .types.patch_api2rel_table_int_request_table import PatchApi2RelTableIntRequestTable
from .types.put_api2rel_table_int_request_table import PutApi2RelTableIntRequestTable


OMIT = typing.cast(typing.Any, ...)


class RelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRelClient
        """
        return self._raw_client

    def list_all_entity_relation_records(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageRelation:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageRelation
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.rel.list_all_entity_relation_records()
        """
        _response = self._raw_client.list_all_entity_relation_records(q=q, request_options=request_options)
        return _response.data

    def retrieve_an_existing_entity_relation_record(
        self,
        table: GetApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemRelation:
        """
        Parameters
        ----------
        table : GetApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemRelation
            Success

        Examples
        --------
        from fern.rel import GetApi2RelTableIntRequestTable

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.rel.retrieve_an_existing_entity_relation_record(
            table=GetApi2RelTableIntRequestTable.M,
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_entity_relation_record(
            table, int_, request_options=request_options
        )
        return _response.data

    def modify_an_existing_entity_relation_record(
        self,
        table: PutApi2RelTableIntRequestTable,
        int_: int,
        *,
        id: typing.Optional[Mscid] = OMIT,
        parent_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        supported_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        input_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        output_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        endorsed_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        maintainers: typing.Optional[typing.Sequence[str]] = OMIT,
        funders: typing.Optional[typing.Sequence[str]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        originators: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessRelation:
        """
        Parameters
        ----------
        table : PutApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        id : typing.Optional[Mscid]

        parent_schemes : typing.Optional[typing.Sequence[str]]
            Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.

        supported_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which the tool’s input metadata should conform, or output metadata does conform.

        input_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which a metadata record input to the current mapping must conform.

        output_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which metadata records output from the current mapping conform.

        endorsed_schemes : typing.Optional[typing.Sequence[str]]
            Schemes endorsed by the current endorsement.

        maintainers : typing.Optional[typing.Sequence[str]]
            Organizations that maintain the current scheme, tool or mapping.

        funders : typing.Optional[typing.Sequence[str]]
            Organizations that fund the current scheme, tool or mapping.

        users : typing.Optional[typing.Sequence[str]]
            Organizations that are known to use the current scheme.

        originators : typing.Optional[typing.Sequence[str]]
            Organizations that have made the current endorsement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessRelation
            Success

        Examples
        --------
        from fern.rel import PutApi2RelTableIntRequestTable

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.rel.modify_an_existing_entity_relation_record(
            table=PutApi2RelTableIntRequestTable.M,
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_entity_relation_record(
            table,
            int_,
            id=id,
            parent_schemes=parent_schemes,
            supported_schemes=supported_schemes,
            input_schemes=input_schemes,
            output_schemes=output_schemes,
            endorsed_schemes=endorsed_schemes,
            maintainers=maintainers,
            funders=funders,
            users=users,
            originators=originators,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_entity_relation_record(
        self,
        table: DeleteApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        table : DeleteApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.rel import DeleteApi2RelTableIntRequestTable

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.rel.remove_an_existing_entity_relation_record(
            table=DeleteApi2RelTableIntRequestTable.M,
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_entity_relation_record(
            table, int_, request_options=request_options
        )
        return _response.data

    def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2RelTableIntRequestTable,
        int_: int,
        *,
        request: PatchRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessRelation:
        """
        Parameters
        ----------
        table : PatchApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessRelation
            Success

        Examples
        --------
        from fern.rel import PatchApi2RelTableIntRequestTable

        from fern import FernApi, PatchRelationItemZero

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.rel.add_or_remove_an_individual_entity_relation(
            table=PatchApi2RelTableIntRequestTable.M,
            int_=1,
            request=[PatchRelationItemZero()],
        )
        """
        _response = self._raw_client.add_or_remove_an_individual_entity_relation(
            table, int_, request=request, request_options=request_options
        )
        return _response.data


class AsyncRelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRelClient
        """
        return self._raw_client

    async def list_all_entity_relation_records(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageRelation:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageRelation
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
            await client.rel.list_all_entity_relation_records()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_entity_relation_records(q=q, request_options=request_options)
        return _response.data

    async def retrieve_an_existing_entity_relation_record(
        self,
        table: GetApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseItemRelation:
        """
        Parameters
        ----------
        table : GetApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemRelation
            Success

        Examples
        --------
        import asyncio

        from fern.rel import GetApi2RelTableIntRequestTable

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.rel.retrieve_an_existing_entity_relation_record(
                table=GetApi2RelTableIntRequestTable.M,
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_entity_relation_record(
            table, int_, request_options=request_options
        )
        return _response.data

    async def modify_an_existing_entity_relation_record(
        self,
        table: PutApi2RelTableIntRequestTable,
        int_: int,
        *,
        id: typing.Optional[Mscid] = OMIT,
        parent_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        supported_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        input_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        output_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        endorsed_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        maintainers: typing.Optional[typing.Sequence[str]] = OMIT,
        funders: typing.Optional[typing.Sequence[str]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        originators: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessRelation:
        """
        Parameters
        ----------
        table : PutApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        id : typing.Optional[Mscid]

        parent_schemes : typing.Optional[typing.Sequence[str]]
            Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.

        supported_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which the tool’s input metadata should conform, or output metadata does conform.

        input_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which a metadata record input to the current mapping must conform.

        output_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which metadata records output from the current mapping conform.

        endorsed_schemes : typing.Optional[typing.Sequence[str]]
            Schemes endorsed by the current endorsement.

        maintainers : typing.Optional[typing.Sequence[str]]
            Organizations that maintain the current scheme, tool or mapping.

        funders : typing.Optional[typing.Sequence[str]]
            Organizations that fund the current scheme, tool or mapping.

        users : typing.Optional[typing.Sequence[str]]
            Organizations that are known to use the current scheme.

        originators : typing.Optional[typing.Sequence[str]]
            Organizations that have made the current endorsement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessRelation
            Success

        Examples
        --------
        import asyncio

        from fern.rel import PutApi2RelTableIntRequestTable

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.rel.modify_an_existing_entity_relation_record(
                table=PutApi2RelTableIntRequestTable.M,
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_entity_relation_record(
            table,
            int_,
            id=id,
            parent_schemes=parent_schemes,
            supported_schemes=supported_schemes,
            input_schemes=input_schemes,
            output_schemes=output_schemes,
            endorsed_schemes=endorsed_schemes,
            maintainers=maintainers,
            funders=funders,
            users=users,
            originators=originators,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_entity_relation_record(
        self,
        table: DeleteApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        table : DeleteApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.rel import DeleteApi2RelTableIntRequestTable

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.rel.remove_an_existing_entity_relation_record(
                table=DeleteApi2RelTableIntRequestTable.M,
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_entity_relation_record(
            table, int_, request_options=request_options
        )
        return _response.data

    async def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2RelTableIntRequestTable,
        int_: int,
        *,
        request: PatchRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessRelation:
        """
        Parameters
        ----------
        table : PatchApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessRelation
            Success

        Examples
        --------
        import asyncio

        from fern.rel import PatchApi2RelTableIntRequestTable

        from fern import AsyncFernApi, PatchRelationItemZero

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.rel.add_or_remove_an_individual_entity_relation(
                table=PatchApi2RelTableIntRequestTable.M,
                int_=1,
                request=[PatchRelationItemZero()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_or_remove_an_individual_entity_relation(
            table, int_, request=request, request_options=request_options
        )
        return _response.data
