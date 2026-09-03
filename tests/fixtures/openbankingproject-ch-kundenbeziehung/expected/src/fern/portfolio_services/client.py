

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.portfolio_sync_response import PortfolioSyncResponse
from ..types.provider_relationship import ProviderRelationship
from .raw_client import AsyncRawPortfolioServicesClient, RawPortfolioServicesClient
from .types.portfolio_sync_request_asset_categories_item import PortfolioSyncRequestAssetCategoriesItem
from .types.portfolio_sync_request_transfer_type import PortfolioSyncRequestTransferType


OMIT = typing.cast(typing.Any, ...)


class PortfolioServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioServicesClient
        """
        return self._raw_client

    def sync_portfolio_data(
        self,
        *,
        customer_id: str,
        source_providers: typing.Sequence[ProviderRelationship],
        target_provider: str,
        transfer_type: typing.Optional[PortfolioSyncRequestTransferType] = OMIT,
        asset_categories: typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PortfolioSyncResponse:
        """
        Synchronisiert Portfolio-Daten zwischen verschiedenen Wealth Management Providern

        Parameters
        ----------
        customer_id : str

        source_providers : typing.Sequence[ProviderRelationship]

        target_provider : str

        transfer_type : typing.Optional[PortfolioSyncRequestTransferType]

        asset_categories : typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PortfolioSyncResponse
            Portfolio-Synchronisation erfolgreich

        Examples
        --------
        from fern import FernApi, ProviderRelationship

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.portfolio_services.sync_portfolio_data(
            customer_id="customerId",
            source_providers=[ProviderRelationship()],
            target_provider="targetProvider",
        )
        """
        _response = self._raw_client.sync_portfolio_data(
            customer_id=customer_id,
            source_providers=source_providers,
            target_provider=target_provider,
            transfer_type=transfer_type,
            asset_categories=asset_categories,
            request_options=request_options,
        )
        return _response.data


class AsyncPortfolioServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioServicesClient
        """
        return self._raw_client

    async def sync_portfolio_data(
        self,
        *,
        customer_id: str,
        source_providers: typing.Sequence[ProviderRelationship],
        target_provider: str,
        transfer_type: typing.Optional[PortfolioSyncRequestTransferType] = OMIT,
        asset_categories: typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PortfolioSyncResponse:
        """
        Synchronisiert Portfolio-Daten zwischen verschiedenen Wealth Management Providern

        Parameters
        ----------
        customer_id : str

        source_providers : typing.Sequence[ProviderRelationship]

        target_provider : str

        transfer_type : typing.Optional[PortfolioSyncRequestTransferType]

        asset_categories : typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PortfolioSyncResponse
            Portfolio-Synchronisation erfolgreich

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProviderRelationship

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.portfolio_services.sync_portfolio_data(
                customer_id="customerId",
                source_providers=[ProviderRelationship()],
                target_provider="targetProvider",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_portfolio_data(
            customer_id=customer_id,
            source_providers=source_providers,
            target_provider=target_provider,
            transfer_type=transfer_type,
            asset_categories=asset_categories,
            request_options=request_options,
        )
        return _response.data
