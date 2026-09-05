

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawIkeGatewayClient, RawIkeGatewayClient
from .types.get_v1ike_gateways_read_response import GetV1IkeGatewaysReadResponse


OMIT = typing.cast(typing.Any, ...)


class IkeGatewayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIkeGatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIkeGatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIkeGatewayClient
        """
        return self._raw_client

    def get_v1ike_gateways_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IkeGatewaysReadResponse:
        """
        Retrieve the list of IKE gateway configurations for the specified UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IkeGatewaysReadResponse
            List of ike gateways configurations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_gateway.get_v1ike_gateways_read(
            id="id",
        )
        """
        _response = self._raw_client.get_v1ike_gateways_read(id=id, request_options=request_options)
        return _response.data

    def post_v1ike_gateways_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_gateways_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Request to read the remote network IKE gateways for the specified IKE gateway names.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_gateways_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ike_gateway.post_v1ike_gateways_read()
        """
        _response = self._raw_client.post_v1ike_gateways_read(
            sub_tenant_name=sub_tenant_name, ike_gateways_names=ike_gateways_names, request_options=request_options
        )
        return _response.data


class AsyncIkeGatewayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIkeGatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIkeGatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIkeGatewayClient
        """
        return self._raw_client

    async def get_v1ike_gateways_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IkeGatewaysReadResponse:
        """
        Retrieve the list of IKE gateway configurations for the specified UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IkeGatewaysReadResponse
            List of ike gateways configurations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_gateway.get_v1ike_gateways_read(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1ike_gateways_read(id=id, request_options=request_options)
        return _response.data

    async def post_v1ike_gateways_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_gateways_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Request to read the remote network IKE gateways for the specified IKE gateway names.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_gateways_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ike_gateway.post_v1ike_gateways_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1ike_gateways_read(
            sub_tenant_name=sub_tenant_name, ike_gateways_names=ike_gateways_names, request_options=request_options
        )
        return _response.data
