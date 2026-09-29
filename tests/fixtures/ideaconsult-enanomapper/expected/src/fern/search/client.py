

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.solr_response import SolrResponse
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.solrquery_get_request_wt import SolrqueryGetRequestWt
from .types.solrquery_post_request_params import SolrqueryPostRequestParams
from .types.solrquery_post_request_wt import SolrqueryPostRequestWt


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def solrquery_get(
        self,
        *,
        q: typing.Optional[str] = None,
        fq: typing.Optional[str] = None,
        fl: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        rows: typing.Optional[int] = None,
        wt: typing.Optional[SolrqueryGetRequestWt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolrResponse:
        """
        GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.

        Parameters
        ----------
        q : typing.Optional[str]
            The query

        fq : typing.Optional[str]
            Filter query

        fl : typing.Optional[str]
            Field list

        start : typing.Optional[int]
            Starting page

        rows : typing.Optional[int]
            Page size

        wt : typing.Optional[SolrqueryGetRequestWt]
            Response format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolrResponse
            Query performed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search.solrquery_get(
            q="*:*",
            fl="*",
        )
        """
        _response = self._raw_client.solrquery_get(
            q=q, fq=fq, fl=fl, start=start, rows=rows, wt=wt, request_options=request_options
        )
        return _response.data

    def solrquery_post(
        self,
        *,
        wt: typing.Optional[SolrqueryPostRequestWt] = None,
        facet: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        params: typing.Optional[SolrqueryPostRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolrResponse:
        """
        POST is more complex to use, but also allows for much for complex and lengthy queries.

        Parameters
        ----------
        wt : typing.Optional[SolrqueryPostRequestWt]
            Response format

        facet : typing.Optional[typing.Dict[str, typing.Any]]

        params : typing.Optional[SolrqueryPostRequestParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolrResponse
            Query performed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.search.solrquery_post()
        """
        _response = self._raw_client.solrquery_post(wt=wt, facet=facet, params=params, request_options=request_options)
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def solrquery_get(
        self,
        *,
        q: typing.Optional[str] = None,
        fq: typing.Optional[str] = None,
        fl: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        rows: typing.Optional[int] = None,
        wt: typing.Optional[SolrqueryGetRequestWt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolrResponse:
        """
        GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.

        Parameters
        ----------
        q : typing.Optional[str]
            The query

        fq : typing.Optional[str]
            Filter query

        fl : typing.Optional[str]
            Field list

        start : typing.Optional[int]
            Starting page

        rows : typing.Optional[int]
            Page size

        wt : typing.Optional[SolrqueryGetRequestWt]
            Response format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolrResponse
            Query performed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search.solrquery_get(
                q="*:*",
                fl="*",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.solrquery_get(
            q=q, fq=fq, fl=fl, start=start, rows=rows, wt=wt, request_options=request_options
        )
        return _response.data

    async def solrquery_post(
        self,
        *,
        wt: typing.Optional[SolrqueryPostRequestWt] = None,
        facet: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        params: typing.Optional[SolrqueryPostRequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolrResponse:
        """
        POST is more complex to use, but also allows for much for complex and lengthy queries.

        Parameters
        ----------
        wt : typing.Optional[SolrqueryPostRequestWt]
            Response format

        facet : typing.Optional[typing.Dict[str, typing.Any]]

        params : typing.Optional[SolrqueryPostRequestParams]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolrResponse
            Query performed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.search.solrquery_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.solrquery_post(
            wt=wt, facet=facet, params=params, request_options=request_options
        )
        return _response.data
