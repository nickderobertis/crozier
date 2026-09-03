

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.portfolio_sync_response import PortfolioSyncResponse
from ..types.provider_relationship import ProviderRelationship
from .types.portfolio_sync_request_asset_categories_item import PortfolioSyncRequestAssetCategoriesItem
from .types.portfolio_sync_request_transfer_type import PortfolioSyncRequestTransferType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPortfolioServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sync_portfolio_data(
        self,
        *,
        customer_id: str,
        source_providers: typing.Sequence[ProviderRelationship],
        target_provider: str,
        transfer_type: typing.Optional[PortfolioSyncRequestTransferType] = OMIT,
        asset_categories: typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PortfolioSyncResponse]:
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
        HttpResponse[PortfolioSyncResponse]
            Portfolio-Synchronisation erfolgreich
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/sync",
            method="POST",
            json={
                "customerId": customer_id,
                "sourceProviders": convert_and_respect_annotation_metadata(
                    object_=source_providers, annotation=typing.Sequence[ProviderRelationship], direction="write"
                ),
                "targetProvider": target_provider,
                "transferType": transfer_type,
                "assetCategories": asset_categories,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PortfolioSyncResponse,
                    parse_obj_as(
                        type_=PortfolioSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPortfolioServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sync_portfolio_data(
        self,
        *,
        customer_id: str,
        source_providers: typing.Sequence[ProviderRelationship],
        target_provider: str,
        transfer_type: typing.Optional[PortfolioSyncRequestTransferType] = OMIT,
        asset_categories: typing.Optional[typing.Sequence[PortfolioSyncRequestAssetCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PortfolioSyncResponse]:
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
        AsyncHttpResponse[PortfolioSyncResponse]
            Portfolio-Synchronisation erfolgreich
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/sync",
            method="POST",
            json={
                "customerId": customer_id,
                "sourceProviders": convert_and_respect_annotation_metadata(
                    object_=source_providers, annotation=typing.Sequence[ProviderRelationship], direction="write"
                ),
                "targetProvider": target_provider,
                "transferType": transfer_type,
                "assetCategories": asset_categories,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PortfolioSyncResponse,
                    parse_obj_as(
                        type_=PortfolioSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
