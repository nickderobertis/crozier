

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.remote_networks_ipsec_tunnel import RemoteNetworksIpsecTunnel
from ..types.remote_networks_read_result import RemoteNetworksReadResult
from ..types.remote_networks_response import RemoteNetworksResponse
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawRemoteNetworksClient, RawRemoteNetworksClient


OMIT = typing.cast(typing.Any, ...)


class RemoteNetworksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRemoteNetworksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRemoteNetworksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRemoteNetworksClient
        """
        return self._raw_client

    def get_v1remote_networks(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteNetworksResponse:
        """
        Get remote networks IPSec tunnel details for create, modify, or delete by ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteNetworksResponse
            Remote networks IPSEC tunnel details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.remote_networks.get_v1remote_networks(
            id="id",
        )
        """
        _response = self._raw_client.get_v1remote_networks(id=id, request_options=request_options)
        return _response.data

    def post_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create  remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

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
        client.remote_networks.post_v1remote_networks(
            name="name",
        )
        """
        _response = self._raw_client.post_v1remote_networks(
            name=name,
            sub_tenant_name=sub_tenant_name,
            remote_networks_ipsec_tunnels=remote_networks_ipsec_tunnels,
            request_options=request_options,
        )
        return _response.data

    def put_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

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
        client.remote_networks.put_v1remote_networks(
            name="name",
        )
        """
        _response = self._raw_client.put_v1remote_networks(
            name=name,
            sub_tenant_name=sub_tenant_name,
            remote_networks_ipsec_tunnels=remote_networks_ipsec_tunnels,
            request_options=request_options,
        )
        return _response.data

    def delete_v1remote_networks(
        self,
        *,
        remote_networks_prefix: str,
        sub_tenant_name: typing.Optional[str] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allows you to delete the set of IPSec tunnels.

        Parameters
        ----------
        remote_networks_prefix : str
            remote networks prefix for bulk deletion

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of remote networks along with their names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.remote_networks.delete_v1remote_networks(
            remote_networks_prefix="remote_networks_prefix",
        )
        """
        _response = self._raw_client.delete_v1remote_networks(
            remote_networks_prefix=remote_networks_prefix,
            sub_tenant_name=sub_tenant_name,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def get_v1remote_networks_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteNetworksReadResult:
        """
        Read the remote networks IPSec tunnel status by UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteNetworksReadResult
            Get the remote networks IPSEC tunnel status by UUID.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.remote_networks.get_v1remote_networks_read(
            id="id",
        )
        """
        _response = self._raw_client.get_v1remote_networks_read(id=id, request_options=request_options)
        return _response.data

    def post_v1remote_networks_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read remote network IPSec tunnels.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_names : typing.Optional[typing.Sequence[str]]

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
        client.remote_networks.post_v1remote_networks_read()
        """
        _response = self._raw_client.post_v1remote_networks_read(
            sub_tenant_name=sub_tenant_name,
            remote_networks_names=remote_networks_names,
            request_options=request_options,
        )
        return _response.data


class AsyncRemoteNetworksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRemoteNetworksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRemoteNetworksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRemoteNetworksClient
        """
        return self._raw_client

    async def get_v1remote_networks(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteNetworksResponse:
        """
        Get remote networks IPSec tunnel details for create, modify, or delete by ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteNetworksResponse
            Remote networks IPSEC tunnel details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.remote_networks.get_v1remote_networks(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1remote_networks(id=id, request_options=request_options)
        return _response.data

    async def post_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create  remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

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
            await client.remote_networks.post_v1remote_networks(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1remote_networks(
            name=name,
            sub_tenant_name=sub_tenant_name,
            remote_networks_ipsec_tunnels=remote_networks_ipsec_tunnels,
            request_options=request_options,
        )
        return _response.data

    async def put_v1remote_networks(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_ipsec_tunnels: typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify remote network IPSec tunnels.

        Parameters
        ----------
        name : str
            provide a name to use as a suffix for bulk operations

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_ipsec_tunnels : typing.Optional[typing.Sequence[RemoteNetworksIpsecTunnel]]

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
            await client.remote_networks.put_v1remote_networks(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_v1remote_networks(
            name=name,
            sub_tenant_name=sub_tenant_name,
            remote_networks_ipsec_tunnels=remote_networks_ipsec_tunnels,
            request_options=request_options,
        )
        return _response.data

    async def delete_v1remote_networks(
        self,
        *,
        remote_networks_prefix: str,
        sub_tenant_name: typing.Optional[str] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allows you to delete the set of IPSec tunnels.

        Parameters
        ----------
        remote_networks_prefix : str
            remote networks prefix for bulk deletion

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of remote networks along with their names.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.remote_networks.delete_v1remote_networks(
                remote_networks_prefix="remote_networks_prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_v1remote_networks(
            remote_networks_prefix=remote_networks_prefix,
            sub_tenant_name=sub_tenant_name,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def get_v1remote_networks_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteNetworksReadResult:
        """
        Read the remote networks IPSec tunnel status by UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteNetworksReadResult
            Get the remote networks IPSEC tunnel status by UUID.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.remote_networks.get_v1remote_networks_read(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1remote_networks_read(id=id, request_options=request_options)
        return _response.data

    async def post_v1remote_networks_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        remote_networks_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read remote network IPSec tunnels.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        remote_networks_names : typing.Optional[typing.Sequence[str]]

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
            await client.remote_networks.post_v1remote_networks_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1remote_networks_read(
            sub_tenant_name=sub_tenant_name,
            remote_networks_names=remote_networks_names,
            request_options=request_options,
        )
        return _response.data
