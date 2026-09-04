

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consent_response import ConsentResponse
from ..types.consent_status import ConsentStatus
from ..types.data_category import DataCategory
from .raw_client import AsyncRawConsentManagementClient, RawConsentManagementClient
from .types.consent_request_customer_contact_method import ConsentRequestCustomerContactMethod
from .types.consent_request_purpose import ConsentRequestPurpose


OMIT = typing.cast(typing.Any, ...)


class ConsentManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsentManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsentManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsentManagementClient
        """
        return self._raw_client

    def create_consent(
        self,
        *,
        customer_id: str,
        requesting_institution: str,
        data_categories: typing.Sequence[DataCategory],
        purpose: ConsentRequestPurpose,
        expiry_date: dt.datetime,
        providing_institution: typing.Optional[str] = OMIT,
        customer_contact_method: typing.Optional[ConsentRequestCustomerContactMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsentResponse:
        """
        Initiiert einen Consent-Flow für Datenaustausch zwischen Institutionen

        Parameters
        ----------
        customer_id : str
            Eindeutige Kunden-ID (sharedCustomerHash)

        requesting_institution : str
            Institution die Daten anfordert

        data_categories : typing.Sequence[DataCategory]
            Angeforderte Datenkategorien

        purpose : ConsentRequestPurpose
            Zweck der Datenverwendung

        expiry_date : dt.datetime
            Ablaufzeitpunkt des Consents

        providing_institution : typing.Optional[str]
            Institution die Daten bereitstellt

        customer_contact_method : typing.Optional[ConsentRequestCustomerContactMethod]
            Bevorzugter Kontaktweg für Consent-Bestätigung

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentResponse
            Consent erfolgreich erstellt

        Examples
        --------
        import datetime

        from fern.consent_management import (
            ConsentRequestCustomerContactMethod,
            ConsentRequestPurpose,
        )

        from fern import DataCategory, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.consent_management.create_consent(
            customer_id="sha256:a1b2c3d4e5f6...",
            requesting_institution="CH-BANK-001",
            providing_institution="CH-BANK-002",
            data_categories=[
                DataCategory.BASIC_DATA,
                DataCategory.IDENTIFICATION,
                DataCategory.KYC_DATA,
            ],
            purpose=ConsentRequestPurpose.ACCOUNT_OPENING,
            expiry_date=datetime.datetime.fromisoformat(
                "2024-12-31 23:59:59+00:00",
            ),
            customer_contact_method=ConsentRequestCustomerContactMethod.EMAIL,
        )
        """
        _response = self._raw_client.create_consent(
            customer_id=customer_id,
            requesting_institution=requesting_institution,
            data_categories=data_categories,
            purpose=purpose,
            expiry_date=expiry_date,
            providing_institution=providing_institution,
            customer_contact_method=customer_contact_method,
            request_options=request_options,
        )
        return _response.data

    def get_consent_status(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsentStatus:
        """
        Ruft den aktuellen Status eines Consent-Requests ab

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentStatus
            Consent-Status erfolgreich abgerufen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.consent_management.get_consent_status(
            consent_id="123e4567-e89b-12d3-a456-426614174000",
        )
        """
        _response = self._raw_client.get_consent_status(consent_id, request_options=request_options)
        return _response.data

    def revoke_consent(self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Widerruft einen bestehenden Consent

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.consent_management.revoke_consent(
            consent_id="consentId",
        )
        """
        _response = self._raw_client.revoke_consent(consent_id, request_options=request_options)
        return _response.data


class AsyncConsentManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsentManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsentManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsentManagementClient
        """
        return self._raw_client

    async def create_consent(
        self,
        *,
        customer_id: str,
        requesting_institution: str,
        data_categories: typing.Sequence[DataCategory],
        purpose: ConsentRequestPurpose,
        expiry_date: dt.datetime,
        providing_institution: typing.Optional[str] = OMIT,
        customer_contact_method: typing.Optional[ConsentRequestCustomerContactMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConsentResponse:
        """
        Initiiert einen Consent-Flow für Datenaustausch zwischen Institutionen

        Parameters
        ----------
        customer_id : str
            Eindeutige Kunden-ID (sharedCustomerHash)

        requesting_institution : str
            Institution die Daten anfordert

        data_categories : typing.Sequence[DataCategory]
            Angeforderte Datenkategorien

        purpose : ConsentRequestPurpose
            Zweck der Datenverwendung

        expiry_date : dt.datetime
            Ablaufzeitpunkt des Consents

        providing_institution : typing.Optional[str]
            Institution die Daten bereitstellt

        customer_contact_method : typing.Optional[ConsentRequestCustomerContactMethod]
            Bevorzugter Kontaktweg für Consent-Bestätigung

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentResponse
            Consent erfolgreich erstellt

        Examples
        --------
        import asyncio
        import datetime

        from fern.consent_management import (
            ConsentRequestCustomerContactMethod,
            ConsentRequestPurpose,
        )

        from fern import AsyncFernApi, DataCategory

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent_management.create_consent(
                customer_id="sha256:a1b2c3d4e5f6...",
                requesting_institution="CH-BANK-001",
                providing_institution="CH-BANK-002",
                data_categories=[
                    DataCategory.BASIC_DATA,
                    DataCategory.IDENTIFICATION,
                    DataCategory.KYC_DATA,
                ],
                purpose=ConsentRequestPurpose.ACCOUNT_OPENING,
                expiry_date=datetime.datetime.fromisoformat(
                    "2024-12-31 23:59:59+00:00",
                ),
                customer_contact_method=ConsentRequestCustomerContactMethod.EMAIL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_consent(
            customer_id=customer_id,
            requesting_institution=requesting_institution,
            data_categories=data_categories,
            purpose=purpose,
            expiry_date=expiry_date,
            providing_institution=providing_institution,
            customer_contact_method=customer_contact_method,
            request_options=request_options,
        )
        return _response.data

    async def get_consent_status(
        self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsentStatus:
        """
        Ruft den aktuellen Status eines Consent-Requests ab

        Parameters
        ----------
        consent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsentStatus
            Consent-Status erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent_management.get_consent_status(
                consent_id="123e4567-e89b-12d3-a456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_consent_status(consent_id, request_options=request_options)
        return _response.data

    async def revoke_consent(self, consent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Widerruft einen bestehenden Consent

        Parameters
        ----------
        consent_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent_management.revoke_consent(
                consent_id="consentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_consent(consent_id, request_options=request_options)
        return _response.data
