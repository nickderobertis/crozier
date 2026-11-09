

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.build_id import BuildId
from ..types.container_port import ContainerPort
from ..types.deployment_id import DeploymentId
from ..types.deployment_v2 import DeploymentV2
from ..types.num_rooms_per_process import NumRoomsPerProcess
from ..types.transport_type import TransportType
from .raw_client import AsyncRawDeploymentV2Client, RawDeploymentV2Client
from .types.deployment_config_v2env_item import DeploymentConfigV2EnvItem


OMIT = typing.cast(typing.Any, ...)


class DeploymentV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeploymentV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeploymentV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeploymentV2Client
        """
        return self._raw_client

    def get_deployments(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeploymentV2]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeploymentV2]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v2.get_deployments(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_deployments(app_id, request_options=request_options)
        return _response.data

    def get_latest_deployment(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentV2:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v2.get_latest_deployment(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_latest_deployment(app_id, request_options=request_options)
        return _response.data

    def get_deployment_info(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentV2:
        """
        Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v2.get_deployment_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            deployment_id=1,
        )
        """
        _response = self._raw_client.get_deployment_info(app_id, deployment_id, request_options=request_options)
        return _response.data

    def create_deployment(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        idle_timeout_enabled: bool,
        env: typing.Sequence[DeploymentConfigV2EnvItem],
        rooms_per_process: NumRoomsPerProcess,
        transport_type: TransportType,
        container_port: int,
        requested_memory_mb: float,
        requested_cpu: float,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeploymentV2:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        idle_timeout_enabled : bool
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        env : typing.Sequence[DeploymentConfigV2EnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        requested_memory_mb : float
            The amount of memory allocated to your process.

        requested_cpu : float
            The number of cores allocated to your process.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2


        Examples
        --------
        from fern.deployment_v2 import DeploymentConfigV2EnvItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v2.create_deployment(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            build_id=1,
            idle_timeout_enabled=True,
            env=[
                DeploymentConfigV2EnvItem(
                    value="TRUE",
                    name="EULA",
                )
            ],
            rooms_per_process=3,
            transport_type="tcp",
            container_port=4000,
            requested_memory_mb=1024.0,
            requested_cpu=0.5,
        )
        """
        _response = self._raw_client.create_deployment(
            app_id,
            build_id,
            idle_timeout_enabled=idle_timeout_enabled,
            env=env,
            rooms_per_process=rooms_per_process,
            transport_type=transport_type,
            container_port=container_port,
            requested_memory_mb=requested_memory_mb,
            requested_cpu=requested_cpu,
            additional_container_ports=additional_container_ports,
            request_options=request_options,
        )
        return _response.data


class AsyncDeploymentV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeploymentV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeploymentV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeploymentV2Client
        """
        return self._raw_client

    async def get_deployments(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeploymentV2]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeploymentV2]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v2.get_deployments(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deployments(app_id, request_options=request_options)
        return _response.data

    async def get_latest_deployment(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentV2:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v2.get_latest_deployment(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_deployment(app_id, request_options=request_options)
        return _response.data

    async def get_deployment_info(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentV2:
        """
        Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v2.get_deployment_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                deployment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deployment_info(app_id, deployment_id, request_options=request_options)
        return _response.data

    async def create_deployment(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        idle_timeout_enabled: bool,
        env: typing.Sequence[DeploymentConfigV2EnvItem],
        rooms_per_process: NumRoomsPerProcess,
        transport_type: TransportType,
        container_port: int,
        requested_memory_mb: float,
        requested_cpu: float,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeploymentV2:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        idle_timeout_enabled : bool
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        env : typing.Sequence[DeploymentConfigV2EnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        requested_memory_mb : float
            The amount of memory allocated to your process.

        requested_cpu : float
            The number of cores allocated to your process.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentV2


        Examples
        --------
        import asyncio

        from fern.deployment_v2 import DeploymentConfigV2EnvItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v2.create_deployment(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                build_id=1,
                idle_timeout_enabled=True,
                env=[
                    DeploymentConfigV2EnvItem(
                        value="TRUE",
                        name="EULA",
                    )
                ],
                rooms_per_process=3,
                transport_type="tcp",
                container_port=4000,
                requested_memory_mb=1024.0,
                requested_cpu=0.5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_deployment(
            app_id,
            build_id,
            idle_timeout_enabled=idle_timeout_enabled,
            env=env,
            rooms_per_process=rooms_per_process,
            transport_type=transport_type,
            container_port=container_port,
            requested_memory_mb=requested_memory_mb,
            requested_cpu=requested_cpu,
            additional_container_ports=additional_container_ports,
            request_options=request_options,
        )
        return _response.data
