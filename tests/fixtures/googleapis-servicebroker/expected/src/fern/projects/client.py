

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.google_cloud_servicebroker_v1alpha1create_binding_response import (
    GoogleCloudServicebrokerV1Alpha1CreateBindingResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1create_service_instance_response import (
    GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1delete_service_instance_response import (
    GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1get_binding_response import (
    GoogleCloudServicebrokerV1Alpha1GetBindingResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1list_bindings_response import (
    GoogleCloudServicebrokerV1Alpha1ListBindingsResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1list_catalog_response import (
    GoogleCloudServicebrokerV1Alpha1ListCatalogResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1list_service_instances_response import (
    GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse,
)
from ..types.google_cloud_servicebroker_v1alpha1operation import GoogleCloudServicebrokerV1Alpha1Operation
from ..types.google_cloud_servicebroker_v1alpha1service_instance import GoogleCloudServicebrokerV1Alpha1ServiceInstance
from ..types.google_cloud_servicebroker_v1alpha1update_service_instance_response import (
    GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse,
)
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.servicebroker_projects_brokers_instances_service_bindings_list_request_alt import (
    ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt,
)
from .types.servicebroker_projects_brokers_instances_service_bindings_list_request_xgafv import (
    ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv,
)
from .types.servicebroker_projects_brokers_service_instances_list_request_alt import (
    ServicebrokerProjectsBrokersServiceInstancesListRequestAlt,
)
from .types.servicebroker_projects_brokers_service_instances_list_request_xgafv import (
    ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2catalog_list_request_alt import (
    ServicebrokerProjectsBrokersV2CatalogListRequestAlt,
)
from .types.servicebroker_projects_brokers_v2catalog_list_request_xgafv import (
    ServicebrokerProjectsBrokersV2CatalogListRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_create_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_create_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_delete_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_delete_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_get_last_operation_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_get_last_operation_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_get_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_get_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_patch_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_patch_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_alt import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt,
)
from .types.servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_xgafv import (
    ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv,
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

    def servicebroker_projects_brokers_v2service_instances_get(
        self,
        name: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ServiceInstance:
        """
        Gets the given service instance from the system.
        This API is an extension and not part of the OSB spec.
        Hence the path is a standard Google API URL.

        Parameters
        ----------
        name : str
            The resource name of the instance to return.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ServiceInstance
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_get(
            name="name",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_get(
            name,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_instances_service_bindings_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListBindingsResponse:
        """
        Lists all the bindings in the instance

        Parameters
        ----------
        parent : str
            Parent must match
            `projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListBindingsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_instances_service_bindings_list(
            parent="parent",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_instances_service_bindings_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_service_instances_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse:
        """
        Lists all the instances in the brokers
        This API is an extension and not part of the OSB spec.
        Hence the path is a standard Google API URL.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_service_instances_list(
            parent="parent",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_service_instances_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2catalog_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListCatalogResponse:
        """
        Lists all the Services registered with this broker for consumption for
        given service registry broker, which contains an set of services.
        Note, that Service producer API is separate from Broker API.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListCatalogResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2catalog_list(
            parent="parent",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2catalog_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_delete(
        self,
        parent: str,
        instance_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse:
        """
        Deprovisions a service instance.
        For synchronous/asynchronous request details see CreateServiceInstance
        method.
        If service instance does not exist HTTP 410 status will be returned.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id to deprovision.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        plan_id : typing.Optional[str]
            The plan id of the service instance.

        service_id : typing.Optional[str]
            The service id of the service instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_delete(
            parent="parent",
            instance_id="instanceId",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_delete(
            parent,
            instance_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_get_last_operation(
        self,
        parent: str,
        instance_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        operation: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1Operation:
        """
        Returns the state of the last operation for the service instance.
        Only last (or current) operation can be polled.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id for which to return the last operation status.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        operation : typing.Optional[str]
            If `operation` was returned during mutation operation, this field must be
            populated with the provided value.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1Operation
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_get_last_operation(
            parent="parent",
            instance_id="instanceId",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_get_last_operation(
            parent,
            instance_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            operation=operation,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_service_bindings_get(
        self,
        parent: str,
        instance_id: str,
        binding_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1GetBindingResponse:
        """
        GetBinding returns the binding information.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            Instance id to which the binding is bound.

        binding_id : str
            The binding id.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1GetBindingResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get(
            parent="parent",
            instance_id="instanceId",
            binding_id="bindingId",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_get(
            parent,
            instance_id,
            binding_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
        self,
        parent: str,
        instance_id: str,
        binding_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[
            ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv
        ] = None,
        alt: typing.Optional[
            ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt
        ] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        operation: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1Operation:
        """
        Returns the state of the last operation for the binding.
        Only last (or current) operation can be polled.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id that the binding is bound to.

        binding_id : str
            The binding id for which to return the last operation

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        operation : typing.Optional[str]
            If `operation` was returned during mutation operation, this field must be
            populated with the provided value.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1Operation
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
            parent="parent",
            instance_id="instanceId",
            binding_id="bindingId",
        )
        """
        _response = (
            self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
                parent,
                instance_id,
                binding_id,
                upload_protocol=upload_protocol,
                quota_user=quota_user,
                pretty_print=pretty_print,
                upload_type=upload_type,
                fields=fields,
                callback=callback,
                oauth_token=oauth_token,
                xgafv=xgafv,
                alt=alt,
                key=key,
                access_token=access_token,
                operation=operation,
                plan_id=plan_id,
                service_id=service_id,
                request_options=request_options,
            )
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_service_bindings_create(
        self,
        parent: str,
        instance_id: str,
        binding_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        bind_resource: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        binding_id: typing.Optional[str] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1CreateBindingResponse:
        """
        CreateBinding generates a service binding to an existing service instance.
        See ProviServiceInstance for async operation details.

        Parameters
        ----------
        parent : str
            The GCP container.
            Must match
            `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The service instance to which to bind.

        binding_id_ : str
            The id of the binding. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        bind_resource : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object that contains data for platform resources associated with
            the binding to be created.

        binding_id : typing.Optional[str]
            The id of the binding. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the binding was created.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service binding.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1CreateBindingResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_create(
            parent="parent",
            instance_id="instanceId",
            binding_id_="binding_id",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_create(
            parent,
            instance_id,
            binding_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            bind_resource=bind_resource,
            binding_id=binding_id,
            create_time=create_time,
            parameters=parameters,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_create(
        self,
        parent: str,
        instance_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        instance_id: typing.Optional[str] = OMIT,
        organization_guid: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        previous_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        resource_name: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        space_guid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse:
        """
        Provisions a service instance.
        If `request.accepts_incomplete` is false and Broker cannot execute request
        synchronously HTTP 422 error will be returned along with
        FAILED_PRECONDITION status.
        If `request.accepts_incomplete` is true and the Broker decides to execute
        resource asynchronously then HTTP 202 response code will be returned and a
        valid polling operation in the response will be included.
        If Broker executes the request synchronously and it succeeds HTTP 201
        response will be furnished.
        If identical instance exists, then HTTP 200 response will be returned.
        If an instance with identical ID but mismatching parameters exists, then
        HTTP 409 status code will be returned.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id_ : str
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            Value indicating that API client supports asynchronous operations. If
            Broker cannot execute the request synchronously HTTP 422 code will be
            returned to HTTP clients along with FAILED_PRECONDITION error.
            If true and broker will execute request asynchronously 202 HTTP code will
            be returned.
            This broker always requires this to be true as all mutator operations are
            asynchronous.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Platform specific contextual information under which the service instance
            is to be provisioned. This replaces organization_guid and space_guid.
            But can also contain anything.
            Currently only used for logging context information.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the instance was created.

        deployment_name : typing.Optional[str]
            Output only. Name of the Deployment Manager deployment used for provisioning of this
            service instance.

        instance_id : typing.Optional[str]
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        organization_guid : typing.Optional[str]
            The platform GUID for the organization under which the service is to be
            provisioned.
            Required.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service instance.
            Parameters is JSON object serialized to string.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        previous_values : typing.Optional[typing.Dict[str, typing.Any]]
            Used only in UpdateServiceInstance request to optionally specify previous
            fields.

        resource_name : typing.Optional[str]
            Output only. The resource name of the instance, e.g.
            projects/project_id/brokers/broker_id/service_instances/instance_id

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        space_guid : typing.Optional[str]
            The identifier for the project space within the platform organization.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_create(
            parent="parent",
            instance_id_="instance_id",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_create(
            parent,
            instance_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            context=context,
            create_time=create_time,
            deployment_name=deployment_name,
            instance_id=instance_id,
            organization_guid=organization_guid,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            resource_name=resource_name,
            service_id=service_id,
            space_guid=space_guid,
            request_options=request_options,
        )
        return _response.data

    def servicebroker_projects_brokers_v2service_instances_patch(
        self,
        parent: str,
        instance_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        instance_id: typing.Optional[str] = OMIT,
        organization_guid: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        previous_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        resource_name: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        space_guid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse:
        """
        Updates an existing service instance.
        See CreateServiceInstance for possible response codes.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id_ : str
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Platform specific contextual information under which the service instance
            is to be provisioned. This replaces organization_guid and space_guid.
            But can also contain anything.
            Currently only used for logging context information.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the instance was created.

        deployment_name : typing.Optional[str]
            Output only. Name of the Deployment Manager deployment used for provisioning of this
            service instance.

        instance_id : typing.Optional[str]
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        organization_guid : typing.Optional[str]
            The platform GUID for the organization under which the service is to be
            provisioned.
            Required.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service instance.
            Parameters is JSON object serialized to string.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        previous_values : typing.Optional[typing.Dict[str, typing.Any]]
            Used only in UpdateServiceInstance request to optionally specify previous
            fields.

        resource_name : typing.Optional[str]
            Output only. The resource name of the instance, e.g.
            projects/project_id/brokers/broker_id/service_instances/instance_id

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        space_guid : typing.Optional[str]
            The identifier for the project space within the platform organization.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.servicebroker_projects_brokers_v2service_instances_patch(
            parent="parent",
            instance_id_="instance_id",
        )
        """
        _response = self._raw_client.servicebroker_projects_brokers_v2service_instances_patch(
            parent,
            instance_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            context=context,
            create_time=create_time,
            deployment_name=deployment_name,
            instance_id=instance_id,
            organization_guid=organization_guid,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            resource_name=resource_name,
            service_id=service_id,
            space_guid=space_guid,
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

    async def servicebroker_projects_brokers_v2service_instances_get(
        self,
        name: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ServiceInstance:
        """
        Gets the given service instance from the system.
        This API is an extension and not part of the OSB spec.
        Hence the path is a standard Google API URL.

        Parameters
        ----------
        name : str
            The resource name of the instance to return.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ServiceInstance
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_get(
            name,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_instances_service_bindings_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListBindingsResponse:
        """
        Lists all the bindings in the instance

        Parameters
        ----------
        parent : str
            Parent must match
            `projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListBindingsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_instances_service_bindings_list(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_instances_service_bindings_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_service_instances_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse:
        """
        Lists all the instances in the brokers
        This API is an extension and not part of the OSB spec.
        Hence the path is a standard Google API URL.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_service_instances_list(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_service_instances_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2catalog_list(
        self,
        parent: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1ListCatalogResponse:
        """
        Lists all the Services registered with this broker for consumption for
        given service registry broker, which contains an set of services.
        Note, that Service producer API is separate from Broker API.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        page_size : typing.Optional[int]
            Specifies the number of results to return per page. If there are fewer
            elements than the specified number, returns all elements.
            Optional. If unset or 0, all the results will be returned.

        page_token : typing.Optional[str]
            Specifies a page token to use. Set `pageToken` to a `nextPageToken`
            returned by a previous list request to get the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1ListCatalogResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2catalog_list(
                parent="parent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2catalog_list(
            parent,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_delete(
        self,
        parent: str,
        instance_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse:
        """
        Deprovisions a service instance.
        For synchronous/asynchronous request details see CreateServiceInstance
        method.
        If service instance does not exist HTTP 410 status will be returned.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id to deprovision.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        plan_id : typing.Optional[str]
            The plan id of the service instance.

        service_id : typing.Optional[str]
            The service id of the service instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_delete(
                parent="parent",
                instance_id="instanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_delete(
            parent,
            instance_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_get_last_operation(
        self,
        parent: str,
        instance_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        operation: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1Operation:
        """
        Returns the state of the last operation for the service instance.
        Only last (or current) operation can be polled.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id for which to return the last operation status.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        operation : typing.Optional[str]
            If `operation` was returned during mutation operation, this field must be
            populated with the provided value.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1Operation
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_get_last_operation(
                parent="parent",
                instance_id="instanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_get_last_operation(
            parent,
            instance_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            operation=operation,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_service_bindings_get(
        self,
        parent: str,
        instance_id: str,
        binding_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1GetBindingResponse:
        """
        GetBinding returns the binding information.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            Instance id to which the binding is bound.

        binding_id : str
            The binding id.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1GetBindingResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get(
                parent="parent",
                instance_id="instanceId",
                binding_id="bindingId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_get(
            parent,
            instance_id,
            binding_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
        self,
        parent: str,
        instance_id: str,
        binding_id: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[
            ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv
        ] = None,
        alt: typing.Optional[
            ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt
        ] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        operation: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1Operation:
        """
        Returns the state of the last operation for the binding.
        Only last (or current) operation can be polled.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The instance id that the binding is bound to.

        binding_id : str
            The binding id for which to return the last operation

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        operation : typing.Optional[str]
            If `operation` was returned during mutation operation, this field must be
            populated with the provided value.

        plan_id : typing.Optional[str]
            Plan id.

        service_id : typing.Optional[str]
            Service id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1Operation
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
                parent="parent",
                instance_id="instanceId",
                binding_id="bindingId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
            parent,
            instance_id,
            binding_id,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            operation=operation,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_service_bindings_create(
        self,
        parent: str,
        instance_id: str,
        binding_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        bind_resource: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        binding_id: typing.Optional[str] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1CreateBindingResponse:
        """
        CreateBinding generates a service binding to an existing service instance.
        See ProviServiceInstance for async operation details.

        Parameters
        ----------
        parent : str
            The GCP container.
            Must match
            `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id : str
            The service instance to which to bind.

        binding_id_ : str
            The id of the binding. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        bind_resource : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object that contains data for platform resources associated with
            the binding to be created.

        binding_id : typing.Optional[str]
            The id of the binding. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the binding was created.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service binding.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1CreateBindingResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_create(
                parent="parent",
                instance_id="instanceId",
                binding_id_="binding_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_service_bindings_create(
            parent,
            instance_id,
            binding_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            bind_resource=bind_resource,
            binding_id=binding_id,
            create_time=create_time,
            parameters=parameters,
            plan_id=plan_id,
            service_id=service_id,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_create(
        self,
        parent: str,
        instance_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        instance_id: typing.Optional[str] = OMIT,
        organization_guid: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        previous_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        resource_name: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        space_guid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse:
        """
        Provisions a service instance.
        If `request.accepts_incomplete` is false and Broker cannot execute request
        synchronously HTTP 422 error will be returned along with
        FAILED_PRECONDITION status.
        If `request.accepts_incomplete` is true and the Broker decides to execute
        resource asynchronously then HTTP 202 response code will be returned and a
        valid polling operation in the response will be included.
        If Broker executes the request synchronously and it succeeds HTTP 201
        response will be furnished.
        If identical instance exists, then HTTP 200 response will be returned.
        If an instance with identical ID but mismatching parameters exists, then
        HTTP 409 status code will be returned.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id_ : str
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            Value indicating that API client supports asynchronous operations. If
            Broker cannot execute the request synchronously HTTP 422 code will be
            returned to HTTP clients along with FAILED_PRECONDITION error.
            If true and broker will execute request asynchronously 202 HTTP code will
            be returned.
            This broker always requires this to be true as all mutator operations are
            asynchronous.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Platform specific contextual information under which the service instance
            is to be provisioned. This replaces organization_guid and space_guid.
            But can also contain anything.
            Currently only used for logging context information.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the instance was created.

        deployment_name : typing.Optional[str]
            Output only. Name of the Deployment Manager deployment used for provisioning of this
            service instance.

        instance_id : typing.Optional[str]
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        organization_guid : typing.Optional[str]
            The platform GUID for the organization under which the service is to be
            provisioned.
            Required.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service instance.
            Parameters is JSON object serialized to string.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        previous_values : typing.Optional[typing.Dict[str, typing.Any]]
            Used only in UpdateServiceInstance request to optionally specify previous
            fields.

        resource_name : typing.Optional[str]
            Output only. The resource name of the instance, e.g.
            projects/project_id/brokers/broker_id/service_instances/instance_id

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        space_guid : typing.Optional[str]
            The identifier for the project space within the platform organization.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_create(
                parent="parent",
                instance_id_="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_create(
            parent,
            instance_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            context=context,
            create_time=create_time,
            deployment_name=deployment_name,
            instance_id=instance_id,
            organization_guid=organization_guid,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            resource_name=resource_name,
            service_id=service_id,
            space_guid=space_guid,
            request_options=request_options,
        )
        return _response.data

    async def servicebroker_projects_brokers_v2service_instances_patch(
        self,
        parent: str,
        instance_id_: str,
        *,
        upload_protocol: typing.Optional[str] = None,
        quota_user: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        upload_type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        callback: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        xgafv: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv] = None,
        alt: typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt] = None,
        key: typing.Optional[str] = None,
        access_token: typing.Optional[str] = None,
        accepts_incomplete: typing.Optional[bool] = None,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        create_time: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        instance_id: typing.Optional[str] = OMIT,
        organization_guid: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        previous_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        resource_name: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        space_guid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse:
        """
        Updates an existing service instance.
        See CreateServiceInstance for possible response codes.

        Parameters
        ----------
        parent : str
            Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.

        instance_id_ : str
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        callback : typing.Optional[str]
            JSONP

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        xgafv : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv]
            V1 error format.

        alt : typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt]
            Data format for response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        access_token : typing.Optional[str]
            OAuth access token.

        accepts_incomplete : typing.Optional[bool]
            See CreateServiceInstanceRequest for details.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Platform specific contextual information under which the service instance
            is to be provisioned. This replaces organization_guid and space_guid.
            But can also contain anything.
            Currently only used for logging context information.

        create_time : typing.Optional[str]
            Output only. Timestamp for when the instance was created.

        deployment_name : typing.Optional[str]
            Output only. Name of the Deployment Manager deployment used for provisioning of this
            service instance.

        instance_id : typing.Optional[str]
            The id of the service instance. Must be unique within GCP project.
            Maximum length is 64, GUID recommended.
            Required.

        organization_guid : typing.Optional[str]
            The platform GUID for the organization under which the service is to be
            provisioned.
            Required.

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration options for the service instance.
            Parameters is JSON object serialized to string.

        plan_id : typing.Optional[str]
            The ID of the plan. See `Service` and `Plan` resources for details.
            Maximum length is 64, GUID recommended.
            Required.

        previous_values : typing.Optional[typing.Dict[str, typing.Any]]
            Used only in UpdateServiceInstance request to optionally specify previous
            fields.

        resource_name : typing.Optional[str]
            Output only. The resource name of the instance, e.g.
            projects/project_id/brokers/broker_id/service_instances/instance_id

        service_id : typing.Optional[str]
            The id of the service. Must be a valid identifier of a service
            contained in the list from a `ListServices()` call.
            Maximum length is 64, GUID recommended.
            Required.

        space_guid : typing.Optional[str]
            The identifier for the project space within the platform organization.
            Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.servicebroker_projects_brokers_v2service_instances_patch(
                parent="parent",
                instance_id_="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.servicebroker_projects_brokers_v2service_instances_patch(
            parent,
            instance_id_,
            upload_protocol=upload_protocol,
            quota_user=quota_user,
            pretty_print=pretty_print,
            upload_type=upload_type,
            fields=fields,
            callback=callback,
            oauth_token=oauth_token,
            xgafv=xgafv,
            alt=alt,
            key=key,
            access_token=access_token,
            accepts_incomplete=accepts_incomplete,
            context=context,
            create_time=create_time,
            deployment_name=deployment_name,
            instance_id=instance_id,
            organization_guid=organization_guid,
            parameters=parameters,
            plan_id=plan_id,
            previous_values=previous_values,
            resource_name=resource_name,
            service_id=service_id,
            space_guid=space_guid,
            request_options=request_options,
        )
        return _response.data
