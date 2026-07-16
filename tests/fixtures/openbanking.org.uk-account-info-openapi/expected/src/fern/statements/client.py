

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file import File
from ..types.ob_read_statement2 import ObReadStatement2
from .raw_client import AsyncRawStatementsClient, RawStatementsClient


class StatementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatementsClient
        """
        return self._raw_client

    def get_accounts_account_id_statements(
        self,
        account_id: str,
        *,
        from_statement_date_time: typing.Optional[dt.datetime] = None,
        to_statement_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadStatement2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStatement2
            Statements Read

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
        client.statements.get_accounts_account_id_statements(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_statements(
            account_id,
            from_statement_date_time=from_statement_date_time,
            to_statement_date_time=to_statement_date_time,
            request_options=request_options,
        )
        return _response.data

    def get_accounts_account_id_statements_statement_id(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadStatement2:
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
        ObReadStatement2
            Statements Read

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
        client.statements.get_accounts_account_id_statements_statement_id(
            account_id="AccountId",
            statement_id="StatementId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_statements_statement_id(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    def get_accounts_account_id_statements_statement_id_file(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> File:
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
        File
            Statements Read

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
        client.statements.get_accounts_account_id_statements_statement_id_file(
            account_id="AccountId",
            statement_id="StatementId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_statements_statement_id_file(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    def get_statements(
        self,
        *,
        from_statement_date_time: typing.Optional[dt.datetime] = None,
        to_statement_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadStatement2:
        """
        Parameters
        ----------
        from_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStatement2
            Statements Read

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
        client.statements.get_statements()
        """
        _response = self._raw_client.get_statements(
            from_statement_date_time=from_statement_date_time,
            to_statement_date_time=to_statement_date_time,
            request_options=request_options,
        )
        return _response.data


class AsyncStatementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatementsClient
        """
        return self._raw_client

    async def get_accounts_account_id_statements(
        self,
        account_id: str,
        *,
        from_statement_date_time: typing.Optional[dt.datetime] = None,
        to_statement_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadStatement2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStatement2
            Statements Read

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
            await client.statements.get_accounts_account_id_statements(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_statements(
            account_id,
            from_statement_date_time=from_statement_date_time,
            to_statement_date_time=to_statement_date_time,
            request_options=request_options,
        )
        return _response.data

    async def get_accounts_account_id_statements_statement_id(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadStatement2:
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
        ObReadStatement2
            Statements Read

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
            await client.statements.get_accounts_account_id_statements_statement_id(
                account_id="AccountId",
                statement_id="StatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_statements_statement_id(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    async def get_accounts_account_id_statements_statement_id_file(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> File:
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
        File
            Statements Read

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
            await client.statements.get_accounts_account_id_statements_statement_id_file(
                account_id="AccountId",
                statement_id="StatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_statements_statement_id_file(
            account_id, statement_id, request_options=request_options
        )
        return _response.data

    async def get_statements(
        self,
        *,
        from_statement_date_time: typing.Optional[dt.datetime] = None,
        to_statement_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObReadStatement2:
        """
        Parameters
        ----------
        from_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_statement_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter statements TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadStatement2
            Statements Read

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
            await client.statements.get_statements()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_statements(
            from_statement_date_time=from_statement_date_time,
            to_statement_date_time=to_statement_date_time,
            request_options=request_options,
        )
        return _response.data
