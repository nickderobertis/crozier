

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_beneficiary5 import ObReadBeneficiary5
from .raw_client import AsyncRawBeneficiariesClient, RawBeneficiariesClient


class BeneficiariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeneficiariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBeneficiariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeneficiariesClient
        """
        return self._raw_client

    def get_accounts_account_id_beneficiaries(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadBeneficiary5:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadBeneficiary5
            Beneficiaries Read

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
        client.beneficiaries.get_accounts_account_id_beneficiaries(
            account_id="AccountId",
        )
        """
        _response = self._raw_client.get_accounts_account_id_beneficiaries(account_id, request_options=request_options)
        return _response.data

    def get_beneficiaries(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadBeneficiary5:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadBeneficiary5
            Beneficiaries Read

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
        client.beneficiaries.get_beneficiaries()
        """
        _response = self._raw_client.get_beneficiaries(request_options=request_options)
        return _response.data


class AsyncBeneficiariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeneficiariesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBeneficiariesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeneficiariesClient
        """
        return self._raw_client

    async def get_accounts_account_id_beneficiaries(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadBeneficiary5:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadBeneficiary5
            Beneficiaries Read

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
            await client.beneficiaries.get_accounts_account_id_beneficiaries(
                account_id="AccountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_account_id_beneficiaries(
            account_id, request_options=request_options
        )
        return _response.data

    async def get_beneficiaries(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObReadBeneficiary5:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadBeneficiary5
            Beneficiaries Read

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
            await client.beneficiaries.get_beneficiaries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_beneficiaries(request_options=request_options)
        return _response.data
