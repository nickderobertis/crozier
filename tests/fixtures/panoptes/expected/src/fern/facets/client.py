

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.facet_result import FacetResult
from .raw_client import AsyncRawFacetsClient, RawFacetsClient
from .types.get_datasets_dataset_name_facets_response_item import GetDatasetsDatasetNameFacetsResponseItem
from .types.post_datasets_dataset_name_facet_request_facets_value import PostDatasetsDatasetNameFacetRequestFacetsValue
from .types.post_datasets_dataset_name_facet_request_sort import PostDatasetsDatasetNameFacetRequestSort


OMIT = typing.cast(typing.Any, ...)


class FacetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFacetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFacetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFacetsClient
        """
        return self._raw_client

    def get_facets(
        self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatasetsDatasetNameFacetsResponseItem]:
        """
        Get the facets used in this dataset.

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatasetsDatasetNameFacetsResponseItem]
            Facets

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.facets.get_facets(
            dataset_name="dataset_name",
        )
        """
        _response = self._raw_client.get_facets(dataset_name, request_options=request_options)
        return _response.data

    def get_facet_options(
        self,
        dataset_name: str,
        *,
        name: typing.Optional[str] = OMIT,
        amount: typing.Optional[int] = OMIT,
        filter: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostDatasetsDatasetNameFacetRequestSort] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FacetResult]:
        """
        Get the available options for a specific facet.

        Parameters
        ----------
        dataset_name : str

        name : typing.Optional[str]
            The Facet for which to get options

        amount : typing.Optional[int]
            How many results to retrieve

        filter : typing.Optional[str]
            String to filter results on. For searching in the list of facet options.

        query : typing.Optional[str]
            Text query used for filtering search results (not facet options). Used to make sure the counts reflect the actual search results.

        sort : typing.Optional[PostDatasetsDatasetNameFacetRequestSort]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FacetResult]
            Facet results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.facets.get_facet_options(
            dataset_name="dataset_name",
        )
        """
        _response = self._raw_client.get_facet_options(
            dataset_name,
            name=name,
            amount=amount,
            filter=filter,
            query=query,
            sort=sort,
            facets=facets,
            request_options=request_options,
        )
        return _response.data


class AsyncFacetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFacetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFacetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFacetsClient
        """
        return self._raw_client

    async def get_facets(
        self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatasetsDatasetNameFacetsResponseItem]:
        """
        Get the facets used in this dataset.

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatasetsDatasetNameFacetsResponseItem]
            Facets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.facets.get_facets(
                dataset_name="dataset_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_facets(dataset_name, request_options=request_options)
        return _response.data

    async def get_facet_options(
        self,
        dataset_name: str,
        *,
        name: typing.Optional[str] = OMIT,
        amount: typing.Optional[int] = OMIT,
        filter: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        sort: typing.Optional[PostDatasetsDatasetNameFacetRequestSort] = OMIT,
        facets: typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FacetResult]:
        """
        Get the available options for a specific facet.

        Parameters
        ----------
        dataset_name : str

        name : typing.Optional[str]
            The Facet for which to get options

        amount : typing.Optional[int]
            How many results to retrieve

        filter : typing.Optional[str]
            String to filter results on. For searching in the list of facet options.

        query : typing.Optional[str]
            Text query used for filtering search results (not facet options). Used to make sure the counts reflect the actual search results.

        sort : typing.Optional[PostDatasetsDatasetNameFacetRequestSort]

        facets : typing.Optional[typing.Dict[str, PostDatasetsDatasetNameFacetRequestFacetsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FacetResult]
            Facet results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.facets.get_facet_options(
                dataset_name="dataset_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_facet_options(
            dataset_name,
            name=name,
            amount=amount,
            filter=filter,
            query=query,
            sort=sort,
            facets=facets,
            request_options=request_options,
        )
        return _response.data
