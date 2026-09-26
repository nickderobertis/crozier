

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
from ..types.column_layout import ColumnLayout
from ..types.dashboard import Dashboard
from ..types.dashboard_filter import DashboardFilter
from ..types.empty import Empty
from ..types.grid_layout import GridLayout
from ..types.http_body import HttpBody
from ..types.list_dashboards_response import ListDashboardsResponse
from ..types.mosaic_layout import MosaicLayout
from ..types.row_layout import RowLayout
from .types.monitoring_projects_dashboards_create_request_alt import MonitoringProjectsDashboardsCreateRequestAlt
from .types.monitoring_projects_dashboards_create_request_xgafv import MonitoringProjectsDashboardsCreateRequestXgafv
from .types.monitoring_projects_dashboards_delete_request_alt import MonitoringProjectsDashboardsDeleteRequestAlt
from .types.monitoring_projects_dashboards_delete_request_xgafv import MonitoringProjectsDashboardsDeleteRequestXgafv
from .types.monitoring_projects_dashboards_get_request_alt import MonitoringProjectsDashboardsGetRequestAlt
from .types.monitoring_projects_dashboards_get_request_xgafv import MonitoringProjectsDashboardsGetRequestXgafv
from .types.monitoring_projects_dashboards_list_request_alt import MonitoringProjectsDashboardsListRequestAlt
from .types.monitoring_projects_dashboards_list_request_xgafv import MonitoringProjectsDashboardsListRequestXgafv
from .types.monitoring_projects_dashboards_patch_request_alt import MonitoringProjectsDashboardsPatchRequestAlt
from .types.monitoring_projects_dashboards_patch_request_xgafv import MonitoringProjectsDashboardsPatchRequestXgafv
from .types.monitoring_projects_location_prometheus_api_v1label_values_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1label_values_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1labels_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1labels_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1metadata_list_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1metadata_list_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1query_exemplars_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1query_exemplars_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1query_range_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1query_range_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1query_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1query_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv,
)
from .types.monitoring_projects_location_prometheus_api_v1series_request_alt import (
    MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt,
)
from .types.monitoring_projects_location_prometheus_api_v1series_request_xgafv import (
    MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def monitoring_projects_dashboards_get(
        self,
        name: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsGetRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsGetRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dashboard]:
        """
        Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name : str
            Required. The resource name of the Dashboard. The format is one of: dashboards/[DASHBOARD_ID] (for system dashboards) projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID] (for custom dashboards).

        xgafv : typing.Optional[MonitoringProjectsDashboardsGetRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsGetRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dashboard]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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

    def monitoring_projects_dashboards_delete(
        self,
        name: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsDeleteRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsDeleteRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Empty]:
        """
        Deletes an existing custom dashboard.This method requires the monitoring.dashboards.delete permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name : str
            Required. The resource name of the Dashboard. The format is: projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]

        xgafv : typing.Optional[MonitoringProjectsDashboardsDeleteRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsDeleteRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Empty]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}",
            method="DELETE",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Empty,
                    parse_obj_as(
                        type_=Empty,
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

    def monitoring_projects_dashboards_patch(
        self,
        name_: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsPatchRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsPatchRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        validate_only: typing.Optional[bool] = None,
        column_layout: typing.Optional[ColumnLayout] = OMIT,
        dashboard_filters: typing.Optional[typing.Sequence[DashboardFilter]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        grid_layout: typing.Optional[GridLayout] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        mosaic_layout: typing.Optional[MosaicLayout] = OMIT,
        name: typing.Optional[str] = OMIT,
        row_layout: typing.Optional[RowLayout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dashboard]:
        """
        Replaces an existing custom dashboard with a new definition.This method requires the monitoring.dashboards.update permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name_ : str
            Identifier. The resource name of the dashboard.

        xgafv : typing.Optional[MonitoringProjectsDashboardsPatchRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsPatchRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        validate_only : typing.Optional[bool]
            If set, validate the request and preview the review, but do not actually save it.

        column_layout : typing.Optional[ColumnLayout]
            The content is divided into equally spaced columns and the widgets are arranged vertically.

        dashboard_filters : typing.Optional[typing.Sequence[DashboardFilter]]
            Filters to reduce the amount of data charted based on the filter criteria.

        display_name : typing.Optional[str]
            Required. The mutable, human-readable name.

        etag : typing.Optional[str]
            etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.

        grid_layout : typing.Optional[GridLayout]
            Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the dashboard

        mosaic_layout : typing.Optional[MosaicLayout]
            The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.

        name : typing.Optional[str]
            Identifier. The resource name of the dashboard.

        row_layout : typing.Optional[RowLayout]
            The content is divided into equally spaced rows and the widgets are arranged horizontally.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dashboard]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name_)}",
            method="PATCH",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "validateOnly": validate_only,
            },
            json={
                "columnLayout": convert_and_respect_annotation_metadata(
                    object_=column_layout, annotation=ColumnLayout, direction="write"
                ),
                "dashboardFilters": convert_and_respect_annotation_metadata(
                    object_=dashboard_filters, annotation=typing.Sequence[DashboardFilter], direction="write"
                ),
                "displayName": display_name,
                "etag": etag,
                "gridLayout": convert_and_respect_annotation_metadata(
                    object_=grid_layout, annotation=GridLayout, direction="write"
                ),
                "labels": labels,
                "mosaicLayout": convert_and_respect_annotation_metadata(
                    object_=mosaic_layout, annotation=MosaicLayout, direction="write"
                ),
                "name": name,
                "rowLayout": convert_and_respect_annotation_metadata(
                    object_=row_layout, annotation=RowLayout, direction="write"
                ),
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
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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

    def monitoring_projects_location_prometheus_api_v1label_values(
        self,
        name: str,
        location: str,
        label: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        match: typing.Optional[str] = None,
        start: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Lists possible values for a given label name.

        Parameters
        ----------
        name : str
            The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" now.

        label : str
            The label name for which values are queried.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        match : typing.Optional[str]
            A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/label/{encode_path_param(label)}/values",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "end": end,
                "match": match,
                "start": start,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1labels(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        match: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Lists labels for metrics.

        Parameters
        ----------
        name : str
            The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        match : typing.Optional[str]
            A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/labels",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "match": match,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1metadata_list(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Lists metadata for metrics.

        Parameters
        ----------
        name : str
            Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" for now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        limit : typing.Optional[str]
            Maximum number of metrics to return.

        metric : typing.Optional[str]
            The metric name for which to query metadata. If unset, all metric metadata is returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/metadata",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "limit": limit,
                "metric": metric,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1query(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        query: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Evaluate a PromQL query at a single point in time.

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        time : typing.Optional[str]
            The single point in time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        timeout : typing.Optional[str]
            An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "query": query,
                "time": time,
                "timeout": timeout,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1query_exemplars(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Lists exemplars relevant to a given PromQL query,

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query_exemplars",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "query": query,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1query_range(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Evaluate a PromQL query with start, end time range.

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        step : typing.Optional[str]
            The resolution of query result. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        timeout : typing.Optional[str]
            An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query_range",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "query": query,
                "start": start,
                "step": step,
                "timeout": timeout,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_location_prometheus_api_v1series(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HttpBody]:
        """
        Lists metadata for metrics.

        Parameters
        ----------
        name : str
            Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" for now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpBody]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/series",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    def monitoring_projects_dashboards_list(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDashboardsResponse]:
        """
        Lists the existing dashboards.This method requires the monitoring.dashboards.list permission on the specified project. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        parent : str
            Required. The scope of the dashboards to list. The format is: projects/[PROJECT_ID_OR_NUMBER]

        xgafv : typing.Optional[MonitoringProjectsDashboardsListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        page_size : typing.Optional[int]
            A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used.

        page_token : typing.Optional[str]
            Optional. If this field is not empty then it must contain the nextPageToken value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDashboardsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(parent)}/dashboards",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDashboardsResponse,
                    parse_obj_as(
                        type_=ListDashboardsResponse,
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

    def monitoring_projects_dashboards_create(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsCreateRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsCreateRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        validate_only: typing.Optional[bool] = None,
        column_layout: typing.Optional[ColumnLayout] = OMIT,
        dashboard_filters: typing.Optional[typing.Sequence[DashboardFilter]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        grid_layout: typing.Optional[GridLayout] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        mosaic_layout: typing.Optional[MosaicLayout] = OMIT,
        name: typing.Optional[str] = OMIT,
        row_layout: typing.Optional[RowLayout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dashboard]:
        """
        Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see Managing dashboards by API (https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the monitoring.dashboards.create permission on the specified project. For more information about permissions, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        parent : str
            Required. The project on which to execute the request. The format is: projects/[PROJECT_ID_OR_NUMBER] The [PROJECT_ID_OR_NUMBER] must match the dashboard resource name.

        xgafv : typing.Optional[MonitoringProjectsDashboardsCreateRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsCreateRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        validate_only : typing.Optional[bool]
            If set, validate the request and preview the review, but do not actually save it.

        column_layout : typing.Optional[ColumnLayout]
            The content is divided into equally spaced columns and the widgets are arranged vertically.

        dashboard_filters : typing.Optional[typing.Sequence[DashboardFilter]]
            Filters to reduce the amount of data charted based on the filter criteria.

        display_name : typing.Optional[str]
            Required. The mutable, human-readable name.

        etag : typing.Optional[str]
            etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.

        grid_layout : typing.Optional[GridLayout]
            Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the dashboard

        mosaic_layout : typing.Optional[MosaicLayout]
            The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.

        name : typing.Optional[str]
            Identifier. The resource name of the dashboard.

        row_layout : typing.Optional[RowLayout]
            The content is divided into equally spaced rows and the widgets are arranged horizontally.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dashboard]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(parent)}/dashboards",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "validateOnly": validate_only,
            },
            json={
                "columnLayout": convert_and_respect_annotation_metadata(
                    object_=column_layout, annotation=ColumnLayout, direction="write"
                ),
                "dashboardFilters": convert_and_respect_annotation_metadata(
                    object_=dashboard_filters, annotation=typing.Sequence[DashboardFilter], direction="write"
                ),
                "displayName": display_name,
                "etag": etag,
                "gridLayout": convert_and_respect_annotation_metadata(
                    object_=grid_layout, annotation=GridLayout, direction="write"
                ),
                "labels": labels,
                "mosaicLayout": convert_and_respect_annotation_metadata(
                    object_=mosaic_layout, annotation=MosaicLayout, direction="write"
                ),
                "name": name,
                "rowLayout": convert_and_respect_annotation_metadata(
                    object_=row_layout, annotation=RowLayout, direction="write"
                ),
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
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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


class AsyncRawProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def monitoring_projects_dashboards_get(
        self,
        name: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsGetRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsGetRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dashboard]:
        """
        Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name : str
            Required. The resource name of the Dashboard. The format is one of: dashboards/[DASHBOARD_ID] (for system dashboards) projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID] (for custom dashboards).

        xgafv : typing.Optional[MonitoringProjectsDashboardsGetRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsGetRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dashboard]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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

    async def monitoring_projects_dashboards_delete(
        self,
        name: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsDeleteRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsDeleteRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Empty]:
        """
        Deletes an existing custom dashboard.This method requires the monitoring.dashboards.delete permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name : str
            Required. The resource name of the Dashboard. The format is: projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]

        xgafv : typing.Optional[MonitoringProjectsDashboardsDeleteRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsDeleteRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Empty]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}",
            method="DELETE",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Empty,
                    parse_obj_as(
                        type_=Empty,
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

    async def monitoring_projects_dashboards_patch(
        self,
        name_: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsPatchRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsPatchRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        validate_only: typing.Optional[bool] = None,
        column_layout: typing.Optional[ColumnLayout] = OMIT,
        dashboard_filters: typing.Optional[typing.Sequence[DashboardFilter]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        grid_layout: typing.Optional[GridLayout] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        mosaic_layout: typing.Optional[MosaicLayout] = OMIT,
        name: typing.Optional[str] = OMIT,
        row_layout: typing.Optional[RowLayout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dashboard]:
        """
        Replaces an existing custom dashboard with a new definition.This method requires the monitoring.dashboards.update permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        name_ : str
            Identifier. The resource name of the dashboard.

        xgafv : typing.Optional[MonitoringProjectsDashboardsPatchRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsPatchRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        validate_only : typing.Optional[bool]
            If set, validate the request and preview the review, but do not actually save it.

        column_layout : typing.Optional[ColumnLayout]
            The content is divided into equally spaced columns and the widgets are arranged vertically.

        dashboard_filters : typing.Optional[typing.Sequence[DashboardFilter]]
            Filters to reduce the amount of data charted based on the filter criteria.

        display_name : typing.Optional[str]
            Required. The mutable, human-readable name.

        etag : typing.Optional[str]
            etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.

        grid_layout : typing.Optional[GridLayout]
            Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the dashboard

        mosaic_layout : typing.Optional[MosaicLayout]
            The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.

        name : typing.Optional[str]
            Identifier. The resource name of the dashboard.

        row_layout : typing.Optional[RowLayout]
            The content is divided into equally spaced rows and the widgets are arranged horizontally.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dashboard]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name_)}",
            method="PATCH",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "validateOnly": validate_only,
            },
            json={
                "columnLayout": convert_and_respect_annotation_metadata(
                    object_=column_layout, annotation=ColumnLayout, direction="write"
                ),
                "dashboardFilters": convert_and_respect_annotation_metadata(
                    object_=dashboard_filters, annotation=typing.Sequence[DashboardFilter], direction="write"
                ),
                "displayName": display_name,
                "etag": etag,
                "gridLayout": convert_and_respect_annotation_metadata(
                    object_=grid_layout, annotation=GridLayout, direction="write"
                ),
                "labels": labels,
                "mosaicLayout": convert_and_respect_annotation_metadata(
                    object_=mosaic_layout, annotation=MosaicLayout, direction="write"
                ),
                "name": name,
                "rowLayout": convert_and_respect_annotation_metadata(
                    object_=row_layout, annotation=RowLayout, direction="write"
                ),
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
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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

    async def monitoring_projects_location_prometheus_api_v1label_values(
        self,
        name: str,
        location: str,
        label: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        match: typing.Optional[str] = None,
        start: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Lists possible values for a given label name.

        Parameters
        ----------
        name : str
            The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" now.

        label : str
            The label name for which values are queried.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        match : typing.Optional[str]
            A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/label/{encode_path_param(label)}/values",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "end": end,
                "match": match,
                "start": start,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1labels(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        match: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Lists labels for metrics.

        Parameters
        ----------
        name : str
            The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        match : typing.Optional[str]
            A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/labels",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "match": match,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1metadata_list(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Lists metadata for metrics.

        Parameters
        ----------
        name : str
            Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" for now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        limit : typing.Optional[str]
            Maximum number of metrics to return.

        metric : typing.Optional[str]
            The metric name for which to query metadata. If unset, all metric metadata is returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/metadata",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "limit": limit,
                "metric": metric,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1query(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        query: typing.Optional[str] = OMIT,
        time: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Evaluate a PromQL query at a single point in time.

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        time : typing.Optional[str]
            The single point in time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        timeout : typing.Optional[str]
            An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "query": query,
                "time": time,
                "timeout": timeout,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1query_exemplars(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Lists exemplars relevant to a given PromQL query,

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query_exemplars",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "query": query,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1query_range(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        step: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Evaluate a PromQL query with start, end time range.

        Parameters
        ----------
        name : str
            The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.

        location : str
            Location of the resource information. Has to be "global" now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        query : typing.Optional[str]
            A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        step : typing.Optional[str]
            The resolution of query result. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        timeout : typing.Optional[str]
            An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/query_range",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "query": query,
                "start": start,
                "step": step,
                "timeout": timeout,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_location_prometheus_api_v1series(
        self,
        name: str,
        location: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        end: typing.Optional[str] = OMIT,
        start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HttpBody]:
        """
        Lists metadata for metrics.

        Parameters
        ----------
        name : str
            Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.

        location : str
            Location of the resource information. Has to be "global" for now.

        xgafv : typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        end : typing.Optional[str]
            The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        start : typing.Optional[str]
            The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpBody]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(name)}/location/{encode_path_param(location)}/prometheus/api/v1/series",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
            },
            json={
                "end": end,
                "start": start,
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
                    HttpBody,
                    parse_obj_as(
                        type_=HttpBody,
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

    async def monitoring_projects_dashboards_list(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDashboardsResponse]:
        """
        Lists the existing dashboards.This method requires the monitoring.dashboards.list permission on the specified project. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        parent : str
            Required. The scope of the dashboards to list. The format is: projects/[PROJECT_ID_OR_NUMBER]

        xgafv : typing.Optional[MonitoringProjectsDashboardsListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        page_size : typing.Optional[int]
            A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used.

        page_token : typing.Optional[str]
            Optional. If this field is not empty then it must contain the nextPageToken value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDashboardsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(parent)}/dashboards",
            method="GET",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDashboardsResponse,
                    parse_obj_as(
                        type_=ListDashboardsResponse,
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

    async def monitoring_projects_dashboards_create(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringProjectsDashboardsCreateRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringProjectsDashboardsCreateRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        validate_only: typing.Optional[bool] = None,
        column_layout: typing.Optional[ColumnLayout] = OMIT,
        dashboard_filters: typing.Optional[typing.Sequence[DashboardFilter]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        etag: typing.Optional[str] = OMIT,
        grid_layout: typing.Optional[GridLayout] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        mosaic_layout: typing.Optional[MosaicLayout] = OMIT,
        name: typing.Optional[str] = OMIT,
        row_layout: typing.Optional[RowLayout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dashboard]:
        """
        Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see Managing dashboards by API (https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the monitoring.dashboards.create permission on the specified project. For more information about permissions, see Cloud Identity and Access Management (https://cloud.google.com/iam).

        Parameters
        ----------
        parent : str
            Required. The project on which to execute the request. The format is: projects/[PROJECT_ID_OR_NUMBER] The [PROJECT_ID_OR_NUMBER] must match the dashboard resource name.

        xgafv : typing.Optional[MonitoringProjectsDashboardsCreateRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringProjectsDashboardsCreateRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        validate_only : typing.Optional[bool]
            If set, validate the request and preview the review, but do not actually save it.

        column_layout : typing.Optional[ColumnLayout]
            The content is divided into equally spaced columns and the widgets are arranged vertically.

        dashboard_filters : typing.Optional[typing.Sequence[DashboardFilter]]
            Filters to reduce the amount of data charted based on the filter criteria.

        display_name : typing.Optional[str]
            Required. The mutable, human-readable name.

        etag : typing.Optional[str]
            etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.

        grid_layout : typing.Optional[GridLayout]
            Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the dashboard

        mosaic_layout : typing.Optional[MosaicLayout]
            The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.

        name : typing.Optional[str]
            Identifier. The resource name of the dashboard.

        row_layout : typing.Optional[RowLayout]
            The content is divided into equally spaced rows and the widgets are arranged horizontally.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dashboard]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(parent)}/dashboards",
            method="POST",
            params={
                "$.xgafv": xgafv,
                "access_token": access_token,
                "alt": alt,
                "callback": callback,
                "fields": fields,
                "key": key,
                "oauth_token": oauth_token,
                "prettyPrint": pretty_print,
                "quotaUser": quota_user,
                "upload_protocol": upload_protocol,
                "uploadType": upload_type,
                "validateOnly": validate_only,
            },
            json={
                "columnLayout": convert_and_respect_annotation_metadata(
                    object_=column_layout, annotation=ColumnLayout, direction="write"
                ),
                "dashboardFilters": convert_and_respect_annotation_metadata(
                    object_=dashboard_filters, annotation=typing.Sequence[DashboardFilter], direction="write"
                ),
                "displayName": display_name,
                "etag": etag,
                "gridLayout": convert_and_respect_annotation_metadata(
                    object_=grid_layout, annotation=GridLayout, direction="write"
                ),
                "labels": labels,
                "mosaicLayout": convert_and_respect_annotation_metadata(
                    object_=mosaic_layout, annotation=MosaicLayout, direction="write"
                ),
                "name": name,
                "rowLayout": convert_and_respect_annotation_metadata(
                    object_=row_layout, annotation=RowLayout, direction="write"
                ),
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
                    Dashboard,
                    parse_obj_as(
                        type_=Dashboard,
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
