

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsPricesClient, RawAssetsPricesClient
from .types.post_assets_prices_adjusted_forward_request_assets_item import (
    PostAssetsPricesAdjustedForwardRequestAssetsItem,
)
from .types.post_assets_prices_adjusted_forward_response import PostAssetsPricesAdjustedForwardResponse
from .types.post_assets_prices_adjusted_request_assets_item import PostAssetsPricesAdjustedRequestAssetsItem
from .types.post_assets_prices_adjusted_response import PostAssetsPricesAdjustedResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsPricesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsPricesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsPricesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsPricesClient
        """
        return self._raw_client

    def adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsPricesAdjustedResponse:
        """
        Compute the backward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the last date for which unadjusted prices are available, which implies that:
        * The price on the last date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the last date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsPricesAdjustedResponse
            OK

        Examples
        --------
        from fern.assets_prices import (
            PostAssetsPricesAdjustedRequestAssetsItem,
            PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem,
            PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_prices.adjusted_prices(
            assets=[
                PostAssetsPricesAdjustedRequestAssetsItem(
                    asset_prices=[
                        PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                            close=2213.4,
                            date="2020-08-28",
                        ),
                        PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                            close=498.32,
                            date="2020-08-31",
                        ),
                        PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                            close=475.05,
                            date="2020-09-01",
                        ),
                    ],
                    asset_splits=[
                        PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem(
                            date="2020-08-31",
                            factor=5.0,
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.adjusted_prices(assets=assets, request_options=request_options)
        return _response.data

    def forward_adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsPricesAdjustedForwardResponse:
        """
        Compute the forward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the first date for which unadjusted prices are available, which implies that:
        * The price on the first date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the first date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsPricesAdjustedForwardResponse
            OK

        Examples
        --------
        from fern.assets_prices import (
            PostAssetsPricesAdjustedForwardRequestAssetsItem,
            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem,
            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_prices.forward_adjusted_prices(
            assets=[
                PostAssetsPricesAdjustedForwardRequestAssetsItem(
                    asset_prices=[
                        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                            close=2213.4,
                            date="2020-08-28",
                        ),
                        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                            close=498.32,
                            date="2020-08-31",
                        ),
                        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                            close=475.05,
                            date="2020-09-01",
                        ),
                    ],
                    asset_splits=[
                        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem(
                            date="2020-08-31",
                            factor=5.0,
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.forward_adjusted_prices(assets=assets, request_options=request_options)
        return _response.data


class AsyncAssetsPricesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsPricesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsPricesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsPricesClient
        """
        return self._raw_client

    async def adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsPricesAdjustedResponse:
        """
        Compute the backward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the last date for which unadjusted prices are available, which implies that:
        * The price on the last date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the last date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsPricesAdjustedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_prices import (
            PostAssetsPricesAdjustedRequestAssetsItem,
            PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem,
            PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_prices.adjusted_prices(
                assets=[
                    PostAssetsPricesAdjustedRequestAssetsItem(
                        asset_prices=[
                            PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                                close=2213.4,
                                date="2020-08-28",
                            ),
                            PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                                close=498.32,
                                date="2020-08-31",
                            ),
                            PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                                close=475.05,
                                date="2020-09-01",
                            ),
                        ],
                        asset_splits=[
                            PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem(
                                date="2020-08-31",
                                factor=5.0,
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adjusted_prices(assets=assets, request_options=request_options)
        return _response.data

    async def forward_adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsPricesAdjustedForwardResponse:
        """
        Compute the forward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the first date for which unadjusted prices are available, which implies that:
        * The price on the first date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the first date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsPricesAdjustedForwardResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_prices import (
            PostAssetsPricesAdjustedForwardRequestAssetsItem,
            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem,
            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_prices.forward_adjusted_prices(
                assets=[
                    PostAssetsPricesAdjustedForwardRequestAssetsItem(
                        asset_prices=[
                            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                                close=2213.4,
                                date="2020-08-28",
                            ),
                            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                                close=498.32,
                                date="2020-08-31",
                            ),
                            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                                close=475.05,
                                date="2020-09-01",
                            ),
                        ],
                        asset_splits=[
                            PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem(
                                date="2020-08-31",
                                factor=5.0,
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forward_adjusted_prices(assets=assets, request_options=request_options)
        return _response.data
