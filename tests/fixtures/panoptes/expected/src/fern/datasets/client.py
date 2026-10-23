

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_set import DataSet
from .raw_client import AsyncRawDatasetsClient, RawDatasetsClient
from .types.get_datasets_dataset_name_details_item_id_response import GetDatasetsDatasetNameDetailsItemIdResponse
from .types.post_datasets_dataset_name_search_request_facets_value import (
    PostDatasetsDatasetNameSearchRequestFacetsValue,
)
from .types.post_datasets_dataset_name_search_response import PostDatasetsDatasetNameSearchResponse


OMIT = typing.cast(typing.Any, ...)


class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetsClient
        """
        return self._raw_client

    def get_available_data_sets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DataSet]:
        """
        Get the available data sets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataSet]
            Available data sets results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.datasets.get_available_data_sets()
        """
        _response = self._raw_client.get_available_data_sets(request_options=request_options)
        return _response.data

    def search_dataset(
        self,
        dataset_name: str,
        *,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameSearchRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDatasetsDatasetNameSearchResponse:
        """
        Search in the index of the dataset.

        Parameters
        ----------
        dataset_name : str

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        query : typing.Optional[str]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameSearchRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDatasetsDatasetNameSearchResponse
            Search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.datasets.search_dataset(
            dataset_name="dataset_name",
        )
        """
        _response = self._raw_client.search_dataset(
            dataset_name, offset=offset, limit=limit, query=query, facets=facets, request_options=request_options
        )
        return _response.data

    def get_item_details(
        self, dataset_name: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDatasetsDatasetNameDetailsItemIdResponse:
        """
        Get the details for a specific item in the dataset.

        Parameters
        ----------
        dataset_name : str

        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDatasetsDatasetNameDetailsItemIdResponse
            Item details

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.datasets.get_item_details(
            dataset_name="dataset_name",
            item_id="item_id",
        )
        """
        _response = self._raw_client.get_item_details(dataset_name, item_id, request_options=request_options)
        return _response.data


class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetsClient
        """
        return self._raw_client

    async def get_available_data_sets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DataSet]:
        """
        Get the available data sets.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataSet]
            Available data sets results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.datasets.get_available_data_sets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_available_data_sets(request_options=request_options)
        return _response.data

    async def search_dataset(
        self,
        dataset_name: str,
        *,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[str] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameSearchRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDatasetsDatasetNameSearchResponse:
        """
        Search in the index of the dataset.

        Parameters
        ----------
        dataset_name : str

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        query : typing.Optional[str]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameSearchRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDatasetsDatasetNameSearchResponse
            Search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.datasets.search_dataset(
                dataset_name="dataset_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_dataset(
            dataset_name, offset=offset, limit=limit, query=query, facets=facets, request_options=request_options
        )
        return _response.data

    async def get_item_details(
        self, dataset_name: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDatasetsDatasetNameDetailsItemIdResponse:
        """
        Get the details for a specific item in the dataset.

        Parameters
        ----------
        dataset_name : str

        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDatasetsDatasetNameDetailsItemIdResponse
            Item details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.datasets.get_item_details(
                dataset_name="dataset_name",
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item_details(dataset_name, item_id, request_options=request_options)
        return _response.data
