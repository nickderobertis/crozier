

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.skg_if_json_ld_response import SkgIfJsonLdResponse
from .raw_client import AsyncRawProductsClient, RawProductsClient


class ProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsClient
        """
        return self._raw_client

    def search6(
        self,
        *,
        filter: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SkgIfJsonLdResponse:
        """
        Get a list of `product` matching the provided filter criteria.

        Parameters
        ----------
        filter : str
               Filter string with pipe-separated values for multiple values per key.

               **Format:** `key1:value1|value2,key2:value3`

               **Examples:**
               - Single values: `product_type:publication,cf.search.title:ocean`
               - Multiple values: `product_type:publication|dataset|software`
               - Mixed: `product_type:publication|dataset,cf.search.title:ocean`

               **IMPORTANT:** Duplicate keys are not allowed (use pipe `|` to separate multiple values)

               **Attribute Filters:**
            - `product_type`: publication, dataset, software, other
            - `identifiers.id`: product identifier (DOI, arXiv, etc.)
            - `identifiers.scheme`: identifier scheme (doi, arxiv, etc.)
            - `contributions.by.local_identifier`: contributor local ID
            - `contributions.by.identifiers.id`: contributor identifier (ORCID, etc.)
            - `contributions.by.identifiers.scheme`: contributor ID scheme (orcid, etc.)
            - `contributions.by.family_name`: contributor family name
            - `contributions.by.given_name`: contributor given name
            - `contributions.by.name`: contributor full name
            - `contributions.declared_affiliations.local_identifier`: affiliation local ID
            - `contributions.declared_affiliations.identifiers.id`: affiliation identifier
            - `contributions.declared_affiliations.identifiers.scheme`: affiliation ID scheme
            - `contributions.declared_affiliations.name`: affiliation name
            - `contributions.declared_affiliations.short_name`: affiliation short name
            - `funding.local_identifier`: funding local identifier
            - `funding.grant_number`: funding grant number
            - `funding.identifiers.id`: funding identifier
            - `funding.identifiers.scheme`: funding identifier scheme

            **Convenience Filters:**
            - `cf.search.title`: title search
            - `cf.search.title_abstract`: title and abstract search
            - `cf.contributions_orcid`: ORCID-based contributor search
            - `cf.cites`: citation relationships
            - `cf.subject`: subject classification
            - `cf.publication_year`: publication year
            - `cf.language`: language filter
            - `cf.access_rights`: access rights filter

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkgIfJsonLdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.search6(
            filter="product_type:publication",
        )
        """
        _response = self._raw_client.search6(
            filter=filter, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_by_id6(
        self, local_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SkgIfJsonLdResponse:
        """
        Get product by local identifier.

        Parameters
        ----------
        local_identifier : str
            The local identifier of the product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkgIfJsonLdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.products.get_by_id6(
            local_identifier="localIdentifier",
        )
        """
        _response = self._raw_client.get_by_id6(local_identifier, request_options=request_options)
        return _response.data


class AsyncProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsClient
        """
        return self._raw_client

    async def search6(
        self,
        *,
        filter: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SkgIfJsonLdResponse:
        """
        Get a list of `product` matching the provided filter criteria.

        Parameters
        ----------
        filter : str
               Filter string with pipe-separated values for multiple values per key.

               **Format:** `key1:value1|value2,key2:value3`

               **Examples:**
               - Single values: `product_type:publication,cf.search.title:ocean`
               - Multiple values: `product_type:publication|dataset|software`
               - Mixed: `product_type:publication|dataset,cf.search.title:ocean`

               **IMPORTANT:** Duplicate keys are not allowed (use pipe `|` to separate multiple values)

               **Attribute Filters:**
            - `product_type`: publication, dataset, software, other
            - `identifiers.id`: product identifier (DOI, arXiv, etc.)
            - `identifiers.scheme`: identifier scheme (doi, arxiv, etc.)
            - `contributions.by.local_identifier`: contributor local ID
            - `contributions.by.identifiers.id`: contributor identifier (ORCID, etc.)
            - `contributions.by.identifiers.scheme`: contributor ID scheme (orcid, etc.)
            - `contributions.by.family_name`: contributor family name
            - `contributions.by.given_name`: contributor given name
            - `contributions.by.name`: contributor full name
            - `contributions.declared_affiliations.local_identifier`: affiliation local ID
            - `contributions.declared_affiliations.identifiers.id`: affiliation identifier
            - `contributions.declared_affiliations.identifiers.scheme`: affiliation ID scheme
            - `contributions.declared_affiliations.name`: affiliation name
            - `contributions.declared_affiliations.short_name`: affiliation short name
            - `funding.local_identifier`: funding local identifier
            - `funding.grant_number`: funding grant number
            - `funding.identifiers.id`: funding identifier
            - `funding.identifiers.scheme`: funding identifier scheme

            **Convenience Filters:**
            - `cf.search.title`: title search
            - `cf.search.title_abstract`: title and abstract search
            - `cf.contributions_orcid`: ORCID-based contributor search
            - `cf.cites`: citation relationships
            - `cf.subject`: subject classification
            - `cf.publication_year`: publication year
            - `cf.language`: language filter
            - `cf.access_rights`: access rights filter

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkgIfJsonLdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.search6(
                filter="product_type:publication",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search6(
            filter=filter, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_by_id6(
        self, local_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SkgIfJsonLdResponse:
        """
        Get product by local identifier.

        Parameters
        ----------
        local_identifier : str
            The local identifier of the product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkgIfJsonLdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.products.get_by_id6(
                local_identifier="localIdentifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_id6(local_identifier, request_options=request_options)
        return _response.data
