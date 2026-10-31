

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cluster_control_plane import ClusterControlPlane
from ..types.control_plane_config_history import ControlPlaneConfigHistory
from .raw_client import AsyncRawControlPlaneClient, RawControlPlaneClient


class ControlPlaneClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawControlPlaneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawControlPlaneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawControlPlaneClient
        """
        return self._raw_client

    def get_cluster_control_plane(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterControlPlane:
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
        ClusterControlPlane
            Control-plane configuration and status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.control_plane.get_cluster_control_plane(
            cluster_id="clusterID",
        )
        """
        _response = self._raw_client.get_cluster_control_plane(cluster_id, request_options=request_options)
        return _response.data

    def get_cluster_control_plane_config_history(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ControlPlaneConfigHistory:
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
        ControlPlaneConfigHistory
            The control-plane config history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.control_plane.get_cluster_control_plane_config_history(
            cluster_id="clusterID",
        )
        """
        _response = self._raw_client.get_cluster_control_plane_config_history(
            cluster_id, request_options=request_options
        )
        return _response.data


class AsyncControlPlaneClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawControlPlaneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawControlPlaneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawControlPlaneClient
        """
        return self._raw_client

    async def get_cluster_control_plane(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterControlPlane:
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
        ClusterControlPlane
            Control-plane configuration and status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.control_plane.get_cluster_control_plane(
                cluster_id="clusterID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cluster_control_plane(cluster_id, request_options=request_options)
        return _response.data

    async def get_cluster_control_plane_config_history(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ControlPlaneConfigHistory:
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
        ControlPlaneConfigHistory
            The control-plane config history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.control_plane.get_cluster_control_plane_config_history(
                cluster_id="clusterID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cluster_control_plane_config_history(
            cluster_id, request_options=request_options
        )
        return _response.data
