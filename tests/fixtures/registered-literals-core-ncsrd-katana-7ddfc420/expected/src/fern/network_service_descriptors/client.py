

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.nsd import Nsd
from .raw_client import AsyncRawNetworkServiceDescriptorsClient, RawNetworkServiceDescriptorsClient


class NetworkServiceDescriptorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetworkServiceDescriptorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetworkServiceDescriptorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetworkServiceDescriptorsClient
        """
        return self._raw_client

    def returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
        self,
        *,
        nsd_id: typing.Optional[str] = None,
        nfvo_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Nsd]:
        """
        Parameters
        ----------
        nsd_id : typing.Optional[str]
            The id for a specific NSD

        nfvo_id : typing.Optional[str]
            The id for a specific NFVO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Nsd]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network_service_descriptors.returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm()
        """
        _response = self._raw_client.returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
            nsd_id=nsd_id, nfvo_id=nfvo_id, request_options=request_options
        )
        return _response.data


class AsyncNetworkServiceDescriptorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetworkServiceDescriptorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetworkServiceDescriptorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetworkServiceDescriptorsClient
        """
        return self._raw_client

    async def returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
        self,
        *,
        nsd_id: typing.Optional[str] = None,
        nfvo_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Nsd]:
        """
        Parameters
        ----------
        nsd_id : typing.Optional[str]
            The id for a specific NSD

        nfvo_id : typing.Optional[str]
            The id for a specific NFVO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Nsd]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.network_service_descriptors.returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
            nsd_id=nsd_id, nfvo_id=nfvo_id, request_options=request_options
        )
        return _response.data
