

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
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.empty import Empty
from ..types.error_response import ErrorResponse
from ..types.otoroshi_ssl_cert import OtoroshiSslCert
from ..types.otoroshi_ssl_cert_ca_ref import OtoroshiSslCertCaRef
from ..types.otoroshi_ssl_cert_cert_type import OtoroshiSslCertCertType
from ..types.otoroshi_ssl_cert_password import OtoroshiSslCertPassword
from ..types.pem_certificate_body import PemCertificateBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    def otoroshi_controllers_adminapi_certificates_controller_renew_cert(
        self, cert_id: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslCert]:
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
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(cert_id)}/_renew",
            method="POST",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    def otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiSslCert], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    def otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiSslCert], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    def otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    def otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    def otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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
    ) -> HttpResponse[OtoroshiSslCert]:
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
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PUT",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    def otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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
    ) -> HttpResponse[OtoroshiSslCert]:
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
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PATCH",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    def otoroshi_controllers_adminapi_pki_controller_import_bundle(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates/_bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    def otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OtoroshiSslCert]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OtoroshiSslCert]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiSslCert],
                    parse_obj_as(
                        type_=typing.List[OtoroshiSslCert],
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
    ) -> HttpResponse[OtoroshiSslCert]:
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
        HttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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


class AsyncRawCertificatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_templates_controller_initiate_certificate(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    async def otoroshi_controllers_adminapi_certificates_controller_renew_cert(
        self, cert_id: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
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
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(cert_id)}/_renew",
            method="POST",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiSslCert], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiSslCert], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiSslCert]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[OtoroshiSslCert], direction="write"
            ),
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    async def otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BulkResponseBody]:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkResponseBody]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_bulk",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkResponseBody,
                    parse_obj_as(
                        type_=BulkResponseBody,
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

    async def otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
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
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PUT",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    async def otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
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
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PATCH",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    async def otoroshi_controllers_adminapi_pki_controller_import_bundle(
        self, *, request: PemCertificateBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
        """
        Parameters
        ----------
        request : PemCertificateBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates/_bundle",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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

    async def otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OtoroshiSslCert]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OtoroshiSslCert]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OtoroshiSslCert],
                    parse_obj_as(
                        type_=typing.List[OtoroshiSslCert],
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
    ) -> AsyncHttpResponse[OtoroshiSslCert]:
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
        AsyncHttpResponse[OtoroshiSslCert]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates",
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
            headers={
                "content-type": "application/x-ndjson",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiSslCert,
                    parse_obj_as(
                        type_=OtoroshiSslCert,
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
