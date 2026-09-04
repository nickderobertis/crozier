

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.biometric_data import BiometricData
from ..types.document_data import DocumentData
from ..types.identification_response import IdentificationResponse
from ..types.identification_status_response import IdentificationStatusResponse
from .raw_client import AsyncRawIdentificationClient, RawIdentificationClient
from .types.identification_request_identification_type import IdentificationRequestIdentificationType


OMIT = typing.cast(typing.Any, ...)


class IdentificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentificationClient
        """
        return self._raw_client

    def get_identification_status(
        self, verification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IdentificationStatusResponse:
        """
        Ruft den Status einer bestehenden Identifikation ab (für UC2 Re-identification)

        Parameters
        ----------
        verification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentificationStatusResponse
            Identifikations-Status erfolgreich abgerufen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identification.get_identification_status(
            verification_id="VER-20240115-001",
        )
        """
        _response = self._raw_client.get_identification_status(verification_id, request_options=request_options)
        return _response.data

    def verify_identification(
        self,
        *,
        customer_id: str,
        identification_type: IdentificationRequestIdentificationType,
        document_data: typing.Optional[DocumentData] = OMIT,
        biometric_data: typing.Optional[BiometricData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentificationResponse:
        """
        Verifiziert Identifikationsdaten gegen E-ID oder andere Quellen

        Parameters
        ----------
        customer_id : str

        identification_type : IdentificationRequestIdentificationType

        document_data : typing.Optional[DocumentData]

        biometric_data : typing.Optional[BiometricData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentificationResponse
            Identifikation erfolgreich verifiziert

        Examples
        --------
        from fern.identification import IdentificationRequestIdentificationType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identification.verify_identification(
            customer_id="customerId",
            identification_type=IdentificationRequestIdentificationType.EID_VERIFICATION,
        )
        """
        _response = self._raw_client.verify_identification(
            customer_id=customer_id,
            identification_type=identification_type,
            document_data=document_data,
            biometric_data=biometric_data,
            request_options=request_options,
        )
        return _response.data


class AsyncIdentificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentificationClient
        """
        return self._raw_client

    async def get_identification_status(
        self, verification_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IdentificationStatusResponse:
        """
        Ruft den Status einer bestehenden Identifikation ab (für UC2 Re-identification)

        Parameters
        ----------
        verification_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentificationStatusResponse
            Identifikations-Status erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identification.get_identification_status(
                verification_id="VER-20240115-001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_identification_status(verification_id, request_options=request_options)
        return _response.data

    async def verify_identification(
        self,
        *,
        customer_id: str,
        identification_type: IdentificationRequestIdentificationType,
        document_data: typing.Optional[DocumentData] = OMIT,
        biometric_data: typing.Optional[BiometricData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdentificationResponse:
        """
        Verifiziert Identifikationsdaten gegen E-ID oder andere Quellen

        Parameters
        ----------
        customer_id : str

        identification_type : IdentificationRequestIdentificationType

        document_data : typing.Optional[DocumentData]

        biometric_data : typing.Optional[BiometricData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdentificationResponse
            Identifikation erfolgreich verifiziert

        Examples
        --------
        import asyncio

        from fern.identification import IdentificationRequestIdentificationType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identification.verify_identification(
                customer_id="customerId",
                identification_type=IdentificationRequestIdentificationType.EID_VERIFICATION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_identification(
            customer_id=customer_id,
            identification_type=identification_type,
            document_data=document_data,
            biometric_data=biometric_data,
            request_options=request_options,
        )
        return _response.data
