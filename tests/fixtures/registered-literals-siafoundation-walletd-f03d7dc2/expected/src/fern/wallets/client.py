

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.balance import Balance
from ..types.currency import Currency
from ..types.event import Event
from ..types.hash256 import Hash256
from ..types.siacoin_output import SiacoinOutput
from ..types.siafund_output import SiafundOutput
from ..types.spend_policy import SpendPolicy
from ..types.transaction import Transaction
from ..types.unspent_siacoin_elements_response import UnspentSiacoinElementsResponse
from ..types.unspent_siafund_elements_response import UnspentSiafundElementsResponse
from ..types.wallet import Wallet
from ..types.wallet_address import WalletAddress
from ..types.wallet_construct_response import WalletConstructResponse
from ..types.wallet_construct_v2response import WalletConstructV2Response
from ..types.wallet_fund_response import WalletFundResponse
from .raw_client import AsyncRawWalletsClient, RawWalletsClient


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

    def get_wallets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Wallet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Wallet]
            Wallets registered with walletd.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallets()
        """
        _response = self._raw_client.get_wallets(request_options=request_options)
        return _response.data

    def post_wallet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Wallet:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wallet
            Wallet created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet()
        """
        _response = self._raw_client.post_wallet(
            name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    def post_wallet_by_id(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Wallet:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wallet
            Wallet updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet_by_id(
            id=1000000,
        )
        """
        _response = self._raw_client.post_wallet_by_id(
            id, name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    def delete_wallet_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.delete_wallet_by_id(
            id=1000000,
        )
        """
        _response = self._raw_client.delete_wallet_by_id(id, request_options=request_options)
        return _response.data

    def get_wallet_addresses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WalletAddress]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WalletAddress]
            Addresses assigned to the wallet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_addresses(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_addresses(id, request_options=request_options)
        return _response.data

    def put_wallet_address(
        self,
        id: int,
        *,
        address: Address,
        description: str,
        spend_policy: typing.Optional[SpendPolicy] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        address : Address

        description : str

        spend_policy : typing.Optional[SpendPolicy]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.put_wallet_address(
            id=1000000,
            address="address",
            description="description",
        )
        """
        _response = self._raw_client.put_wallet_address(
            id,
            address=address,
            description=description,
            spend_policy=spend_policy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def put_wallet_batch_addresses(
        self,
        id: int,
        *,
        request: typing.Sequence[WalletAddress],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request : typing.Sequence[WalletAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, WalletAddress

        client = FernApi()
        client.wallets.put_wallet_batch_addresses(
            id=1000000,
            request=[
                WalletAddress(
                    address="address",
                    description="description",
                )
            ],
        )
        """
        _response = self._raw_client.put_wallet_batch_addresses(id, request=request, request_options=request_options)
        return _response.data

    def delete_wallet_address(
        self, id: int, addr: Address, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        addr : Address
            Sia address (unlock hash).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.delete_wallet_address(
            id=1000000,
            addr="addr",
        )
        """
        _response = self._raw_client.delete_wallet_address(id, addr, request_options=request_options)
        return _response.data

    def get_wallet_balance(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Balance:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balance
            Wallet balance with immature breakdown.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_balance(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_balance(id, request_options=request_options)
        return _response.data

    def get_wallet_events(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 500).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Events relevant to the wallet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_events(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_events(id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def get_wallet_events_unconfirmed(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Unconfirmed events referencing the wallet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_events_unconfirmed(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_events_unconfirmed(id, request_options=request_options)
        return _response.data

    def get_wallet_siacoin_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnspentSiacoinElementsResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnspentSiacoinElementsResponse
            Unspent siacoin elements tracked by the wallet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_siacoin_outputs(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_siacoin_outputs(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_wallet_siafund_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnspentSiafundElementsResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnspentSiafundElementsResponse
            Unspent siafund elements tracked by the wallet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.get_wallet_siafund_outputs(
            id=1000000,
        )
        """
        _response = self._raw_client.get_wallet_siafund_outputs(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_wallet_reserve(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet_reserve(
            id=1000000,
        )
        """
        _response = self._raw_client.post_wallet_reserve(
            id, siacoin_outputs=siacoin_outputs, siafund_outputs=siafund_outputs, request_options=request_options
        )
        return _response.data

    def post_wallet_release(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet_release(
            id=1000000,
        )
        """
        _response = self._raw_client.post_wallet_release(
            id, siacoin_outputs=siacoin_outputs, siafund_outputs=siafund_outputs, request_options=request_options
        )
        return _response.data

    def post_wallet_fund(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: Currency,
        change_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletFundResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : Currency

        change_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletFundResponse
            Transaction funded and inputs listed for signing.

        Examples
        --------
        from fern import FernApi, Transaction

        client = FernApi()
        client.wallets.post_wallet_fund(
            id=1000000,
            transaction=Transaction(
                id="id",
            ),
            amount="amount",
        )
        """
        _response = self._raw_client.post_wallet_fund(
            id, transaction=transaction, amount=amount, change_address=change_address, request_options=request_options
        )
        return _response.data

    def post_wallet_fund_siafunds(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: int,
        change_address: typing.Optional[Address] = OMIT,
        claim_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletFundResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : int

        change_address : typing.Optional[Address]

        claim_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletFundResponse
            Transaction funded with siafund inputs.

        Examples
        --------
        from fern import FernApi, Transaction

        client = FernApi()
        client.wallets.post_wallet_fund_siafunds(
            id=1000000,
            transaction=Transaction(
                id="id",
            ),
            amount=1000000,
        )
        """
        _response = self._raw_client.post_wallet_fund_siafunds(
            id,
            transaction=transaction,
            amount=amount,
            change_address=change_address,
            claim_address=claim_address,
            request_options=request_options,
        )
        return _response.data

    def post_wallet_construct_transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletConstructResponse:
        """
        Selects wallet-managed UTXOs, adds change outputs as needed, and returns a fully-formed v1 transaction with signature placeholders.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletConstructResponse
            Constructed v1 transaction and metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet_construct_transaction(
            id=1000000,
            change_address="changeAddress",
        )
        """
        _response = self._raw_client.post_wallet_construct_transaction(
            id, change_address=change_address, siacoins=siacoins, siafunds=siafunds, request_options=request_options
        )
        return _response.data

    def post_wallet_construct_v2transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletConstructV2Response:
        """
        Builds a v2 transaction using wallet-managed UTXOs and optional outputs. Walletd fills in satisfied spend policies and updates proofs to the latest basis.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletConstructV2Response
            Constructed v2 transaction and metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wallets.post_wallet_construct_v2transaction(
            id=1000000,
            change_address="changeAddress",
        )
        """
        _response = self._raw_client.post_wallet_construct_v2transaction(
            id, change_address=change_address, siacoins=siacoins, siafunds=siafunds, request_options=request_options
        )
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

    async def get_wallets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Wallet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Wallet]
            Wallets registered with walletd.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallets(request_options=request_options)
        return _response.data

    async def post_wallet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Wallet:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wallet
            Wallet created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet(
            name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def post_wallet_by_id(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Wallet:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wallet
            Wallet updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet_by_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_by_id(
            id, name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def delete_wallet_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

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
            await client.wallets.delete_wallet_by_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_wallet_by_id(id, request_options=request_options)
        return _response.data

    async def get_wallet_addresses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WalletAddress]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WalletAddress]
            Addresses assigned to the wallet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_addresses(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_addresses(id, request_options=request_options)
        return _response.data

    async def put_wallet_address(
        self,
        id: int,
        *,
        address: Address,
        description: str,
        spend_policy: typing.Optional[SpendPolicy] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        address : Address

        description : str

        spend_policy : typing.Optional[SpendPolicy]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

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
            await client.wallets.put_wallet_address(
                id=1000000,
                address="address",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_wallet_address(
            id,
            address=address,
            description=description,
            spend_policy=spend_policy,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def put_wallet_batch_addresses(
        self,
        id: int,
        *,
        request: typing.Sequence[WalletAddress],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request : typing.Sequence[WalletAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WalletAddress

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.put_wallet_batch_addresses(
                id=1000000,
                request=[
                    WalletAddress(
                        address="address",
                        description="description",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_wallet_batch_addresses(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_wallet_address(
        self, id: int, addr: Address, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        addr : Address
            Sia address (unlock hash).

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
            await client.wallets.delete_wallet_address(
                id=1000000,
                addr="addr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_wallet_address(id, addr, request_options=request_options)
        return _response.data

    async def get_wallet_balance(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Balance:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balance
            Wallet balance with immature breakdown.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_balance(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_balance(id, request_options=request_options)
        return _response.data

    async def get_wallet_events(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 500).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Events relevant to the wallet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_events(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_events(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_wallet_events_unconfirmed(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Unconfirmed events referencing the wallet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_events_unconfirmed(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_events_unconfirmed(id, request_options=request_options)
        return _response.data

    async def get_wallet_siacoin_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnspentSiacoinElementsResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnspentSiacoinElementsResponse
            Unspent siacoin elements tracked by the wallet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_siacoin_outputs(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_siacoin_outputs(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_wallet_siafund_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnspentSiafundElementsResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnspentSiafundElementsResponse
            Unspent siafund elements tracked by the wallet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.get_wallet_siafund_outputs(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wallet_siafund_outputs(
            id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_wallet_reserve(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

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
            await client.wallets.post_wallet_reserve(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_reserve(
            id, siacoin_outputs=siacoin_outputs, siafund_outputs=siafund_outputs, request_options=request_options
        )
        return _response.data

    async def post_wallet_release(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

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
            await client.wallets.post_wallet_release(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_release(
            id, siacoin_outputs=siacoin_outputs, siafund_outputs=siafund_outputs, request_options=request_options
        )
        return _response.data

    async def post_wallet_fund(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: Currency,
        change_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletFundResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : Currency

        change_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletFundResponse
            Transaction funded and inputs listed for signing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Transaction

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet_fund(
                id=1000000,
                transaction=Transaction(
                    id="id",
                ),
                amount="amount",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_fund(
            id, transaction=transaction, amount=amount, change_address=change_address, request_options=request_options
        )
        return _response.data

    async def post_wallet_fund_siafunds(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: int,
        change_address: typing.Optional[Address] = OMIT,
        claim_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletFundResponse:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : int

        change_address : typing.Optional[Address]

        claim_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletFundResponse
            Transaction funded with siafund inputs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Transaction

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet_fund_siafunds(
                id=1000000,
                transaction=Transaction(
                    id="id",
                ),
                amount=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_fund_siafunds(
            id,
            transaction=transaction,
            amount=amount,
            change_address=change_address,
            claim_address=claim_address,
            request_options=request_options,
        )
        return _response.data

    async def post_wallet_construct_transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletConstructResponse:
        """
        Selects wallet-managed UTXOs, adds change outputs as needed, and returns a fully-formed v1 transaction with signature placeholders.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletConstructResponse
            Constructed v1 transaction and metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet_construct_transaction(
                id=1000000,
                change_address="changeAddress",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_construct_transaction(
            id, change_address=change_address, siacoins=siacoins, siafunds=siafunds, request_options=request_options
        )
        return _response.data

    async def post_wallet_construct_v2transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WalletConstructV2Response:
        """
        Builds a v2 transaction using wallet-managed UTXOs and optional outputs. Walletd fills in satisfied spend policies and updates proofs to the latest basis.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WalletConstructV2Response
            Constructed v2 transaction and metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wallets.post_wallet_construct_v2transaction(
                id=1000000,
                change_address="changeAddress",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_construct_v2transaction(
            id, change_address=change_address, siacoins=siacoins, siafunds=siafunds, request_options=request_options
        )
        return _response.data
