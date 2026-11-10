

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_balance_transfers_response import ListBalanceTransfersResponse
from ..types.list_credit_transfers_response import ListCreditTransfersResponse
from ..types.transfer_balance_response import TransferBalanceResponse
from ..types.transfer_credit_response import TransferCreditResponse
from ..types.transfer_number_response import TransferNumberResponse
from .raw_client import AsyncRawTransfersClient, RawTransfersClient


OMIT = typing.cast(typing.Any, ...)


class TransfersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransfersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransfersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransfersClient
        """
        return self._raw_client

    def retrieve_balance_transfers(
        self,
        api_key: str,
        *,
        start_date: str,
        end_date: typing.Optional[str] = None,
        subaccount: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBalanceTransfersResponse:
        """
        Retrieve a list of balance transfers that have taken place for a primary account within a specified time period.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        start_date : str
            Start of the retrieval period.

        end_date : typing.Optional[str]
            End of the retrieval period. If absent then all transfers until now is returned.

        subaccount : typing.Optional[str]
            Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBalanceTransfersResponse
            List balance transfers response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.transfers.retrieve_balance_transfers(
            api_key="api_key",
            start_date="start_date",
        )
        """
        _response = self._raw_client.retrieve_balance_transfers(
            api_key, start_date=start_date, end_date=end_date, subaccount=subaccount, request_options=request_options
        )
        return _response.data

    def transfer_balance(
        self,
        api_key: str,
        *,
        amount: float,
        from_: str,
        to: str,
        reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferBalanceResponse:
        """
        Transfer balance between a primary account and one of its subaccounts. Note that balance_available_for_transfer = |account_balance - credit_limit| of the source account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        amount : float

        from_ : str

        to : str

        reference : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferBalanceResponse
            Balance transfer response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.transfers.transfer_balance(
            api_key="api_key",
            amount=1.1,
            from_="7c9738e6",
            to="ad6dc56f",
        )
        """
        _response = self._raw_client.transfer_balance(
            api_key, amount=amount, from_=from_, to=to, reference=reference, request_options=request_options
        )
        return _response.data

    def retrieve_credit_transfers(
        self,
        api_key: str,
        *,
        start_date: str,
        end_date: typing.Optional[str] = None,
        subaccount: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCreditTransfersResponse:
        """
        Retrieve a list of credit transfers that have taken place for a primary account within a specified time period.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        start_date : str
            Start of the retrieval period.

        end_date : typing.Optional[str]
            End of the retrieval period. If absent then all transfers until now is returned.

        subaccount : typing.Optional[str]
            Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCreditTransfersResponse
            List credit transfers response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.transfers.retrieve_credit_transfers(
            api_key="api_key",
            start_date="start_date",
        )
        """
        _response = self._raw_client.retrieve_credit_transfers(
            api_key, start_date=start_date, end_date=end_date, subaccount=subaccount, request_options=request_options
        )
        return _response.data

    def transfer_credit(
        self,
        api_key: str,
        *,
        amount: float,
        from_: str,
        to: str,
        reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCreditResponse:
        """
        Transfer credit limit between a primary account and one of its subaccounts.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        amount : float

        from_ : str

        to : str

        reference : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCreditResponse
            Credit transfer response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.transfers.transfer_credit(
            api_key="api_key",
            amount=1.1,
            from_="7c9738e6",
            to="ad6dc56f",
        )
        """
        _response = self._raw_client.transfer_credit(
            api_key, amount=amount, from_=from_, to=to, reference=reference, request_options=request_options
        )
        return _response.data

    def transfer_number(
        self,
        api_key: str,
        *,
        country: typing.Optional[str] = OMIT,
        from_: typing.Optional[str] = OMIT,
        number: typing.Optional[float] = OMIT,
        to: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferNumberResponse:
        """
        Transfer number from one account to another.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        country : typing.Optional[str]

        from_ : typing.Optional[str]

        number : typing.Optional[float]

        to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferNumberResponse
            Number transfer response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.transfers.transfer_number(
            api_key="api_key",
        )
        """
        _response = self._raw_client.transfer_number(
            api_key, country=country, from_=from_, number=number, to=to, request_options=request_options
        )
        return _response.data


class AsyncTransfersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransfersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransfersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransfersClient
        """
        return self._raw_client

    async def retrieve_balance_transfers(
        self,
        api_key: str,
        *,
        start_date: str,
        end_date: typing.Optional[str] = None,
        subaccount: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBalanceTransfersResponse:
        """
        Retrieve a list of balance transfers that have taken place for a primary account within a specified time period.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        start_date : str
            Start of the retrieval period.

        end_date : typing.Optional[str]
            End of the retrieval period. If absent then all transfers until now is returned.

        subaccount : typing.Optional[str]
            Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBalanceTransfersResponse
            List balance transfers response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.transfers.retrieve_balance_transfers(
                api_key="api_key",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_balance_transfers(
            api_key, start_date=start_date, end_date=end_date, subaccount=subaccount, request_options=request_options
        )
        return _response.data

    async def transfer_balance(
        self,
        api_key: str,
        *,
        amount: float,
        from_: str,
        to: str,
        reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferBalanceResponse:
        """
        Transfer balance between a primary account and one of its subaccounts. Note that balance_available_for_transfer = |account_balance - credit_limit| of the source account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        amount : float

        from_ : str

        to : str

        reference : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferBalanceResponse
            Balance transfer response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.transfers.transfer_balance(
                api_key="api_key",
                amount=1.1,
                from_="7c9738e6",
                to="ad6dc56f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_balance(
            api_key, amount=amount, from_=from_, to=to, reference=reference, request_options=request_options
        )
        return _response.data

    async def retrieve_credit_transfers(
        self,
        api_key: str,
        *,
        start_date: str,
        end_date: typing.Optional[str] = None,
        subaccount: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCreditTransfersResponse:
        """
        Retrieve a list of credit transfers that have taken place for a primary account within a specified time period.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        start_date : str
            Start of the retrieval period.

        end_date : typing.Optional[str]
            End of the retrieval period. If absent then all transfers until now is returned.

        subaccount : typing.Optional[str]
            Subaccount to filter by. You may send this multiple times to filter on multiple subaccounts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCreditTransfersResponse
            List credit transfers response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.transfers.retrieve_credit_transfers(
                api_key="api_key",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_credit_transfers(
            api_key, start_date=start_date, end_date=end_date, subaccount=subaccount, request_options=request_options
        )
        return _response.data

    async def transfer_credit(
        self,
        api_key: str,
        *,
        amount: float,
        from_: str,
        to: str,
        reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferCreditResponse:
        """
        Transfer credit limit between a primary account and one of its subaccounts.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        amount : float

        from_ : str

        to : str

        reference : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCreditResponse
            Credit transfer response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.transfers.transfer_credit(
                api_key="api_key",
                amount=1.1,
                from_="7c9738e6",
                to="ad6dc56f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_credit(
            api_key, amount=amount, from_=from_, to=to, reference=reference, request_options=request_options
        )
        return _response.data

    async def transfer_number(
        self,
        api_key: str,
        *,
        country: typing.Optional[str] = OMIT,
        from_: typing.Optional[str] = OMIT,
        number: typing.Optional[float] = OMIT,
        to: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TransferNumberResponse:
        """
        Transfer number from one account to another.

        Parameters
        ----------
        api_key : str
            ID of the primary account.

        country : typing.Optional[str]

        from_ : typing.Optional[str]

        number : typing.Optional[float]

        to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferNumberResponse
            Number transfer response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.transfers.transfer_number(
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transfer_number(
            api_key, country=country, from_=from_, number=number, to=to, request_options=request_options
        )
        return _response.data
