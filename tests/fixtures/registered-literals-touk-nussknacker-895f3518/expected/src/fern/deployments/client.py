

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_deployment_status_response import GetDeploymentStatusResponse
from ..types.map_node_id_string import MapNodeIdString
from ..types.ui_action_parameters_dto import UiActionParametersDto
from .raw_client import AsyncRawDeploymentsClient, RawDeploymentsClient


OMIT = typing.cast(typing.Any, ...)


class DeploymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeploymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeploymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeploymentsClient
        """
        return self._raw_client

    def get_api_actioninfo_scenarioname_parameters(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UiActionParametersDto:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiActionParametersDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.get_api_actioninfo_scenarioname_parameters(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_actioninfo_scenarioname_parameters(
            scenario_name, request_options=request_options
        )
        return _response.data

    def get_api_deployments_deploymentid_status(
        self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeploymentStatusResponse:
        """
        Parameters
        ----------
        deployment_id : str
            Identifier in the UUID format that will be used for the verification of deployment's status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeploymentStatusResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.get_api_deployments_deploymentid_status(
            deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
        )
        """
        _response = self._raw_client.get_api_deployments_deploymentid_status(
            deployment_id, request_options=request_options
        )
        return _response.data

    def put_api_deployments_deploymentid(
        self,
        deployment_id: str,
        *,
        scenario_name: str,
        nodes_deployment_data: MapNodeIdString,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        deployment_id : str
            Identifier in the UUID format that will be used for the verification of deployment's status

        scenario_name : str

        nodes_deployment_data : MapNodeIdString

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.put_api_deployments_deploymentid(
            deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
            scenario_name="scenario1",
            nodes_deployment_data={"sourceNodeId1": "field1 = 'value'"},
        )
        """
        _response = self._raw_client.put_api_deployments_deploymentid(
            deployment_id,
            scenario_name=scenario_name,
            nodes_deployment_data=nodes_deployment_data,
            comment=comment,
            request_options=request_options,
        )
        return _response.data


class AsyncDeploymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeploymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeploymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeploymentsClient
        """
        return self._raw_client

    async def get_api_actioninfo_scenarioname_parameters(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UiActionParametersDto:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UiActionParametersDto


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.get_api_actioninfo_scenarioname_parameters(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_actioninfo_scenarioname_parameters(
            scenario_name, request_options=request_options
        )
        return _response.data

    async def get_api_deployments_deploymentid_status(
        self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeploymentStatusResponse:
        """
        Parameters
        ----------
        deployment_id : str
            Identifier in the UUID format that will be used for the verification of deployment's status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeploymentStatusResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.get_api_deployments_deploymentid_status(
                deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_deployments_deploymentid_status(
            deployment_id, request_options=request_options
        )
        return _response.data

    async def put_api_deployments_deploymentid(
        self,
        deployment_id: str,
        *,
        scenario_name: str,
        nodes_deployment_data: MapNodeIdString,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        deployment_id : str
            Identifier in the UUID format that will be used for the verification of deployment's status

        scenario_name : str

        nodes_deployment_data : MapNodeIdString

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.put_api_deployments_deploymentid(
                deployment_id="a9a1e269-0b71-4582-a948-603482d27298",
                scenario_name="scenario1",
                nodes_deployment_data={"sourceNodeId1": "field1 = 'value'"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_deployments_deploymentid(
            deployment_id,
            scenario_name=scenario_name,
            nodes_deployment_data=nodes_deployment_data,
            comment=comment,
            request_options=request_options,
        )
        return _response.data
