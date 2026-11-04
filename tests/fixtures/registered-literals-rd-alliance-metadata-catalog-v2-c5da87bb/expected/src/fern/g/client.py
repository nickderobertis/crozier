

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.identifier import Identifier
from ..types.location import Location
from ..types.mscid import Mscid
from ..types.organization_related_entities_item import OrganizationRelatedEntitiesItem
from ..types.response_item_organization import ResponseItemOrganization
from ..types.response_page_organization import ResponsePageOrganization
from ..types.response_success_organization import ResponseSuccessOrganization
from ..types.slug import Slug
from ..types.uri import Uri
from .raw_client import AsyncRawGClient, RawGClient


OMIT = typing.cast(typing.Any, ...)


class GClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGClient
        """
        return self._raw_client

    def list_all_organizations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageOrganization:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageOrganization
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.g.list_all_organizations()
        """
        _response = self._raw_client.list_all_organizations(q=q, request_options=request_options)
        return _response.data

    def submit_a_new_organization_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessOrganization:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            The full name of the organization as it is usually given.

        description : typing.Optional[str]
            A sentence or several describing the organization and its relevance to research data and metadata.

        types : typing.Optional[typing.Sequence[str]]

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the organization may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the organization.

        related_entities : typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessOrganization
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.g.submit_a_new_organization_record()
        """
        _response = self._raw_client.submit_a_new_organization_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            types=types,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    def retrieve_an_existing_organization_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemOrganization:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemOrganization
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.g.retrieve_an_existing_organization_record(
            int_=1,
        )
        """
        _response = self._raw_client.retrieve_an_existing_organization_record(int_, request_options=request_options)
        return _response.data

    def modify_an_existing_organization_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessOrganization:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            The full name of the organization as it is usually given.

        description : typing.Optional[str]
            A sentence or several describing the organization and its relevance to research data and metadata.

        types : typing.Optional[typing.Sequence[str]]

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the organization may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the organization.

        related_entities : typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessOrganization
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.g.modify_an_existing_organization_record(
            int_=1,
        )
        """
        _response = self._raw_client.modify_an_existing_organization_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            types=types,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    def remove_an_existing_organization_record(
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
        client.g.remove_an_existing_organization_record(
            int_=1,
        )
        """
        _response = self._raw_client.remove_an_existing_organization_record(int_, request_options=request_options)
        return _response.data


class AsyncGClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGClient
        """
        return self._raw_client

    async def list_all_organizations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePageOrganization:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePageOrganization
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
            await client.g.list_all_organizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_organizations(q=q, request_options=request_options)
        return _response.data

    async def submit_a_new_organization_record(
        self,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessOrganization:
        """
        Parameters
        ----------
        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            The full name of the organization as it is usually given.

        description : typing.Optional[str]
            A sentence or several describing the organization and its relevance to research data and metadata.

        types : typing.Optional[typing.Sequence[str]]

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the organization may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the organization.

        related_entities : typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessOrganization
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
            await client.g.submit_a_new_organization_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_organization_record(
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            types=types,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_an_existing_organization_record(
        self, int_: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponseItemOrganization:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseItemOrganization
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
            await client.g.retrieve_an_existing_organization_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_existing_organization_record(
            int_, request_options=request_options
        )
        return _response.data

    async def modify_an_existing_organization_record(
        self,
        int_: int,
        *,
        slug: typing.Optional[Slug] = OMIT,
        mscid: typing.Optional[Mscid] = OMIT,
        uri: typing.Optional[Uri] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        identifiers: typing.Optional[typing.Sequence[Identifier]] = OMIT,
        related_entities: typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResponseSuccessOrganization:
        """
        Parameters
        ----------
        int_ : int
            Numeric portion of the MSC ID.

        slug : typing.Optional[Slug]

        mscid : typing.Optional[Mscid]

        uri : typing.Optional[Uri]

        name : typing.Optional[str]
            The full name of the organization as it is usually given.

        description : typing.Optional[str]
            A sentence or several describing the organization and its relevance to research data and metadata.

        types : typing.Optional[typing.Sequence[str]]

        locations : typing.Optional[typing.Sequence[Location]]
            Locations where further information about the organization may be accessed.

        identifiers : typing.Optional[typing.Sequence[Identifier]]
            Strings used to identify the organization.

        related_entities : typing.Optional[typing.Sequence[OrganizationRelatedEntitiesItem]]
            Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponseSuccessOrganization
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
            await client.g.modify_an_existing_organization_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_an_existing_organization_record(
            int_,
            slug=slug,
            mscid=mscid,
            uri=uri,
            name=name,
            description=description,
            types=types,
            locations=locations,
            identifiers=identifiers,
            related_entities=related_entities,
            request_options=request_options,
        )
        return _response.data

    async def remove_an_existing_organization_record(
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
            await client.g.remove_an_existing_organization_record(
                int_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_an_existing_organization_record(int_, request_options=request_options)
        return _response.data
