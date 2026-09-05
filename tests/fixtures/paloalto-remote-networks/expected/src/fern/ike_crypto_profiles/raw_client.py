

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.generic_error import GenericError
from ..types.ike_crypto_profiles_dh_group_item import IkeCryptoProfilesDhGroupItem
from ..types.ike_crypto_profiles_encryption_item import IkeCryptoProfilesEncryptionItem
from ..types.ike_crypto_profiles_hash_item import IkeCryptoProfilesHashItem
from ..types.ike_crypto_profiles_lifetime import IkeCryptoProfilesLifetime
from ..types.ike_crypto_profiles_response import IkeCryptoProfilesResponse
from ..types.uuid_response import UuidResponse
from .types.get_v1ike_crypto_profiles_read_response import GetV1IkeCryptoProfilesReadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIkeCryptoProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1ike_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IkeCryptoProfilesResponse]:
        """
        Provides a status of Internet Key Exchange(IKE) Crypto Profiles created along with the UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IkeCryptoProfilesResponse]
            Status of the created IKE Crypto Profiles.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IkeCryptoProfilesResponse,
                    parse_obj_as(
                        type_=IkeCryptoProfilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def post_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "authentication_multiple": authentication_multiple,
                "dh_group": dh_group,
                "encryption": encryption,
                "hash": hash,
                "id": id,
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=IkeCryptoProfilesLifetime, direction="write"
                ),
                "name": name,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def put_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Edit an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "authentication_multiple": authentication_multiple,
                "dh_group": dh_group,
                "encryption": encryption,
                "hash": hash,
                "id": id,
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=IkeCryptoProfilesLifetime, direction="write"
                ),
                "name": name,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def delete_v1ike_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Delete an IKE Crypto Profiles.

        Parameters
        ----------
        name : str
            IKE Crypto Profile name.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def get_v1ike_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetV1IkeCryptoProfilesReadResponse]:
        """
        Read the list of IKE Crypto Profiles.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1IkeCryptoProfilesReadResponse]
            List of IKE Crypto Profiles configurations.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1IkeCryptoProfilesReadResponse,
                    parse_obj_as(
                        type_=GetV1IkeCryptoProfilesReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def post_v1ike_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create a request to read the list of IKE Crypto Profiles.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ike_crypto_profiles_names": ike_crypto_profiles_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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


class AsyncRawIkeCryptoProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1ike_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IkeCryptoProfilesResponse]:
        """
        Provides a status of Internet Key Exchange(IKE) Crypto Profiles created along with the UUID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IkeCryptoProfilesResponse]
            Status of the created IKE Crypto Profiles.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IkeCryptoProfilesResponse,
                    parse_obj_as(
                        type_=IkeCryptoProfilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def post_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "authentication_multiple": authentication_multiple,
                "dh_group": dh_group,
                "encryption": encryption,
                "hash": hash,
                "id": id,
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=IkeCryptoProfilesLifetime, direction="write"
                ),
                "name": name,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def put_v1ike_crypto_profiles(
        self,
        *,
        dh_group: typing.Sequence[IkeCryptoProfilesDhGroupItem],
        encryption: typing.Sequence[IkeCryptoProfilesEncryptionItem],
        hash: typing.Sequence[IkeCryptoProfilesHashItem],
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        authentication_multiple: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        lifetime: typing.Optional[IkeCryptoProfilesLifetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Edit an IKE Crypto Profiles.

        Parameters
        ----------
        dh_group : typing.Sequence[IkeCryptoProfilesDhGroupItem]

        encryption : typing.Sequence[IkeCryptoProfilesEncryptionItem]
            Encryption algorithm

        hash : typing.Sequence[IkeCryptoProfilesHashItem]

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        authentication_multiple : typing.Optional[int]
            IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled

        id : typing.Optional[str]
            uuid of the resource

        lifetime : typing.Optional[IkeCryptoProfilesLifetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "authentication_multiple": authentication_multiple,
                "dh_group": dh_group,
                "encryption": encryption,
                "hash": hash,
                "id": id,
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=IkeCryptoProfilesLifetime, direction="write"
                ),
                "name": name,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def delete_v1ike_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Delete an IKE Crypto Profiles.

        Parameters
        ----------
        name : str
            IKE Crypto Profile name.

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles",
            method="DELETE",
            params={
                "SubTenantName": sub_tenant_name,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def get_v1ike_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetV1IkeCryptoProfilesReadResponse]:
        """
        Read the list of IKE Crypto Profiles.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1IkeCryptoProfilesReadResponse]
            List of IKE Crypto Profiles configurations.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1IkeCryptoProfilesReadResponse,
                    parse_obj_as(
                        type_=GetV1IkeCryptoProfilesReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def post_v1ike_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ike_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create a request to read the list of IKE Crypto Profiles.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ike_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ike-crypto-profiles-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ike_crypto_profiles_names": ike_crypto_profiles_names,
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
                    UuidResponse,
                    parse_obj_as(
                        type_=UuidResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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
