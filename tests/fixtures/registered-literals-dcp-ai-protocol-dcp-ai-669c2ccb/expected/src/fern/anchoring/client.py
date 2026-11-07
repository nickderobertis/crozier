

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.anchor_receipt import AnchorReceipt
from .raw_client import AsyncRawAnchoringClient, RawAnchoringClient
from .types.anchor_hash_request_chain import AnchorHashRequestChain


OMIT = typing.cast(typing.Any, ...)


class AnchoringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnchoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnchoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnchoringClient
        """
        return self._raw_client

    def anchor_hash(
        self,
        *,
        bundle_hash: str,
        chain: typing.Optional[AnchorHashRequestChain] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchorReceipt:
        """
        Anchors a bundle hash (or batch of hashes) to an L2 blockchain.
        Returns 501 on the reference gateway; use the anchor service (port 3001) directly.

        Parameters
        ----------
        bundle_hash : str

        chain : typing.Optional[AnchorHashRequestChain]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchorReceipt
            Anchor receipt

        Examples
        --------
        from fern.anchoring import AnchorHashRequestChain

        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.anchoring.anchor_hash(
            bundle_hash="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            chain=AnchorHashRequestChain.BASE,
        )
        """
        _response = self._raw_client.anchor_hash(bundle_hash=bundle_hash, chain=chain, request_options=request_options)
        return _response.data


class AsyncAnchoringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnchoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnchoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnchoringClient
        """
        return self._raw_client

    async def anchor_hash(
        self,
        *,
        bundle_hash: str,
        chain: typing.Optional[AnchorHashRequestChain] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnchorReceipt:
        """
        Anchors a bundle hash (or batch of hashes) to an L2 blockchain.
        Returns 501 on the reference gateway; use the anchor service (port 3001) directly.

        Parameters
        ----------
        bundle_hash : str

        chain : typing.Optional[AnchorHashRequestChain]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnchorReceipt
            Anchor receipt

        Examples
        --------
        import asyncio

        from fern.anchoring import AnchorHashRequestChain

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.anchoring.anchor_hash(
                bundle_hash="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                chain=AnchorHashRequestChain.BASE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.anchor_hash(
            bundle_hash=bundle_hash, chain=chain, request_options=request_options
        )
        return _response.data
