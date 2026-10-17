

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCartClient, RawCartClient
from .types.apply_coupon_to_cart_action_request_data import ApplyCouponToCartActionRequestData
from .types.checkout_cart_action_request_data import CheckoutCartActionRequestData


OMIT = typing.cast(typing.Any, ...)


class CartClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCartClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCartClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCartClient
        """
        return self._raw_client

    def list_cart_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List cart lines

        Parameters
        ----------
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
        client.cart.list_cart_lines()
        """
        _response = self._raw_client.list_cart_lines(request_options=request_options)
        return _response.data

    def list_cart_lines_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List cart lines relationships

        Parameters
        ----------
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
        client.cart.list_cart_lines_relationships()
        """
        _response = self._raw_client.list_cart_lines_relationships(request_options=request_options)
        return _response.data

    def get_cart(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get cart

        Parameters
        ----------
        include : typing.Optional[str]

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
        client.cart.get_cart(
            include="transactions",
        )
        """
        _response = self._raw_client.get_cart(include=include, request_options=request_options)
        return _response.data

    def apply_coupon_to_cart_action(
        self,
        *,
        data: typing.Optional[ApplyCouponToCartActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Apply coupon to cart action

        Parameters
        ----------
        data : typing.Optional[ApplyCouponToCartActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart import (
            ApplyCouponToCartActionRequestData,
            ApplyCouponToCartActionRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart.apply_coupon_to_cart_action(
            data=ApplyCouponToCartActionRequestData(
                attributes=ApplyCouponToCartActionRequestDataAttributes(
                    coupon_code="code",
                ),
                type="carts",
            ),
        )
        """
        _response = self._raw_client.apply_coupon_to_cart_action(data=data, request_options=request_options)
        return _response.data

    def get_cart_for_logged_in_user_action(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get cart for logged in user action

        Parameters
        ----------
        include : typing.Optional[str]

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
        client.cart.get_cart_for_logged_in_user_action(
            include="cart_lines",
        )
        """
        _response = self._raw_client.get_cart_for_logged_in_user_action(
            include=include, request_options=request_options
        )
        return _response.data

    def clear_cart_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clear cart action

        Parameters
        ----------
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
        client.cart.clear_cart_action()
        """
        _response = self._raw_client.clear_cart_action(request_options=request_options)
        return _response.data

    def checkout_cart_action(
        self,
        *,
        data: typing.Optional[CheckoutCartActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Checkout cart action

        Parameters
        ----------
        data : typing.Optional[CheckoutCartActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart import (
            CheckoutCartActionRequestData,
            CheckoutCartActionRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart.checkout_cart_action(
            data=CheckoutCartActionRequestData(
                attributes=CheckoutCartActionRequestDataAttributes(
                    agree=True,
                    create_user=True,
                ),
                type="carts",
            ),
        )
        """
        _response = self._raw_client.checkout_cart_action(data=data, request_options=request_options)
        return _response.data


class AsyncCartClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCartClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCartClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCartClient
        """
        return self._raw_client

    async def list_cart_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List cart lines

        Parameters
        ----------
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
            await client.cart.list_cart_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cart_lines(request_options=request_options)
        return _response.data

    async def list_cart_lines_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List cart lines relationships

        Parameters
        ----------
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
            await client.cart.list_cart_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cart_lines_relationships(request_options=request_options)
        return _response.data

    async def get_cart(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get cart

        Parameters
        ----------
        include : typing.Optional[str]

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
            await client.cart.get_cart(
                include="transactions",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cart(include=include, request_options=request_options)
        return _response.data

    async def apply_coupon_to_cart_action(
        self,
        *,
        data: typing.Optional[ApplyCouponToCartActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Apply coupon to cart action

        Parameters
        ----------
        data : typing.Optional[ApplyCouponToCartActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart import (
            ApplyCouponToCartActionRequestData,
            ApplyCouponToCartActionRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart.apply_coupon_to_cart_action(
                data=ApplyCouponToCartActionRequestData(
                    attributes=ApplyCouponToCartActionRequestDataAttributes(
                        coupon_code="code",
                    ),
                    type="carts",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply_coupon_to_cart_action(data=data, request_options=request_options)
        return _response.data

    async def get_cart_for_logged_in_user_action(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get cart for logged in user action

        Parameters
        ----------
        include : typing.Optional[str]

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
            await client.cart.get_cart_for_logged_in_user_action(
                include="cart_lines",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cart_for_logged_in_user_action(
            include=include, request_options=request_options
        )
        return _response.data

    async def clear_cart_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clear cart action

        Parameters
        ----------
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
            await client.cart.clear_cart_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_cart_action(request_options=request_options)
        return _response.data

    async def checkout_cart_action(
        self,
        *,
        data: typing.Optional[CheckoutCartActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Checkout cart action

        Parameters
        ----------
        data : typing.Optional[CheckoutCartActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart import (
            CheckoutCartActionRequestData,
            CheckoutCartActionRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart.checkout_cart_action(
                data=CheckoutCartActionRequestData(
                    attributes=CheckoutCartActionRequestDataAttributes(
                        agree=True,
                        create_user=True,
                    ),
                    type="carts",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.checkout_cart_action(data=data, request_options=request_options)
        return _response.data
