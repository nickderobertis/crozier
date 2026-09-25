

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCouponsClient, RawCouponsClient
from .types.create_coupon_request_discount_type import CreateCouponRequestDiscountType
from .types.create_coupon_response import CreateCouponResponse
from .types.list_coupons_response import ListCouponsResponse


OMIT = typing.cast(typing.Any, ...)


class CouponsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCouponsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCouponsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCouponsClient
        """
        return self._raw_client

    def list_coupons(
        self, *, product_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCouponsResponse:
        """
        Get a list of coupons for the account.

        Parameters
        ----------
        product_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCouponsResponse
            List of coupons

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.coupons.list_coupons()
        """
        _response = self._raw_client.list_coupons(product_id=product_id, request_options=request_options)
        return _response.data

    def create_coupon(
        self,
        *,
        code: str,
        product_id: int,
        discount_type: typing.Optional[CreateCouponRequestDiscountType] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        uses_limit: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCouponResponse:
        """
        Create a new discount coupon.

        Parameters
        ----------
        code : str
            Coupon code

        product_id : int

        discount_type : typing.Optional[CreateCouponRequestDiscountType]

        discount_amount : typing.Optional[float]

        uses_limit : typing.Optional[int]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCouponResponse
            Coupon created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.coupons.create_coupon(
            code="code",
            product_id=1,
        )
        """
        _response = self._raw_client.create_coupon(
            code=code,
            product_id=product_id,
            discount_type=discount_type,
            discount_amount=discount_amount,
            uses_limit=uses_limit,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data


class AsyncCouponsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCouponsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCouponsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCouponsClient
        """
        return self._raw_client

    async def list_coupons(
        self, *, product_id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCouponsResponse:
        """
        Get a list of coupons for the account.

        Parameters
        ----------
        product_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCouponsResponse
            List of coupons

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.coupons.list_coupons()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_coupons(product_id=product_id, request_options=request_options)
        return _response.data

    async def create_coupon(
        self,
        *,
        code: str,
        product_id: int,
        discount_type: typing.Optional[CreateCouponRequestDiscountType] = OMIT,
        discount_amount: typing.Optional[float] = OMIT,
        uses_limit: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCouponResponse:
        """
        Create a new discount coupon.

        Parameters
        ----------
        code : str
            Coupon code

        product_id : int

        discount_type : typing.Optional[CreateCouponRequestDiscountType]

        discount_amount : typing.Optional[float]

        uses_limit : typing.Optional[int]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCouponResponse
            Coupon created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.coupons.create_coupon(
                code="code",
                product_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_coupon(
            code=code,
            product_id=product_id,
            discount_type=discount_type,
            discount_amount=discount_amount,
            uses_limit=uses_limit,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data
