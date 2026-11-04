

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTaxonomiesClient, RawTaxonomiesClient
from .types.taxonomies_list_response_item import TaxonomiesListResponseItem
from .types.taxonomies_read_response import TaxonomiesReadResponse


class TaxonomiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaxonomiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaxonomiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaxonomiesClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TaxonomiesListResponseItem]:
        """

        A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf).
        Note: this API endpoint is under active development, and is subject to change in the future.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include taxonomies that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter['id']='{taxonomy_id}'.

        Taxonomies may be filtered by their `id`, `parents`, and `text`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaxonomiesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.taxonomies.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def read(
        self, taxonomy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaxonomiesReadResponse:
        """
        Retrieves the details of a taxonomy.
        #### Returns

        Returns a JSON object with a `data` key containing the representation of the requested taxonomy, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        taxonomy_id : str
            The unique identifier of the taxonomy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaxonomiesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.taxonomies.read(
            taxonomy_id="taxonomy_id",
        )
        """
        _response = self._raw_client.read(taxonomy_id, request_options=request_options)
        return _response.data


class AsyncTaxonomiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaxonomiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaxonomiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaxonomiesClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TaxonomiesListResponseItem]:
        """

        A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf).
        Note: this API endpoint is under active development, and is subject to change in the future.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include taxonomies that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter['id']='{taxonomy_id}'.

        Taxonomies may be filtered by their `id`, `parents`, and `text`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaxonomiesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.taxonomies.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def read(
        self, taxonomy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaxonomiesReadResponse:
        """
        Retrieves the details of a taxonomy.
        #### Returns

        Returns a JSON object with a `data` key containing the representation of the requested taxonomy, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        taxonomy_id : str
            The unique identifier of the taxonomy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaxonomiesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.taxonomies.read(
                taxonomy_id="taxonomy_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(taxonomy_id, request_options=request_options)
        return _response.data
