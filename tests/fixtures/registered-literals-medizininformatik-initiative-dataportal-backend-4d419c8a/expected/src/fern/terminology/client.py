

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.criteria_profile_data import CriteriaProfileData
from ..types.elastic_search_bulk_result import ElasticSearchBulkResult
from ..types.elastic_search_result import ElasticSearchResult
from ..types.elastic_search_result_entry import ElasticSearchResultEntry
from ..types.filter import Filter
from ..types.relations_entry import RelationsEntry
from ..types.terminology_systems import TerminologySystems
from ..types.ui_profile_list import UiProfileList
from .raw_client import AsyncRawTerminologyClient, RawTerminologyClient


OMIT = typing.cast(typing.Any, ...)


class TerminologyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTerminologyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTerminologyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTerminologyClient
        """
        return self._raw_client

    def get_filters(
        self,
        *,
        target_filter: typing.Optional[str] = None,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Filter]:
        """
        Can optionally be filtered to only get the filters of one category, depending on the selections of other categories

        Parameters
        ----------
        target_filter : typing.Optional[str]
            The requested filter category. Only if this is set, the further filters for contexts, kds-modules and terminologies are considered. If it is empty or null, ALL entries are returned.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Filter]
            Ok, return the list of available filters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_filters(
            target_filter="terminology",
            searchterm="terminology",
            contexts=["Diagnosis"],
            terminologies=["ICD10"],
            kds_modules=["Condition"],
        )
        """
        _response = self._raw_client.get_filters(
            target_filter=target_filter,
            searchterm=searchterm,
            contexts=contexts,
            terminologies=terminologies,
            kds_modules=kds_modules,
            request_options=request_options,
        )
        return _response.data

    def get_terminology_systems(self, *, request_options: typing.Optional[RequestOptions] = None) -> TerminologySystems:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TerminologySystems
            System mapping file found and readable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_terminology_systems()
        """
        _response = self._raw_client.get_terminology_systems(request_options=request_options)
        return _response.data

    def search_entry(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        criteria_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        availability: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ElasticSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        criteria_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain criteria sets (specified via url)

        availability : typing.Optional[bool]
            Limit the search to available items? (Maybe better invert this one to make this the default?)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchResult
            Ok, return the list of results for the search

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.search_entry(
            searchterm="Diabetes Mellitus",
            contexts=["Diagnosis"],
            terminologies=["ICD10"],
            kds_modules=["Condition"],
            criteria_sets=["http://fhir.de/CodeSystem/bfarm/icd-10-gm"],
        )
        """
        _response = self._raw_client.search_entry(
            searchterm=searchterm,
            contexts=contexts,
            terminologies=terminologies,
            kds_modules=kds_modules,
            criteria_sets=criteria_sets,
            availability=availability,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def bulk_search_entry(
        self,
        *,
        terminology: str,
        context: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ElasticSearchBulkResult:
        """
        Parameters
        ----------
        terminology : str

        context : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchBulkResult
            Ok, return the list of results for the search

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.bulk_search_entry(
            terminology="http://fhir.de/CodeSystem/bfarm/icd-10-gm",
            context="Diagnose",
            searchterms=["Z01.81"],
        )
        """
        _response = self._raw_client.bulk_search_entry(
            terminology=terminology, context=context, searchterms=searchterms, request_options=request_options
        )
        return _response.data

    def get_entry_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RelationsEntry:
        """
        Parameters
        ----------
        id : str
            The id (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelationsEntry
            Entry found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_entry_by_id(
            id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
        )
        """
        _response = self._raw_client.get_entry_by_id(id, request_options=request_options)
        return _response.data

    def get_entries_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElasticSearchResultEntry:
        """
        This should be in the getEntryById call, but for better distinction between the return values it is listed separately here

        Parameters
        ----------
        id : str
            The ids (contextualized termcode hash) of the entries that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchResultEntry
            Entry found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_entries_by_id(
            id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
        )
        """
        _response = self._raw_client.get_entries_by_id(id, request_options=request_options)
        return _response.data

    def get_entries_by_ids_with_detail(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CriteriaProfileData]:
        """
        This should return all the information needed to build criteria in the frontend.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (contextualized termcode hashes) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CriteriaProfileData]
            Entries found. May contain empty entries if some were not found.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_entries_by_ids_with_detail(
            ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
        )
        """
        _response = self._raw_client.get_entries_by_ids_with_detail(ids=ids, request_options=request_options)
        return _response.data

    def get_ui_profiles(self, *, request_options: typing.Optional[RequestOptions] = None) -> UiProfileList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiProfileList
            Get all UiProfiles

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.terminology.get_ui_profiles()
        """
        _response = self._raw_client.get_ui_profiles(request_options=request_options)
        return _response.data


class AsyncTerminologyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTerminologyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTerminologyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTerminologyClient
        """
        return self._raw_client

    async def get_filters(
        self,
        *,
        target_filter: typing.Optional[str] = None,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Filter]:
        """
        Can optionally be filtered to only get the filters of one category, depending on the selections of other categories

        Parameters
        ----------
        target_filter : typing.Optional[str]
            The requested filter category. Only if this is set, the further filters for contexts, kds-modules and terminologies are considered. If it is empty or null, ALL entries are returned.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Filter]
            Ok, return the list of available filters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_filters(
                target_filter="terminology",
                searchterm="terminology",
                contexts=["Diagnosis"],
                terminologies=["ICD10"],
                kds_modules=["Condition"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_filters(
            target_filter=target_filter,
            searchterm=searchterm,
            contexts=contexts,
            terminologies=terminologies,
            kds_modules=kds_modules,
            request_options=request_options,
        )
        return _response.data

    async def get_terminology_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TerminologySystems:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TerminologySystems
            System mapping file found and readable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_terminology_systems()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_terminology_systems(request_options=request_options)
        return _response.data

    async def search_entry(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        contexts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        terminologies: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        kds_modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        criteria_sets: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        availability: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ElasticSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        contexts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given contexts

        terminologies : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to a any of the given terminologies

        kds_modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given KDS modules

        criteria_sets : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to certain criteria sets (specified via url)

        availability : typing.Optional[bool]
            Limit the search to available items? (Maybe better invert this one to make this the default?)

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchResult
            Ok, return the list of results for the search

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.search_entry(
                searchterm="Diabetes Mellitus",
                contexts=["Diagnosis"],
                terminologies=["ICD10"],
                kds_modules=["Condition"],
                criteria_sets=["http://fhir.de/CodeSystem/bfarm/icd-10-gm"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_entry(
            searchterm=searchterm,
            contexts=contexts,
            terminologies=terminologies,
            kds_modules=kds_modules,
            criteria_sets=criteria_sets,
            availability=availability,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def bulk_search_entry(
        self,
        *,
        terminology: str,
        context: str,
        searchterms: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ElasticSearchBulkResult:
        """
        Parameters
        ----------
        terminology : str

        context : str

        searchterms : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchBulkResult
            Ok, return the list of results for the search

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.bulk_search_entry(
                terminology="http://fhir.de/CodeSystem/bfarm/icd-10-gm",
                context="Diagnose",
                searchterms=["Z01.81"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_search_entry(
            terminology=terminology, context=context, searchterms=searchterms, request_options=request_options
        )
        return _response.data

    async def get_entry_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RelationsEntry:
        """
        Parameters
        ----------
        id : str
            The id (contextualized termcode hash) of the entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelationsEntry
            Entry found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_entry_by_id(
                id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entry_by_id(id, request_options=request_options)
        return _response.data

    async def get_entries_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ElasticSearchResultEntry:
        """
        This should be in the getEntryById call, but for better distinction between the return values it is listed separately here

        Parameters
        ----------
        id : str
            The ids (contextualized termcode hash) of the entries that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ElasticSearchResultEntry
            Entry found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_entries_by_id(
                id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entries_by_id(id, request_options=request_options)
        return _response.data

    async def get_entries_by_ids_with_detail(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CriteriaProfileData]:
        """
        This should return all the information needed to build criteria in the frontend.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (contextualized termcode hashes) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CriteriaProfileData]
            Entries found. May contain empty entries if some were not found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_entries_by_ids_with_detail(
                ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entries_by_ids_with_detail(ids=ids, request_options=request_options)
        return _response.data

    async def get_ui_profiles(self, *, request_options: typing.Optional[RequestOptions] = None) -> UiProfileList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiProfileList
            Get all UiProfiles

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.terminology.get_ui_profiles()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ui_profiles(request_options=request_options)
        return _response.data
