

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.update_system_models_package_type import UpdateSystemModelsPackageType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPackagetypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsPackageType]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsPackageType]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackageType,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackageType,
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

    def post(
        self,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypes",
            method="POST",
            json={
                "Attribute": attribute,
                "Category": category,
                "Description": description,
                "Icon": icon,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "MaxDeltaPackages": max_delta_packages,
                "PackageTypeID": package_type_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def put(
        self,
        id: str,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="PUT",
            json={
                "Attribute": attribute,
                "Category": category,
                "Description": description,
                "Icon": icon,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "MaxDeltaPackages": max_delta_packages,
                "PackageTypeID": package_type_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def addpackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def removepackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPackagetypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsPackageType]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsPackageType]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackageType,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackageType,
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

    async def post(
        self,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypes",
            method="POST",
            json={
                "Attribute": attribute,
                "Category": category,
                "Description": description,
                "Icon": icon,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "MaxDeltaPackages": max_delta_packages,
                "PackageTypeID": package_type_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def put(
        self,
        id: str,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="PUT",
            json={
                "Attribute": attribute,
                "Category": category,
                "Description": description,
                "Icon": icon,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "MaxDeltaPackages": max_delta_packages,
                "PackageTypeID": package_type_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def addpackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def removepackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PackageTypes/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
