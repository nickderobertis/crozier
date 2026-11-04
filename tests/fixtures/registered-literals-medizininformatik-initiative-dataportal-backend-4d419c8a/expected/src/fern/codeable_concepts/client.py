

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.codeable_concept_bulk_search_result import CodeableConceptBulkSearchResult
from ..types.codeable_concept_entry import CodeableConceptEntry
from ..types.codeable_concept_search_result import CodeableConceptSearchResult
from .raw_client import AsyncRawCodeableConceptsClient, RawCodeableConceptsClient


OMIT = typing.cast(typing.Any, ...)


class CodeableConceptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCodeableConceptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCodeableConceptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCodeableConceptsClient
        """
        return self._raw_client

    def search_codeable_concepts(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        value_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeableConceptSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        value_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain value sets (specified via url)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptSearchResult
            Ok, return the page of results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.codeable_concepts.search_codeable_concepts(
            searchterm="Diabetes Mellitus",
            value_sets=["http://fhir.de/CodeSystem/bfarm/icd-10-gm"],
        )
        """
        _response = self._raw_client.search_codeable_concepts(
            searchterm=searchterm,
            value_sets=value_sets,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def bulk_search_codeable_concepts(
        self,
        *,
        value_set: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeableConceptBulkSearchResult:
        """
        Parameters
        ----------
        value_set : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptBulkSearchResult
            Ok, return a list with found codes and a list with codes that were not found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.codeable_concepts.bulk_search_codeable_concepts(
            value_set="https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/sct-body-structures",
            searchterms=["something invalid"],
        )
        """
        _response = self._raw_client.bulk_search_codeable_concepts(
            value_set=value_set, searchterms=searchterms, request_options=request_options
        )
        return _response.data

    def get_codeable_concepts_by_code(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CodeableConceptEntry:
        """
        Parameters
        ----------
        ids : str
            The ids (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptEntry
            Ok, return the codeable concept

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.codeable_concepts.get_codeable_concepts_by_code(
            ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
        )
        """
        _response = self._raw_client.get_codeable_concepts_by_code(ids=ids, request_options=request_options)
        return _response.data


class AsyncCodeableConceptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCodeableConceptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCodeableConceptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCodeableConceptsClient
        """
        return self._raw_client

    async def search_codeable_concepts(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        value_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeableConceptSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        value_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain value sets (specified via url)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptSearchResult
            Ok, return the page of results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.codeable_concepts.search_codeable_concepts(
                searchterm="Diabetes Mellitus",
                value_sets=["http://fhir.de/CodeSystem/bfarm/icd-10-gm"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_codeable_concepts(
            searchterm=searchterm,
            value_sets=value_sets,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def bulk_search_codeable_concepts(
        self,
        *,
        value_set: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeableConceptBulkSearchResult:
        """
        Parameters
        ----------
        value_set : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptBulkSearchResult
            Ok, return a list with found codes and a list with codes that were not found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.codeable_concepts.bulk_search_codeable_concepts(
                value_set="https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/sct-body-structures",
                searchterms=["something invalid"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_search_codeable_concepts(
            value_set=value_set, searchterms=searchterms, request_options=request_options
        )
        return _response.data

    async def get_codeable_concepts_by_code(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CodeableConceptEntry:
        """
        Parameters
        ----------
        ids : str
            The ids (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeableConceptEntry
            Ok, return the codeable concept

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.codeable_concepts.get_codeable_concepts_by_code(
                ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_codeable_concepts_by_code(ids=ids, request_options=request_options)
        return _response.data
