

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_licensed_item_purchase_get import EnvelopeLicensedItemPurchaseGet
from ..types.licensed_item_purchase_get import LicensedItemPurchaseGet
from ..types.page_licensed_item_purchase_get import PageLicensedItemPurchaseGet
from ..types.page_licensed_item_rest_get import PageLicensedItemRestGet
from ..types.wallet_id_int import WalletIdInt
from .raw_client import AsyncRawLicensesClient, RawLicensesClient


OMIT = typing.cast(typing.Any, ...)


class LicensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLicensesClient
        """
        return self._raw_client

    def list_licensed_items(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemRestGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.list_licensed_items()
        """
        _response = self._raw_client.list_licensed_items(
            order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def purchase_licensed_item(
        self,
        licensed_item_id: str,
        *,
        wallet_id: WalletIdInt,
        pricing_plan_id: int,
        pricing_unit_id: int,
        num_of_seats: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_id : str

        wallet_id : WalletIdInt

        pricing_plan_id : int

        pricing_unit_id : int

        num_of_seats : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.purchase_licensed_item(
            licensed_item_id="licensed_item_id",
            wallet_id=1,
            pricing_plan_id=1,
            pricing_unit_id=1,
            num_of_seats=1,
        )
        """
        _response = self._raw_client.purchase_licensed_item(
            licensed_item_id,
            wallet_id=wallet_id,
            pricing_plan_id=pricing_plan_id,
            pricing_unit_id=pricing_unit_id,
            num_of_seats=num_of_seats,
            request_options=request_options,
        )
        return _response.data

    def list_wallet_licensed_items_purchases(
        self,
        wallet_id: WalletIdInt,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.list_wallet_licensed_items_purchases(
            wallet_id=1,
        )
        """
        _response = self._raw_client.list_wallet_licensed_items_purchases(
            wallet_id, order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_licensed_item_purchase(
        self, licensed_item_purchase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_purchase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.get_licensed_item_purchase(
            licensed_item_purchase_id="licensed_item_purchase_id",
        )
        """
        _response = self._raw_client.get_licensed_item_purchase(
            licensed_item_purchase_id, request_options=request_options
        )
        return _response.data

    def list_licensed_item_checkouts_for_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.list_licensed_item_checkouts_for_wallet(
            wallet_id=1,
        )
        """
        _response = self._raw_client.list_licensed_item_checkouts_for_wallet(
            wallet_id, order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_licensed_item_checkout(
        self, licensed_item_checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_checkout_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.get_licensed_item_checkout(
            licensed_item_checkout_id="licensed_item_checkout_id",
        )
        """
        _response = self._raw_client.get_licensed_item_checkout(
            licensed_item_checkout_id, request_options=request_options
        )
        return _response.data


class AsyncLicensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLicensesClient
        """
        return self._raw_client

    async def list_licensed_items(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemRestGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.list_licensed_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_licensed_items(
            order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def purchase_licensed_item(
        self,
        licensed_item_id: str,
        *,
        wallet_id: WalletIdInt,
        pricing_plan_id: int,
        pricing_unit_id: int,
        num_of_seats: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_id : str

        wallet_id : WalletIdInt

        pricing_plan_id : int

        pricing_unit_id : int

        num_of_seats : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.purchase_licensed_item(
                licensed_item_id="licensed_item_id",
                wallet_id=1,
                pricing_plan_id=1,
                pricing_unit_id=1,
                num_of_seats=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.purchase_licensed_item(
            licensed_item_id,
            wallet_id=wallet_id,
            pricing_plan_id=pricing_plan_id,
            pricing_unit_id=pricing_unit_id,
            num_of_seats=num_of_seats,
            request_options=request_options,
        )
        return _response.data

    async def list_wallet_licensed_items_purchases(
        self,
        wallet_id: WalletIdInt,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.list_wallet_licensed_items_purchases(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_wallet_licensed_items_purchases(
            wallet_id, order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_licensed_item_purchase(
        self, licensed_item_purchase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_purchase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.get_licensed_item_purchase(
                licensed_item_purchase_id="licensed_item_purchase_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licensed_item_purchase(
            licensed_item_purchase_id, request_options=request_options
        )
        return _response.data

    async def list_licensed_item_checkouts_for_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.list_licensed_item_checkouts_for_wallet(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_licensed_item_checkouts_for_wallet(
            wallet_id, order_by=order_by, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_licensed_item_checkout(
        self, licensed_item_checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeLicensedItemPurchaseGet:
        """
        Parameters
        ----------
        licensed_item_checkout_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeLicensedItemPurchaseGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.get_licensed_item_checkout(
                licensed_item_checkout_id="licensed_item_checkout_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licensed_item_checkout(
            licensed_item_checkout_id, request_options=request_options
        )
        return _response.data
