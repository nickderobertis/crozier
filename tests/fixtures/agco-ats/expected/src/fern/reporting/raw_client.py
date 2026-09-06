

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_bundle import ApiPagedResponseUpdateSystemModelsBundle
from ..types.api_paged_response_update_system_models_client_status_update_system_models_paged_client_status_metadata import (
    ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
)
from ..types.api_paged_response_update_system_models_package_status_summary import (
    ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
)
from ..types.api_paged_response_update_system_models_update_group import ApiPagedResponseUpdateSystemModelsUpdateGroup
from ..types.api_paged_response_update_system_models_update_group_client_relationship import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
)
from ..types.update_system_models_client import UpdateSystemModelsClient
from ..types.update_system_models_client_info import UpdateSystemModelsClientInfo
from ..types.update_system_models_package import UpdateSystemModelsPackage
from ..types.update_system_models_package_status_summary import UpdateSystemModelsPackageStatusSummary
from ..types.update_system_models_update_metrics_data import UpdateSystemModelsUpdateMetricsData
from .types.reporting_current_packages_in_update_group_request_subscription_type_filter import (
    ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter,
)
from pydantic import ValidationError


class RawReportingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def bundlestatussummary(
        self,
        *,
        bundle_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsPackageStatusSummary]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsPackageStatusSummary]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/BundleStatusSummary",
            method="GET",
            params={
                "BundleID": bundle_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
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

    def bundlesinupdategroup(
        self,
        *,
        id: str,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/BundlesInUpdateGroup",
            method="GET",
            params={
                "ID": id,
                "IncludeInactive": include_inactive,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsBundle,
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

    def clientinfo(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsClientInfo]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsClientInfo]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/ClientInfo",
            method="GET",
            params={
                "ClientID": client_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClientInfo,
                    parse_obj_as(
                        type_=UpdateSystemModelsClientInfo,
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

    def currentpackagesinupdategroup(
        self,
        *,
        id: str,
        subscription_type_filter: typing.Optional[
            ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[UpdateSystemModelsPackage]]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        subscription_type_filter : typing.Optional[ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter]
            Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[UpdateSystemModelsPackage]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/CurrentPackagesInUpdateGroup",
            method="GET",
            params={
                "ID": id,
                "SubscriptionTypeFilter": subscription_type_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UpdateSystemModelsPackage],
                    parse_obj_as(
                        type_=typing.List[UpdateSystemModelsPackage],
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

    def getclient(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsClient]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsClient]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/GetClient",
            method="GET",
            params={
                "ID": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClient,
                    parse_obj_as(
                        type_=UpdateSystemModelsClient,
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

    def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/GetSubscriptions",
            method="GET",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
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

    def packagestatussummary(
        self, *, package_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsPackageStatusSummary]:
        """
        No Documentation Found.

        Parameters
        ----------
        package_id : str
            The Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsPackageStatusSummary]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/PackageStatusSummary",
            method="GET",
            params={
                "PackageID": package_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackageStatusSummary,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackageStatusSummary,
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

    def registeredclients(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        report_result: typing.Optional[str] = None,
        report_result_is_valid: typing.Optional[bool] = None,
        report_value: typing.Optional[str] = None,
        last_check_in_before: typing.Optional[dt.datetime] = None,
        last_check_in_after: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.

        client_id : typing.Optional[str]
            Optional. Filter where ClientID matches a value. Wildcards are supported (*).

        tag : typing.Optional[str]
            Optional. Filter where Tag matches a value. Wildcards are supported (*).

        report_result : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).

        report_result_is_valid : typing.Optional[bool]
            Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.

        report_value : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).

        last_check_in_before : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured before the provided date.

        last_check_in_after : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured after the provided date.

        order_by : typing.Optional[str]
            Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...
                        If sort direction is not provided for a field, it will be sorted ascending.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/RegisteredClients",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "ClientID": client_id,
                "Tag": tag,
                "ReportResult": report_result,
                "ReportResultIsValid": report_result_is_valid,
                "ReportValue": report_value,
                "LastCheckInBefore": serialize_datetime(last_check_in_before)
                if last_check_in_before is not None
                else None,
                "LastCheckInAfter": serialize_datetime(last_check_in_after)
                if last_check_in_after is not None
                else None,
                "OrderBy": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
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

    def updategroups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroup]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroup]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/UpdateGroups",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroup,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroup,
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

    def updatemetrics(
        self,
        *,
        update_group_id: str,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSystemModelsUpdateMetricsData]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : str
            The UpdateType in which clients must be for the report to include them.

        bundle_number : typing.Optional[int]
            Optional. Tells us which chart to show based upon filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsUpdateMetricsData]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/UpdateMetrics",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "bundleNumber": bundle_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateMetricsData,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateMetricsData,
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


class AsyncRawReportingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def bundlestatussummary(
        self,
        *,
        bundle_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackageStatusSummary]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsPackageStatusSummary]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/BundleStatusSummary",
            method="GET",
            params={
                "BundleID": bundle_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
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

    async def bundlesinupdategroup(
        self,
        *,
        id: str,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/BundlesInUpdateGroup",
            method="GET",
            params={
                "ID": id,
                "IncludeInactive": include_inactive,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsBundle,
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

    async def clientinfo(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsClientInfo]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsClientInfo]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/ClientInfo",
            method="GET",
            params={
                "ClientID": client_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClientInfo,
                    parse_obj_as(
                        type_=UpdateSystemModelsClientInfo,
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

    async def currentpackagesinupdategroup(
        self,
        *,
        id: str,
        subscription_type_filter: typing.Optional[
            ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[UpdateSystemModelsPackage]]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        subscription_type_filter : typing.Optional[ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter]
            Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[UpdateSystemModelsPackage]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/CurrentPackagesInUpdateGroup",
            method="GET",
            params={
                "ID": id,
                "SubscriptionTypeFilter": subscription_type_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UpdateSystemModelsPackage],
                    parse_obj_as(
                        type_=typing.List[UpdateSystemModelsPackage],
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

    async def getclient(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsClient]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsClient]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/GetClient",
            method="GET",
            params={
                "ID": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClient,
                    parse_obj_as(
                        type_=UpdateSystemModelsClient,
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

    async def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/GetSubscriptions",
            method="GET",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
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

    async def packagestatussummary(
        self, *, package_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsPackageStatusSummary]:
        """
        No Documentation Found.

        Parameters
        ----------
        package_id : str
            The Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsPackageStatusSummary]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/PackageStatusSummary",
            method="GET",
            params={
                "PackageID": package_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsPackageStatusSummary,
                    parse_obj_as(
                        type_=UpdateSystemModelsPackageStatusSummary,
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

    async def registeredclients(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        report_result: typing.Optional[str] = None,
        report_result_is_valid: typing.Optional[bool] = None,
        report_value: typing.Optional[str] = None,
        last_check_in_before: typing.Optional[dt.datetime] = None,
        last_check_in_after: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.

        client_id : typing.Optional[str]
            Optional. Filter where ClientID matches a value. Wildcards are supported (*).

        tag : typing.Optional[str]
            Optional. Filter where Tag matches a value. Wildcards are supported (*).

        report_result : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).

        report_result_is_valid : typing.Optional[bool]
            Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.

        report_value : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).

        last_check_in_before : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured before the provided date.

        last_check_in_after : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured after the provided date.

        order_by : typing.Optional[str]
            Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...
                        If sort direction is not provided for a field, it will be sorted ascending.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/RegisteredClients",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "ClientID": client_id,
                "Tag": tag,
                "ReportResult": report_result,
                "ReportResultIsValid": report_result_is_valid,
                "ReportValue": report_value,
                "LastCheckInBefore": serialize_datetime(last_check_in_before)
                if last_check_in_before is not None
                else None,
                "LastCheckInAfter": serialize_datetime(last_check_in_after)
                if last_check_in_after is not None
                else None,
                "OrderBy": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
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

    async def updategroups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroup]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroup]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/UpdateGroups",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroup,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroup,
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

    async def updatemetrics(
        self,
        *,
        update_group_id: str,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSystemModelsUpdateMetricsData]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : str
            The UpdateType in which clients must be for the report to include them.

        bundle_number : typing.Optional[int]
            Optional. Tells us which chart to show based upon filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsUpdateMetricsData]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Reporting/UpdateMetrics",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "bundleNumber": bundle_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateMetricsData,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateMetricsData,
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
