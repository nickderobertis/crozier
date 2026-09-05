

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_wallet_payment_price_dollars import CreateWalletPaymentPriceDollars
from ..types.envelope_get_wallet_auto_recharge import EnvelopeGetWalletAutoRecharge
from ..types.envelope_list_payment_method_get import EnvelopeListPaymentMethodGet
from ..types.envelope_list_wallet_get_with_available_credits import EnvelopeListWalletGetWithAvailableCredits
from ..types.envelope_list_wallet_group_get import EnvelopeListWalletGroupGet
from ..types.envelope_payment_method_get import EnvelopePaymentMethodGet
from ..types.envelope_payment_method_initiated import EnvelopePaymentMethodInitiated
from ..types.envelope_wallet_get import EnvelopeWalletGet
from ..types.envelope_wallet_get_with_available_credits import EnvelopeWalletGetWithAvailableCredits
from ..types.envelope_wallet_group_get import EnvelopeWalletGroupGet
from ..types.envelope_wallet_payment_initiated import EnvelopeWalletPaymentInitiated
from ..types.group_id_int import GroupIdInt
from ..types.page_payment_transaction import PagePaymentTransaction
from ..types.wallet_id_int import WalletIdInt
from ..types.wallet_status import WalletStatus
from .raw_client import AsyncRawWalletsClient, RawWalletsClient
from .types.replace_wallet_auto_recharge_monthly_limit_in_usd import ReplaceWalletAutoRechargeMonthlyLimitInUsd
from .types.replace_wallet_auto_recharge_top_up_amount_in_usd import ReplaceWalletAutoRechargeTopUpAmountInUsd


OMIT = typing.cast(typing.Any, ...)


class WalletsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWalletsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWalletsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWalletsClient
        """
        return self._raw_client

    def list_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.list_wallets()
        """
        _response = self._raw_client.list_wallets(request_options=request_options)
        return _response.data

    def create_wallet(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGet:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.create_wallet(
            name="name",
        )
        """
        _response = self._raw_client.create_wallet(
            name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    def get_default_wallet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_default_wallet()
        """
        _response = self._raw_client.get_default_wallet(request_options=request_options)
        return _response.data

    def get_wallet(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet(
            wallet_id=1,
        )
        """
        _response = self._raw_client.get_wallet(wallet_id, request_options=request_options)
        return _response.data

    def update_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        name: str,
        status: WalletStatus,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        name : str

        status : WalletStatus

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        from fern import FernApi, WalletStatus

        client = FernApi()
        client.wallets.update_wallet(
            wallet_id=1,
            name="name",
            status=WalletStatus.ACTIVE,
        )
        """
        _response = self._raw_client.update_wallet(
            wallet_id,
            name=name,
            status=status,
            description=description,
            thumbnail=thumbnail,
            request_options=request_options,
        )
        return _response.data

    def create_payment(
        self,
        wallet_id: WalletIdInt,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletPaymentInitiated:
        """
        Creates payment to wallet `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletPaymentInitiated
            Payment initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.create_payment(
            wallet_id=1,
            price_dollars=1.1,
        )
        """
        _response = self._raw_client.create_payment(
            wallet_id, price_dollars=price_dollars, comment=comment, request_options=request_options
        )
        return _response.data

    def list_all_payments(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePaymentTransaction:
        """
        Lists all user payments to his/her wallets (only the ones he/she created)

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePaymentTransaction
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.list_all_payments()
        """
        _response = self._raw_client.list_all_payments(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def get_payment_invoice_link(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_payment_invoice_link(
            wallet_id=1,
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.get_payment_invoice_link(wallet_id, payment_id, request_options=request_options)
        return _response.data

    def cancel_payment(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.cancel_payment(
            wallet_id=1,
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.cancel_payment(wallet_id, payment_id, request_options=request_options)
        return _response.data

    def init_creation_of_payment_method(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePaymentMethodInitiated:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePaymentMethodInitiated
            Successfully initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.init_creation_of_payment_method(
            wallet_id=1,
        )
        """
        _response = self._raw_client.init_creation_of_payment_method(wallet_id, request_options=request_options)
        return _response.data

    def cancel_creation_of_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.cancel_creation_of_payment_method(
            wallet_id=1,
            payment_method_id="payment_method_id",
        )
        """
        _response = self._raw_client.cancel_creation_of_payment_method(
            wallet_id, payment_method_id, request_options=request_options
        )
        return _response.data

    def list_payments_methods(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListPaymentMethodGet:
        """
        Lists all payments method associated to `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListPaymentMethodGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.list_payments_methods(
            wallet_id=1,
        )
        """
        _response = self._raw_client.list_payments_methods(wallet_id, request_options=request_options)
        return _response.data

    def get_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePaymentMethodGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePaymentMethodGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_payment_method(
            wallet_id=1,
            payment_method_id="payment_method_id",
        )
        """
        _response = self._raw_client.get_payment_method(wallet_id, payment_method_id, request_options=request_options)
        return _response.data

    def delete_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.delete_payment_method(
            wallet_id=1,
            payment_method_id="payment_method_id",
        )
        """
        _response = self._raw_client.delete_payment_method(
            wallet_id, payment_method_id, request_options=request_options
        )
        return _response.data

    def pay_with_payment_method(
        self,
        wallet_id: WalletIdInt,
        payment_method_id: str,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletPaymentInitiated:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletPaymentInitiated
            Pay with payment-method

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.pay_with_payment_method(
            wallet_id=1,
            payment_method_id="payment_method_id",
            price_dollars=1.1,
        )
        """
        _response = self._raw_client.pay_with_payment_method(
            wallet_id, payment_method_id, price_dollars=price_dollars, comment=comment, request_options=request_options
        )
        return _response.data

    def get_wallet_autorecharge(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetWalletAutoRecharge:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetWalletAutoRecharge
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_autorecharge(
            wallet_id=1,
        )
        """
        _response = self._raw_client.get_wallet_autorecharge(wallet_id, request_options=request_options)
        return _response.data

    def replace_wallet_autorecharge(
        self,
        wallet_id: WalletIdInt,
        *,
        enabled: bool,
        payment_method_id: str,
        top_up_amount_in_usd: ReplaceWalletAutoRechargeTopUpAmountInUsd,
        monthly_limit_in_usd: typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGetWalletAutoRecharge:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        enabled : bool

        payment_method_id : str

        top_up_amount_in_usd : ReplaceWalletAutoRechargeTopUpAmountInUsd

        monthly_limit_in_usd : typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetWalletAutoRecharge
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.replace_wallet_autorecharge(
            wallet_id=1,
            enabled=True,
            payment_method_id="paymentMethodId",
            top_up_amount_in_usd=1.1,
        )
        """
        _response = self._raw_client.replace_wallet_autorecharge(
            wallet_id,
            enabled=enabled,
            payment_method_id=payment_method_id,
            top_up_amount_in_usd=top_up_amount_in_usd,
            monthly_limit_in_usd=monthly_limit_in_usd,
            request_options=request_options,
        )
        return _response.data

    def create_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.create_wallet_group(
            wallet_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.create_wallet_group(
            wallet_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def update_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.update_wallet_group(
            wallet_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.update_wallet_group(
            wallet_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def delete_wallet_group(
        self, wallet_id: WalletIdInt, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.delete_wallet_group(
            wallet_id=1,
            group_id=1,
        )
        """
        _response = self._raw_client.delete_wallet_group(wallet_id, group_id, request_options=request_options)
        return _response.data

    def list_wallet_groups(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWalletGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.list_wallet_groups(
            wallet_id=1,
        )
        """
        _response = self._raw_client.list_wallet_groups(wallet_id, request_options=request_options)
        return _response.data


class AsyncWalletsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWalletsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWalletsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWalletsClient
        """
        return self._raw_client

    async def list_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.list_wallets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_wallets(request_options=request_options)
        return _response.data

    async def create_wallet(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGet:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.create_wallet(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_wallet(
            name=name, description=description, thumbnail=thumbnail, request_options=request_options
        )
        return _response.data

    async def get_default_wallet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_default_wallet()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_default_wallet(request_options=request_options)
        return _response.data

    async def get_wallet(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeWalletGetWithAvailableCredits:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGetWithAvailableCredits
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet(wallet_id, request_options=request_options)
        return _response.data

    async def update_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        name: str,
        status: WalletStatus,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        name : str

        status : WalletStatus

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WalletStatus

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.update_wallet(
                wallet_id=1,
                name="name",
                status=WalletStatus.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_wallet(
            wallet_id,
            name=name,
            status=status,
            description=description,
            thumbnail=thumbnail,
            request_options=request_options,
        )
        return _response.data

    async def create_payment(
        self,
        wallet_id: WalletIdInt,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletPaymentInitiated:
        """
        Creates payment to wallet `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletPaymentInitiated
            Payment initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.create_payment(
                wallet_id=1,
                price_dollars=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment(
            wallet_id, price_dollars=price_dollars, comment=comment, request_options=request_options
        )
        return _response.data

    async def list_all_payments(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePaymentTransaction:
        """
        Lists all user payments to his/her wallets (only the ones he/she created)

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePaymentTransaction
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.list_all_payments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payments(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_payment_invoice_link(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_payment_invoice_link(
                wallet_id=1,
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment_invoice_link(
            wallet_id, payment_id, request_options=request_options
        )
        return _response.data

    async def cancel_payment(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.cancel_payment(
                wallet_id=1,
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_payment(wallet_id, payment_id, request_options=request_options)
        return _response.data

    async def init_creation_of_payment_method(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePaymentMethodInitiated:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePaymentMethodInitiated
            Successfully initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.init_creation_of_payment_method(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.init_creation_of_payment_method(wallet_id, request_options=request_options)
        return _response.data

    async def cancel_creation_of_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.cancel_creation_of_payment_method(
                wallet_id=1,
                payment_method_id="payment_method_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_creation_of_payment_method(
            wallet_id, payment_method_id, request_options=request_options
        )
        return _response.data

    async def list_payments_methods(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListPaymentMethodGet:
        """
        Lists all payments method associated to `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListPaymentMethodGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.list_payments_methods(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payments_methods(wallet_id, request_options=request_options)
        return _response.data

    async def get_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePaymentMethodGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePaymentMethodGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_payment_method(
                wallet_id=1,
                payment_method_id="payment_method_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment_method(
            wallet_id, payment_method_id, request_options=request_options
        )
        return _response.data

    async def delete_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.delete_payment_method(
                wallet_id=1,
                payment_method_id="payment_method_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_payment_method(
            wallet_id, payment_method_id, request_options=request_options
        )
        return _response.data

    async def pay_with_payment_method(
        self,
        wallet_id: WalletIdInt,
        payment_method_id: str,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletPaymentInitiated:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletPaymentInitiated
            Pay with payment-method

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.pay_with_payment_method(
                wallet_id=1,
                payment_method_id="payment_method_id",
                price_dollars=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pay_with_payment_method(
            wallet_id, payment_method_id, price_dollars=price_dollars, comment=comment, request_options=request_options
        )
        return _response.data

    async def get_wallet_autorecharge(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeGetWalletAutoRecharge:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetWalletAutoRecharge
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_autorecharge(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_autorecharge(wallet_id, request_options=request_options)
        return _response.data

    async def replace_wallet_autorecharge(
        self,
        wallet_id: WalletIdInt,
        *,
        enabled: bool,
        payment_method_id: str,
        top_up_amount_in_usd: ReplaceWalletAutoRechargeTopUpAmountInUsd,
        monthly_limit_in_usd: typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeGetWalletAutoRecharge:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        enabled : bool

        payment_method_id : str

        top_up_amount_in_usd : ReplaceWalletAutoRechargeTopUpAmountInUsd

        monthly_limit_in_usd : typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeGetWalletAutoRecharge
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.replace_wallet_autorecharge(
                wallet_id=1,
                enabled=True,
                payment_method_id="paymentMethodId",
                top_up_amount_in_usd=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_wallet_autorecharge(
            wallet_id,
            enabled=enabled,
            payment_method_id=payment_method_id,
            top_up_amount_in_usd=top_up_amount_in_usd,
            monthly_limit_in_usd=monthly_limit_in_usd,
            request_options=request_options,
        )
        return _response.data

    async def create_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.create_wallet_group(
                wallet_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_wallet_group(
            wallet_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def update_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeWalletGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.update_wallet_group(
                wallet_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_wallet_group(
            wallet_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def delete_wallet_group(
        self, wallet_id: WalletIdInt, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.delete_wallet_group(
                wallet_id=1,
                group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_wallet_group(wallet_id, group_id, request_options=request_options)
        return _response.data

    async def list_wallet_groups(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListWalletGroupGet:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListWalletGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.list_wallet_groups(
                wallet_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_wallet_groups(wallet_id, request_options=request_options)
        return _response.data
