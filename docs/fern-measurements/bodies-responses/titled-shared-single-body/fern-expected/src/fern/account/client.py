

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_request import AccountRequest
from ..types.ledger_request import LedgerRequest
from .raw_client import AsyncRawAccountClient, RawAccountClient


OMIT = typing.cast(typing.Any, ...)


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def replace_account(
        self, *, request: AccountRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AccountRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.replace_account(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_account(request=request, request_options=request_options)
        return _response.data

    def replace_named_account(
        self, account_id: str, *, request: AccountRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        account_id : str

        request : AccountRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.replace_named_account(
            account_id="accountId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_named_account(account_id, request=request, request_options=request_options)
        return _response.data

    def replace_ledger(
        self, *, request: LedgerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : LedgerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.replace_ledger(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_ledger(request=request, request_options=request_options)
        return _response.data

    def replace_named_ledger(
        self, ledger_id: str, *, request: LedgerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ledger_id : str

        request : LedgerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.replace_named_ledger(
            ledger_id="ledgerId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.replace_named_ledger(ledger_id, request=request, request_options=request_options)
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def replace_account(
        self, *, request: AccountRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AccountRequest

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
            await client.account.replace_account(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_account(request=request, request_options=request_options)
        return _response.data

    async def replace_named_account(
        self, account_id: str, *, request: AccountRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        account_id : str

        request : AccountRequest

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
            await client.account.replace_named_account(
                account_id="accountId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_named_account(
            account_id, request=request, request_options=request_options
        )
        return _response.data

    async def replace_ledger(
        self, *, request: LedgerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : LedgerRequest

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
            await client.account.replace_ledger(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_ledger(request=request, request_options=request_options)
        return _response.data

    async def replace_named_ledger(
        self, ledger_id: str, *, request: LedgerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ledger_id : str

        request : LedgerRequest

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
            await client.account.replace_named_ledger(
                ledger_id="ledgerId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_named_ledger(
            ledger_id, request=request, request_options=request_options
        )
        return _response.data
