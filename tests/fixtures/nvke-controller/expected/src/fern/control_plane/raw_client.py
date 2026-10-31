

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.cluster_control_plane import ClusterControlPlane
from ..types.control_plane_config_history import ControlPlaneConfigHistory
from ..types.generic_error import GenericError
from pydantic import ValidationError


class RawControlPlaneClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_cluster_control_plane(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClusterControlPlane]:
        """
        Read-only view of the control plane: the persisted configuration plus
        aggregate runtime status (node counts, current Kubernetes version,
        rollout progress, and upgrade and recycling conditions). Change the
        control plane through `PATCH /clusters/{clusterID}`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClusterControlPlane]
            Control-plane configuration and status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/control-plane",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterControlPlane,
                    parse_obj_as(
                        type_=ClusterControlPlane,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_cluster_control_plane_config_history(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ControlPlaneConfigHistory]:
        """
        Returns the control-plane configuration change history, oldest first.
        Each entry shows which rollout-relevant fields changed relative to the
        previous snapshot. Use it to resolve the `pinnedConfigurationID` on each
        control-plane node and the cluster's desired `configurationId`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ControlPlaneConfigHistory]
            The control-plane config history
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/control-plane/configHistory",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ControlPlaneConfigHistory,
                    parse_obj_as(
                        type_=ControlPlaneConfigHistory,
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


class AsyncRawControlPlaneClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_cluster_control_plane(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClusterControlPlane]:
        """
        Read-only view of the control plane: the persisted configuration plus
        aggregate runtime status (node counts, current Kubernetes version,
        rollout progress, and upgrade and recycling conditions). Change the
        control plane through `PATCH /clusters/{clusterID}`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClusterControlPlane]
            Control-plane configuration and status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/control-plane",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterControlPlane,
                    parse_obj_as(
                        type_=ClusterControlPlane,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_cluster_control_plane_config_history(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ControlPlaneConfigHistory]:
        """
        Returns the control-plane configuration change history, oldest first.
        Each entry shows which rollout-relevant fields changed relative to the
        previous snapshot. Use it to resolve the `pinnedConfigurationID` on each
        control-plane node and the cluster's desired `configurationId`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ControlPlaneConfigHistory]
            The control-plane config history
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clusters/{encode_path_param(cluster_id)}/control-plane/configHistory",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ControlPlaneConfigHistory,
                    parse_obj_as(
                        type_=ControlPlaneConfigHistory,
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
