

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPubkeyClient, RawPubkeyClient


class PubkeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPubkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPubkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPubkeyClient
        """
        return self._raw_client

    def get_public_key(
        self, *, tree_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the public key that can be used to validate the signed tree head

        Parameters
        ----------
        tree_id : typing.Optional[str]
            The tree ID of the tree you wish to get a public key for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.pubkey.get_public_key()
        """
        _response = self._raw_client.get_public_key(tree_id=tree_id, request_options=request_options)
        return _response.data


class AsyncPubkeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPubkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPubkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPubkeyClient
        """
        return self._raw_client

    async def get_public_key(
        self, *, tree_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the public key that can be used to validate the signed tree head

        Parameters
        ----------
        tree_id : typing.Optional[str]
            The tree ID of the tree you wish to get a public key for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.pubkey.get_public_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_public_key(tree_id=tree_id, request_options=request_options)
        return _response.data
