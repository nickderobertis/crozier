

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_transaction6 import ObReadTransaction6
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionsClient
        """
        return self._raw_client

    def get_accounts_account_id_statements_statement_id_transactions(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        statement_id : str
            StatementId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.transactions.get_accounts_account_id_statements_statement_id_transactions(
            account_id="AccountId",
            statement_id="StatementId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_statements_statement_id_transactions(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    def get_accounts_account_id_transactions(
        self,
        account_id: str,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.transactions.get_accounts_account_id_transactions(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_transactions(
            account_id,
            from_booking_date_time=from_booking_date_time,
            to_booking_date_time=to_booking_date_time,
            request_options=request_options,
        )
        return _response.data

    def get_transactions(
        self,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.transactions.get_transactions()
        """
        _response = self._raw_client.get_transactions(
            from_booking_date_time=from_booking_date_time,
            to_booking_date_time=to_booking_date_time,
            request_options=request_options,
        )
        return _response.data


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionsClient
        """
        return self._raw_client

    async def get_accounts_account_id_statements_statement_id_transactions(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        statement_id : str
            StatementId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.get_accounts_account_id_statements_statement_id_transactions(
                account_id="AccountId",
                statement_id="StatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_statements_statement_id_transactions(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    async def get_accounts_account_id_transactions(
        self,
        account_id: str,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.get_accounts_account_id_transactions(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_transactions(
            account_id,
            from_booking_date_time=from_booking_date_time,
            to_booking_date_time=to_booking_date_time,
            request_options=request_options,
        )
        return _response.data

    async def get_transactions(
        self,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadTransaction6:
        """
        Parameters
        ----------
        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadTransaction6
            Transactions Read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.get_transactions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transactions(
            from_booking_date_time=from_booking_date_time,
            to_booking_date_time=to_booking_date_time,
            request_options=request_options,
        )
        return _response.data
