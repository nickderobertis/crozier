

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.column_layout import ColumnLayout
from ..types.dashboard import Dashboard
from ..types.dashboard_filter import DashboardFilter
from ..types.empty import Empty
from ..types.grid_layout import GridLayout
from ..types.http_body import HttpBody
from ..types.list_dashboards_response import ListDashboardsResponse
from ..types.mosaic_layout import MosaicLayout
from ..types.row_layout import RowLayout
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
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


OMIT = typing.cast(typing.Any, ...)


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_dashboards_get(
            name="name",
        )
        """
        _response = self._raw_client.monitoring_projects_dashboards_get(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Empty:
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
        Empty
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_dashboards_delete(
            name="name",
        )
        """
        _response = self._raw_client.monitoring_projects_dashboards_delete(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_dashboards_patch(
            name_="name",
        )
        """
        _response = self._raw_client.monitoring_projects_dashboards_patch(
            name_,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            validate_only=validate_only,
            column_layout=column_layout,
            dashboard_filters=dashboard_filters,
            display_name=display_name,
            etag=etag,
            grid_layout=grid_layout,
            labels=labels,
            mosaic_layout=mosaic_layout,
            name=name,
            row_layout=row_layout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1label_values(
            name="name",
            location="location",
            label="label",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1label_values(
            name,
            location,
            label,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            match=match,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1labels(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1labels(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            match=match,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1metadata_list(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1metadata_list(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            limit=limit,
            metric=metric,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1query(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1query(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            query=query,
            time=time,
            timeout=timeout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1query_exemplars(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1query_exemplars(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            query=query,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1query_range(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1query_range(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            query=query,
            start=start,
            step=step,
            timeout=timeout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_location_prometheus_api_v1series(
            name="name",
            location="location",
        )
        """
        _response = self._raw_client.monitoring_projects_location_prometheus_api_v1series(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ListDashboardsResponse:
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
        ListDashboardsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_dashboards_list(
            parent="parent",
        )
        """
        _response = self._raw_client.monitoring_projects_dashboards_list(
            parent,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.monitoring_projects_dashboards_create(
            parent="parent",
        )
        """
        _response = self._raw_client.monitoring_projects_dashboards_create(
            parent,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            validate_only=validate_only,
            column_layout=column_layout,
            dashboard_filters=dashboard_filters,
            display_name=display_name,
            etag=etag,
            grid_layout=grid_layout,
            labels=labels,
            mosaic_layout=mosaic_layout,
            name=name,
            row_layout=row_layout,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_dashboards_get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_dashboards_get(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Empty:
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
        Empty
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_dashboards_delete(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_dashboards_delete(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_dashboards_patch(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_dashboards_patch(
            name_,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            validate_only=validate_only,
            column_layout=column_layout,
            dashboard_filters=dashboard_filters,
            display_name=display_name,
            etag=etag,
            grid_layout=grid_layout,
            labels=labels,
            mosaic_layout=mosaic_layout,
            name=name,
            row_layout=row_layout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1label_values(
                name="name",
                location="location",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1label_values(
            name,
            location,
            label,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            match=match,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1labels(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1labels(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            match=match,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1metadata_list(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1metadata_list(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            limit=limit,
            metric=metric,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1query(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1query(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            query=query,
            time=time,
            timeout=timeout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1query_exemplars(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1query_exemplars(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            query=query,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1query_range(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1query_range(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            query=query,
            start=start,
            step=step,
            timeout=timeout,
            request_options=request_options,
        )
        return _response.data

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
    ) -> HttpBody:
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
        HttpBody
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_location_prometheus_api_v1series(
                name="name",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_location_prometheus_api_v1series(
            name,
            location,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            end=end,
            start=start,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ListDashboardsResponse:
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
        ListDashboardsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_dashboards_list(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_dashboards_list(
            parent,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Dashboard:
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
        Dashboard
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.monitoring_projects_dashboards_create(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_projects_dashboards_create(
            parent,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            validate_only=validate_only,
            column_layout=column_layout,
            dashboard_filters=dashboard_filters,
            display_name=display_name,
            etag=etag,
            grid_layout=grid_layout,
            labels=labels,
            mosaic_layout=mosaic_layout,
            name=name,
            row_layout=row_layout,
            request_options=request_options,
        )
        return _response.data
