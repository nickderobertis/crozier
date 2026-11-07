

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
from ..types.metadata_scheme_versions_item import MetadataSchemeVersionsItem
from ..types.mscid import Mscid
from ..types.namespace import Namespace
from ..types.response_item_metadata_scheme import ResponseItemMetadataScheme
from ..types.response_page_metadata_scheme import ResponsePageMetadataScheme
from ..types.response_success_metadata_scheme import ResponseSuccessMetadataScheme
from ..types.slug import Slug
from ..types.uri import Uri
from .raw_client import AsyncRawMClient, RawMClient


OMIT = typing.cast(typing.Any, ...)


class MClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMClient
        """
        return self._raw_client

    def list_all_metadata_schemes(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageMetadataScheme:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageMetadataScheme
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.m.list_all_metadata_schemes()
        """
        _response = self._raw_client.list_all_metadata_schemes(q=q, request_options=request_options)
        return _response.data

    def submit_a_new_metadata_scheme_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMetadataScheme:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMetadataScheme
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.m.submit_a_new_metadata_scheme_record()
        """
        _response = self._raw_client.submit_a_new_metadata_scheme_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            keywords=keywords,
            data_types=data_types,
            locations=locations,
            namespaces=namespaces,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def retrieve_an_existing_metadata_scheme_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemMetadataScheme:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemMetadataScheme
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.m.retrieve_an_existing_metadata_scheme_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_metadata_scheme_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_metadata_scheme_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMetadataScheme:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMetadataScheme
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.m.modify_an_existing_metadata_scheme_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_metadata_scheme_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            keywords=keywords,
            data_types=data_types,
            locations=locations,
            namespaces=namespaces,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_metadata_scheme_record(
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
        client.m.remove_an_existing_metadata_scheme_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_metadata_scheme_record(int_, request_options=request_options)
        return _response.data


class AsyncMClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMClient
        """
        return self._raw_client

    async def list_all_metadata_schemes(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageMetadataScheme:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageMetadataScheme
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
            await client.m.list_all_metadata_schemes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_metadata_schemes(q=q, request_options=request_options)
        return _response.data

    async def submit_a_new_metadata_scheme_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMetadataScheme:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMetadataScheme
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
            await client.m.submit_a_new_metadata_scheme_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_metadata_scheme_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            keywords=keywords,
            data_types=data_types,
            locations=locations,
            namespaces=namespaces,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_an_existing_metadata_scheme_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemMetadataScheme:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemMetadataScheme
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
            await client.m.retrieve_an_existing_metadata_scheme_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_metadata_scheme_record(
            int_, request_options=request_options
        )
        return _response.data

    async def modify_an_existing_metadata_scheme_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        data_types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        namespaces: typing.Optional[typing.Sequence[Namespace]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMetadataScheme:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        title : typing.Optional[str]
            The full, human understandable name of the metadata scheme.
            - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
            - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.

        description : typing.Optional[str]
            A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.

        keywords : typing.Optional[typing.Sequence[str]]
            Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.

        data_types : typing.Optional[typing.Sequence[str]]
            Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the scheme may be accessed.

        namespaces : typing.Optional[typing.Sequence[Namespace]]
            Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify all versions of this scheme collectively.

        related_entities : typing.Optional[typing.Sequence[MetadataSchemeRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MetadataSchemeVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMetadataScheme
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
            await client.m.modify_an_existing_metadata_scheme_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_metadata_scheme_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            title=title,
            description=description,
            keywords=keywords,
            data_types=data_types,
            locations=locations,
            namespaces=namespaces,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_metadata_scheme_record(
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
            await client.m.remove_an_existing_metadata_scheme_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_metadata_scheme_record(
            int_, request_options=request_options
        )
        return _response.data
