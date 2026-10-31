

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
from ..types.cluster import Cluster
from ..types.cluster_network_create_config import ClusterNetworkCreateConfig
from ..types.cluster_spire_server_status import ClusterSpireServerStatus
from ..types.create_cluster_control_plane_config import CreateClusterControlPlaneConfig
from ..types.generic_error import GenericError
from ..types.launch_layer_cluster_provider import LaunchLayerClusterProvider
from ..types.list_clusters_response import ListClustersResponse
from ..types.nico_cluster_provider import NicoClusterProvider
from ..types.node_pool_create_config import NodePoolCreateConfig
from ..types.update_cluster_control_plane_config import UpdateClusterControlPlaneConfig
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClustersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_clusters(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListClustersResponse]:
        """
        Returns all clusters, or the cluster whose name matches `name`.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter clusters by name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListClustersResponse]
            A list of clusters
        """
        _response = self._client_wrapper.httpx_client.request(
            "clusters",
            method="GET",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListClustersResponse,
                    parse_obj_as(
                        type_=ListClustersResponse,
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

    def create_cluster(
        self,
        *,
        name: str,
        control_plane_kubernetes_version: str,
        etcd_encrypted: bool,
        control_plane_vip: typing.Optional[str] = OMIT,
        network: typing.Optional[ClusterNetworkCreateConfig] = OMIT,
        node_pools: typing.Optional[typing.Sequence[NodePoolCreateConfig]] = OMIT,
        control_plane_config: typing.Optional[CreateClusterControlPlaneConfig] = OMIT,
        nico: typing.Optional[NicoClusterProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerClusterProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Cluster]:
        """
        Creates a cluster and starts provisioning. The cluster is returned before
        provisioning completes.

        Returns 400 for, among others: a duplicate cluster name; missing
        `nico.orgID`, `siteID` or `vpcID`; an unsupported `cniPlugin`; a
        missing `controlPlaneConfig.nico.release`; a
        control-plane `maxSurge` greater than 1; a pod CIDR too small for the
        requested nodes plus surge; a `controlPlaneVIP` inside the pod or
        service CIDR.

        Parameters
        ----------
        name : str
            Cluster name. Lowercase DNS label, unique per management plane. Node names are derived from it.

        control_plane_kubernetes_version : str
            Kubernetes version for the cluster, as X.Y.Z with no leading "v".

        etcd_encrypted : bool
            Encrypt etcd at rest. Can be turned on later with `enableEtcdEncryption`; cannot be turned off.

        control_plane_vip : typing.Optional[str]
            Virtual IP for the API server through kube-vip. Omit to skip kube-vip and
            use the first control-plane node's IP as the API server endpoint. Must not
            fall inside the pod or service CIDR. An explicit empty string is rejected.
            By default, a cluster without a VIP must have exactly one desired
            control-plane node. Scale-up above one node, upgrades and node replacement
            require a VIP unless the controller deployment enables the development-only
            allowControlPlaneWithoutVIP setting. That override keeps the initializing
            node's IP as the endpoint; replacing that node can break API access.
            Quorum, health and deletion protections still apply.

        network : typing.Optional[ClusterNetworkCreateConfig]

        node_pools : typing.Optional[typing.Sequence[NodePoolCreateConfig]]
            Initial worker node pools.

        control_plane_config : typing.Optional[CreateClusterControlPlaneConfig]

        nico : typing.Optional[NicoClusterProvider]

        launch_layer : typing.Optional[LaunchLayerClusterProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cluster]
            Cluster created; provisioning has started
        """
        _response = self._client_wrapper.httpx_client.request(
            "clusters",
            method="POST",
            json={
                "name": name,
                "controlPlaneKubernetesVersion": control_plane_kubernetes_version,
                "etcdEncrypted": etcd_encrypted,
                "controlPlaneVIP": control_plane_vip,
                "network": convert_and_respect_annotation_metadata(
                    object_=network, annotation=ClusterNetworkCreateConfig, direction="write"
                ),
                "nodePools": convert_and_respect_annotation_metadata(
                    object_=node_pools, annotation=typing.Sequence[NodePoolCreateConfig], direction="write"
                ),
                "controlPlaneConfig": convert_and_respect_annotation_metadata(
                    object_=control_plane_config, annotation=CreateClusterControlPlaneConfig, direction="write"
                ),
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoClusterProvider, direction="write"
                ),
                "launchLayer": convert_and_respect_annotation_metadata(
                    object_=launch_layer, annotation=LaunchLayerClusterProvider, direction="write"
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_cluster(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Cluster]:
        """
        Returns one cluster. Once provisioning finishes, `conditions.provisioning`
        is False and `conditions.provisioned` is True.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cluster]
            The requested cluster
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    def delete_cluster(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Starts deletion and sets `conditions.deleting` to `True`. A cluster can
        be deleted in any state, including while it is provisioning or
        upgrading. Deletion takes precedence over an in-progress or retained
        etcd encryption, etcd key rotation or certificate renewal.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def update_cluster(
        self,
        cluster_id: str,
        *,
        enable_cp_node_recycling: typing.Optional[bool] = OMIT,
        control_plane_kubernetes_version: typing.Optional[str] = OMIT,
        enable_etcd_encryption: typing.Optional[bool] = OMIT,
        enable_oidc: typing.Optional[bool] = OMIT,
        control_plane_config: typing.Optional[UpdateClusterControlPlaneConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Cluster]:
        """
        All fields are optional. See the API description for merge rules.

        Returns 400 for, among others: a Kubernetes downgrade, major-version
        change, or a jump of more than one minor version; an upgrade that would
        leave a worker pool more than 3 minor versions behind;
        `enableEtcdEncryption: false` or `enableOidc: false`; combining OIDC or
        etcd enablement with a version upgrade; etcd or OIDC enablement on a
        cluster that is not provisioned or is deleting; any `network` value;
        a control-plane `maxSurge` greater than 1.

        Returns 409 when another mutually exclusive cluster operation is in
        progress (`etcd_encryption`, `etcd_key_rotation`, `k8s_upgrade`,
        `cp_nodes_recycling`, `oidc_enable`, `certificate_renewal`), or the
        control plane is upgrading or recycling nodes. A failed certificate
        renewal can retain the lock until an operator clears it; see the
        retained-lock recovery procedure in
        controller/docs/certificate-renewal.md. A rotation that fails after
        `prepare` keeps the `etcd_key_rotation` lock until its workflow is
        reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        enable_cp_node_recycling : typing.Optional[bool]
            Turn automatic control-plane node replacement on or off.

        control_plane_kubernetes_version : typing.Optional[str]
            Target control-plane version, as X.Y.Z with no leading "v". Must be newer than
            the current version by at most one minor version and keep every worker pool
            within 3 minor versions.
            The cluster must have controlPlaneVIP configured unless the development-only
            allowControlPlaneWithoutVIP setting is enabled.

        enable_etcd_encryption : typing.Optional[bool]
            `true` starts one-way etcd encryption on a provisioned cluster. `false` is
            rejected. `true` on an already-encrypted cluster does nothing. Other updates
            return 409 while it runs.

        enable_oidc : typing.Optional[bool]
            `true` starts one-way OIDC authentication enablement. `false` is rejected.
            Cannot be combined with a control-plane upgrade or etcd enablement. Other
            updates return 409 while it runs.

        control_plane_config : typing.Optional[UpdateClusterControlPlaneConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cluster]
            Update accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="PATCH",
            json={
                "enableCPNodeRecycling": enable_cp_node_recycling,
                "controlPlaneKubernetesVersion": control_plane_kubernetes_version,
                "enableEtcdEncryption": enable_etcd_encryption,
                "enableOidc": enable_oidc,
                "controlPlaneConfig": convert_and_respect_annotation_metadata(
                    object_=control_plane_config, annotation=UpdateClusterControlPlaneConfig, direction="write"
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    def get_cluster_spire_server(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClusterSpireServerStatus]:
        """
        Returns the SPIRE server last requested through
        `PATCH /clusters/{clusterID}/spire-server`, and for each node the
        server its SPIRE agent points at and whether the agent holds a valid
        X.509 SVID from it. Node status is read live from each node agent on
        every call; an unreachable node is reported with `reachable: false`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClusterSpireServerStatus]
            Requested server and live per-node SPIRE agent status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/spire-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterSpireServerStatus,
                    parse_obj_as(
                        type_=ClusterSpireServerStatus,
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

    def update_cluster_spire_server(
        self, cluster_id: str, *, address: str, port: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Starts a `spire_server_update` operation that points the SPIRE agent on
        every node of the cluster at the given server and waits for each agent
        to hold an SVID from it. Track it through `conditions.updateInProgress`
        and `conditions.updateFailed` on the cluster, and per node through
        `GET /clusters/{clusterID}/spire-server`. Repeating the request with
        the same server is safe, including while it is in progress.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        address : str
            Host name or IP address of the SPIRE server.

        port : int
            SPIRE server port.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/spire-server",
            method="PATCH",
            json={
                "address": address,
                "port": port,
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


class AsyncRawClustersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_clusters(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListClustersResponse]:
        """
        Returns all clusters, or the cluster whose name matches `name`.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter clusters by name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListClustersResponse]
            A list of clusters
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clusters",
            method="GET",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListClustersResponse,
                    parse_obj_as(
                        type_=ListClustersResponse,
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

    async def create_cluster(
        self,
        *,
        name: str,
        control_plane_kubernetes_version: str,
        etcd_encrypted: bool,
        control_plane_vip: typing.Optional[str] = OMIT,
        network: typing.Optional[ClusterNetworkCreateConfig] = OMIT,
        node_pools: typing.Optional[typing.Sequence[NodePoolCreateConfig]] = OMIT,
        control_plane_config: typing.Optional[CreateClusterControlPlaneConfig] = OMIT,
        nico: typing.Optional[NicoClusterProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerClusterProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Cluster]:
        """
        Creates a cluster and starts provisioning. The cluster is returned before
        provisioning completes.

        Returns 400 for, among others: a duplicate cluster name; missing
        `nico.orgID`, `siteID` or `vpcID`; an unsupported `cniPlugin`; a
        missing `controlPlaneConfig.nico.release`; a
        control-plane `maxSurge` greater than 1; a pod CIDR too small for the
        requested nodes plus surge; a `controlPlaneVIP` inside the pod or
        service CIDR.

        Parameters
        ----------
        name : str
            Cluster name. Lowercase DNS label, unique per management plane. Node names are derived from it.

        control_plane_kubernetes_version : str
            Kubernetes version for the cluster, as X.Y.Z with no leading "v".

        etcd_encrypted : bool
            Encrypt etcd at rest. Can be turned on later with `enableEtcdEncryption`; cannot be turned off.

        control_plane_vip : typing.Optional[str]
            Virtual IP for the API server through kube-vip. Omit to skip kube-vip and
            use the first control-plane node's IP as the API server endpoint. Must not
            fall inside the pod or service CIDR. An explicit empty string is rejected.
            By default, a cluster without a VIP must have exactly one desired
            control-plane node. Scale-up above one node, upgrades and node replacement
            require a VIP unless the controller deployment enables the development-only
            allowControlPlaneWithoutVIP setting. That override keeps the initializing
            node's IP as the endpoint; replacing that node can break API access.
            Quorum, health and deletion protections still apply.

        network : typing.Optional[ClusterNetworkCreateConfig]

        node_pools : typing.Optional[typing.Sequence[NodePoolCreateConfig]]
            Initial worker node pools.

        control_plane_config : typing.Optional[CreateClusterControlPlaneConfig]

        nico : typing.Optional[NicoClusterProvider]

        launch_layer : typing.Optional[LaunchLayerClusterProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cluster]
            Cluster created; provisioning has started
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clusters",
            method="POST",
            json={
                "name": name,
                "controlPlaneKubernetesVersion": control_plane_kubernetes_version,
                "etcdEncrypted": etcd_encrypted,
                "controlPlaneVIP": control_plane_vip,
                "network": convert_and_respect_annotation_metadata(
                    object_=network, annotation=ClusterNetworkCreateConfig, direction="write"
                ),
                "nodePools": convert_and_respect_annotation_metadata(
                    object_=node_pools, annotation=typing.Sequence[NodePoolCreateConfig], direction="write"
                ),
                "controlPlaneConfig": convert_and_respect_annotation_metadata(
                    object_=control_plane_config, annotation=CreateClusterControlPlaneConfig, direction="write"
                ),
                "nico": convert_and_respect_annotation_metadata(
                    object_=nico, annotation=NicoClusterProvider, direction="write"
                ),
                "launchLayer": convert_and_respect_annotation_metadata(
                    object_=launch_layer, annotation=LaunchLayerClusterProvider, direction="write"
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_cluster(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Cluster]:
        """
        Returns one cluster. Once provisioning finishes, `conditions.provisioning`
        is False and `conditions.provisioned` is True.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cluster]
            The requested cluster
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    async def delete_cluster(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Starts deletion and sets `conditions.deleting` to `True`. A cluster can
        be deleted in any state, including while it is provisioning or
        upgrading. Deletion takes precedence over an in-progress or retained
        etcd encryption, etcd key rotation or certificate renewal.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def update_cluster(
        self,
        cluster_id: str,
        *,
        enable_cp_node_recycling: typing.Optional[bool] = OMIT,
        control_plane_kubernetes_version: typing.Optional[str] = OMIT,
        enable_etcd_encryption: typing.Optional[bool] = OMIT,
        enable_oidc: typing.Optional[bool] = OMIT,
        control_plane_config: typing.Optional[UpdateClusterControlPlaneConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Cluster]:
        """
        All fields are optional. See the API description for merge rules.

        Returns 400 for, among others: a Kubernetes downgrade, major-version
        change, or a jump of more than one minor version; an upgrade that would
        leave a worker pool more than 3 minor versions behind;
        `enableEtcdEncryption: false` or `enableOidc: false`; combining OIDC or
        etcd enablement with a version upgrade; etcd or OIDC enablement on a
        cluster that is not provisioned or is deleting; any `network` value;
        a control-plane `maxSurge` greater than 1.

        Returns 409 when another mutually exclusive cluster operation is in
        progress (`etcd_encryption`, `etcd_key_rotation`, `k8s_upgrade`,
        `cp_nodes_recycling`, `oidc_enable`, `certificate_renewal`), or the
        control plane is upgrading or recycling nodes. A failed certificate
        renewal can retain the lock until an operator clears it; see the
        retained-lock recovery procedure in
        controller/docs/certificate-renewal.md. A rotation that fails after
        `prepare` keeps the `etcd_key_rotation` lock until its workflow is
        reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        enable_cp_node_recycling : typing.Optional[bool]
            Turn automatic control-plane node replacement on or off.

        control_plane_kubernetes_version : typing.Optional[str]
            Target control-plane version, as X.Y.Z with no leading "v". Must be newer than
            the current version by at most one minor version and keep every worker pool
            within 3 minor versions.
            The cluster must have controlPlaneVIP configured unless the development-only
            allowControlPlaneWithoutVIP setting is enabled.

        enable_etcd_encryption : typing.Optional[bool]
            `true` starts one-way etcd encryption on a provisioned cluster. `false` is
            rejected. `true` on an already-encrypted cluster does nothing. Other updates
            return 409 while it runs.

        enable_oidc : typing.Optional[bool]
            `true` starts one-way OIDC authentication enablement. `false` is rejected.
            Cannot be combined with a control-plane upgrade or etcd enablement. Other
            updates return 409 while it runs.

        control_plane_config : typing.Optional[UpdateClusterControlPlaneConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cluster]
            Update accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}",
            method="PATCH",
            json={
                "enableCPNodeRecycling": enable_cp_node_recycling,
                "controlPlaneKubernetesVersion": control_plane_kubernetes_version,
                "enableEtcdEncryption": enable_etcd_encryption,
                "enableOidc": enable_oidc,
                "controlPlaneConfig": convert_and_respect_annotation_metadata(
                    object_=control_plane_config, annotation=UpdateClusterControlPlaneConfig, direction="write"
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    async def get_cluster_spire_server(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClusterSpireServerStatus]:
        """
        Returns the SPIRE server last requested through
        `PATCH /clusters/{clusterID}/spire-server`, and for each node the
        server its SPIRE agent points at and whether the agent holds a valid
        X.509 SVID from it. Node status is read live from each node agent on
        every call; an unreachable node is reported with `reachable: false`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClusterSpireServerStatus]
            Requested server and live per-node SPIRE agent status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/spire-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterSpireServerStatus,
                    parse_obj_as(
                        type_=ClusterSpireServerStatus,
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

    async def update_cluster_spire_server(
        self, cluster_id: str, *, address: str, port: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Starts a `spire_server_update` operation that points the SPIRE agent on
        every node of the cluster at the given server and waits for each agent
        to hold an SVID from it. Track it through `conditions.updateInProgress`
        and `conditions.updateFailed` on the cluster, and per node through
        `GET /clusters/{clusterID}/spire-server`. Repeating the request with
        the same server is safe, including while it is in progress.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        address : str
            Host name or IP address of the SPIRE server.

        port : int
            SPIRE server port.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/spire-server",
            method="PATCH",
            json={
                "address": address,
                "port": port,
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
