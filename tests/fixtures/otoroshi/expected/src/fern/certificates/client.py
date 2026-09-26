

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.empty import Empty
from ..types.otoroshi_ssl_cert import OtoroshiSslCert
from ..types.otoroshi_ssl_cert_ca_ref import OtoroshiSslCertCaRef
from ..types.otoroshi_ssl_cert_cert_type import OtoroshiSslCertCertType
from ..types.otoroshi_ssl_cert_password import OtoroshiSslCertPassword
from ..types.pem_certificate_body import PemCertificateBody
from .raw_client import AsyncRawCertificatesClient, RawCertificatesClient


OMIT = typing.cast(typing.Any, ...)


class CertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCertificatesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_templates_controller_initiate_certificate()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_renew_cert(
        self, cert_id: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        cert_id : str
            The certId param of the target entity

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_renew_cert(
            cert_id="certId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_renew_cert(
            cert_id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiSslCert

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
            request=[OtoroshiSslCert()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiSslCert

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
            request=[OtoroshiSslCert()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
        self,
        id_: str,
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
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

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
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
            id_,
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

    def otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
        self,
        id_: str,
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
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

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
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
            id_,
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

    def otoroshi_controllers_adminapi_pki_controller_import_bundle(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_pki_controller_import_bundle(
            request="string",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_pki_controller_import_bundle(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiSslCert]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_certificates_controller_create_action(
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
    ) -> OtoroshiSslCert:
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
        OtoroshiSslCert
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.otoroshi_controllers_adminapi_certificates_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_certificates_controller_create_action(
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


class AsyncCertificatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCertificatesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_templates_controller_initiate_certificate()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_renew_cert(
        self, cert_id: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        cert_id : str
            The certId param of the target entity

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_renew_cert(
                cert_id="certId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_renew_cert(
            cert_id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiSslCert

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
                request=[OtoroshiSslCert()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiSslCert

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
                request=[OtoroshiSslCert()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
        self,
        id_: str,
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
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

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
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_update_entity_action(
            id_,
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

    async def otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
        self,
        id_: str,
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
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

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
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(
            id_,
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

    async def otoroshi_controllers_adminapi_pki_controller_import_bundle(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiSslCert:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_pki_controller_import_bundle(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_pki_controller_import_bundle(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiSslCert]
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_certificates_controller_create_action(
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
    ) -> OtoroshiSslCert:
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
        OtoroshiSslCert
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
            await client.certificates.otoroshi_controllers_adminapi_certificates_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_certificates_controller_create_action(
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
