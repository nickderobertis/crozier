

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tunnel_port_info_result import TunnelPortInfoResult
from .raw_client import AsyncRawTunnelClient, RawTunnelClient


class TunnelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTunnelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTunnelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTunnelClient
        """
        return self._raw_client

    def get_api_v1tunnel_environment_id_port_info(
        self,
        environment_id: str,
        *,
        port_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TunnelPortInfoResult:
        """
        Parameters
        ----------
        environment_id : str

        port_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TunnelPortInfoResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tunnel.get_api_v1tunnel_environment_id_port_info(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1tunnel_environment_id_port_info(
            environment_id, port_number=port_number, request_options=request_options
        )
        return _response.data


class AsyncTunnelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTunnelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTunnelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTunnelClient
        """
        return self._raw_client

    async def get_api_v1tunnel_environment_id_port_info(
        self,
        environment_id: str,
        *,
        port_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TunnelPortInfoResult:
        """
        Parameters
        ----------
        environment_id : str

        port_number : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TunnelPortInfoResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tunnel.get_api_v1tunnel_environment_id_port_info(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tunnel_environment_id_port_info(
            environment_id, port_number=port_number, request_options=request_options
        )
        return _response.data
