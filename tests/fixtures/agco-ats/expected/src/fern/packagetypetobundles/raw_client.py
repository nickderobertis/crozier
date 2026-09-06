

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_package_type_i_dto_bundle import (
    ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
)
from ..types.update_system_models_package_type_i_dto_bundle_subscription_type import (
    UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPackagetypetobundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        bundle_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        package_version: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        package_version : typing.Optional[int]
            Optional. Filter by PackageVersion.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="GET",
            params={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
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
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="POST",
            json={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "Priority": priority,
                "SubscriptionType": subscription_type,
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

    def put(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="PUT",
            json={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "Priority": priority,
                "SubscriptionType": subscription_type,
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

    def delete(
        self, *, bundle_id: str, package_type_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        package_type_id : str
            The PackageTypeID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="DELETE",
            params={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
            },
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


class AsyncRawPackagetypetobundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        bundle_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        package_version: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        package_version : typing.Optional[int]
            Optional. Filter by PackageVersion.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="GET",
            params={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
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
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="POST",
            json={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "Priority": priority,
                "SubscriptionType": subscription_type,
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

    async def put(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="PUT",
            json={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
                "PackageVersion": package_version,
                "Priority": priority,
                "SubscriptionType": subscription_type,
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
        self, *, bundle_id: str, package_type_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        package_type_id : str
            The PackageTypeID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/PackageTypetoBundles",
            method="DELETE",
            params={
                "BundleID": bundle_id,
                "PackageTypeID": package_type_id,
            },
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
