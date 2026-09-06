

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_package import ApiPagedResponseUpdateSystemModelsPackage
from ..types.update_system_models_package import UpdateSystemModelsPackage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPackagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getpackages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        released: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        package_type_id : typing.Optional[str]
            Optional. If provided, filters by PackageTypeID.

        version : typing.Optional[int]
            Optional. If provided, filters by Version.

        released : typing.Optional[bool]
            Optional. If provided, filters by Released.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsPackage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Packages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "PackageTypeID": package_type_id,
                "Version": version,
                "Released": released,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackage,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackage,
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

    def postpackage(
        self,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Packages",
            method="POST",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "Description": description,
                "LocalizedName": localized_name,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "Url": url,
                "Version": version,
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

    def getpackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsPackage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackage,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackage,
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

    def putpackage(
        self,
        id: str,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Package

        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
            method="PUT",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "Description": description,
                "LocalizedName": localized_name,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "Url": url,
                "Version": version,
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

    def deletepackage(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
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


class AsyncRawPackagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getpackages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        released: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        package_type_id : typing.Optional[str]
            Optional. If provided, filters by PackageTypeID.

        version : typing.Optional[int]
            Optional. If provided, filters by Version.

        released : typing.Optional[bool]
            Optional. If provided, filters by Released.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Packages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "PackageTypeID": package_type_id,
                "Version": version,
                "Released": released,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackage,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackage,
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

    async def postpackage(
        self,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Packages",
            method="POST",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "Description": description,
                "LocalizedName": localized_name,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "Url": url,
                "Version": version,
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

    async def getpackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsPackage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackage,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackage,
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

    async def putpackage(
        self,
        id: str,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Package

        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
            method="PUT",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "Description": description,
                "LocalizedName": localized_name,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "Url": url,
                "Version": version,
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

    async def deletepackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Packages/{encode_path_param(id)}",
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
