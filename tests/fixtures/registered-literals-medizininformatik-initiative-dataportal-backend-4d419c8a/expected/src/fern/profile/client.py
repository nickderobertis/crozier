

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.profile_entry import ProfileEntry
from ..types.profile_filter import ProfileFilter
from ..types.profile_search_result import ProfileSearchResult
from .raw_client import AsyncRawProfileClient, RawProfileClient
from .types.get_filter_request_target_filter import GetFilterRequestTargetFilter


class ProfileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfileClient
        """
        return self._raw_client

    def search_profiles(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfileSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileSearchResult
            Ok, return the page of results. Only selectable profiles are returned.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profile.search_profiles(
            searchterm="Diagnose",
            modules=["Diagnose"],
            categories=["element"],
            resource_types=["Condition"],
        )
        """
        _response = self._raw_client.search_profiles(
            searchterm=searchterm,
            modules=modules,
            categories=categories,
            resource_types=resource_types,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def get_profile_list_details_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfileEntry:
        """
        Parameters
        ----------
        id : str
            The id of the profile entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileEntry
            Entry found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profile.get_profile_list_details_by_id(
            id="diagnose-condition-id",
        )
        """
        _response = self._raw_client.get_profile_list_details_by_id(id, request_options=request_options)
        return _response.data

    def get_filter(
        self,
        *,
        target_filter: typing.Optional[GetFilterRequestTargetFilter] = None,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProfileFilter]:
        """
        Can optionally be filtered to only get the filter of one target category, depending on the selections of the other categories and/or a searchterm

        Parameters
        ----------
        target_filter : typing.Optional[GetFilterRequestTargetFilter]
            The requested filter category. Only if this is set, the further filters for searchterm, modules, categories and resource-types are considered. If it is empty or null, ALL filters are returned unfiltered.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProfileFilter]
            Ok, return the list of available filters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profile.get_filter(
            searchterm="Diagnose",
            modules=["Diagnose"],
            categories=["element"],
            resource_types=["Condition"],
        )
        """
        _response = self._raw_client.get_filter(
            target_filter=target_filter,
            searchterm=searchterm,
            modules=modules,
            categories=categories,
            resource_types=resource_types,
            request_options=request_options,
        )
        return _response.data


class AsyncProfileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfileClient
        """
        return self._raw_client

    async def search_profiles(
        self,
        *,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfileSearchResult:
        """
        Parameters
        ----------
        searchterm : typing.Optional[str]
            The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        page_size : typing.Optional[int]
            How many results shall be returned per page

        page : typing.Optional[int]
            Which page shall be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileSearchResult
            Ok, return the page of results. Only selectable profiles are returned.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profile.search_profiles(
                searchterm="Diagnose",
                modules=["Diagnose"],
                categories=["element"],
                resource_types=["Condition"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_profiles(
            searchterm=searchterm,
            modules=modules,
            categories=categories,
            resource_types=resource_types,
            page_size=page_size,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def get_profile_list_details_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfileEntry:
        """
        Parameters
        ----------
        id : str
            The id of the profile entry that shall be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileEntry
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
            await client.profile.get_profile_list_details_by_id(
                id="diagnose-condition-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_profile_list_details_by_id(id, request_options=request_options)
        return _response.data

    async def get_filter(
        self,
        *,
        target_filter: typing.Optional[GetFilterRequestTargetFilter] = None,
        searchterm: typing.Optional[str] = None,
        modules: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        categories: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        resource_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProfileFilter]:
        """
        Can optionally be filtered to only get the filter of one target category, depending on the selections of the other categories and/or a searchterm

        Parameters
        ----------
        target_filter : typing.Optional[GetFilterRequestTargetFilter]
            The requested filter category. Only if this is set, the further filters for searchterm, modules, categories and resource-types are considered. If it is empty or null, ALL filters are returned unfiltered.

        searchterm : typing.Optional[str]
            Allow to take the searchterm into consideration to narrow down the results further.

        modules : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given modules

        categories : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given categories

        resource_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Limit the search to any of the given FHIR resource types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProfileFilter]
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
            await client.profile.get_filter(
                searchterm="Diagnose",
                modules=["Diagnose"],
                categories=["element"],
                resource_types=["Condition"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_filter(
            target_filter=target_filter,
            searchterm=searchterm,
            modules=modules,
            categories=categories,
            resource_types=resource_types,
            request_options=request_options,
        )
        return _response.data
