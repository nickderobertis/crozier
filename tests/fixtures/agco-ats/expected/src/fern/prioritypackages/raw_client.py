

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
from ..types.api_paged_response_update_system_models_priority_package import (
    ApiPagedResponseUpdateSystemModelsPriorityPackage,
)
from ..types.update_system_models_priority_package import UpdateSystemModelsPriorityPackage
from .types.priority_packages_get_priority_packages_request_status import (
    PriorityPackagesGetPriorityPackagesRequestStatus,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPrioritypackagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getprioritypackages(
        self,
        *,
        client_id: typing.Optional[str] = None,
        status: typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsPriorityPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter priority packages by ClientID.

        status : typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus]
            Optional. Filter returned packages by status. By default only active packages will be returned.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsPriorityPackage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PriorityPackages",
            method="GET",
            params={
                "ClientID": client_id,
                "Status": status,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPriorityPackage,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPriorityPackage,
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

    def postprioritypackages(
        self,
        *,
        client_id: str,
        package_id: str,
        autorun: typing.Optional[bool] = OMIT,
        crc: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        priority_package_id: typing.Optional[str] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ID of the client to receive the priority package

        package_id : str
            The ID of the package to push as a priority package.

        autorun : typing.Optional[bool]
            Read Only. From the package specified by package ID.
                        Value is true if package should run automatically. Default value is false.

        crc : typing.Optional[str]
            Read Only. From the package specified by package ID.

        description : typing.Optional[str]
            Read Only. From the package specified by package ID.

        notes : typing.Optional[str]
            Read Only. From the package specified by package ID.

        package_type_id : typing.Optional[str]
            Read Only. From the package specified by package ID.

        previous_version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        priority_package_id : typing.Optional[str]
            Read Only. The ID of the priority package.

        release_date : typing.Optional[dt.datetime]
            Read Only. From the package specified by package ID.
                        The date the package was released

        released : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        remove_on_success : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        size : typing.Optional[int]
            Read Only. From the package specified by package ID.

        switches : typing.Optional[str]
            The command line arguments for the priority package.  Default value is an empty string.

        time_stamp : typing.Optional[dt.datetime]
            Read Only. The timestamp of the priority package.

        url : typing.Optional[str]
            Read Only. From the package specified by package ID.

        version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PriorityPackages",
            method="POST",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "ClientID": client_id,
                "Description": description,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "PriorityPackageID": priority_package_id,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "TimeStamp": time_stamp,
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

    def getprioritypackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsPriorityPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsPriorityPackage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PriorityPackages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPriorityPackage,
                    parse_obj_as(
                        type_=UpdateSystemModelsPriorityPackage,
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

    def deleteprioritypackages(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/PriorityPackages/{encode_path_param(id)}",
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


class AsyncRawPrioritypackagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getprioritypackages(
        self,
        *,
        client_id: typing.Optional[str] = None,
        status: typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPriorityPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter priority packages by ClientID.

        status : typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus]
            Optional. Filter returned packages by status. By default only active packages will be returned.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPriorityPackage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PriorityPackages",
            method="GET",
            params={
                "ClientID": client_id,
                "Status": status,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPriorityPackage,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPriorityPackage,
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

    async def postprioritypackages(
        self,
        *,
        client_id: str,
        package_id: str,
        autorun: typing.Optional[bool] = OMIT,
        crc: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        priority_package_id: typing.Optional[str] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ID of the client to receive the priority package

        package_id : str
            The ID of the package to push as a priority package.

        autorun : typing.Optional[bool]
            Read Only. From the package specified by package ID.
                        Value is true if package should run automatically. Default value is false.

        crc : typing.Optional[str]
            Read Only. From the package specified by package ID.

        description : typing.Optional[str]
            Read Only. From the package specified by package ID.

        notes : typing.Optional[str]
            Read Only. From the package specified by package ID.

        package_type_id : typing.Optional[str]
            Read Only. From the package specified by package ID.

        previous_version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        priority_package_id : typing.Optional[str]
            Read Only. The ID of the priority package.

        release_date : typing.Optional[dt.datetime]
            Read Only. From the package specified by package ID.
                        The date the package was released

        released : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        remove_on_success : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        size : typing.Optional[int]
            Read Only. From the package specified by package ID.

        switches : typing.Optional[str]
            The command line arguments for the priority package.  Default value is an empty string.

        time_stamp : typing.Optional[dt.datetime]
            Read Only. The timestamp of the priority package.

        url : typing.Optional[str]
            Read Only. From the package specified by package ID.

        version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PriorityPackages",
            method="POST",
            json={
                "Autorun": autorun,
                "CRC": crc,
                "ClientID": client_id,
                "Description": description,
                "Notes": notes,
                "PackageID": package_id,
                "PackageTypeID": package_type_id,
                "PreviousVersion": previous_version,
                "PriorityPackageID": priority_package_id,
                "ReleaseDate": release_date,
                "Released": released,
                "RemoveOnSuccess": remove_on_success,
                "Size": size,
                "Switches": switches,
                "TimeStamp": time_stamp,
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

    async def getprioritypackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsPriorityPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsPriorityPackage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PriorityPackages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPriorityPackage,
                    parse_obj_as(
                        type_=UpdateSystemModelsPriorityPackage,
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

    async def deleteprioritypackages(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/PriorityPackages/{encode_path_param(id)}",
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
