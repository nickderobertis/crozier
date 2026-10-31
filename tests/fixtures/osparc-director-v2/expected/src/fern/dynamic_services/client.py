

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_project_inactivity_response import GetProjectInactivityResponse
from ..types.hardware_info import HardwareInfo
from ..types.pricing_info import PricingInfo
from ..types.retrieve_data_out_enveloped import RetrieveDataOutEnveloped
from ..types.running_dynamic_service_details import RunningDynamicServiceDetails
from ..types.user_id_int import UserIdInt
from ..types.wallet_info_input import WalletInfoInput
from .raw_client import AsyncRawDynamicServicesClient, RawDynamicServicesClient


OMIT = typing.cast(typing.Any, ...)


class DynamicServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDynamicServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDynamicServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDynamicServicesClient
        """
        return self._raw_client

    def list_tracked_dynamic_services(
        self,
        *,
        user_id: typing.Optional[UserIdInt] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        user_id : typing.Optional[UserIdInt]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RunningDynamicServiceDetails]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.list_tracked_dynamic_services()
        """
        _response = self._raw_client.list_tracked_dynamic_services(
            user_id=user_id, project_id=project_id, request_options=request_options
        )
        return _response.data

    def create_dynamic_service(
        self,
        *,
        dynamic_sidecar_request_dns: str,
        dynamic_sidecar_request_scheme: str,
        simcore_user_agent: str,
        service_key: str,
        service_version: str,
        user_id: UserIdInt,
        project_id: str,
        service_uuid: str,
        service_resources: typing.Dict[str, typing.Any],
        product_name: str,
        product_api_base_url: str,
        can_save: bool,
        service_basepath: typing.Optional[str] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        pricing_info: typing.Optional[PricingInfo] = OMIT,
        hardware_info: typing.Optional[HardwareInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunningDynamicServiceDetails:
        """
        Parameters
        ----------
        dynamic_sidecar_request_dns : str

        dynamic_sidecar_request_scheme : str

        simcore_user_agent : str

        service_key : str
            distinctive name for the node based on the docker registry path

        service_version : str
            semantic version number of the node

        user_id : UserIdInt

        project_id : str

        service_uuid : str

        service_resources : typing.Dict[str, typing.Any]

        product_name : str
            Current product name

        product_api_base_url : str
            Current product API base URL

        can_save : bool
            the service data must be saved when closing

        service_basepath : typing.Optional[str]
            predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        pricing_info : typing.Optional[PricingInfo]
            contains pricing information (ex. pricing plan and unit ids)

        hardware_info : typing.Optional[HardwareInfo]
            contains hardware information (ex. aws_ec2_instances)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDynamicServiceDetails
            Successful Response

        Examples
        --------
        from fern import FernApi, HardwareInfo, PricingInfo, WalletInfoInput

        client = FernApi()
        client.dynamic_services.create_dynamic_service(
            dynamic_sidecar_request_dns="x-dynamic-sidecar-request-dns",
            dynamic_sidecar_request_scheme="x-dynamic-sidecar-request-scheme",
            simcore_user_agent="x-simcore-user-agent",
            service_key="service_key",
            service_version="service_version",
            user_id=234,
            project_id="dd1d04d9-d704-4f7e-8f0f-1ca60cc771fe",
            service_uuid="service_uuid",
            service_resources={
                "container": {
                    "boot_modes": ["CPU"],
                    "image": "simcore/services/dynamic/jupyter-math:2.0.5",
                    "resources": {
                        "CPU": {"limit": 0.1, "reservation": 0.1},
                        "RAM": {"limit": 2147483648, "reservation": 2147483648},
                    },
                }
            },
            product_name="osparc",
            product_api_base_url="https://api.local/",
            can_save=True,
            wallet_info=WalletInfoInput(
                wallet_id=1,
                wallet_name="My Wallet",
                wallet_credit_amount="10",
            ),
            pricing_info=PricingInfo(
                pricing_plan_id=1,
                pricing_unit_id=1,
                pricing_unit_cost_id=1,
            ),
            hardware_info=HardwareInfo(
                aws_ec2instances=["c6a.4xlarge"],
            ),
        )
        """
        _response = self._raw_client.create_dynamic_service(
            dynamic_sidecar_request_dns=dynamic_sidecar_request_dns,
            dynamic_sidecar_request_scheme=dynamic_sidecar_request_scheme,
            simcore_user_agent=simcore_user_agent,
            service_key=service_key,
            service_version=service_version,
            user_id=user_id,
            project_id=project_id,
            service_uuid=service_uuid,
            service_resources=service_resources,
            product_name=product_name,
            product_api_base_url=product_api_base_url,
            can_save=can_save,
            service_basepath=service_basepath,
            wallet_info=wallet_info,
            pricing_info=pricing_info,
            hardware_info=hardware_info,
            request_options=request_options,
        )
        return _response.data

    def get_dynamic_sidecar_status(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningDynamicServiceDetails:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDynamicServiceDetails
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.get_dynamic_sidecar_status(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.get_dynamic_sidecar_status(node_uuid, request_options=request_options)
        return _response.data

    def stop_dynamic_service(
        self,
        node_uuid: str,
        *,
        can_save: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        can_save : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.stop_dynamic_service(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.stop_dynamic_service(node_uuid, can_save=can_save, request_options=request_options)
        return _response.data

    def service_retrieve_data_on_ports(
        self,
        node_uuid: str,
        *,
        port_keys: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveDataOutEnveloped:
        """
        Parameters
        ----------
        node_uuid : str

        port_keys : typing.Sequence[str]
            The port keys to retrieve data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDataOutEnveloped
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.service_retrieve_data_on_ports(
            node_uuid="node_uuid",
            port_keys=["port_keys"],
        )
        """
        _response = self._raw_client.service_retrieve_data_on_ports(
            node_uuid, port_keys=port_keys, request_options=request_options
        )
        return _response.data

    def service_restart_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.service_restart_containers(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.service_restart_containers(node_uuid, request_options=request_options)
        return _response.data

    def update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
            project_id="project_id",
        )
        """
        _response = self._raw_client.update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
            project_id, request_options=request_options
        )
        return _response.data

    def get_project_inactivity(
        self, project_id: str, *, max_inactivity_seconds: float, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectInactivityResponse:
        """
        Parameters
        ----------
        project_id : str

        max_inactivity_seconds : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectInactivityResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dynamic_services.get_project_inactivity(
            project_id="project_id",
            max_inactivity_seconds=1.1,
        )
        """
        _response = self._raw_client.get_project_inactivity(
            project_id, max_inactivity_seconds=max_inactivity_seconds, request_options=request_options
        )
        return _response.data


class AsyncDynamicServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDynamicServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDynamicServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDynamicServicesClient
        """
        return self._raw_client

    async def list_tracked_dynamic_services(
        self,
        *,
        user_id: typing.Optional[UserIdInt] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        user_id : typing.Optional[UserIdInt]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RunningDynamicServiceDetails]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.list_tracked_dynamic_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tracked_dynamic_services(
            user_id=user_id, project_id=project_id, request_options=request_options
        )
        return _response.data

    async def create_dynamic_service(
        self,
        *,
        dynamic_sidecar_request_dns: str,
        dynamic_sidecar_request_scheme: str,
        simcore_user_agent: str,
        service_key: str,
        service_version: str,
        user_id: UserIdInt,
        project_id: str,
        service_uuid: str,
        service_resources: typing.Dict[str, typing.Any],
        product_name: str,
        product_api_base_url: str,
        can_save: bool,
        service_basepath: typing.Optional[str] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        pricing_info: typing.Optional[PricingInfo] = OMIT,
        hardware_info: typing.Optional[HardwareInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunningDynamicServiceDetails:
        """
        Parameters
        ----------
        dynamic_sidecar_request_dns : str

        dynamic_sidecar_request_scheme : str

        simcore_user_agent : str

        service_key : str
            distinctive name for the node based on the docker registry path

        service_version : str
            semantic version number of the node

        user_id : UserIdInt

        project_id : str

        service_uuid : str

        service_resources : typing.Dict[str, typing.Any]

        product_name : str
            Current product name

        product_api_base_url : str
            Current product API base URL

        can_save : bool
            the service data must be saved when closing

        service_basepath : typing.Optional[str]
            predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        pricing_info : typing.Optional[PricingInfo]
            contains pricing information (ex. pricing plan and unit ids)

        hardware_info : typing.Optional[HardwareInfo]
            contains hardware information (ex. aws_ec2_instances)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDynamicServiceDetails
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HardwareInfo, PricingInfo, WalletInfoInput

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.create_dynamic_service(
                dynamic_sidecar_request_dns="x-dynamic-sidecar-request-dns",
                dynamic_sidecar_request_scheme="x-dynamic-sidecar-request-scheme",
                simcore_user_agent="x-simcore-user-agent",
                service_key="service_key",
                service_version="service_version",
                user_id=234,
                project_id="dd1d04d9-d704-4f7e-8f0f-1ca60cc771fe",
                service_uuid="service_uuid",
                service_resources={
                    "container": {
                        "boot_modes": ["CPU"],
                        "image": "simcore/services/dynamic/jupyter-math:2.0.5",
                        "resources": {
                            "CPU": {"limit": 0.1, "reservation": 0.1},
                            "RAM": {"limit": 2147483648, "reservation": 2147483648},
                        },
                    }
                },
                product_name="osparc",
                product_api_base_url="https://api.local/",
                can_save=True,
                wallet_info=WalletInfoInput(
                    wallet_id=1,
                    wallet_name="My Wallet",
                    wallet_credit_amount="10",
                ),
                pricing_info=PricingInfo(
                    pricing_plan_id=1,
                    pricing_unit_id=1,
                    pricing_unit_cost_id=1,
                ),
                hardware_info=HardwareInfo(
                    aws_ec2instances=["c6a.4xlarge"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dynamic_service(
            dynamic_sidecar_request_dns=dynamic_sidecar_request_dns,
            dynamic_sidecar_request_scheme=dynamic_sidecar_request_scheme,
            simcore_user_agent=simcore_user_agent,
            service_key=service_key,
            service_version=service_version,
            user_id=user_id,
            project_id=project_id,
            service_uuid=service_uuid,
            service_resources=service_resources,
            product_name=product_name,
            product_api_base_url=product_api_base_url,
            can_save=can_save,
            service_basepath=service_basepath,
            wallet_info=wallet_info,
            pricing_info=pricing_info,
            hardware_info=hardware_info,
            request_options=request_options,
        )
        return _response.data

    async def get_dynamic_sidecar_status(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunningDynamicServiceDetails:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunningDynamicServiceDetails
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.get_dynamic_sidecar_status(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dynamic_sidecar_status(node_uuid, request_options=request_options)
        return _response.data

    async def stop_dynamic_service(
        self,
        node_uuid: str,
        *,
        can_save: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        can_save : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.stop_dynamic_service(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_dynamic_service(
            node_uuid, can_save=can_save, request_options=request_options
        )
        return _response.data

    async def service_retrieve_data_on_ports(
        self,
        node_uuid: str,
        *,
        port_keys: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveDataOutEnveloped:
        """
        Parameters
        ----------
        node_uuid : str

        port_keys : typing.Sequence[str]
            The port keys to retrieve data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveDataOutEnveloped
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.service_retrieve_data_on_ports(
                node_uuid="node_uuid",
                port_keys=["port_keys"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_retrieve_data_on_ports(
            node_uuid, port_keys=port_keys, request_options=request_options
        )
        return _response.data

    async def service_restart_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.service_restart_containers(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_restart_containers(node_uuid, request_options=request_options)
        return _response.data

    async def update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
                project_id, request_options=request_options
            )
        )
        return _response.data

    async def get_project_inactivity(
        self, project_id: str, *, max_inactivity_seconds: float, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectInactivityResponse:
        """
        Parameters
        ----------
        project_id : str

        max_inactivity_seconds : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectInactivityResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dynamic_services.get_project_inactivity(
                project_id="project_id",
                max_inactivity_seconds=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_inactivity(
            project_id, max_inactivity_seconds=max_inactivity_seconds, request_options=request_options
        )
        return _response.data
