

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.generic_error import GenericError
from ..types.launch_layer_node_pool_provider import LaunchLayerNodePoolProvider
from ..types.launch_layer_node_pool_provider_update import LaunchLayerNodePoolProviderUpdate
from ..types.list_node_pools_response import ListNodePoolsResponse
from ..types.nico_node_pool_provider import NicoNodePoolProvider
from ..types.nico_node_pool_provider_update import NicoNodePoolProviderUpdate
from ..types.node_name_prefix import NodeNamePrefix
from ..types.node_pool import NodePool
from ..types.node_taint import NodeTaint
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNodePoolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_node_pools(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListNodePoolsResponse]:
        """
        Returns all node pools, filtered by the query parameters.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node pool name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListNodePoolsResponse]
            A list of node pools
        """
        _response = self._client_wrapper.httpx_client.request(
            "nodePools",
            method="GET",
            params={
                "clusterID": cluster_id,
                "clusterName": cluster_name,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNodePoolsResponse,
                    parse_obj_as(
                        type_=ListNodePoolsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def create_node_pool(
        self,
        *,
        cluster_id: str,
        name: str,
        node_name_prefix: NodeNamePrefix,
        desired_node_count: int,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        machine_annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        machine_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_taints: typing.Optional[typing.Sequence[NodeTaint]] = OMIT,
        description: typing.Optional[str] = OMIT,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        nico: typing.Optional[NicoNodePoolProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NodePool]:
        """
        Creates a worker node pool and starts provisioning. The pool takes the
        cluster's Kubernetes version.

        Returns 400 for, among others: parent cluster not found; a duplicate
        pool name in the cluster; missing `nico.instanceTypeID`
        or `nico.release`; not exactly one of
        `subnetIDs` and `vpcPrefixIDs`; a pod CIDR too small for the requested
        nodes.

        Parameters
        ----------
        cluster_id : str
            Parent cluster.

        name : str
            Unique within the cluster. Immutable.

        node_name_prefix : NodeNamePrefix

        desired_node_count : int
            The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. Default 2Gi.

        machine_annotations : typing.Optional[typing.Dict[str, str]]
            Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        machine_labels : typing.Optional[typing.Dict[str, str]]
            Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        node_labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.

        node_taints : typing.Optional[typing.Sequence[NodeTaint]]
            Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.

        description : typing.Optional[str]
            Free-text description.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        nico : typing.Optional[NicoNodePoolProvider]

        launch_layer : typing.Optional[LaunchLayerNodePoolProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodePool]
            Node pool created; provisioning has started
        """
        _response = self._client_wrapper.httpx_client.request(
            "nodePools",
            method="POST",
            json={
                "clusterID": cluster_id,
                "name": name,
                "nodeNamePrefix": node_name_prefix,
                "systemReservedMemory": system_reserved_memory,
                "kubeReservedMemory": kube_reserved_memory,
                "machineAnnotations": machine_annotations,
                "machineLabels": machine_labels,
                "nodeLabels": node_labels,
                "nodeTaints": convert_and_respect_annotation_metadata(
                    object_=node_taints, annotation=typing.Sequence[NodeTaint], direction="write"
                ),
                "desiredNodeCount": desired_node_count,
                "description": description,
                "autoProvisionDisabled": auto_provision_disabled,
                "autoModeDisabled": auto_mode_disabled,
                "provisioningMonitorDisabled": provisioning_monitor_disabled,
                "recycleBudget": recycle_budget,
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoNodePoolProvider, direction="write"
                ),
                "launchLayer": convert_and_respect_annotation_metadata(
                    object_=launch_layer, annotation=LaunchLayerNodePoolProvider, direction="write"
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
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def get_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NodePool]:
        """
        Returns one node pool.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodePool]
            The requested node pool
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a node pool from a running cluster. Also returns 202, with no
        further effect, if the pool or its cluster is already being deleted.

        Returns 409 for a control-plane node pool while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    def update_node_pool(
        self,
        node_pool_id: str,
        *,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        desired_node_count: typing.Optional[int] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        max_surge: typing.Optional[int] = OMIT,
        kubernetes_version: typing.Optional[str] = OMIT,
        nico: typing.Optional[NicoNodePoolProviderUpdate] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProviderUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NodePool]:
        """
        All fields are optional. Changes to the Kubernetes version, release
        or other node configuration create a new NodeSet and roll the pool's
        nodes to it.

        Returns 400 for, among others: sending a field that is fixed at
        creation (for example `instanceTypeID`); `nico.release: ""`; any update
        to a control-plane node pool, which is configured through the cluster's
        `controlPlaneConfig` instead. That last refusal does not depend on the
        control-plane mutation lock, so retrying later does not help.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. An empty string restores the 2Gi default.

        description : typing.Optional[str]
            Free-text description.

        desired_node_count : typing.Optional[int]
            The desired number of nodes in the pool. Increasing aggregate control-plane capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        max_surge : typing.Optional[int]
            Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
            node is torn down before its replacement is provisioned.

        kubernetes_version : typing.Optional[str]
            Desired Kubernetes version for the pool's nodes, as X.Y.Z with no leading "v".
            Must be newer than the current version.

        nico : typing.Optional[NicoNodePoolProviderUpdate]

        launch_layer : typing.Optional[LaunchLayerNodePoolProviderUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NodePool]
            Update accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="PATCH",
            json={
                "autoProvisionDisabled": auto_provision_disabled,
                "autoModeDisabled": auto_mode_disabled,
                "provisioningMonitorDisabled": provisioning_monitor_disabled,
                "systemReservedMemory": system_reserved_memory,
                "kubeReservedMemory": kube_reserved_memory,
                "description": description,
                "desiredNodeCount": desired_node_count,
                "recycleBudget": recycle_budget,
                "maxSurge": max_surge,
                "kubernetesVersion": kubernetes_version,
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoNodePoolProviderUpdate, direction="write"
                ),
                "launchLayer": launch_layer,
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
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawNodePoolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_node_pools(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListNodePoolsResponse]:
        """
        Returns all node pools, filtered by the query parameters.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node pool name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListNodePoolsResponse]
            A list of node pools
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nodePools",
            method="GET",
            params={
                "clusterID": cluster_id,
                "clusterName": cluster_name,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNodePoolsResponse,
                    parse_obj_as(
                        type_=ListNodePoolsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def create_node_pool(
        self,
        *,
        cluster_id: str,
        name: str,
        node_name_prefix: NodeNamePrefix,
        desired_node_count: int,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        machine_annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        machine_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_taints: typing.Optional[typing.Sequence[NodeTaint]] = OMIT,
        description: typing.Optional[str] = OMIT,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        nico: typing.Optional[NicoNodePoolProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NodePool]:
        """
        Creates a worker node pool and starts provisioning. The pool takes the
        cluster's Kubernetes version.

        Returns 400 for, among others: parent cluster not found; a duplicate
        pool name in the cluster; missing `nico.instanceTypeID`
        or `nico.release`; not exactly one of
        `subnetIDs` and `vpcPrefixIDs`; a pod CIDR too small for the requested
        nodes.

        Parameters
        ----------
        cluster_id : str
            Parent cluster.

        name : str
            Unique within the cluster. Immutable.

        node_name_prefix : NodeNamePrefix

        desired_node_count : int
            The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. Default 2Gi.

        machine_annotations : typing.Optional[typing.Dict[str, str]]
            Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        machine_labels : typing.Optional[typing.Dict[str, str]]
            Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        node_labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.

        node_taints : typing.Optional[typing.Sequence[NodeTaint]]
            Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.

        description : typing.Optional[str]
            Free-text description.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        nico : typing.Optional[NicoNodePoolProvider]

        launch_layer : typing.Optional[LaunchLayerNodePoolProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodePool]
            Node pool created; provisioning has started
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nodePools",
            method="POST",
            json={
                "clusterID": cluster_id,
                "name": name,
                "nodeNamePrefix": node_name_prefix,
                "systemReservedMemory": system_reserved_memory,
                "kubeReservedMemory": kube_reserved_memory,
                "machineAnnotations": machine_annotations,
                "machineLabels": machine_labels,
                "nodeLabels": node_labels,
                "nodeTaints": convert_and_respect_annotation_metadata(
                    object_=node_taints, annotation=typing.Sequence[NodeTaint], direction="write"
                ),
                "desiredNodeCount": desired_node_count,
                "description": description,
                "autoProvisionDisabled": auto_provision_disabled,
                "autoModeDisabled": auto_mode_disabled,
                "provisioningMonitorDisabled": provisioning_monitor_disabled,
                "recycleBudget": recycle_budget,
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoNodePoolProvider, direction="write"
                ),
                "launchLayer": convert_and_respect_annotation_metadata(
                    object_=launch_layer, annotation=LaunchLayerNodePoolProvider, direction="write"
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
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def get_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NodePool]:
        """
        Returns one node pool.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodePool]
            The requested node pool
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a node pool from a running cluster. Also returns 202, with no
        further effect, if the pool or its cluster is already being deleted.

        Returns 409 for a control-plane node pool while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
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

    async def update_node_pool(
        self,
        node_pool_id: str,
        *,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        desired_node_count: typing.Optional[int] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        max_surge: typing.Optional[int] = OMIT,
        kubernetes_version: typing.Optional[str] = OMIT,
        nico: typing.Optional[NicoNodePoolProviderUpdate] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProviderUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NodePool]:
        """
        All fields are optional. Changes to the Kubernetes version, release
        or other node configuration create a new NodeSet and roll the pool's
        nodes to it.

        Returns 400 for, among others: sending a field that is fixed at
        creation (for example `instanceTypeID`); `nico.release: ""`; any update
        to a control-plane node pool, which is configured through the cluster's
        `controlPlaneConfig` instead. That last refusal does not depend on the
        control-plane mutation lock, so retrying later does not help.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. An empty string restores the 2Gi default.

        description : typing.Optional[str]
            Free-text description.

        desired_node_count : typing.Optional[int]
            The desired number of nodes in the pool. Increasing aggregate control-plane capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        max_surge : typing.Optional[int]
            Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
            node is torn down before its replacement is provisioned.

        kubernetes_version : typing.Optional[str]
            Desired Kubernetes version for the pool's nodes, as X.Y.Z with no leading "v".
            Must be newer than the current version.

        nico : typing.Optional[NicoNodePoolProviderUpdate]

        launch_layer : typing.Optional[LaunchLayerNodePoolProviderUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NodePool]
            Update accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodePools/{encode_path_param(node_pool_id)}",
            method="PATCH",
            json={
                "autoProvisionDisabled": auto_provision_disabled,
                "autoModeDisabled": auto_mode_disabled,
                "provisioningMonitorDisabled": provisioning_monitor_disabled,
                "systemReservedMemory": system_reserved_memory,
                "kubeReservedMemory": kube_reserved_memory,
                "description": description,
                "desiredNodeCount": desired_node_count,
                "recycleBudget": recycle_budget,
                "maxSurge": max_surge,
                "kubernetesVersion": kubernetes_version,
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoNodePoolProviderUpdate, direction="write"
                ),
                "launchLayer": launch_layer,
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
                    NodePool,
                    parse_obj_as(
                        type_=NodePool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GenericError,
                        parse_obj_as(
                            type_=GenericError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
