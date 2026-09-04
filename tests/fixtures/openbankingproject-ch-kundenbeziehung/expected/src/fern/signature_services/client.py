

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.document_to_sign import DocumentToSign
from ..types.signature_response import SignatureResponse
from ..types.signature_status import SignatureStatus
from .raw_client import AsyncRawSignatureServicesClient, RawSignatureServicesClient
from .types.signature_request_notification_method import SignatureRequestNotificationMethod
from .types.signature_request_signature_type import SignatureRequestSignatureType


OMIT = typing.cast(typing.Any, ...)


class SignatureServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignatureServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignatureServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignatureServicesClient
        """
        return self._raw_client

    def initiate_signature(
        self,
        *,
        customer_id: str,
        documents: typing.Sequence[DocumentToSign],
        signature_type: SignatureRequestSignatureType,
        notification_method: typing.Optional[SignatureRequestNotificationMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignatureResponse:
        """
        Startet einen QES- oder eSignatur-Prozess

        Parameters
        ----------
        customer_id : str

        documents : typing.Sequence[DocumentToSign]

        signature_type : SignatureRequestSignatureType

        notification_method : typing.Optional[SignatureRequestNotificationMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignatureResponse
            Signatur-Prozess erfolgreich initiiert

        Examples
        --------
        from fern.signature_services import SignatureRequestSignatureType

        from fern import DocumentToSign, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.signature_services.initiate_signature(
            customer_id="customerId",
            documents=[
                DocumentToSign(
                    document_id="documentId",
                    document_name="documentName",
                    document_hash="documentHash",
                )
            ],
            signature_type=SignatureRequestSignatureType.QES,
        )
        """
        _response = self._raw_client.initiate_signature(
            customer_id=customer_id,
            documents=documents,
            signature_type=signature_type,
            notification_method=notification_method,
            request_options=request_options,
        )
        return _response.data

    def get_signature_status(
        self, signature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SignatureStatus:
        """
        Ruft den Status eines Signatur-Prozesses ab

        Parameters
        ----------
        signature_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignatureStatus
            Signatur-Status erfolgreich abgerufen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.signature_services.get_signature_status(
            signature_id="signatureId",
        )
        """
        _response = self._raw_client.get_signature_status(signature_id, request_options=request_options)
        return _response.data


class AsyncSignatureServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignatureServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignatureServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignatureServicesClient
        """
        return self._raw_client

    async def initiate_signature(
        self,
        *,
        customer_id: str,
        documents: typing.Sequence[DocumentToSign],
        signature_type: SignatureRequestSignatureType,
        notification_method: typing.Optional[SignatureRequestNotificationMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignatureResponse:
        """
        Startet einen QES- oder eSignatur-Prozess

        Parameters
        ----------
        customer_id : str

        documents : typing.Sequence[DocumentToSign]

        signature_type : SignatureRequestSignatureType

        notification_method : typing.Optional[SignatureRequestNotificationMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignatureResponse
            Signatur-Prozess erfolgreich initiiert

        Examples
        --------
        import asyncio

        from fern.signature_services import SignatureRequestSignatureType

        from fern import AsyncFernApi, DocumentToSign

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.signature_services.initiate_signature(
                customer_id="customerId",
                documents=[
                    DocumentToSign(
                        document_id="documentId",
                        document_name="documentName",
                        document_hash="documentHash",
                    )
                ],
                signature_type=SignatureRequestSignatureType.QES,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_signature(
            customer_id=customer_id,
            documents=documents,
            signature_type=signature_type,
            notification_method=notification_method,
            request_options=request_options,
        )
        return _response.data

    async def get_signature_status(
        self, signature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SignatureStatus:
        """
        Ruft den Status eines Signatur-Prozesses ab

        Parameters
        ----------
        signature_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignatureStatus
            Signatur-Status erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.signature_services.get_signature_status(
                signature_id="signatureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_signature_status(signature_id, request_options=request_options)
        return _response.data
