

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tree_node import TreeNode
from .raw_client import AsyncRawTreeClient, RawTreeClient


OMIT = typing.cast(typing.Any, ...)


class TreeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTreeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTreeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTreeClient
        """
        return self._raw_client

    def put_tree(
        self,
        *,
        value: typing.Optional[str] = OMIT,
        children: typing.Optional[typing.Sequence[TreeNode]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        value : typing.Optional[str]

        children : typing.Optional[typing.Sequence[TreeNode]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tree.put_tree()
        """
        _response = self._raw_client.put_tree(value=value, children=children, request_options=request_options)
        return _response.data


class AsyncTreeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTreeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTreeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTreeClient
        """
        return self._raw_client

    async def put_tree(
        self,
        *,
        value: typing.Optional[str] = OMIT,
        children: typing.Optional[typing.Sequence[TreeNode]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        value : typing.Optional[str]

        children : typing.Optional[typing.Sequence[TreeNode]]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tree.put_tree()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_tree(value=value, children=children, request_options=request_options)
        return _response.data
