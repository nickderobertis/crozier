

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_party2 import ObReadParty2
from ..types.ob_read_party3 import ObReadParty3
from .raw_client import AsyncRawPartiesClient, RawPartiesClient


class PartiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPartiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPartiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPartiesClient
        """
        return self._raw_client

    def get_accounts_account_id_parties(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadParty3:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty3
            Parties Read

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
        client.parties.get_accounts_account_id_parties(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_parties(account_id, request_options=request_options)
        return _response.data

    def get_accounts_account_id_party(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadParty2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty2
            Parties Read

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
        client.parties.get_accounts_account_id_party(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_party(account_id, request_options=request_options)
        return _response.data

    def get_party(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadParty2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty2
            Parties Read

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
        client.parties.get_party()
        """
        _response = self._raw_client.get_party(request_options=request_options)
        return _response.data


class AsyncPartiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPartiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPartiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPartiesClient
        """
        return self._raw_client

    async def get_accounts_account_id_parties(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadParty3:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty3
            Parties Read

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
            await client.parties.get_accounts_account_id_parties(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_parties(account_id, request_options=request_options)
        return _response.data

    async def get_accounts_account_id_party(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadParty2:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty2
            Parties Read

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
            await client.parties.get_accounts_account_id_party(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_party(account_id, request_options=request_options)
        return _response.data

    async def get_party(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadParty2:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadParty2
            Parties Read

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
            await client.parties.get_party()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party(request_options=request_options)
        return _response.data
