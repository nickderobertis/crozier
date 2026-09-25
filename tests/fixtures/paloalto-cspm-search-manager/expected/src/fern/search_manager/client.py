

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.saved_recent_search import SavedRecentSearch
from ..types.search_model import SearchModel
from ..types.search_model_cloud_type import SearchModelCloudType
from ..types.search_model_search_type import SearchModelSearchType
from ..types.search_model_time_range import SearchModelTimeRange
from ..types.search_response_model_search_model import SearchResponseModelSearchModel
from ..types.ui_filter_model import UiFilterModel
from .raw_client import AsyncRawSearchManagerClient, RawSearchManagerClient


OMIT = typing.cast(typing.Any, ...)


class SearchManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchManagerClient
        """
        return self._raw_client

    def search_history(
        self,
        *,
        filter: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SavedRecentSearch]:
        """
        Lists saved or recent search queries based on your filter.

        Parameters
        ----------
        filter : str
            Available values: recent, saved

        limit : typing.Optional[int]
            Maximum number of searches to be returned. A single API call retrieves a maximum of 1000 searches, which is also the default. Setting the limit to -1 will also return the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SavedRecentSearch]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search_manager.search_history(
            filter="filter",
        )
        """
        _response = self._raw_client.search_history(filter=filter, limit=limit, request_options=request_options)
        return _response.data

    def search_history_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SearchModel:
        """
        Returns a search query. You can access only queries that are either saved or recent searches.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchModel
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search_manager.search_history_by_id(
            id="id",
        )
        """
        _response = self._raw_client.search_history_by_id(id, request_options=request_options)
        return _response.data

    def search_history_manage(
        self,
        id_: str,
        *,
        query: str,
        time_range: SearchModelTimeRange,
        alert_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        async_result_url: typing.Optional[str] = OMIT,
        cloud_type: typing.Optional[SearchModelCloudType] = OMIT,
        cursor: typing.Optional[int] = OMIT,
        default: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        saved: typing.Optional[bool] = OMIT,
        search_type: typing.Optional[SearchModelSearchType] = OMIT,
        time_granularity: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponseModelSearchModel:
        """
        Allows you to manage a search query (save a search query to the **Saved Searches** list under the specified ID, convert a recent search to a saved search, update an existing search). For details on how to manage a saved search, see [Manage Saved Search](/prisma-cloud/docs/cspm/manage-saved-search)

        Required parameters include the search ID, the RQL query, the flag that
        marks this search as saved, and a unique name for the saved search. A best
        practice is to copy data from the results of a search history, update the
        data as necessary, and set the **saved** parameter to **true**.

        This API requires Prisma Cloud system administrator role access if you don't own the search with the given search ID.

        Parameters
        ----------
        id_ : str
            Search ID

        query : str
            RQL Query

        time_range : SearchModelTimeRange
            Time Range

        alert_id : typing.Optional[str]
            Alert ID

        async_ : typing.Optional[bool]
            true = Is Async

        async_result_url : typing.Optional[str]
            Async Result Url

        cloud_type : typing.Optional[SearchModelCloudType]
            Cloud Type

        cursor : typing.Optional[int]
            Cursor

        default : typing.Optional[bool]

        description : typing.Optional[str]
            Search Description

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            View Order

        group_by : typing.Optional[typing.Sequence[str]]
            Group By

        id : typing.Optional[str]
            Search ID

        name : typing.Optional[str]
            Search Name

        read_only : typing.Optional[bool]
            Read Only

        saved : typing.Optional[bool]
            Search Exists

        search_type : typing.Optional[SearchModelSearchType]
            Search Type

        time_granularity : typing.Optional[str]
            Time Granularity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponseModelSearchModel
            successful operation

        Examples
        --------
        from fern import (
            AbsoluteTimeRangeConfigModelValue,
            FernApi,
            SearchModelTimeRange_Absolute,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search_manager.search_history_manage(
            id_="id",
            query="query",
            time_range=SearchModelTimeRange_Absolute(
                value=AbsoluteTimeRangeConfigModelValue(),
            ),
        )
        """
        _response = self._raw_client.search_history_manage(
            id_,
            query=query,
            time_range=time_range,
            alert_id=alert_id,
            async_=async_,
            async_result_url=async_result_url,
            cloud_type=cloud_type,
            cursor=cursor,
            default=default,
            description=description,
            filters=filters,
            group_by=group_by,
            id=id,
            name=name,
            read_only=read_only,
            saved=saved,
            search_type=search_type,
            time_granularity=time_granularity,
            request_options=request_options,
        )
        return _response.data

    def search_history_delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a saved search query.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search_manager.search_history_delete(
            id="id",
        )
        """
        _response = self._raw_client.search_history_delete(id, request_options=request_options)
        return _response.data


class AsyncSearchManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchManagerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchManagerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchManagerClient
        """
        return self._raw_client

    async def search_history(
        self,
        *,
        filter: str,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SavedRecentSearch]:
        """
        Lists saved or recent search queries based on your filter.

        Parameters
        ----------
        filter : str
            Available values: recent, saved

        limit : typing.Optional[int]
            Maximum number of searches to be returned. A single API call retrieves a maximum of 1000 searches, which is also the default. Setting the limit to -1 will also return the default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SavedRecentSearch]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_manager.search_history(
                filter="filter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_history(filter=filter, limit=limit, request_options=request_options)
        return _response.data

    async def search_history_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchModel:
        """
        Returns a search query. You can access only queries that are either saved or recent searches.

        Parameters
        ----------
        id : str
            Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_manager.search_history_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_history_by_id(id, request_options=request_options)
        return _response.data

    async def search_history_manage(
        self,
        id_: str,
        *,
        query: str,
        time_range: SearchModelTimeRange,
        alert_id: typing.Optional[str] = OMIT,
        async_: typing.Optional[bool] = OMIT,
        async_result_url: typing.Optional[str] = OMIT,
        cloud_type: typing.Optional[SearchModelCloudType] = OMIT,
        cursor: typing.Optional[int] = OMIT,
        default: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        saved: typing.Optional[bool] = OMIT,
        search_type: typing.Optional[SearchModelSearchType] = OMIT,
        time_granularity: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponseModelSearchModel:
        """
        Allows you to manage a search query (save a search query to the **Saved Searches** list under the specified ID, convert a recent search to a saved search, update an existing search). For details on how to manage a saved search, see [Manage Saved Search](/prisma-cloud/docs/cspm/manage-saved-search)

        Required parameters include the search ID, the RQL query, the flag that
        marks this search as saved, and a unique name for the saved search. A best
        practice is to copy data from the results of a search history, update the
        data as necessary, and set the **saved** parameter to **true**.

        This API requires Prisma Cloud system administrator role access if you don't own the search with the given search ID.

        Parameters
        ----------
        id_ : str
            Search ID

        query : str
            RQL Query

        time_range : SearchModelTimeRange
            Time Range

        alert_id : typing.Optional[str]
            Alert ID

        async_ : typing.Optional[bool]
            true = Is Async

        async_result_url : typing.Optional[str]
            Async Result Url

        cloud_type : typing.Optional[SearchModelCloudType]
            Cloud Type

        cursor : typing.Optional[int]
            Cursor

        default : typing.Optional[bool]

        description : typing.Optional[str]
            Search Description

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            View Order

        group_by : typing.Optional[typing.Sequence[str]]
            Group By

        id : typing.Optional[str]
            Search ID

        name : typing.Optional[str]
            Search Name

        read_only : typing.Optional[bool]
            Read Only

        saved : typing.Optional[bool]
            Search Exists

        search_type : typing.Optional[SearchModelSearchType]
            Search Type

        time_granularity : typing.Optional[str]
            Time Granularity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponseModelSearchModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AbsoluteTimeRangeConfigModelValue,
            AsyncFernApi,
            SearchModelTimeRange_Absolute,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_manager.search_history_manage(
                id_="id",
                query="query",
                time_range=SearchModelTimeRange_Absolute(
                    value=AbsoluteTimeRangeConfigModelValue(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_history_manage(
            id_,
            query=query,
            time_range=time_range,
            alert_id=alert_id,
            async_=async_,
            async_result_url=async_result_url,
            cloud_type=cloud_type,
            cursor=cursor,
            default=default,
            description=description,
            filters=filters,
            group_by=group_by,
            id=id,
            name=name,
            read_only=read_only,
            saved=saved,
            search_type=search_type,
            time_granularity=time_granularity,
            request_options=request_options,
        )
        return _response.data

    async def search_history_delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a saved search query.

        Parameters
        ----------
        id : str
            Search ID

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_manager.search_history_delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_history_delete(id, request_options=request_options)
        return _response.data
