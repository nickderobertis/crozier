

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.registry_settlement import RegistrySettlement
from ..types.registry_settlement_create import RegistrySettlementCreate
from ..types.registry_settlement_listing import RegistrySettlementListing
from ..types.registry_settlement_read import RegistrySettlementRead
from .raw_client import AsyncRawRegistrySettlementClient, RawRegistrySettlementClient


OMIT = typing.cast(typing.Any, ...)


class RegistrySettlementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistrySettlementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistrySettlementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistrySettlementClient
        """
        return self._raw_client

    def list_all_registry_settlement_for_user_registry(
        self, user_id: int, registry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RegistrySettlementListing]:
        """
        Get a listing of all Slice group settlements.

        Parameters
        ----------
        user_id : int


        registry_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RegistrySettlementListing]
            Used to settle a Slice group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.registry_settlement.list_all_registry_settlement_for_user_registry(
            user_id=1,
            registry_id=1,
        )
        """
        _response = self._raw_client.list_all_registry_settlement_for_user_registry(
            user_id, registry_id, request_options=request_options
        )
        return _response.data

    def create_registry_settlement_for_user_registry(
        self,
        user_id: int,
        registry_id: int,
        *,
        request: RegistrySettlement,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistrySettlementCreate:
        """
        Create a new Slice group settlement.

        Parameters
        ----------
        user_id : int


        registry_id : int


        request : RegistrySettlement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrySettlementCreate
            Used to settle a Slice group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.registry_settlement.create_registry_settlement_for_user_registry(
            user_id=1,
            registry_id=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_registry_settlement_for_user_registry(
            user_id, registry_id, request=request, request_options=request_options
        )
        return _response.data

    def read_registry_settlement_for_user_registry(
        self, user_id: int, registry_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistrySettlementRead:
        """
        Get a specific Slice group settlement.

        Parameters
        ----------
        user_id : int


        registry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrySettlementRead
            Used to settle a Slice group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.registry_settlement.read_registry_settlement_for_user_registry(
            user_id=1,
            registry_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_registry_settlement_for_user_registry(
            user_id, registry_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncRegistrySettlementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistrySettlementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistrySettlementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistrySettlementClient
        """
        return self._raw_client

    async def list_all_registry_settlement_for_user_registry(
        self, user_id: int, registry_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RegistrySettlementListing]:
        """
        Get a listing of all Slice group settlements.

        Parameters
        ----------
        user_id : int


        registry_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RegistrySettlementListing]
            Used to settle a Slice group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.registry_settlement.list_all_registry_settlement_for_user_registry(
                user_id=1,
                registry_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registry_settlement_for_user_registry(
            user_id, registry_id, request_options=request_options
        )
        return _response.data

    async def create_registry_settlement_for_user_registry(
        self,
        user_id: int,
        registry_id: int,
        *,
        request: RegistrySettlement,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistrySettlementCreate:
        """
        Create a new Slice group settlement.

        Parameters
        ----------
        user_id : int


        registry_id : int


        request : RegistrySettlement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrySettlementCreate
            Used to settle a Slice group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.registry_settlement.create_registry_settlement_for_user_registry(
                user_id=1,
                registry_id=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_registry_settlement_for_user_registry(
            user_id, registry_id, request=request, request_options=request_options
        )
        return _response.data

    async def read_registry_settlement_for_user_registry(
        self, user_id: int, registry_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistrySettlementRead:
        """
        Get a specific Slice group settlement.

        Parameters
        ----------
        user_id : int


        registry_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistrySettlementRead
            Used to settle a Slice group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.registry_settlement.read_registry_settlement_for_user_registry(
                user_id=1,
                registry_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_registry_settlement_for_user_registry(
            user_id, registry_id, item_id, request_options=request_options
        )
        return _response.data
