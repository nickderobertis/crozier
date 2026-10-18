

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCartAddressesClient, RawCartAddressesClient
from .types.attach_shipping_option_action_request_data import AttachShippingOptionActionRequestData
from .types.continuous_update_action_request_data import ContinuousUpdateActionRequestData
from .types.create_cart_address_request_data import CreateCartAddressRequestData
from .types.detach_shipping_option_action_request_data import DetachShippingOptionActionRequestData
from .types.update_cart_address_country_action_request_data import UpdateCartAddressCountryActionRequestData
from .types.update_cart_address_request_data import UpdateCartAddressRequestData


OMIT = typing.cast(typing.Any, ...)


class CartAddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCartAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCartAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCartAddressesClient
        """
        return self._raw_client

    def create_cart_address(
        self,
        *,
        data: typing.Optional[CreateCartAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create cart address

        Parameters
        ----------
        data : typing.Optional[CreateCartAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            CreateCartAddressRequestData,
            CreateCartAddressRequestDataAttributes,
            CreateCartAddressRequestDataRelationships,
            CreateCartAddressRequestDataRelationshipsCart,
            CreateCartAddressRequestDataRelationshipsCartData,
            CreateCartAddressRequestDataRelationshipsCountry,
            CreateCartAddressRequestDataRelationshipsCountryData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.create_cart_address(
            data=CreateCartAddressRequestData(
                attributes=CreateCartAddressRequestDataAttributes(
                    address_type="shipping",
                    city="New York",
                    company_in="12345678",
                    company_name="ABC Company",
                    company_tin="CZ12345678",
                    contact_email="bob6@mail.com",
                    contact_phone="777888999",
                    first_name="John",
                    last_name="Doe",
                    line_one="123 Main Street",
                    postcode="10001",
                    shipping_option="Friendly Freight Co.",
                ),
                relationships=CreateCartAddressRequestDataRelationships(
                    cart=CreateCartAddressRequestDataRelationshipsCart(
                        data=CreateCartAddressRequestDataRelationshipsCartData(
                            id="1949444",
                            type="carts",
                        ),
                    ),
                    country=CreateCartAddressRequestDataRelationshipsCountry(
                        data=CreateCartAddressRequestDataRelationshipsCountryData(
                            id="1",
                            type="countries",
                        ),
                    ),
                ),
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.create_cart_address(data=data, request_options=request_options)
        return _response.data

    def update_cart_address(
        self,
        *,
        data: typing.Optional[UpdateCartAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart address

        Parameters
        ----------
        data : typing.Optional[UpdateCartAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            UpdateCartAddressRequestData,
            UpdateCartAddressRequestDataAttributes,
            UpdateCartAddressRequestDataRelationships,
            UpdateCartAddressRequestDataRelationshipsCart,
            UpdateCartAddressRequestDataRelationshipsCartData,
            UpdateCartAddressRequestDataRelationshipsCountry,
            UpdateCartAddressRequestDataRelationshipsCountryData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.update_cart_address(
            data=UpdateCartAddressRequestData(
                attributes=UpdateCartAddressRequestDataAttributes(
                    address_type="shipping",
                    city="New York",
                    company_in="12345678",
                    company_name="ABC Company",
                    company_tin="CZ12345678",
                    contact_email="bob6@mail.com",
                    contact_phone="777888999",
                    first_name="John",
                    last_name="Doe",
                    line_one="123 Main Street",
                    postcode="10001",
                    shipping_option="SODEL",
                ),
                id="1",
                relationships=UpdateCartAddressRequestDataRelationships(
                    cart=UpdateCartAddressRequestDataRelationshipsCart(
                        data=UpdateCartAddressRequestDataRelationshipsCartData(
                            id="1",
                            type="carts",
                        ),
                    ),
                    country=UpdateCartAddressRequestDataRelationshipsCountry(
                        data=UpdateCartAddressRequestDataRelationshipsCountryData(
                            id="1",
                            type="countries",
                        ),
                    ),
                ),
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.update_cart_address(data=data, request_options=request_options)
        return _response.data

    def attach_shipping_option_action(
        self,
        *,
        data: typing.Optional[AttachShippingOptionActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Attach shipping option action

        Parameters
        ----------
        data : typing.Optional[AttachShippingOptionActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            AttachShippingOptionActionRequestData,
            AttachShippingOptionActionRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.attach_shipping_option_action(
            data=AttachShippingOptionActionRequestData(
                attributes=AttachShippingOptionActionRequestDataAttributes(
                    shipping_option="DPDDEL",
                ),
                id="1",
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.attach_shipping_option_action(data=data, request_options=request_options)
        return _response.data

    def detach_shipping_option_action(
        self,
        *,
        data: typing.Optional[DetachShippingOptionActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Detach shipping option action

        Parameters
        ----------
        data : typing.Optional[DetachShippingOptionActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            DetachShippingOptionActionRequestData,
            DetachShippingOptionActionRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.detach_shipping_option_action(
            data=DetachShippingOptionActionRequestData(
                attributes=DetachShippingOptionActionRequestDataAttributes(
                    shipping_option="DPDDEL",
                ),
                id="1",
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.detach_shipping_option_action(data=data, request_options=request_options)
        return _response.data

    def continuous_update_action(
        self,
        *,
        data: typing.Optional[ContinuousUpdateActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Continuous update action

        Parameters
        ----------
        data : typing.Optional[ContinuousUpdateActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            ContinuousUpdateActionRequestData,
            ContinuousUpdateActionRequestDataAttributes,
            ContinuousUpdateActionRequestDataRelationships,
            ContinuousUpdateActionRequestDataRelationshipsCart,
            ContinuousUpdateActionRequestDataRelationshipsCartData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.continuous_update_action(
            data=ContinuousUpdateActionRequestData(
                attributes=ContinuousUpdateActionRequestDataAttributes(
                    address_type="billing",
                    company_in="12345678",
                    company_name="Hovno",
                    company_tin="CZ12345678",
                ),
                id="1",
                relationships=ContinuousUpdateActionRequestDataRelationships(
                    cart=ContinuousUpdateActionRequestDataRelationshipsCart(
                        data=ContinuousUpdateActionRequestDataRelationshipsCartData(
                            id="1",
                            type="carts",
                        ),
                    ),
                ),
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.continuous_update_action(data=data, request_options=request_options)
        return _response.data

    def update_cart_address_country_action(
        self,
        *,
        data: typing.Optional[UpdateCartAddressCountryActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart address country action

        Parameters
        ----------
        data : typing.Optional[UpdateCartAddressCountryActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.cart_addresses import (
            UpdateCartAddressCountryActionRequestData,
            UpdateCartAddressCountryActionRequestDataRelationships,
            UpdateCartAddressCountryActionRequestDataRelationshipsCountry,
            UpdateCartAddressCountryActionRequestDataRelationshipsCountryData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cart_addresses.update_cart_address_country_action(
            data=UpdateCartAddressCountryActionRequestData(
                id="1",
                relationships=UpdateCartAddressCountryActionRequestDataRelationships(
                    country=UpdateCartAddressCountryActionRequestDataRelationshipsCountry(
                        data=UpdateCartAddressCountryActionRequestDataRelationshipsCountryData(
                            id="2",
                            type="countries",
                        ),
                    ),
                ),
                type="cart-addresses",
            ),
        )
        """
        _response = self._raw_client.update_cart_address_country_action(data=data, request_options=request_options)
        return _response.data


class AsyncCartAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCartAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCartAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCartAddressesClient
        """
        return self._raw_client

    async def create_cart_address(
        self,
        *,
        data: typing.Optional[CreateCartAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create cart address

        Parameters
        ----------
        data : typing.Optional[CreateCartAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            CreateCartAddressRequestData,
            CreateCartAddressRequestDataAttributes,
            CreateCartAddressRequestDataRelationships,
            CreateCartAddressRequestDataRelationshipsCart,
            CreateCartAddressRequestDataRelationshipsCartData,
            CreateCartAddressRequestDataRelationshipsCountry,
            CreateCartAddressRequestDataRelationshipsCountryData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.create_cart_address(
                data=CreateCartAddressRequestData(
                    attributes=CreateCartAddressRequestDataAttributes(
                        address_type="shipping",
                        city="New York",
                        company_in="12345678",
                        company_name="ABC Company",
                        company_tin="CZ12345678",
                        contact_email="bob6@mail.com",
                        contact_phone="777888999",
                        first_name="John",
                        last_name="Doe",
                        line_one="123 Main Street",
                        postcode="10001",
                        shipping_option="Friendly Freight Co.",
                    ),
                    relationships=CreateCartAddressRequestDataRelationships(
                        cart=CreateCartAddressRequestDataRelationshipsCart(
                            data=CreateCartAddressRequestDataRelationshipsCartData(
                                id="1949444",
                                type="carts",
                            ),
                        ),
                        country=CreateCartAddressRequestDataRelationshipsCountry(
                            data=CreateCartAddressRequestDataRelationshipsCountryData(
                                id="1",
                                type="countries",
                            ),
                        ),
                    ),
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cart_address(data=data, request_options=request_options)
        return _response.data

    async def update_cart_address(
        self,
        *,
        data: typing.Optional[UpdateCartAddressRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart address

        Parameters
        ----------
        data : typing.Optional[UpdateCartAddressRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            UpdateCartAddressRequestData,
            UpdateCartAddressRequestDataAttributes,
            UpdateCartAddressRequestDataRelationships,
            UpdateCartAddressRequestDataRelationshipsCart,
            UpdateCartAddressRequestDataRelationshipsCartData,
            UpdateCartAddressRequestDataRelationshipsCountry,
            UpdateCartAddressRequestDataRelationshipsCountryData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.update_cart_address(
                data=UpdateCartAddressRequestData(
                    attributes=UpdateCartAddressRequestDataAttributes(
                        address_type="shipping",
                        city="New York",
                        company_in="12345678",
                        company_name="ABC Company",
                        company_tin="CZ12345678",
                        contact_email="bob6@mail.com",
                        contact_phone="777888999",
                        first_name="John",
                        last_name="Doe",
                        line_one="123 Main Street",
                        postcode="10001",
                        shipping_option="SODEL",
                    ),
                    id="1",
                    relationships=UpdateCartAddressRequestDataRelationships(
                        cart=UpdateCartAddressRequestDataRelationshipsCart(
                            data=UpdateCartAddressRequestDataRelationshipsCartData(
                                id="1",
                                type="carts",
                            ),
                        ),
                        country=UpdateCartAddressRequestDataRelationshipsCountry(
                            data=UpdateCartAddressRequestDataRelationshipsCountryData(
                                id="1",
                                type="countries",
                            ),
                        ),
                    ),
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cart_address(data=data, request_options=request_options)
        return _response.data

    async def attach_shipping_option_action(
        self,
        *,
        data: typing.Optional[AttachShippingOptionActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Attach shipping option action

        Parameters
        ----------
        data : typing.Optional[AttachShippingOptionActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            AttachShippingOptionActionRequestData,
            AttachShippingOptionActionRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.attach_shipping_option_action(
                data=AttachShippingOptionActionRequestData(
                    attributes=AttachShippingOptionActionRequestDataAttributes(
                        shipping_option="DPDDEL",
                    ),
                    id="1",
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach_shipping_option_action(data=data, request_options=request_options)
        return _response.data

    async def detach_shipping_option_action(
        self,
        *,
        data: typing.Optional[DetachShippingOptionActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Detach shipping option action

        Parameters
        ----------
        data : typing.Optional[DetachShippingOptionActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            DetachShippingOptionActionRequestData,
            DetachShippingOptionActionRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.detach_shipping_option_action(
                data=DetachShippingOptionActionRequestData(
                    attributes=DetachShippingOptionActionRequestDataAttributes(
                        shipping_option="DPDDEL",
                    ),
                    id="1",
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detach_shipping_option_action(data=data, request_options=request_options)
        return _response.data

    async def continuous_update_action(
        self,
        *,
        data: typing.Optional[ContinuousUpdateActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Continuous update action

        Parameters
        ----------
        data : typing.Optional[ContinuousUpdateActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            ContinuousUpdateActionRequestData,
            ContinuousUpdateActionRequestDataAttributes,
            ContinuousUpdateActionRequestDataRelationships,
            ContinuousUpdateActionRequestDataRelationshipsCart,
            ContinuousUpdateActionRequestDataRelationshipsCartData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.continuous_update_action(
                data=ContinuousUpdateActionRequestData(
                    attributes=ContinuousUpdateActionRequestDataAttributes(
                        address_type="billing",
                        company_in="12345678",
                        company_name="Hovno",
                        company_tin="CZ12345678",
                    ),
                    id="1",
                    relationships=ContinuousUpdateActionRequestDataRelationships(
                        cart=ContinuousUpdateActionRequestDataRelationshipsCart(
                            data=ContinuousUpdateActionRequestDataRelationshipsCartData(
                                id="1",
                                type="carts",
                            ),
                        ),
                    ),
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.continuous_update_action(data=data, request_options=request_options)
        return _response.data

    async def update_cart_address_country_action(
        self,
        *,
        data: typing.Optional[UpdateCartAddressCountryActionRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update cart address country action

        Parameters
        ----------
        data : typing.Optional[UpdateCartAddressCountryActionRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.cart_addresses import (
            UpdateCartAddressCountryActionRequestData,
            UpdateCartAddressCountryActionRequestDataRelationships,
            UpdateCartAddressCountryActionRequestDataRelationshipsCountry,
            UpdateCartAddressCountryActionRequestDataRelationshipsCountryData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cart_addresses.update_cart_address_country_action(
                data=UpdateCartAddressCountryActionRequestData(
                    id="1",
                    relationships=UpdateCartAddressCountryActionRequestDataRelationships(
                        country=UpdateCartAddressCountryActionRequestDataRelationshipsCountry(
                            data=UpdateCartAddressCountryActionRequestDataRelationshipsCountryData(
                                id="2",
                                type="countries",
                            ),
                        ),
                    ),
                    type="cart-addresses",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cart_address_country_action(
            data=data, request_options=request_options
        )
        return _response.data
