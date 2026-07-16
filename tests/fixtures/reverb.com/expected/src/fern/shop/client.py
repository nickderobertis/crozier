

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawShopClient, RawShopClient
from .types.put_shop_request_address import PutShopRequestAddress
from .types.put_shop_request_currency import PutShopRequestCurrency
from .types.put_shop_request_legal_country_code import PutShopRequestLegalCountryCode
from .types.put_shop_request_shop_type import PutShopRequestShopType


OMIT = typing.cast(typing.Any, ...)


class ShopClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShopClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShopClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShopClient
        """
        return self._raw_client

    def get_your_own_shop_details(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get your own shop details

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
        client.shop.get_your_own_shop_details()
        """
        _response = self._raw_client.get_your_own_shop_details(request_options=request_options)
        return _response.data

    def update_your_shop_profile(
        self,
        *,
        address: typing.Optional[PutShopRequestAddress] = OMIT,
        currency: typing.Optional[PutShopRequestCurrency] = OMIT,
        description: typing.Optional[str] = OMIT,
        legal_country_code: typing.Optional[PutShopRequestLegalCountryCode] = OMIT,
        legal_country_code_confirmed: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        payment_policy: typing.Optional[str] = OMIT,
        return_policy: typing.Optional[str] = OMIT,
        shipping_policy: typing.Optional[str] = OMIT,
        shop_type: typing.Optional[PutShopRequestShopType] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update your shop profile

        Parameters
        ----------
        address : typing.Optional[PutShopRequestAddress]

        currency : typing.Optional[PutShopRequestCurrency]

        description : typing.Optional[str]

        legal_country_code : typing.Optional[PutShopRequestLegalCountryCode]

        legal_country_code_confirmed : typing.Optional[bool]

        name : typing.Optional[str]

        payment_policy : typing.Optional[str]

        return_policy : typing.Optional[str]

        shipping_policy : typing.Optional[str]

        shop_type : typing.Optional[PutShopRequestShopType]

        website : typing.Optional[str]

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
        client.shop.update_your_shop_profile()
        """
        _response = self._raw_client.update_your_shop_profile(
            address=address,
            currency=currency,
            description=description,
            legal_country_code=legal_country_code,
            legal_country_code_confirmed=legal_country_code_confirmed,
            name=name,
            payment_policy=payment_policy,
            return_policy=return_policy,
            shipping_policy=shipping_policy,
            shop_type=shop_type,
            website=website,
            request_options=request_options,
        )
        return _response.data

    def list_of_supported_product_conditions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of supported product conditions

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
        client.shop.list_of_supported_product_conditions()
        """
        _response = self._raw_client.list_of_supported_product_conditions(request_options=request_options)
        return _response.data

    def get_accepted_payment_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get accepted payment methods

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
        client.shop.get_accepted_payment_methods()
        """
        _response = self._raw_client.get_accepted_payment_methods(request_options=request_options)
        return _response.data

    def returns_shop_vacation_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns shop vacation status

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
        client.shop.returns_shop_vacation_status()
        """
        _response = self._raw_client.returns_shop_vacation_status(request_options=request_options)
        return _response.data

    def enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable vacation mode. All listings will be unavailable until vacation mode is turned off.

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
        client.shop.enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off()
        """
        _response = (
            self._raw_client.enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off(
                request_options=request_options
            )
        )
        return _response.data

    def disable_vacation_mode_all_listings_will_be_re_enabled(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable vacation mode. All listings will be re-enabled.

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
        client.shop.disable_vacation_mode_all_listings_will_be_re_enabled()
        """
        _response = self._raw_client.disable_vacation_mode_all_listings_will_be_re_enabled(
            request_options=request_options
        )
        return _response.data


class AsyncShopClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShopClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShopClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShopClient
        """
        return self._raw_client

    async def get_your_own_shop_details(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get your own shop details

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
            await client.shop.get_your_own_shop_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_your_own_shop_details(request_options=request_options)
        return _response.data

    async def update_your_shop_profile(
        self,
        *,
        address: typing.Optional[PutShopRequestAddress] = OMIT,
        currency: typing.Optional[PutShopRequestCurrency] = OMIT,
        description: typing.Optional[str] = OMIT,
        legal_country_code: typing.Optional[PutShopRequestLegalCountryCode] = OMIT,
        legal_country_code_confirmed: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        payment_policy: typing.Optional[str] = OMIT,
        return_policy: typing.Optional[str] = OMIT,
        shipping_policy: typing.Optional[str] = OMIT,
        shop_type: typing.Optional[PutShopRequestShopType] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update your shop profile

        Parameters
        ----------
        address : typing.Optional[PutShopRequestAddress]

        currency : typing.Optional[PutShopRequestCurrency]

        description : typing.Optional[str]

        legal_country_code : typing.Optional[PutShopRequestLegalCountryCode]

        legal_country_code_confirmed : typing.Optional[bool]

        name : typing.Optional[str]

        payment_policy : typing.Optional[str]

        return_policy : typing.Optional[str]

        shipping_policy : typing.Optional[str]

        shop_type : typing.Optional[PutShopRequestShopType]

        website : typing.Optional[str]

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
            await client.shop.update_your_shop_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_your_shop_profile(
            address=address,
            currency=currency,
            description=description,
            legal_country_code=legal_country_code,
            legal_country_code_confirmed=legal_country_code_confirmed,
            name=name,
            payment_policy=payment_policy,
            return_policy=return_policy,
            shipping_policy=shipping_policy,
            shop_type=shop_type,
            website=website,
            request_options=request_options,
        )
        return _response.data

    async def list_of_supported_product_conditions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported product conditions

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
            await client.shop.list_of_supported_product_conditions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_product_conditions(request_options=request_options)
        return _response.data

    async def get_accepted_payment_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get accepted payment methods

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
            await client.shop.get_accepted_payment_methods()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accepted_payment_methods(request_options=request_options)
        return _response.data

    async def returns_shop_vacation_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns shop vacation status

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
            await client.shop.returns_shop_vacation_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_shop_vacation_status(request_options=request_options)
        return _response.data

    async def enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable vacation mode. All listings will be unavailable until vacation mode is turned off.

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
            await client.shop.enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off()


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off(
            request_options=request_options
        )
        return _response.data

    async def disable_vacation_mode_all_listings_will_be_re_enabled(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable vacation mode. All listings will be re-enabled.

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
            await client.shop.disable_vacation_mode_all_listings_will_be_re_enabled()


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_vacation_mode_all_listings_will_be_re_enabled(
            request_options=request_options
        )
        return _response.data
