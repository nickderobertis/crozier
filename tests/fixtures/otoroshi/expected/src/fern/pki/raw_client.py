

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.any import Any
from ..types.byte_stream_body import ByteStreamBody
from ..types.cert_valid_response import CertValidResponse
from ..types.done import Done
from ..types.error_response import ErrorResponse
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPkiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
        self, *, request: LetsEncryptCertBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
        """
        Parameters
        ----------
        request : LetsEncryptCertBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/certs/_letencrypt",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
        self, *, request: ByteStreamBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        request : ByteStreamBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/certs/_p12",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CertValidResponse]:
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
        HttpResponse[CertValidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/certs/_valid",
            method="POST",
            json={
                "certType": cert_type,
                "name": name,
                "revoked": revoked,
                "subject": subject,
                "description": description,
                "tags": tags,
                "domain": domain,
                "ca": ca,
                "keypair": keypair,
                "letsEncrypt": lets_encrypt,
                "autoRenew": auto_renew,
                "caRef": convert_and_respect_annotation_metadata(
                    object_=ca_ref, annotation=OtoroshiSslCertCaRef, direction="write"
                ),
                "to": to,
                "exposed": exposed,
                "id": id,
                "_loc": loc,
                "sans": sans,
                "client": client,
                "from": from_,
                "valid": valid,
                "metadata": metadata,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "chain": chain,
                "password": convert_and_respect_annotation_metadata(
                    object_=password, annotation=OtoroshiSslCertPassword, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CertValidResponse,
                    parse_obj_as(
                        type_=CertValidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def otoroshi_controllers_adminapi_pki_controller_certificate_data(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Any]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/certs/_data",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Any,
                    parse_obj_as(
                        type_=Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/certs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCsrResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenCsrResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/csrs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCsrResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCsrResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
        self,
        *,
        algo: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiSslPkiModelsGenKeyPairResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenKeyPairResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/keys",
            method="POST",
            json={
                "algo": algo,
                "size": size,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenKeyPairResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenKeyPairResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pki/cas",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def otoroshi_controllers_adminapi_pki_controller_sign_cert(
        self, ca: str, *, request: PemCsrBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslPkiModelsSignCertResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsSignCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca)}/certs/_sign",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsSignCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsSignCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca_)}/certs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        HttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca_)}/cas",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPkiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(
        self, *, request: LetsEncryptCertBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
        """
        Parameters
        ----------
        request : LetsEncryptCertBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/certs/_letencrypt",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(
        self, *, request: ByteStreamBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        request : ByteStreamBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/certs/_p12",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CertValidResponse]:
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
        AsyncHttpResponse[CertValidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/certs/_valid",
            method="POST",
            json={
                "certType": cert_type,
                "name": name,
                "revoked": revoked,
                "subject": subject,
                "description": description,
                "tags": tags,
                "domain": domain,
                "ca": ca,
                "keypair": keypair,
                "letsEncrypt": lets_encrypt,
                "autoRenew": auto_renew,
                "caRef": convert_and_respect_annotation_metadata(
                    object_=ca_ref, annotation=OtoroshiSslCertCaRef, direction="write"
                ),
                "to": to,
                "exposed": exposed,
                "id": id,
                "_loc": loc,
                "sans": sans,
                "client": client,
                "from": from_,
                "valid": valid,
                "metadata": metadata,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "chain": chain,
                "password": convert_and_respect_annotation_metadata(
                    object_=password, annotation=OtoroshiSslCertPassword, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CertValidResponse,
                    parse_obj_as(
                        type_=CertValidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def otoroshi_controllers_adminapi_pki_controller_certificate_data(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Any]:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Any]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/certs/_data",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Any,
                    parse_obj_as(
                        type_=Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/certs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCsrResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCsrResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/csrs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCsrResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCsrResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def otoroshi_controllers_adminapi_pki_controller_gen_key_pair(
        self,
        *,
        algo: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenKeyPairResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenKeyPairResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/keys",
            method="POST",
            json={
                "algo": algo,
                "size": size,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenKeyPairResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenKeyPairResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pki/cas",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def otoroshi_controllers_adminapi_pki_controller_sign_cert(
        self, ca: str, *, request: PemCsrBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsSignCertResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsSignCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca)}/certs/_sign",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsSignCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsSignCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca_)}/certs",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]:
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
        AsyncHttpResponse[OtoroshiSslPkiModelsGenCertResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/pki/cas/{encode_path_param(ca_)}/cas",
            method="POST",
            json={
                "client": client,
                "hosts": hosts,
                "key": convert_and_respect_annotation_metadata(
                    object_=key, annotation=OtoroshiSslPkiModelsGenKeyPairQuery, direction="write"
                ),
                "includeAIA": include_aia,
                "signatureAlg": signature_alg,
                "existingSerialNumber": convert_and_respect_annotation_metadata(
                    object_=existing_serial_number,
                    annotation=OtoroshiSslPkiModelsGenCsrQueryExistingSerialNumber,
                    direction="write",
                ),
                "duration": duration,
                "digestAlg": digest_alg,
                "ca": ca,
                "name": name,
                "subject": convert_and_respect_annotation_metadata(
                    object_=subject, annotation=OtoroshiSslPkiModelsGenCsrQuerySubject, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslPkiModelsGenCertResponse,
                    parse_obj_as(
                        type_=OtoroshiSslPkiModelsGenCertResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
