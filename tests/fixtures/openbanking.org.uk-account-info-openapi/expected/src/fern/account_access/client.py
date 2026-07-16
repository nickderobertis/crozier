

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ob_read_consent_response1 import ObReadConsentResponse1
from ..types.ob_risk2 import ObRisk2
from .raw_client import AsyncRawAccountAccessClient, RawAccountAccessClient
from .types.ob_read_consent1data import ObReadConsent1Data


OMIT = typing.cast(typing.Any, ...)


class AccountAccessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountAccessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountAccessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountAccessClient
        """
        return self._raw_client

    def create_account_access_consents(
        self, *, data: ObReadConsent1Data, risk: ObRisk2, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadConsentResponse1:
        """
        Parameters
        ----------
        data : ObReadConsent1Data

        risk : ObRisk2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadConsentResponse1
            Account Access Consents Created

        Examples
        --------
        from fern.account_access import (
            ObReadConsent1Data,
            ObReadConsent1DataPermissionsItem,
        )

        from fern import FernApi, ObRisk2

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )
        client.account_access.create_account_access_consents(
            data=ObReadConsent1Data(
                permissions=[ObReadConsent1DataPermissionsItem.READ_ACCOUNTS_BASIC],
            ),
            risk=ObRisk2(),
        )
        """
        _response = self._raw_client.create_account_access_consents(
            data=data, risk=risk, request_options=request_options
        )
        return _response.data

    def get_account_access_consents_consent_id(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadConsentResponse1:
        """
        Parameters
        ----------
        consent_id : str
            ConsentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadConsentResponse1
            Account Access Consents Read

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
        client.account_access.get_account_access_consents_consent_id(
            consent_id="ConsentId",
        )
        """
        _response = self._raw_client.get_account_access_consents_consent_id(consent_id, request_options=request_options)
        return _response.data

    def delete_account_access_consents_consent_id(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        consent_id : str
            ConsentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

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
        client.account_access.delete_account_access_consents_consent_id(
            consent_id="ConsentId",
        )
        """
        _response = self._raw_client.delete_account_access_consents_consent_id(
            consent_id, request_options=request_options
        )
        return _response.data


class AsyncAccountAccessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountAccessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountAccessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountAccessClient
        """
        return self._raw_client

    async def create_account_access_consents(
        self, *, data: ObReadConsent1Data, risk: ObRisk2, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadConsentResponse1:
        """
        Parameters
        ----------
        data : ObReadConsent1Data

        risk : ObRisk2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadConsentResponse1
            Account Access Consents Created

        Examples
        --------
        import asyncio

        from fern.account_access import (
            ObReadConsent1Data,
            ObReadConsent1DataPermissionsItem,
        )

        from fern import AsyncFernApi, ObRisk2

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_access.create_account_access_consents(
                data=ObReadConsent1Data(
                    permissions=[ObReadConsent1DataPermissionsItem.READ_ACCOUNTS_BASIC],
                ),
                risk=ObRisk2(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_account_access_consents(
            data=data, risk=risk, request_options=request_options
        )
        return _response.data

    async def get_account_access_consents_consent_id(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObReadConsentResponse1:
        """
        Parameters
        ----------
        consent_id : str
            ConsentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObReadConsentResponse1
            Account Access Consents Read

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
            await client.account_access.get_account_access_consents_consent_id(
                consent_id="ConsentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_access_consents_consent_id(
            consent_id, request_options=request_options
        )
        return _response.data

    async def delete_account_access_consents_consent_id(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        consent_id : str
            ConsentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

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
            await client.account_access.delete_account_access_consents_consent_id(
                consent_id="ConsentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_account_access_consents_consent_id(
            consent_id, request_options=request_options
        )
        return _response.data
