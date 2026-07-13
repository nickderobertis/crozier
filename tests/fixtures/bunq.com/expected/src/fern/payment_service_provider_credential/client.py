

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_service_provider_credential_create import PaymentServiceProviderCredentialCreate
from ..types.payment_service_provider_credential_read import PaymentServiceProviderCredentialRead
from .raw_client import AsyncRawPaymentServiceProviderCredentialClient, RawPaymentServiceProviderCredentialClient


OMIT = typing.cast(typing.Any, ...)


class PaymentServiceProviderCredentialClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentServiceProviderCredentialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentServiceProviderCredentialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentServiceProviderCredentialClient
        """
        return self._raw_client

    def create_payment_service_provider_credential(
        self,
        *,
        client_payment_service_provider_certificate: str,
        client_payment_service_provider_certificate_chain: str,
        client_public_key_signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderCredentialCreate:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        client_payment_service_provider_certificate : str
            Payment Services Directive 2 compatible QSEAL certificate

        client_payment_service_provider_certificate_chain : str
            Intermediate and root certificate belonging to the provided certificate.

        client_public_key_signature : str
            The Base64 encoded signature of the public key provided during installation and with the installation token appended as a nonce. Signed with the private key belonging to the QSEAL certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderCredentialCreate
            Register a Payment Service Provider and provide credentials

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_credential.create_payment_service_provider_credential(
            client_payment_service_provider_certificate="client_payment_service_provider_certificate",
            client_payment_service_provider_certificate_chain="client_payment_service_provider_certificate_chain",
            client_public_key_signature="client_public_key_signature",
        )
        """
        _response = self._raw_client.create_payment_service_provider_credential(
            client_payment_service_provider_certificate=client_payment_service_provider_certificate,
            client_payment_service_provider_certificate_chain=client_payment_service_provider_certificate_chain,
            client_public_key_signature=client_public_key_signature,
            request_options=request_options,
        )
        return _response.data

    def read_payment_service_provider_credential(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentServiceProviderCredentialRead:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderCredentialRead
            Register a Payment Service Provider and provide credentials

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.payment_service_provider_credential.read_payment_service_provider_credential(
            item_id=1,
        )
        """
        _response = self._raw_client.read_payment_service_provider_credential(item_id, request_options=request_options)
        return _response.data


class AsyncPaymentServiceProviderCredentialClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentServiceProviderCredentialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentServiceProviderCredentialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentServiceProviderCredentialClient
        """
        return self._raw_client

    async def create_payment_service_provider_credential(
        self,
        *,
        client_payment_service_provider_certificate: str,
        client_payment_service_provider_certificate_chain: str,
        client_public_key_signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentServiceProviderCredentialCreate:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        client_payment_service_provider_certificate : str
            Payment Services Directive 2 compatible QSEAL certificate

        client_payment_service_provider_certificate_chain : str
            Intermediate and root certificate belonging to the provided certificate.

        client_public_key_signature : str
            The Base64 encoded signature of the public key provided during installation and with the installation token appended as a nonce. Signed with the private key belonging to the QSEAL certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderCredentialCreate
            Register a Payment Service Provider and provide credentials

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_credential.create_payment_service_provider_credential(
                client_payment_service_provider_certificate="client_payment_service_provider_certificate",
                client_payment_service_provider_certificate_chain="client_payment_service_provider_certificate_chain",
                client_public_key_signature="client_public_key_signature",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_service_provider_credential(
            client_payment_service_provider_certificate=client_payment_service_provider_certificate,
            client_payment_service_provider_certificate_chain=client_payment_service_provider_certificate_chain,
            client_public_key_signature=client_public_key_signature,
            request_options=request_options,
        )
        return _response.data

    async def read_payment_service_provider_credential(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaymentServiceProviderCredentialRead:
        """
        Register a Payment Service Provider and provide credentials

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentServiceProviderCredentialRead
            Register a Payment Service Provider and provide credentials

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.payment_service_provider_credential.read_payment_service_provider_credential(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_payment_service_provider_credential(
            item_id, request_options=request_options
        )
        return _response.data
