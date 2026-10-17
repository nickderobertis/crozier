

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCartLinesClient, RawCartLinesClient
from .types.create_cart_line_add_to_cart_request_data import CreateCartLineAddToCartRequestData
from .types.update_cart_line_update_quantity_request_data import UpdateCartLineUpdateQuantityRequestData


OMIT = typing.cast(typing.Any, ...)


class CartLinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCartLinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCartLinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCartLinesClient
        """
        return self._raw_client

    def create_cart_line_add_to_cart(
        self,
        *,
        data: typing.Optional[CreateCartLineAddToCartRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create cart line (add to cart)

        Parameters
        ----------
        data : typing.Optional[CreateCartLineAddToCartRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_lines import (
            CreateCartLineAddToCartRequestData,
            CreateCartLineAddToCartRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_lines.create_cart_line_add_to_cart(
            data=CreateCartLineAddToCartRequestData(
                attributes=CreateCartLineAddToCartRequestDataAttributes(
                    purchasable_id=349.0,
                    purchasable_type="Lunar\\Models\\ProductVariant",
                    quantity=1.0,
                ),
                type="cart-lines",
            ),
        )
        """
        _response = self._raw_client.create_cart_line_add_to_cart(data=data, request_options=request_options)
        return _response.data

    def update_cart_line_update_quantity(
        self,
        *,
        data: typing.Optional[UpdateCartLineUpdateQuantityRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart line (update quantity)

        Parameters
        ----------
        data : typing.Optional[UpdateCartLineUpdateQuantityRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_lines import (
            UpdateCartLineUpdateQuantityRequestData,
            UpdateCartLineUpdateQuantityRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_lines.update_cart_line_update_quantity(
            data=UpdateCartLineUpdateQuantityRequestData(
                attributes=UpdateCartLineUpdateQuantityRequestDataAttributes(
                    quantity=5.0,
                ),
                id="13516",
                type="cart-lines",
            ),
        )
        """
        _response = self._raw_client.update_cart_line_update_quantity(data=data, request_options=request_options)
        return _response.data

    def delete_cart_line_remove_from_cart(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete cart line (remove from cart)

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
        client.cart_lines.delete_cart_line_remove_from_cart()
        """
        _response = self._raw_client.delete_cart_line_remove_from_cart(request_options=request_options)
        return _response.data


class AsyncCartLinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCartLinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCartLinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCartLinesClient
        """
        return self._raw_client

    async def create_cart_line_add_to_cart(
        self,
        *,
        data: typing.Optional[CreateCartLineAddToCartRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create cart line (add to cart)

        Parameters
        ----------
        data : typing.Optional[CreateCartLineAddToCartRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_lines import (
            CreateCartLineAddToCartRequestData,
            CreateCartLineAddToCartRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_lines.create_cart_line_add_to_cart(
                data=CreateCartLineAddToCartRequestData(
                    attributes=CreateCartLineAddToCartRequestDataAttributes(
                        purchasable_id=349.0,
                        purchasable_type="Lunar\\Models\\ProductVariant",
                        quantity=1.0,
                    ),
                    type="cart-lines",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cart_line_add_to_cart(data=data, request_options=request_options)
        return _response.data

    async def update_cart_line_update_quantity(
        self,
        *,
        data: typing.Optional[UpdateCartLineUpdateQuantityRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart line (update quantity)

        Parameters
        ----------
        data : typing.Optional[UpdateCartLineUpdateQuantityRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_lines import (
            UpdateCartLineUpdateQuantityRequestData,
            UpdateCartLineUpdateQuantityRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_lines.update_cart_line_update_quantity(
                data=UpdateCartLineUpdateQuantityRequestData(
                    attributes=UpdateCartLineUpdateQuantityRequestDataAttributes(
                        quantity=5.0,
                    ),
                    id="13516",
                    type="cart-lines",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cart_line_update_quantity(data=data, request_options=request_options)
        return _response.data

    async def delete_cart_line_remove_from_cart(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete cart line (remove from cart)

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
            await client.cart_lines.delete_cart_line_remove_from_cart()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cart_line_remove_from_cart(request_options=request_options)
        return _response.data
