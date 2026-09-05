

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bandwidth_allocation import BandwidthAllocation
from ..types.bandwidth_allocation_set import BandwidthAllocationSet
from ..types.bandwidth_allocation_set_v2 import BandwidthAllocationSetV2
from ..types.bandwidth_allocation_v2 import BandwidthAllocationV2
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawBandwidthAllocationsClient, RawBandwidthAllocationsClient


OMIT = typing.cast(typing.Any, ...)


class BandwidthAllocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBandwidthAllocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBandwidthAllocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBandwidthAllocationsClient
        """
        return self._raw_client

    def get_v1bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSet:
        """
        Get the status of aggregated bandwidth regions and allocations, which includes a list of regions and allocations.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSet
            Aggregated bandwidth regions or allocations set.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bandwidth_allocations.get_v1bandwidth_allocations(
            id="id",
        )
        """
        _response = self._raw_client.get_v1bandwidth_allocations(id=id, request_options=request_options)
        return _response.data

    def post_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allocate aggregated bandwidth for the regions based on location data.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
        client.bandwidth_allocations.post_v1bandwidth_allocations()
        """
        _response = self._raw_client.post_v1bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    def put_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify an aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
        client.bandwidth_allocations.put_v1bandwidth_allocations()
        """
        _response = self._raw_client.put_v1bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    def delete_v1bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allows you to delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

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
        client.bandwidth_allocations.delete_v1bandwidth_allocations(
            region="region",
            spn_name="SpnName",
        )
        """
        _response = self._raw_client.delete_v1bandwidth_allocations(
            region=region, spn_name=spn_name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    def get_v1bandwidth_allocations_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSet:
        """
        Retrieve the bandwidth allocation configurations for a specified set of regions.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSet
            List of bandwidth allocation configurations.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bandwidth_allocations.get_v1bandwidth_allocations_read(
            id="id",
        )
        """
        _response = self._raw_client.get_v1bandwidth_allocations_read(id=id, request_options=request_options)
        return _response.data

    def post_v1bandwidth_allocations_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocation_region_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read bandwidth allocation configuration.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocation_region_names : typing.Optional[typing.Sequence[str]]

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
        client.bandwidth_allocations.post_v1bandwidth_allocations_read()
        """
        _response = self._raw_client.post_v1bandwidth_allocations_read(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocation_region_names=bandwidth_allocation_region_names,
            request_options=request_options,
        )
        return _response.data

    def get_v2bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSetV2:
        """
        Get an aggregated bandwidth regions based on the location data.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSetV2
            Status for the given IS

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.bandwidth_allocations.get_v2bandwidth_allocations(
            id="id",
        )
        """
        _response = self._raw_client.get_v2bandwidth_allocations(id=id, request_options=request_options)
        return _response.data

    def post_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Status for the given request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
        client.bandwidth_allocations.post_v2bandwidth_allocations()
        """
        _response = self._raw_client.post_v2bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    def put_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
        client.bandwidth_allocations.put_v2bandwidth_allocations()
        """
        _response = self._raw_client.put_v2bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    def delete_v2bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

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
        client.bandwidth_allocations.delete_v2bandwidth_allocations(
            region="region",
            spn_name="SpnName",
        )
        """
        _response = self._raw_client.delete_v2bandwidth_allocations(
            region=region, spn_name=spn_name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data


class AsyncBandwidthAllocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBandwidthAllocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBandwidthAllocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBandwidthAllocationsClient
        """
        return self._raw_client

    async def get_v1bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSet:
        """
        Get the status of aggregated bandwidth regions and allocations, which includes a list of regions and allocations.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSet
            Aggregated bandwidth regions or allocations set.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bandwidth_allocations.get_v1bandwidth_allocations(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1bandwidth_allocations(id=id, request_options=request_options)
        return _response.data

    async def post_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allocate aggregated bandwidth for the regions based on location data.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
            await client.bandwidth_allocations.post_v1bandwidth_allocations()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    async def put_v1bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocation]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify an aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocation]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
            await client.bandwidth_allocations.put_v1bandwidth_allocations()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_v1bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    async def delete_v1bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Allows you to delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

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
            await client.bandwidth_allocations.delete_v1bandwidth_allocations(
                region="region",
                spn_name="SpnName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_v1bandwidth_allocations(
            region=region, spn_name=spn_name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data

    async def get_v1bandwidth_allocations_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSet:
        """
        Retrieve the bandwidth allocation configurations for a specified set of regions.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSet
            List of bandwidth allocation configurations.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bandwidth_allocations.get_v1bandwidth_allocations_read(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1bandwidth_allocations_read(id=id, request_options=request_options)
        return _response.data

    async def post_v1bandwidth_allocations_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocation_region_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Create a request to read bandwidth allocation configuration.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocation_region_names : typing.Optional[typing.Sequence[str]]

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
            await client.bandwidth_allocations.post_v1bandwidth_allocations_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1bandwidth_allocations_read(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocation_region_names=bandwidth_allocation_region_names,
            request_options=request_options,
        )
        return _response.data

    async def get_v2bandwidth_allocations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BandwidthAllocationSetV2:
        """
        Get an aggregated bandwidth regions based on the location data.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BandwidthAllocationSetV2
            Status for the given IS

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bandwidth_allocations.get_v2bandwidth_allocations(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v2bandwidth_allocations(id=id, request_options=request_options)
        return _response.data

    async def post_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Status for the given request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
            await client.bandwidth_allocations.post_v2bandwidth_allocations()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v2bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    async def put_v2bandwidth_allocations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        bandwidth_allocations: typing.Optional[typing.Sequence[BandwidthAllocationV2]] = OMIT,
        uuid_: typing.Optional[UuidResponse] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Modify aggregated bandwidth regions.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        bandwidth_allocations : typing.Optional[typing.Sequence[BandwidthAllocationV2]]
            bandwidth allocations

        uuid_ : typing.Optional[UuidResponse]

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
            await client.bandwidth_allocations.put_v2bandwidth_allocations()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_v2bandwidth_allocations(
            sub_tenant_name=sub_tenant_name,
            bandwidth_allocations=bandwidth_allocations,
            uuid_=uuid_,
            request_options=request_options,
        )
        return _response.data

    async def delete_v2bandwidth_allocations(
        self,
        *,
        region: str,
        spn_name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Delete an aggregated bandwidth region.

        Parameters
        ----------
        region : str
            The aggregate bandwidth region.

        spn_name : str
            The IPSec termination node.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

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
            await client.bandwidth_allocations.delete_v2bandwidth_allocations(
                region="region",
                spn_name="SpnName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_v2bandwidth_allocations(
            region=region, spn_name=spn_name, sub_tenant_name=sub_tenant_name, request_options=request_options
        )
        return _response.data
