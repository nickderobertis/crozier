

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChannelIngressClient, RawChannelIngressClient
from .types.channel_ingress_approve_response import ChannelIngressApproveResponse
from .types.channel_ingress_list_response import ChannelIngressListResponse
from .types.channel_ingress_revoke_response import ChannelIngressRevokeResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelIngressClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelIngressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelIngressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelIngressClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChannelIngressListResponse:
        """
        Every declaration the gateway can see, each with the digest a guardian would approve, the public paths it would open, and the credential its signatures are verified against. This is the only way to learn that a declaration is waiting: on the public surface a route held back by approval 404s exactly like one nobody declared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.channel_ingress.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def approve(
        self, source: str, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelIngressApproveResponse:
        """
        Records the guardian's approval of the declaration identified by the body's digest, after which the gateway serves its routes. Returns 409 when the digest is not what the source currently declares, and 404 when it declares nothing servable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressApproveResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.channel_ingress.approve(
            source="source",
            digest="digest",
        )
        """
        _response = self._raw_client.approve(source, digest=digest, request_options=request_options)
        return _response.data

    def revoke(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelIngressRevokeResponse:
        """
        Withdraws the source's grant, after which its routes stop being served. Reports whether there was a grant to withdraw. Succeeds even when the declaration itself has become unreadable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressRevokeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.channel_ingress.revoke(
            source="source",
        )
        """
        _response = self._raw_client.revoke(source, request_options=request_options)
        return _response.data


class AsyncChannelIngressClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelIngressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelIngressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelIngressClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ChannelIngressListResponse:
        """
        Every declaration the gateway can see, each with the digest a guardian would approve, the public paths it would open, and the credential its signatures are verified against. This is the only way to learn that a declaration is waiting: on the public surface a route held back by approval 404s exactly like one nobody declared.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_ingress.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def approve(
        self, source: str, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelIngressApproveResponse:
        """
        Records the guardian's approval of the declaration identified by the body's digest, after which the gateway serves its routes. Returns 409 when the digest is not what the source currently declares, and 404 when it declares nothing servable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressApproveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_ingress.approve(
                source="source",
                digest="digest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve(source, digest=digest, request_options=request_options)
        return _response.data

    async def revoke(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelIngressRevokeResponse:
        """
        Withdraws the source's grant, after which its routes stop being served. Reports whether there was a grant to withdraw. Succeeds even when the declaration itself has become unreadable.

        Parameters
        ----------
        source : str
            The declaring ingress source (today, a plugin name)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelIngressRevokeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_ingress.revoke(
                source="source",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(source, request_options=request_options)
        return _response.data
