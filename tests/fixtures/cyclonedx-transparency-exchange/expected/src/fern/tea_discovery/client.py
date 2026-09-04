

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.discovery_info import DiscoveryInfo
from .raw_client import AsyncRawTeaDiscoveryClient, RawTeaDiscoveryClient


class TeaDiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeaDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeaDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeaDiscoveryClient
        """
        return self._raw_client

    def discovery_by_tei(
        self, *, tei: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DiscoveryInfo]:
        """
        Discovery endpoint which resolves TEI into product release UUID.

        Parameters
        ----------
        tei : str
            Transparency Exchange Identifier (TEI) for the product being discovered. Provide the TEI as a URL-encoded string per RFC 3986, RFC 3987.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DiscoveryInfo]
            Discovery information for the requested TEI

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_discovery.discovery_by_tei(
            tei="urn%3Atei%3Auuid%3Aproducts.example.com%3Ad4d9f54a-abcf-11ee-ac79-1a52914d44b",
        )
        """
        _response = self._raw_client.discovery_by_tei(tei=tei, request_options=request_options)
        return _response.data


class AsyncTeaDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeaDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeaDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeaDiscoveryClient
        """
        return self._raw_client

    async def discovery_by_tei(
        self, *, tei: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DiscoveryInfo]:
        """
        Discovery endpoint which resolves TEI into product release UUID.

        Parameters
        ----------
        tei : str
            Transparency Exchange Identifier (TEI) for the product being discovered. Provide the TEI as a URL-encoded string per RFC 3986, RFC 3987.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DiscoveryInfo]
            Discovery information for the requested TEI

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_discovery.discovery_by_tei(
                tei="urn%3Atei%3Auuid%3Aproducts.example.com%3Ad4d9f54a-abcf-11ee-ac79-1a52914d44b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.discovery_by_tei(tei=tei, request_options=request_options)
        return _response.data
