

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEcommerceClient, RawEcommerceClient
from .types.get_settings_ecommerce_response import GetSettingsEcommerceResponse


class EcommerceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEcommerceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEcommerceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEcommerceClient
        """
        return self._raw_client

    def get_settings(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSettingsEcommerceResponse:
        """
        Retrieve ecommerce settings for a site.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSettingsEcommerceResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_settings(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get_settings(site_id, request_options=request_options)
        return _response.data


class AsyncEcommerceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEcommerceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEcommerceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEcommerceClient
        """
        return self._raw_client

    async def get_settings(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSettingsEcommerceResponse:
        """
        Retrieve ecommerce settings for a site.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSettingsEcommerceResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_settings(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings(site_id, request_options=request_options)
        return _response.data
