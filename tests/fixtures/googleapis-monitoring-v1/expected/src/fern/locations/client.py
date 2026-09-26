

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_metrics_scopes_by_monitored_project_response import ListMetricsScopesByMonitoredProjectResponse
from ..types.operation import Operation
from .raw_client import AsyncRawLocationsClient, RawLocationsClient
from .types.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project_request_alt import (
    MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt,
)
from .types.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project_request_xgafv import (
    MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv,
)
from .types.monitoring_locations_global_metrics_scopes_projects_create_request_alt import (
    MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt,
)
from .types.monitoring_locations_global_metrics_scopes_projects_create_request_xgafv import (
    MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv,
)


OMIT = typing.cast(typing.Any, ...)


class LocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationsClient
        """
        return self._raw_client

    def monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project(
        self,
        *,
        xgafv: typing.Optional[
            MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv
        ] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[
            MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt
        ] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        monitored_resource_container: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMetricsScopesByMonitoredProjectResponse:
        """
        Returns a list of every Metrics Scope that a specific MonitoredProject has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

        Parameters
        ----------
        xgafv : typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt]
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

        monitored_resource_container : typing.Optional[str]
            Required. The resource name of the Monitored Project being requested. Example: projects/{MONITORED_PROJECT_ID_OR_NUMBER}

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMetricsScopesByMonitoredProjectResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project()
        """
        _response = (
            self._raw_client.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project(
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
                monitored_resource_container=monitored_resource_container,
                request_options=request_options,
            )
        )
        return _response.data

    def monitoring_locations_global_metrics_scopes_projects_create(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        create_time: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Operation:
        """
        Adds a MonitoredProject with the given project ID to the specified Metrics Scope.

        Parameters
        ----------
        parent : str
            Required. The resource name of the existing Metrics Scope that will monitor this project. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}

        xgafv : typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt]
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

        create_time : typing.Optional[str]
            Output only. The time when this MonitoredProject was created.

        name : typing.Optional[str]
            Immutable. The resource name of the MonitoredProject. On input, the resource name includes the scoping project ID and monitored project ID. On output, it contains the equivalent project numbers. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Operation
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.locations.monitoring_locations_global_metrics_scopes_projects_create(
            parent="parent",
        )
        """
        _response = self._raw_client.monitoring_locations_global_metrics_scopes_projects_create(
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
            create_time=create_time,
            name=name,
            request_options=request_options,
        )
        return _response.data


class AsyncLocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationsClient
        """
        return self._raw_client

    async def monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project(
        self,
        *,
        xgafv: typing.Optional[
            MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv
        ] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[
            MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt
        ] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        monitored_resource_container: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMetricsScopesByMonitoredProjectResponse:
        """
        Returns a list of every Metrics Scope that a specific MonitoredProject has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

        Parameters
        ----------
        xgafv : typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt]
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

        monitored_resource_container : typing.Optional[str]
            Required. The resource name of the Monitored Project being requested. Example: projects/{MONITORED_PROJECT_ID_OR_NUMBER}

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMetricsScopesByMonitoredProjectResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project(
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
                monitored_resource_container=monitored_resource_container,
                request_options=request_options,
            )
        )
        return _response.data

    async def monitoring_locations_global_metrics_scopes_projects_create(
        self,
        parent: str,
        *,
        xgafv: typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        create_time: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Operation:
        """
        Adds a MonitoredProject with the given project ID to the specified Metrics Scope.

        Parameters
        ----------
        parent : str
            Required. The resource name of the existing Metrics Scope that will monitor this project. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}

        xgafv : typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt]
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

        create_time : typing.Optional[str]
            Output only. The time when this MonitoredProject was created.

        name : typing.Optional[str]
            Immutable. The resource name of the MonitoredProject. On input, the resource name includes the scoping project ID and monitored project ID. On output, it contains the equivalent project numbers. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Operation
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.locations.monitoring_locations_global_metrics_scopes_projects_create(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.monitoring_locations_global_metrics_scopes_projects_create(
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
            create_time=create_time,
            name=name,
            request_options=request_options,
        )
        return _response.data
