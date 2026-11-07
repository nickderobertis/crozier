

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.azure_location import AzureLocation
from ..types.resource_subtype import ResourceSubtype
from ..types.resource_type import ResourceType
from .raw_client import AsyncRawVnetPoolDefinitionsClient, RawVnetPoolDefinitionsClient


OMIT = typing.cast(typing.Any, ...)


class VnetPoolDefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVnetPoolDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVnetPoolDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVnetPoolDefinitionsClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_vnet_pool_definitions(
        self,
        *,
        dimensions: typing.Dict[str, typing.Optional[str]],
        is_enabled: bool,
        location: AzureLocation,
        subtype: ResourceSubtype,
        target_count: int,
        type: ResourceType,
        logical_skus: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        dimensions : typing.Dict[str, typing.Optional[str]]

        is_enabled : bool

        location : AzureLocation

        subtype : ResourceSubtype

        target_count : int

        type : ResourceType

        logical_skus : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vnet_pool_definitions.post_api_v1geneva_actions_vnet_pool_definitions(
            dimensions={},
            is_enabled=True,
            location=1,
            subtype=1,
            target_count=1,
            type=1,
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_vnet_pool_definitions(
            dimensions=dimensions,
            is_enabled=is_enabled,
            location=location,
            subtype=subtype,
            target_count=target_count,
            type=type,
            logical_skus=logical_skus,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v1geneva_actions_vnet_pool_definitions(
        self,
        *,
        dimensions: typing.Dict[str, typing.Optional[str]],
        is_enabled: bool,
        location: AzureLocation,
        subtype: ResourceSubtype,
        target_count: int,
        type: ResourceType,
        logical_skus: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        dimensions : typing.Dict[str, typing.Optional[str]]

        is_enabled : bool

        location : AzureLocation

        subtype : ResourceSubtype

        target_count : int

        type : ResourceType

        logical_skus : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vnet_pool_definitions.delete_api_v1geneva_actions_vnet_pool_definitions(
            dimensions={},
            is_enabled=True,
            location=1,
            subtype=1,
            target_count=1,
            type=1,
        )
        """
        _response = self._raw_client.delete_api_v1geneva_actions_vnet_pool_definitions(
            dimensions=dimensions,
            is_enabled=is_enabled,
            location=location,
            subtype=subtype,
            target_count=target_count,
            type=type,
            logical_skus=logical_skus,
            request_options=request_options,
        )
        return _response.data


class AsyncVnetPoolDefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVnetPoolDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVnetPoolDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVnetPoolDefinitionsClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_vnet_pool_definitions(
        self,
        *,
        dimensions: typing.Dict[str, typing.Optional[str]],
        is_enabled: bool,
        location: AzureLocation,
        subtype: ResourceSubtype,
        target_count: int,
        type: ResourceType,
        logical_skus: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        dimensions : typing.Dict[str, typing.Optional[str]]

        is_enabled : bool

        location : AzureLocation

        subtype : ResourceSubtype

        target_count : int

        type : ResourceType

        logical_skus : typing.Optional[typing.Sequence[str]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vnet_pool_definitions.post_api_v1geneva_actions_vnet_pool_definitions(
                dimensions={},
                is_enabled=True,
                location=1,
                subtype=1,
                target_count=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_vnet_pool_definitions(
            dimensions=dimensions,
            is_enabled=is_enabled,
            location=location,
            subtype=subtype,
            target_count=target_count,
            type=type,
            logical_skus=logical_skus,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v1geneva_actions_vnet_pool_definitions(
        self,
        *,
        dimensions: typing.Dict[str, typing.Optional[str]],
        is_enabled: bool,
        location: AzureLocation,
        subtype: ResourceSubtype,
        target_count: int,
        type: ResourceType,
        logical_skus: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        dimensions : typing.Dict[str, typing.Optional[str]]

        is_enabled : bool

        location : AzureLocation

        subtype : ResourceSubtype

        target_count : int

        type : ResourceType

        logical_skus : typing.Optional[typing.Sequence[str]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vnet_pool_definitions.delete_api_v1geneva_actions_vnet_pool_definitions(
                dimensions={},
                is_enabled=True,
                location=1,
                subtype=1,
                target_count=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1geneva_actions_vnet_pool_definitions(
            dimensions=dimensions,
            is_enabled=is_enabled,
            location=location,
            subtype=subtype,
            target_count=target_count,
            type=type,
            logical_skus=logical_skus,
            request_options=request_options,
        )
        return _response.data
