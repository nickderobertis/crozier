

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.any import Any
from ..types.byte_stream_body import ByteStreamBody
from ..types.cert_valid_response import CertValidResponse
from ..types.done import Done
from ..types.lets_encrypt_cert_body import LetsEncryptCertBody
from ..types.otoroshi_ssl_cert_ca_ref import OtoroshiSslCertCaRef
from ..types.otoroshi_ssl_cert_cert_type import OtoroshiSslCertCertType
from ..types.otoroshi_ssl_cert_password import OtoroshiSslCertPassword
from ..types.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
from ..types.otoroshi_ssl_pki_models_gen_csr_query_existing_serial_number import (
    OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
)
from ..types.otoroshi_ssl_pki_models_gen_csr_query_subject import OtoroshiSslPkiModelsGenCsrQuerySubject
from ..types.otoroshi_ssl_pki_models_gen_csr_response import OtoroshiSslPkiModelsGenCsrResponse
from ..types.otoroshi_ssl_pki_models_gen_key_pair_query import OtoroshiSslPkiModelsGenKeyPairQuery
from ..types.otoroshi_ssl_pki_models_gen_key_pair_response import OtoroshiSslPkiModelsGenKeyPairResponse
from ..types.otoroshi_ssl_pki_models_sign_cert_response import OtoroshiSslPkiModelsSignCertResponse
from ..types.pem_certificate_body import PemCertificateBody
from ..types.pem_csr_body import PemCsrBody
from .raw_client import AsyncRawPkiClient, RawPkiClient


OMIT = typing.cast(typing.Any, ...)


class PkiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPkiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPkiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPkiClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
        self, *, request: LetsEncryptCertBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        request : LetsEncryptCertBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
        self, *, request: ByteStreamBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : ByteStreamBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
            request="string",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(
        self,
        *,
        cert_type: typing.Optional[OtoroshiSslCertCertType] = OMIT,
        name: typing.Optional[str] = OMIT,
        revoked: typing.Optional[bool] = OMIT,
        subject: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        keypair: typing.Optional[bool] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        auto_renew: typing.Optional[bool] = OMIT,
        ca_ref: typing.Optional[OtoroshiSslCertCaRef] = OMIT,
        to: typing.Optional[float] = OMIT,
        exposed: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        sans: typing.Optional[typing.Sequence[str]] = OMIT,
        client: typing.Optional[bool] = OMIT,
        from_: typing.Optional[float] = OMIT,
        valid: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        private_key: typing.Optional[str] = OMIT,
        self_signed: typing.Optional[bool] = OMIT,
        chain: typing.Optional[str] = OMIT,
        password: typing.Optional[OtoroshiSslCertPassword] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertValidResponse:
        """
        Parameters
        ----------
        cert_type : typing.Optional[OtoroshiSslCertCertType]
            the kind of certificate

        name : typing.Optional[str]
            Entity name

        revoked : typing.Optional[bool]
            Certificate is revoked

        subject : typing.Optional[str]
            Certificate subject

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        domain : typing.Optional[str]
            Certificate domain

        ca : typing.Optional[bool]
            Is cert a CA ?

        keypair : typing.Optional[bool]
            Is cert used for its keypair only ?

        lets_encrypt : typing.Optional[bool]
            Let's encrypt (ACME) generated

        auto_renew : typing.Optional[bool]
            Auto renew cert

        ca_ref : typing.Optional[OtoroshiSslCertCaRef]
            Reference to the CA (if any)

        to : typing.Optional[float]
            Stop date

        exposed : typing.Optional[bool]
            Is the cert exposed (public key exposed in jwks.json)

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        sans : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        client : typing.Optional[bool]
            Is cert a client cert ?

        from_ : typing.Optional[float]
            Start date

        valid : typing.Optional[bool]
            Is cert valid

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        private_key : typing.Optional[str]
            Certificate private key (PEM encoded)

        self_signed : typing.Optional[bool]
            Is cert self signed

        chain : typing.Optional[str]
            Certicates chain (PEM encoded)

        password : typing.Optional[OtoroshiSslCertPassword]
            Certificate password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertValidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_certificate_is_valid()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(
            cert_type=cert_type,
            name=name,
            revoked=revoked,
            subject=subject,
            description=description,
            tags=tags,
            domain=domain,
            ca=ca,
            keypair=keypair,
            lets_encrypt=lets_encrypt,
            auto_renew=auto_renew,
            ca_ref=ca_ref,
            to=to,
            exposed=exposed,
            id=id,
            loc=loc,
            sans=sans,
            client=client,
            from_=from_,
            valid=valid,
            metadata=metadata,
            private_key=private_key,
            self_signed=self_signed,
            chain=chain,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_certificate_data(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_certificate_data(
            request="string",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_certificate_data(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_csr(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCsrResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCsrResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_csr()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_csr(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
        self,
        *,
        algo: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenKeyPairResponse:
        """
        Parameters
        ----------
        algo : typing.Optional[str]
            Keypair algorithm

        size : typing.Optional[int]
            Keypair size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenKeyPairResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_key_pair()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
            algo=algo, size=size, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_sign_cert(
        self, ca: str, *, request: PemCsrBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslPkiModelsSignCertResponse:
        """
        Parameters
        ----------
        ca : str
            the ca parameter

        request : PemCsrBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsSignCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_sign_cert(
            ca="ca",
            request="string",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_sign_cert(
            ca, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_cert(
        self,
        ca_: str,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        ca_ : str
            the ca parameter

        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_cert(
            ca_="ca",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_cert(
            ca_,
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
        self,
        ca_: str,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        ca_ : str
            the ca parameter

        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.pki.otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
            ca_="ca",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
            ca_,
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data


class AsyncPkiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPkiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPkiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPkiClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
        self, *, request: LetsEncryptCertBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        request : LetsEncryptCertBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
        self, *, request: ByteStreamBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : ByteStreamBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(
        self,
        *,
        cert_type: typing.Optional[OtoroshiSslCertCertType] = OMIT,
        name: typing.Optional[str] = OMIT,
        revoked: typing.Optional[bool] = OMIT,
        subject: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        keypair: typing.Optional[bool] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        auto_renew: typing.Optional[bool] = OMIT,
        ca_ref: typing.Optional[OtoroshiSslCertCaRef] = OMIT,
        to: typing.Optional[float] = OMIT,
        exposed: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        sans: typing.Optional[typing.Sequence[str]] = OMIT,
        client: typing.Optional[bool] = OMIT,
        from_: typing.Optional[float] = OMIT,
        valid: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        private_key: typing.Optional[str] = OMIT,
        self_signed: typing.Optional[bool] = OMIT,
        chain: typing.Optional[str] = OMIT,
        password: typing.Optional[OtoroshiSslCertPassword] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertValidResponse:
        """
        Parameters
        ----------
        cert_type : typing.Optional[OtoroshiSslCertCertType]
            the kind of certificate

        name : typing.Optional[str]
            Entity name

        revoked : typing.Optional[bool]
            Certificate is revoked

        subject : typing.Optional[str]
            Certificate subject

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        domain : typing.Optional[str]
            Certificate domain

        ca : typing.Optional[bool]
            Is cert a CA ?

        keypair : typing.Optional[bool]
            Is cert used for its keypair only ?

        lets_encrypt : typing.Optional[bool]
            Let's encrypt (ACME) generated

        auto_renew : typing.Optional[bool]
            Auto renew cert

        ca_ref : typing.Optional[OtoroshiSslCertCaRef]
            Reference to the CA (if any)

        to : typing.Optional[float]
            Stop date

        exposed : typing.Optional[bool]
            Is the cert exposed (public key exposed in jwks.json)

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        sans : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        client : typing.Optional[bool]
            Is cert a client cert ?

        from_ : typing.Optional[float]
            Start date

        valid : typing.Optional[bool]
            Is cert valid

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        private_key : typing.Optional[str]
            Certificate private key (PEM encoded)

        self_signed : typing.Optional[bool]
            Is cert self signed

        chain : typing.Optional[str]
            Certicates chain (PEM encoded)

        password : typing.Optional[OtoroshiSslCertPassword]
            Certificate password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertValidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_certificate_is_valid()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(
            cert_type=cert_type,
            name=name,
            revoked=revoked,
            subject=subject,
            description=description,
            tags=tags,
            domain=domain,
            ca=ca,
            keypair=keypair,
            lets_encrypt=lets_encrypt,
            auto_renew=auto_renew,
            ca_ref=ca_ref,
            to=to,
            exposed=exposed,
            id=id,
            loc=loc,
            sans=sans,
            client=client,
            from_=from_,
            valid=valid,
            metadata=metadata,
            private_key=private_key,
            self_signed=self_signed,
            chain=chain,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_certificate_data(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_certificate_data(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_certificate_data(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_csr(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCsrResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCsrResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_csr()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_csr(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
        self,
        *,
        algo: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenKeyPairResponse:
        """
        Parameters
        ----------
        algo : typing.Optional[str]
            Keypair algorithm

        size : typing.Optional[int]
            Keypair size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenKeyPairResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_key_pair()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
            algo=algo, size=size, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(
        self,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_sign_cert(
        self, ca: str, *, request: PemCsrBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslPkiModelsSignCertResponse:
        """
        Parameters
        ----------
        ca : str
            the ca parameter

        request : PemCsrBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsSignCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_sign_cert(
                ca="ca",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_sign_cert(
            ca, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_cert(
        self,
        ca_: str,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        ca_ : str
            the ca parameter

        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_cert(
                ca_="ca",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_cert(
            ca_,
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
        self,
        ca_: str,
        *,
        client: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        key: typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery] = OMIT,
        include_aia: typing.Optional[bool] = OMIT,
        signature_alg: typing.Optional[str] = OMIT,
        existing_serial_number: typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber] = OMIT,
        duration: typing.Optional[float] = OMIT,
        digest_alg: typing.Optional[str] = OMIT,
        ca: typing.Optional[bool] = OMIT,
        name: typing.Optional[typing.Dict[str, str]] = OMIT,
        subject: typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiSslPkiModelsGenCertResponse:
        """
        Parameters
        ----------
        ca_ : str
            the ca parameter

        client : typing.Optional[bool]
            Is cert client ?

        hosts : typing.Optional[typing.Sequence[str]]
            Certificate SANs

        key : typing.Optional[OtoroshiSslPkiModelsGenKeyPairQuery]
            Keypair specs

        include_aia : typing.Optional[bool]
            Include AIA extension (if generated from otoroshi CA)

        signature_alg : typing.Optional[str]
            Signature algorithm

        existing_serial_number : typing.Optional[OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber]


        duration : typing.Optional[float]
            Certificate lifespan

        digest_alg : typing.Optional[str]
            Digest algo

        ca : typing.Optional[bool]
            Is cert ca ?

        name : typing.Optional[typing.Dict[str, str]]
            Certificate name

        subject : typing.Optional[OtoroshiSslPkiModelsGenCsrQuerySubject]
            Certificate subject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslPkiModelsGenCertResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.pki.otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
                ca_="ca",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(
            ca_,
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
            request_options=request_options,
        )
        return _response.data
