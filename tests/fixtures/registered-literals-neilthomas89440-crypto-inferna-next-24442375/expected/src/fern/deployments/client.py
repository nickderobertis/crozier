

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deployment_out import DeploymentOut
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

    def list_deployments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeploymentOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeploymentOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.list_deployments()
        """
        _response = self._raw_client.list_deployments(request_options=request_options)
        return _response.data

    def scale_deployment(
        self, deployment_id: str, *, replicas: int, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentOut:
        """
        Parameters
        ----------
        deployment_id : str

        replicas : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.scale_deployment(
            deployment_id="deployment_id",
            replicas=1,
        )
        """
        _response = self._raw_client.scale_deployment(deployment_id, replicas=replicas, request_options=request_options)
        return _response.data

    def delete_deployment(self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        deployment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployments.delete_deployment(
            deployment_id="deployment_id",
        )
        """
        _response = self._raw_client.delete_deployment(deployment_id, request_options=request_options)
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

    async def list_deployments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeploymentOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeploymentOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.list_deployments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_deployments(request_options=request_options)
        return _response.data

    async def scale_deployment(
        self, deployment_id: str, *, replicas: int, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentOut:
        """
        Parameters
        ----------
        deployment_id : str

        replicas : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.scale_deployment(
                deployment_id="deployment_id",
                replicas=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scale_deployment(
            deployment_id, replicas=replicas, request_options=request_options
        )
        return _response.data

    async def delete_deployment(
        self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        deployment_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployments.delete_deployment(
                deployment_id="deployment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_deployment(deployment_id, request_options=request_options)
        return _response.data
