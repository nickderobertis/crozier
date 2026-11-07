

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.build_id import BuildId
from ..types.container_port import ContainerPort
from ..types.deployment import Deployment
from ..types.deployment_id import DeploymentId
from ..types.num_rooms_per_process import NumRoomsPerProcess
from ..types.plan_name import PlanName
from ..types.transport_type import TransportType
from .raw_client import AsyncRawDeploymentV1Client, RawDeploymentV1Client
from .types.deployment_config_env_item import DeploymentConfigEnvItem


OMIT = typing.cast(typing.Any, ...)


class DeploymentV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeploymentV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeploymentV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeploymentV1Client
        """
        return self._raw_client

    def get_deployments_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Deployment]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Deployment]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v1.get_deployments_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_deployments_deprecated(app_id, request_options=request_options)
        return _response.data

    def get_latest_deployment_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deployment:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v1.get_latest_deployment_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_latest_deployment_deprecated(app_id, request_options=request_options)
        return _response.data

    def get_deployment_info_deprecated(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deployment:
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
        Deployment
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v1.get_deployment_info_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            deployment_id=1,
        )
        """
        _response = self._raw_client.get_deployment_info_deprecated(
            app_id, deployment_id, request_options=request_options
        )
        return _response.data

    def create_deployment_deprecated(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        env: typing.Sequence[DeploymentConfigEnvItem],
        rooms_per_process: NumRoomsPerProcess,
        plan_name: PlanName,
        transport_type: TransportType,
        container_port: int,
        idle_timeout_enabled: typing.Optional[bool] = OMIT,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Deployment:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        env : typing.Sequence[DeploymentConfigEnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        plan_name : PlanName

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        idle_timeout_enabled : typing.Optional[bool]
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment


        Examples
        --------
        from fern.deployment_v1 import DeploymentConfigEnvItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.deployment_v1.create_deployment_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            build_id=1,
            env=[
                DeploymentConfigEnvItem(
                    value="TRUE",
                    name="EULA",
                )
            ],
            rooms_per_process=3,
            plan_name="tiny",
            transport_type="tcp",
            container_port=4000,
        )
        """
        _response = self._raw_client.create_deployment_deprecated(
            app_id,
            build_id,
            env=env,
            rooms_per_process=rooms_per_process,
            plan_name=plan_name,
            transport_type=transport_type,
            container_port=container_port,
            idle_timeout_enabled=idle_timeout_enabled,
            additional_container_ports=additional_container_ports,
            request_options=request_options,
        )
        return _response.data


class AsyncDeploymentV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeploymentV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeploymentV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeploymentV1Client
        """
        return self._raw_client

    async def get_deployments_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Deployment]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Deployment]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v1.get_deployments_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deployments_deprecated(app_id, request_options=request_options)
        return _response.data

    async def get_latest_deployment_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deployment:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v1.get_latest_deployment_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_deployment_deprecated(app_id, request_options=request_options)
        return _response.data

    async def get_deployment_info_deprecated(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deployment:
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
        Deployment
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v1.get_deployment_info_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                deployment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deployment_info_deprecated(
            app_id, deployment_id, request_options=request_options
        )
        return _response.data

    async def create_deployment_deprecated(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        env: typing.Sequence[DeploymentConfigEnvItem],
        rooms_per_process: NumRoomsPerProcess,
        plan_name: PlanName,
        transport_type: TransportType,
        container_port: int,
        idle_timeout_enabled: typing.Optional[bool] = OMIT,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Deployment:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        env : typing.Sequence[DeploymentConfigEnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        plan_name : PlanName

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        idle_timeout_enabled : typing.Optional[bool]
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment


        Examples
        --------
        import asyncio

        from fern.deployment_v1 import DeploymentConfigEnvItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.deployment_v1.create_deployment_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                build_id=1,
                env=[
                    DeploymentConfigEnvItem(
                        value="TRUE",
                        name="EULA",
                    )
                ],
                rooms_per_process=3,
                plan_name="tiny",
                transport_type="tcp",
                container_port=4000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_deployment_deprecated(
            app_id,
            build_id,
            env=env,
            rooms_per_process=rooms_per_process,
            plan_name=plan_name,
            transport_type=transport_type,
            container_port=container_port,
            idle_timeout_enabled=idle_timeout_enabled,
            additional_container_ports=additional_container_ports,
            request_options=request_options,
        )
        return _response.data
