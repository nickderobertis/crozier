

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.creator import Creator
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mapping_related_entities_item import MappingRelatedEntitiesItem
from ..types.mapping_versions_item import MappingVersionsItem
from ..types.mscid import Mscid
from ..types.response_item_mapping import ResponseItemMapping
from ..types.response_page_mapping import ResponsePageMapping
from ..types.response_success_mapping import ResponseSuccessMapping
from ..types.slug import Slug
from ..types.uri import Uri
from .raw_client import AsyncRawCClient, RawCClient


OMIT = typing.cast(typing.Any, ...)


class CClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCClient
        """
        return self._raw_client

    def list_all_mappings(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageMapping:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageMapping
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.c.list_all_mappings()
        """
        _response = self._raw_client.list_all_mappings(q=q, request_options=request_options)
        return _response.data

    def submit_a_new_mapping_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMapping:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMapping
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.c.submit_a_new_mapping_record()
        """
        _response = self._raw_client.submit_a_new_mapping_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            creators=creators,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def retrieve_an_existing_mapping_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemMapping:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemMapping
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.c.retrieve_an_existing_mapping_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_mapping_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_mapping_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMapping:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMapping
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.c.modify_an_existing_mapping_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_mapping_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            creators=creators,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_mapping_record(
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
        client.c.remove_an_existing_mapping_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_mapping_record(int_, request_options=request_options)
        return _response.data


class AsyncCClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCClient
        """
        return self._raw_client

    async def list_all_mappings(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageMapping:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageMapping
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
            await client.c.list_all_mappings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_mappings(q=q, request_options=request_options)
        return _response.data

    async def submit_a_new_mapping_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMapping:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMapping
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
            await client.c.submit_a_new_mapping_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_mapping_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            creators=creators,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_an_existing_mapping_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemMapping:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemMapping
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
            await client.c.retrieve_an_existing_mapping_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_mapping_record(int_, request_options=request_options)
        return _response.data

    async def modify_an_existing_mapping_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        creators: typing.Optional[typing.Sequence[Creator]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]] = OMIT,
        versions: typing.Optional[typing.Sequence[MappingVersionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessMapping:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            Name or descriptor for the mapping.

        description : typing.Optional[str]
            A short description of the mapping.
            - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
            - This could recommend steps to be taken before or after applying the mapping in order to improve results.

        creators : typing.Optional[typing.Sequence[Creator]]
            Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the tool may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the mapping or version.

        related_entities : typing.Optional[typing.Sequence[MappingRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        versions : typing.Optional[typing.Sequence[MappingVersionsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessMapping
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
            await client.c.modify_an_existing_mapping_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_mapping_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            creators=creators,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            versions=versions,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_mapping_record(
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
            await client.c.remove_an_existing_mapping_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_mapping_record(int_, request_options=request_options)
        return _response.data
