

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.registry_configuration_list import RegistryConfigurationList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRegistriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_registries(
        self, *, anchore_account: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistryConfigurationList]:
        """
        List all configured registries the system can/will watch

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistryConfigurationList]
            Registry listing
        """
        _response = self._client_wrapper.httpx_client.request(
            "registries",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_registry(
        self,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegistryConfigurationList]:
        """
        Adds a new registry to the system

        Parameters
        ----------
        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry add time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistryConfigurationList]
            Saved registry configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "registries",
            method="POST",
            params={
                "validate": validate,
            },
            json={
                "registry": registry,
                "registry_name": registry_name,
                "registry_pass": registry_pass,
                "registry_type": registry_type,
                "registry_user": registry_user,
                "registry_verify": registry_verify,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegistryConfigurationList]:
        """
        Get information on a specific registry

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistryConfigurationList]
            Registry configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_registry(
        self,
        registry_: str,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegistryConfigurationList]:
        """
        Replaces an existing registry record with the given record

        Parameters
        ----------
        registry_ : str

        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry update time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistryConfigurationList]
            Updated registry configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry_)}",
            method="PUT",
            params={
                "validate": validate,
            },
            json={
                "registry": registry,
                "registry_name": registry_name,
                "registry_pass": registry_pass,
                "registry_type": registry_type,
                "registry_user": registry_user,
                "registry_verify": registry_verify,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a registry configuration record from the system. Does not remove any images.

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawRegistriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_registries(
        self, *, anchore_account: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistryConfigurationList]:
        """
        List all configured registries the system can/will watch

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistryConfigurationList]
            Registry listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "registries",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_registry(
        self,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegistryConfigurationList]:
        """
        Adds a new registry to the system

        Parameters
        ----------
        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry add time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistryConfigurationList]
            Saved registry configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "registries",
            method="POST",
            params={
                "validate": validate,
            },
            json={
                "registry": registry,
                "registry_name": registry_name,
                "registry_pass": registry_pass,
                "registry_type": registry_type,
                "registry_user": registry_user,
                "registry_verify": registry_verify,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegistryConfigurationList]:
        """
        Get information on a specific registry

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistryConfigurationList]
            Registry configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_registry(
        self,
        registry_: str,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegistryConfigurationList]:
        """
        Replaces an existing registry record with the given record

        Parameters
        ----------
        registry_ : str

        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry update time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistryConfigurationList]
            Updated registry configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry_)}",
            method="PUT",
            params={
                "validate": validate,
            },
            json={
                "registry": registry,
                "registry_name": registry_name,
                "registry_pass": registry_pass,
                "registry_type": registry_type,
                "registry_user": registry_user,
                "registry_verify": registry_verify,
            },
            headers={
                "content-type": "application/json",
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistryConfigurationList,
                    parse_obj_as(
                        type_=RegistryConfigurationList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a registry configuration record from the system. Does not remove any images.

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"registries/{encode_path_param(registry)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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
