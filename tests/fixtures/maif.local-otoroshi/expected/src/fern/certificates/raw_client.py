

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
from ..types.certificate import Certificate
from ..types.deleted import Deleted
from ..types.patch import Patch
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_certs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Certificate]]:
        """
        Get all certificates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Certificate]]
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
                    typing.List[Certificate],
                    parse_obj_as(
                        type_=typing.List[Certificate],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def create_cert(
        self,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Certificate]:
        """
        Create one certificate

        Parameters
        ----------
        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Certificate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/certificates",
            method="POST",
            json={
                "autoRenew": auto_renew,
                "ca": ca,
                "caRef": ca_ref,
                "chain": chain,
                "domain": domain,
                "from": from_,
                "id": id,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "subject": subject,
                "to": to,
                "valid": valid,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def one_cert(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Certificate]:
        """
        Get one certificate by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Certificate]
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
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def put_cert(
        self,
        id_: str,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Certificate]:
        """
        Update one certificate by id

        Parameters
        ----------
        id_ : str
            The certificate id

        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Certificate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PUT",
            json={
                "autoRenew": auto_renew,
                "ca": ca,
                "caRef": ca_ref,
                "chain": chain,
                "domain": domain,
                "from": from_,
                "id": id,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "subject": subject,
                "to": to,
                "valid": valid,
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
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def delete_cert(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Deleted]:
        """
        Delete one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
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
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def patch_cert(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Certificate]:
        """
        Update one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Certificate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def all_certs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Certificate]]:
        """
        Get all certificates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Certificate]]
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
                    typing.List[Certificate],
                    parse_obj_as(
                        type_=typing.List[Certificate],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def create_cert(
        self,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Certificate]:
        """
        Create one certificate

        Parameters
        ----------
        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Certificate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/certificates",
            method="POST",
            json={
                "autoRenew": auto_renew,
                "ca": ca,
                "caRef": ca_ref,
                "chain": chain,
                "domain": domain,
                "from": from_,
                "id": id,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "subject": subject,
                "to": to,
                "valid": valid,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def one_cert(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Certificate]:
        """
        Get one certificate by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Certificate]
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
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def put_cert(
        self,
        id_: str,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Certificate]:
        """
        Update one certificate by id

        Parameters
        ----------
        id_ : str
            The certificate id

        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Certificate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id_)}",
            method="PUT",
            json={
                "autoRenew": auto_renew,
                "ca": ca,
                "caRef": ca_ref,
                "chain": chain,
                "domain": domain,
                "from": from_,
                "id": id,
                "privateKey": private_key,
                "selfSigned": self_signed,
                "subject": subject,
                "to": to,
                "valid": valid,
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
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def delete_cert(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
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
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def patch_cert(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Certificate]:
        """
        Update one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Certificate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/certificates/{encode_path_param(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Certificate,
                    parse_obj_as(
                        type_=Certificate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
