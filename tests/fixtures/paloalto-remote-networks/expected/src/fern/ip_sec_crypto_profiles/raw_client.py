

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
from ..types.ipsec_crypto_profiles_ah import IpsecCryptoProfilesAh
from ..types.ipsec_crypto_profiles_dh_group import IpsecCryptoProfilesDhGroup
from ..types.ipsec_crypto_profiles_esp import IpsecCryptoProfilesEsp
from ..types.ipsec_crypto_profiles_response import IpsecCryptoProfilesResponse
from ..types.lifesize import Lifesize
from ..types.lifetime import Lifetime
from ..types.uuid_response import UuidResponse
from .types.get_v1ipsec_crypto_profiles_read_response import GetV1IpsecCryptoProfilesReadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIpSecCryptoProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1ipsec_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IpsecCryptoProfilesResponse]:
        """
        Lists the status of IPSec Crypto Profiles. Shows results of create, modify, and delete actions with their associated UUIDs.
        Users can perform these actions and then use this GET request to verify the status by referencing the UUID received during the initial action.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IpsecCryptoProfilesResponse]
            Status of the created IPSEC Crypto Profiles.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IpsecCryptoProfilesResponse,
                    parse_obj_as(
                        type_=IpsecCryptoProfilesResponse,
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

    def post_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ah": convert_and_respect_annotation_metadata(
                    object_=ah, annotation=IpsecCryptoProfilesAh, direction="write"
                ),
                "dh_group": dh_group,
                "esp": convert_and_respect_annotation_metadata(
                    object_=esp, annotation=IpsecCryptoProfilesEsp, direction="write"
                ),
                "lifesize": convert_and_respect_annotation_metadata(
                    object_=lifesize, annotation=Lifesize, direction="write"
                ),
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=Lifetime, direction="write"
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

    def put_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Edit an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ah": convert_and_respect_annotation_metadata(
                    object_=ah, annotation=IpsecCryptoProfilesAh, direction="write"
                ),
                "dh_group": dh_group,
                "esp": convert_and_respect_annotation_metadata(
                    object_=esp, annotation=IpsecCryptoProfilesEsp, direction="write"
                ),
                "lifesize": convert_and_respect_annotation_metadata(
                    object_=lifesize, annotation=Lifesize, direction="write"
                ),
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=Lifetime, direction="write"
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

    def delete_v1ipsec_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Delete an IPSec crypto profile.

        Parameters
        ----------
        name : str
            IPSEC Crypto Profile name.

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
            "v1/ipsec-crypto-profiles",
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

    def get_v1ipsec_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetV1IpsecCryptoProfilesReadResponse]:
        """
        You can read a list of Internet Protocol Security (IPSec) crypto profiles configurations that are created.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1IpsecCryptoProfilesReadResponse]
            List of IPSEC Crypto Profiles configurations.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1IpsecCryptoProfilesReadResponse,
                    parse_obj_as(
                        type_=GetV1IpsecCryptoProfilesReadResponse,
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

    def post_v1ipsec_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ipsec_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UuidResponse]:
        """
        Create a request to read a list IPSec Crypto Profile.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ipsec_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UuidResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ipsec_crypto_profiles_names": ipsec_crypto_profiles_names,
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


class AsyncRawIpSecCryptoProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1ipsec_crypto_profiles(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IpsecCryptoProfilesResponse]:
        """
        Lists the status of IPSec Crypto Profiles. Shows results of create, modify, and delete actions with their associated UUIDs.
        Users can perform these actions and then use this GET request to verify the status by referencing the UUID received during the initial action.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IpsecCryptoProfilesResponse]
            Status of the created IPSEC Crypto Profiles.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IpsecCryptoProfilesResponse,
                    parse_obj_as(
                        type_=IpsecCryptoProfilesResponse,
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

    async def post_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ah": convert_and_respect_annotation_metadata(
                    object_=ah, annotation=IpsecCryptoProfilesAh, direction="write"
                ),
                "dh_group": dh_group,
                "esp": convert_and_respect_annotation_metadata(
                    object_=esp, annotation=IpsecCryptoProfilesEsp, direction="write"
                ),
                "lifesize": convert_and_respect_annotation_metadata(
                    object_=lifesize, annotation=Lifesize, direction="write"
                ),
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=Lifetime, direction="write"
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

    async def put_v1ipsec_crypto_profiles(
        self,
        *,
        lifetime: Lifetime,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        ah: typing.Optional[IpsecCryptoProfilesAh] = OMIT,
        dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = OMIT,
        esp: typing.Optional[IpsecCryptoProfilesEsp] = OMIT,
        lifesize: typing.Optional[Lifesize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Edit an IPSec crypto profile.

        Parameters
        ----------
        lifetime : Lifetime

        name : str
            Alphanumeric string begin with letter: [0-9a-zA-Z._-]

        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ah : typing.Optional[IpsecCryptoProfilesAh]

        dh_group : typing.Optional[IpsecCryptoProfilesDhGroup]
            phase-2 DH group (PFS DH group)

        esp : typing.Optional[IpsecCryptoProfilesEsp]

        lifesize : typing.Optional[Lifesize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles",
            method="PUT",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ah": convert_and_respect_annotation_metadata(
                    object_=ah, annotation=IpsecCryptoProfilesAh, direction="write"
                ),
                "dh_group": dh_group,
                "esp": convert_and_respect_annotation_metadata(
                    object_=esp, annotation=IpsecCryptoProfilesEsp, direction="write"
                ),
                "lifesize": convert_and_respect_annotation_metadata(
                    object_=lifesize, annotation=Lifesize, direction="write"
                ),
                "lifetime": convert_and_respect_annotation_metadata(
                    object_=lifetime, annotation=Lifetime, direction="write"
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

    async def delete_v1ipsec_crypto_profiles(
        self,
        *,
        name: str,
        sub_tenant_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Delete an IPSec crypto profile.

        Parameters
        ----------
        name : str
            IPSEC Crypto Profile name.

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
            "v1/ipsec-crypto-profiles",
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

    async def get_v1ipsec_crypto_profiles_read(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetV1IpsecCryptoProfilesReadResponse]:
        """
        You can read a list of Internet Protocol Security (IPSec) crypto profiles configurations that are created.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1IpsecCryptoProfilesReadResponse]
            List of IPSEC Crypto Profiles configurations.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles-read",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1IpsecCryptoProfilesReadResponse,
                    parse_obj_as(
                        type_=GetV1IpsecCryptoProfilesReadResponse,
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

    async def post_v1ipsec_crypto_profiles_read(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        ipsec_crypto_profiles_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UuidResponse]:
        """
        Create a request to read a list IPSec Crypto Profile.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        ipsec_crypto_profiles_names : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UuidResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ipsec-crypto-profiles-read",
            method="POST",
            params={
                "SubTenantName": sub_tenant_name,
            },
            json={
                "ipsec_crypto_profiles_names": ipsec_crypto_profiles_names,
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
