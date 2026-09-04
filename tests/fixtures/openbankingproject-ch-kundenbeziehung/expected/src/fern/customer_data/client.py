

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.basic_customer_data import BasicCustomerData
from ..types.customer_check_response import CustomerCheckResponse
from ..types.customer_data_response import CustomerDataResponse
from ..types.full_customer_dataset import FullCustomerDataset
from .raw_client import AsyncRawCustomerDataClient, RawCustomerDataClient
from .types.customer_data_request_purpose import CustomerDataRequestPurpose
from .types.customer_data_request_requested_modules_item import CustomerDataRequestRequestedModulesItem
from .types.full_data_request_purpose import FullDataRequestPurpose


OMIT = typing.cast(typing.Any, ...)


class CustomerDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerDataClient
        """
        return self._raw_client

    def check_customer(
        self,
        *,
        shared_customer_hash: str,
        basic_data: BasicCustomerData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomerCheckResponse:
        """
        Prüft ob ein Kunde bereits bei einer Institution identifiziert wurde (MVP Identifikation)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash der Grunddaten für Matching

        basic_data : BasicCustomerData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomerCheckResponse
            Kunde erfolgreich geprüft

        Examples
        --------
        import datetime

        from fern import BasicCustomerData, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer_data.check_customer(
            shared_customer_hash="sha256:abc123def456...",
            basic_data=BasicCustomerData(
                last_name="Müller",
                given_name="Hans",
                birth_date=datetime.date.fromisoformat(
                    "1985-03-15",
                ),
                nationality=["CH"],
            ),
        )
        """
        _response = self._raw_client.check_customer(
            shared_customer_hash=shared_customer_hash, basic_data=basic_data, request_options=request_options
        )
        return _response.data

    def request_full_customer_data(
        self,
        *,
        shared_customer_hash: str,
        purpose: FullDataRequestPurpose,
        consent_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FullCustomerDataset:
        """
        Fordert das vollständige Kundendatenset an (erfordert gültigen Consent)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        purpose : FullDataRequestPurpose

        consent_token : str
            JWT-Token mit Consent-Nachweis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullCustomerDataset
            Kundendaten erfolgreich übertragen

        Examples
        --------
        from fern.customer_data import FullDataRequestPurpose

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer_data.request_full_customer_data(
            shared_customer_hash="sharedCustomerHash",
            purpose=FullDataRequestPurpose.ACCOUNT_OPENING,
            consent_token="consentToken",
        )
        """
        _response = self._raw_client.request_full_customer_data(
            shared_customer_hash=shared_customer_hash,
            purpose=purpose,
            consent_token=consent_token,
            request_options=request_options,
        )
        return _response.data

    def get_customer_data(
        self,
        *,
        shared_customer_hash: str,
        requested_modules: typing.Sequence[CustomerDataRequestRequestedModulesItem],
        consent_token: str,
        purpose: typing.Optional[CustomerDataRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomerDataResponse:
        """
        Ruft spezifische Kundendatenmodule basierend auf gewährtem Consent ab

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        requested_modules : typing.Sequence[CustomerDataRequestRequestedModulesItem]
            Angeforderte Datenbausteine

        consent_token : str
            JWT-Token mit Consent-Nachweis

        purpose : typing.Optional[CustomerDataRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomerDataResponse
            Kundendaten erfolgreich abgerufen

        Examples
        --------
        from fern.customer_data import CustomerDataRequestRequestedModulesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer_data.get_customer_data(
            shared_customer_hash="sharedCustomerHash",
            requested_modules=[
                CustomerDataRequestRequestedModulesItem.BASISDATEN_MODULE
            ],
            consent_token="consentToken",
        )
        """
        _response = self._raw_client.get_customer_data(
            shared_customer_hash=shared_customer_hash,
            requested_modules=requested_modules,
            consent_token=consent_token,
            purpose=purpose,
            request_options=request_options,
        )
        return _response.data


class AsyncCustomerDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerDataClient
        """
        return self._raw_client

    async def check_customer(
        self,
        *,
        shared_customer_hash: str,
        basic_data: BasicCustomerData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomerCheckResponse:
        """
        Prüft ob ein Kunde bereits bei einer Institution identifiziert wurde (MVP Identifikation)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash der Grunddaten für Matching

        basic_data : BasicCustomerData

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomerCheckResponse
            Kunde erfolgreich geprüft

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, BasicCustomerData

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_data.check_customer(
                shared_customer_hash="sha256:abc123def456...",
                basic_data=BasicCustomerData(
                    last_name="Müller",
                    given_name="Hans",
                    birth_date=datetime.date.fromisoformat(
                        "1985-03-15",
                    ),
                    nationality=["CH"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_customer(
            shared_customer_hash=shared_customer_hash, basic_data=basic_data, request_options=request_options
        )
        return _response.data

    async def request_full_customer_data(
        self,
        *,
        shared_customer_hash: str,
        purpose: FullDataRequestPurpose,
        consent_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FullCustomerDataset:
        """
        Fordert das vollständige Kundendatenset an (erfordert gültigen Consent)

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        purpose : FullDataRequestPurpose

        consent_token : str
            JWT-Token mit Consent-Nachweis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FullCustomerDataset
            Kundendaten erfolgreich übertragen

        Examples
        --------
        import asyncio

        from fern.customer_data import FullDataRequestPurpose

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_data.request_full_customer_data(
                shared_customer_hash="sharedCustomerHash",
                purpose=FullDataRequestPurpose.ACCOUNT_OPENING,
                consent_token="consentToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_full_customer_data(
            shared_customer_hash=shared_customer_hash,
            purpose=purpose,
            consent_token=consent_token,
            request_options=request_options,
        )
        return _response.data

    async def get_customer_data(
        self,
        *,
        shared_customer_hash: str,
        requested_modules: typing.Sequence[CustomerDataRequestRequestedModulesItem],
        consent_token: str,
        purpose: typing.Optional[CustomerDataRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomerDataResponse:
        """
        Ruft spezifische Kundendatenmodule basierend auf gewährtem Consent ab

        Parameters
        ----------
        shared_customer_hash : str
            SHA-256 Hash des Kunden

        requested_modules : typing.Sequence[CustomerDataRequestRequestedModulesItem]
            Angeforderte Datenbausteine

        consent_token : str
            JWT-Token mit Consent-Nachweis

        purpose : typing.Optional[CustomerDataRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomerDataResponse
            Kundendaten erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern.customer_data import CustomerDataRequestRequestedModulesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_data.get_customer_data(
                shared_customer_hash="sharedCustomerHash",
                requested_modules=[
                    CustomerDataRequestRequestedModulesItem.BASISDATEN_MODULE
                ],
                consent_token="consentToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer_data(
            shared_customer_hash=shared_customer_hash,
            requested_modules=requested_modules,
            consent_token=consent_token,
            purpose=purpose,
            request_options=request_options,
        )
        return _response.data
