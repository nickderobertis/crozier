

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
from ..types.list_nodes_response import ListNodesResponse
from ..types.machine_health_issue import MachineHealthIssue
from ..types.node import Node
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_nodes(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        node_pool_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        control_plane: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListNodesResponse]:
        """
        Returns all nodes, filtered by the query parameters. All filters are exact match.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node name (exact match)

        control_plane : typing.Optional[bool]
            `true` returns only control-plane nodes; `false` only workers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListNodesResponse]
            A list of nodes
        """
        _response = self._client_wrapper.httpx_client.request(
            "nodes",
            method="GET",
            params={
                "clusterID": cluster_id,
                "nodePoolID": node_pool_id,
                "clusterName": cluster_name,
                "name": name,
                "controlPlane": control_plane,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNodesResponse,
                    parse_obj_as(
                        type_=ListNodesResponse,
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

    def get_node(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Node]:
        """
        Returns one node. Control-plane nodes do not belong to a node pool, so
        their `nodePoolID` and `nodeSetID` are the nil UUID. `nico` is omitted
        when none of its fields are set.

        Parameters
        ----------
        node_id : str
            Node ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Node]
            The requested node
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Node,
                    parse_obj_as(
                        type_=Node,
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

    def delete_node(
        self,
        node_id: str,
        *,
        machine_health_issue: typing.Optional[MachineHealthIssue] = OMIT,
        force_unreachable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a single node from a running cluster. Include a
        `machineHealthIssue` to flag the underlying machine for repair.

        For control-plane nodes, a delete sets `deleteRequested`; NVKE then
        starts teardowns one node at a time. `forceUnreachable` is applied
        automatically when the node is unhealthy.

        Also returns 202, with no further effect, if the node, pool or cluster
        is already being deleted or a delete is already requested.

        Returns 400 when deletion would leave no joined control-plane node or
        `machineHealthIssue` is invalid. Delete the cluster to remove its last
        joined control-plane node.
        Deleting a control-plane node requires controlPlaneVIP because the controller
        replaces it, unless allowControlPlaneWithoutVIP is enabled for development.
        Worker node deletion is unaffected.

        Returns 409 for a control-plane node while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_id : str
            Node ID.

        machine_health_issue : typing.Optional[MachineHealthIssue]

        force_unreachable : typing.Optional[bool]
            Treat the node as unreachable: graceful drain and shutdown are attempted, and
            failures are tolerated. Failures removing a control-plane node's etcd member are
            not tolerated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}",
            method="DELETE",
            json={
                "machineHealthIssue": convert_and_respect_annotation_metadata(
                    object_=machine_health_issue, annotation=MachineHealthIssue, direction="write"
                ),
                "forceUnreachable": force_unreachable,
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


class AsyncRawNodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_nodes(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        node_pool_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        control_plane: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListNodesResponse]:
        """
        Returns all nodes, filtered by the query parameters. All filters are exact match.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node name (exact match)

        control_plane : typing.Optional[bool]
            `true` returns only control-plane nodes; `false` only workers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListNodesResponse]
            A list of nodes
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nodes",
            method="GET",
            params={
                "clusterID": cluster_id,
                "nodePoolID": node_pool_id,
                "clusterName": cluster_name,
                "name": name,
                "controlPlane": control_plane,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNodesResponse,
                    parse_obj_as(
                        type_=ListNodesResponse,
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

    async def get_node(
        self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Node]:
        """
        Returns one node. Control-plane nodes do not belong to a node pool, so
        their `nodePoolID` and `nodeSetID` are the nil UUID. `nico` is omitted
        when none of its fields are set.

        Parameters
        ----------
        node_id : str
            Node ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Node]
            The requested node
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Node,
                    parse_obj_as(
                        type_=Node,
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

    async def delete_node(
        self,
        node_id: str,
        *,
        machine_health_issue: typing.Optional[MachineHealthIssue] = OMIT,
        force_unreachable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a single node from a running cluster. Include a
        `machineHealthIssue` to flag the underlying machine for repair.

        For control-plane nodes, a delete sets `deleteRequested`; NVKE then
        starts teardowns one node at a time. `forceUnreachable` is applied
        automatically when the node is unhealthy.

        Also returns 202, with no further effect, if the node, pool or cluster
        is already being deleted or a delete is already requested.

        Returns 400 when deletion would leave no joined control-plane node or
        `machineHealthIssue` is invalid. Delete the cluster to remove its last
        joined control-plane node.
        Deleting a control-plane node requires controlPlaneVIP because the controller
        replaces it, unless allowControlPlaneWithoutVIP is enabled for development.
        Worker node deletion is unaffected.

        Returns 409 for a control-plane node while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_id : str
            Node ID.

        machine_health_issue : typing.Optional[MachineHealthIssue]

        force_unreachable : typing.Optional[bool]
            Treat the node as unreachable: graceful drain and shutdown are attempted, and
            failures are tolerated. Failures removing a control-plane node's etcd member are
            not tolerated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"nodes/{encode_path_param(node_id)}",
            method="DELETE",
            json={
                "machineHealthIssue": convert_and_respect_annotation_metadata(
                    object_=machine_health_issue, annotation=MachineHealthIssue, direction="write"
                ),
                "forceUnreachable": force_unreachable,
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
