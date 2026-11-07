

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawViewOnlyLinksClient, RawViewOnlyLinksClient
from .types.view_only_links_node_list_response_item import ViewOnlyLinksNodeListResponseItem
from .types.view_only_links_read_response import ViewOnlyLinksReadResponse


class ViewOnlyLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawViewOnlyLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawViewOnlyLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawViewOnlyLinksClient
        """
        return self._raw_client

    def read(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ViewOnlyLinksReadResponse:
        """
        Retrieves details about a specific view only link.
        #### Permissions
        Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewOnlyLinksReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.view_only_links.read(
            link_id="link_id",
        )
        """
        _response = self._raw_client.read(link_id, request_options=request_options)
        return _response.data

    def node_list(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ViewOnlyLinksNodeListResponseItem]:
        """

        The list of nodes which this view only link gives read-only access to.
        #### Permissions
        Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ViewOnlyLinksNodeListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.view_only_links.node_list(
            link_id="link_id",
        )
        """
        _response = self._raw_client.node_list(link_id, request_options=request_options)
        return _response.data


class AsyncViewOnlyLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawViewOnlyLinksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawViewOnlyLinksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawViewOnlyLinksClient
        """
        return self._raw_client

    async def read(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ViewOnlyLinksReadResponse:
        """
        Retrieves details about a specific view only link.
        #### Permissions
        Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ViewOnlyLinksReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.view_only_links.read(
                link_id="link_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(link_id, request_options=request_options)
        return _response.data

    async def node_list(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ViewOnlyLinksNodeListResponseItem]:
        """

        The list of nodes which this view only link gives read-only access to.
        #### Permissions
        Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        link_id : str
            The unique identifier of the view only link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ViewOnlyLinksNodeListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.view_only_links.node_list(
                link_id="link_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.node_list(link_id, request_options=request_options)
        return _response.data
