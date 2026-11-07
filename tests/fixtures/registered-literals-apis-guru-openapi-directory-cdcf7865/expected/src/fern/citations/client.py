

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCitationsClient, RawCitationsClient
from .types.citations_styles_list_response_item import CitationsStylesListResponseItem
from .types.citations_styles_read_response import CitationsStylesReadResponse


class CitationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCitationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCitationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCitationsClient
        """
        return self._raw_client

    def styles_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CitationsStylesListResponseItem]:
        """

        A paginated list of all standard citation styles available for rendering citations.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 citation styles. Each resource in the array is a separate citation syle and contains the full representation of the citation style object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/citations/styles/?filter[title]=open.

        Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CitationsStylesListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.citations.styles_list()
        """
        _response = self._raw_client.styles_list(request_options=request_options)
        return _response.data

    def styles_read(
        self, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CitationsStylesReadResponse:
        """
        Retrieves the details of a citation style.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested citation style, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CitationsStylesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.citations.styles_read(
            style_id="style_id",
        )
        """
        _response = self._raw_client.styles_read(style_id, request_options=request_options)
        return _response.data


class AsyncCitationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCitationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCitationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCitationsClient
        """
        return self._raw_client

    async def styles_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CitationsStylesListResponseItem]:
        """

        A paginated list of all standard citation styles available for rendering citations.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of 10 citation styles. Each resource in the array is a separate citation syle and contains the full representation of the citation style object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/citations/styles/?filter[title]=open.

        Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CitationsStylesListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.citations.styles_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.styles_list(request_options=request_options)
        return _response.data

    async def styles_read(
        self, style_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CitationsStylesReadResponse:
        """
        Retrieves the details of a citation style.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested citation style, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        style_id : str
            The unique identifier of the citation style.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CitationsStylesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.citations.styles_read(
                style_id="style_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.styles_read(style_id, request_options=request_options)
        return _response.data
