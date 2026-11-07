

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.financial_payouts import FinancialPayouts
from .raw_client import AsyncRawPayoutsClient, RawPayoutsClient
from .types.list_payouts_v1request_format import ListPayoutsV1RequestFormat
from .types.list_payouts_v1request_order import ListPayoutsV1RequestOrder


class PayoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPayoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPayoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPayoutsClient
        """
        return self._raw_client

    def list_payouts_v1(
        self,
        merchant_code: str,
        *,
        start_date: dt.date,
        end_date: dt.date,
        format: typing.Optional[ListPayoutsV1RequestFormat] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListPayoutsV1RequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancialPayouts:
        """
        Lists payout and payout-deduction records for the specified merchant account within the requested date range.

        The response can include:
        - regular payouts (`type = PAYOUT`)
        - deduction records for refunds, chargebacks, direct debit returns, or balance adjustments

        Results are sorted by payout date in the requested `order`.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        start_date : dt.date
            Start date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`).

        end_date : dt.date
            End date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`). Must be greater than or equal to `start_date`.

        format : typing.Optional[ListPayoutsV1RequestFormat]
            Response format for the payout list.

        limit : typing.Optional[int]
            Maximum number of payout records to return.

        order : typing.Optional[ListPayoutsV1RequestOrder]
            Sort direction for the returned payouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancialPayouts
            Returns the list of payout and deduction records for the requested period.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payouts.list_payouts_v1(
            merchant_code="MH4H92C7",
            start_date=datetime.date.fromisoformat(
                "2024-02-01",
            ),
            end_date=datetime.date.fromisoformat(
                "2024-02-29",
            ),
            limit=10,
        )
        """
        _response = self._raw_client.list_payouts_v1(
            merchant_code,
            start_date=start_date,
            end_date=end_date,
            format=format,
            limit=limit,
            order=order,
            request_options=request_options,
        )
        return _response.data


class AsyncPayoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPayoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPayoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPayoutsClient
        """
        return self._raw_client

    async def list_payouts_v1(
        self,
        merchant_code: str,
        *,
        start_date: dt.date,
        end_date: dt.date,
        format: typing.Optional[ListPayoutsV1RequestFormat] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListPayoutsV1RequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancialPayouts:
        """
        Lists payout and payout-deduction records for the specified merchant account within the requested date range.

        The response can include:
        - regular payouts (`type = PAYOUT`)
        - deduction records for refunds, chargebacks, direct debit returns, or balance adjustments

        Results are sorted by payout date in the requested `order`.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        start_date : dt.date
            Start date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`).

        end_date : dt.date
            End date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`). Must be greater than or equal to `start_date`.

        format : typing.Optional[ListPayoutsV1RequestFormat]
            Response format for the payout list.

        limit : typing.Optional[int]
            Maximum number of payout records to return.

        order : typing.Optional[ListPayoutsV1RequestOrder]
            Sort direction for the returned payouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancialPayouts
            Returns the list of payout and deduction records for the requested period.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payouts.list_payouts_v1(
                merchant_code="MH4H92C7",
                start_date=datetime.date.fromisoformat(
                    "2024-02-01",
                ),
                end_date=datetime.date.fromisoformat(
                    "2024-02-29",
                ),
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payouts_v1(
            merchant_code,
            start_date=start_date,
            end_date=end_date,
            format=format,
            limit=limit,
            order=order,
            request_options=request_options,
        )
        return _response.data
