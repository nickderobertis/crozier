

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.creator import Creator
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mscid import Mscid
from ..types.response_item_tool import ResponseItemTool
from ..types.response_page_tool import ResponsePageTool
from ..types.response_success_tool import ResponseSuccessTool
from ..types.slug import Slug
from ..types.tool_related_entities_item import ToolRelatedEntitiesItem
from ..types.tool_versions_item import ToolVersionsItem
from ..types.uri import Uri
from .raw_client import AsyncRawTClient, RawTClient


OMIT = typing.cast(typing.Any, ...)


class TClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTClient
        """
        return self._raw_client

    def list_all_tools(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageTool:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageTool
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.t.list_all_tools()
        """
        _response = self._raw_client.list_all_tools(q=q, request_options=request_options)
        return _response.data

    def submit_a_new_tool_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessTool:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessTool
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.t.submit_a_new_tool_record()
        """
        _response = self._raw_client.submit_a_new_tool_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            types=types,
            identifiers=identifiers,
            locations=locations,
            creators=creators,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def retrieve_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemTool:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemTool
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.t.retrieve_an_existing_tool_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_tool_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_tool_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessTool:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessTool
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.t.modify_an_existing_tool_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_tool_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            types=types,
            identifiers=identifiers,
            locations=locations,
            creators=creators,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.t.remove_an_existing_tool_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_tool_record(int_, request_options=request_options)
        return _response.data


class AsyncTClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTClient
        """
        return self._raw_client

    async def list_all_tools(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageTool:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageTool
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
            await client.t.list_all_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_tools(q=q, request_options=request_options)
        return _response.data

    async def submit_a_new_tool_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessTool:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessTool
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
            await client.t.submit_a_new_tool_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_tool_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            types=types,
            identifiers=identifiers,
            locations=locations,
            creators=creators,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemTool:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemTool
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
            await client.t.retrieve_an_existing_tool_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_tool_record(int_, request_options=request_options)
        return _response.data

    async def modify_an_existing_tool_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[ToolVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessTool:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the tool.
            - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.

        description : typing.Optional[str]
            A short description of the intended use of the tool, and its capabilities.

        types : typing.Optional[typing.Sequence[str]]
            Terms describing how a user interacts with the tool.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the tool or version.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        related_entities : typing.Optional[typing.Sequence[ToolRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[ToolVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessTool
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
            await client.t.modify_an_existing_tool_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_tool_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            types=types,
            identifiers=identifiers,
            locations=locations,
            creators=creators,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_tool_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.t.remove_an_existing_tool_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_tool_record(int_, request_options=request_options)
        return _response.data
