

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.selling_point_in import SellingPointIn
from ..types.sku_meta_in import SkuMetaIn
from ..types.spec_response import SpecResponse
from .raw_client import AsyncRawCopywriterClient, RawCopywriterClient
from .types.spec_request_locale import SpecRequestLocale


OMIT = typing.cast(typing.Any, ...)


class CopywriterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCopywriterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCopywriterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCopywriterClient
        """
        return self._raw_client

    def create_spec(
        self,
        kit_id: str,
        *,
        locale: SpecRequestLocale,
        selling_points: typing.Sequence[SellingPointIn],
        sku_meta: SkuMetaIn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecResponse:
        """
        Generate the marketing spec for *kit_id* under the requested locale.

        Parameters
        ----------
        kit_id : str

        locale : SpecRequestLocale

        selling_points : typing.Sequence[SellingPointIn]

        sku_meta : SkuMetaIn

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecResponse
            Successful Response

        Examples
        --------
        from fern.copywriter import SpecRequestLocale

        from fern import (
            FernApi,
            SellingPointIn,
            SellingPointInPriority,
            SkuMetaIn,
            SkuMetaInProductType,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.copywriter.create_spec(
            kit_id="kit_id",
            locale=SpecRequestLocale.ZH,
            selling_points=[
                SellingPointIn(
                    evidence="evidence",
                    priority=SellingPointInPriority.HIGH,
                    title="title",
                )
            ],
            sku_meta=SkuMetaIn(
                brand="brand",
                category="category",
                price=1.1,
                product_type=SkuMetaInProductType.BLUE_HAT,
            ),
        )
        """
        _response = self._raw_client.create_spec(
            kit_id, locale=locale, selling_points=selling_points, sku_meta=sku_meta, request_options=request_options
        )
        return _response.data


class AsyncCopywriterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCopywriterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCopywriterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCopywriterClient
        """
        return self._raw_client

    async def create_spec(
        self,
        kit_id: str,
        *,
        locale: SpecRequestLocale,
        selling_points: typing.Sequence[SellingPointIn],
        sku_meta: SkuMetaIn,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecResponse:
        """
        Generate the marketing spec for *kit_id* under the requested locale.

        Parameters
        ----------
        kit_id : str

        locale : SpecRequestLocale

        selling_points : typing.Sequence[SellingPointIn]

        sku_meta : SkuMetaIn

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.copywriter import SpecRequestLocale

        from fern import (
            AsyncFernApi,
            SellingPointIn,
            SellingPointInPriority,
            SkuMetaIn,
            SkuMetaInProductType,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.copywriter.create_spec(
                kit_id="kit_id",
                locale=SpecRequestLocale.ZH,
                selling_points=[
                    SellingPointIn(
                        evidence="evidence",
                        priority=SellingPointInPriority.HIGH,
                        title="title",
                    )
                ],
                sku_meta=SkuMetaIn(
                    brand="brand",
                    category="category",
                    price=1.1,
                    product_type=SkuMetaInProductType.BLUE_HAT,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_spec(
            kit_id, locale=locale, selling_points=selling_points, sku_meta=sku_meta, request_options=request_options
        )
        return _response.data
