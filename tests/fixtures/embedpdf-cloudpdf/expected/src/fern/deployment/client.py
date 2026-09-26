

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deployment_license_status_response import DeploymentLicenseStatusResponse
from .raw_client import AsyncRawDeploymentClient, RawDeploymentClient


class DeploymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeploymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeploymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeploymentClient
        """
        return self._raw_client

    def license_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentLicenseStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentLicenseStatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.deployment.license_status()
        """
        _response = self._raw_client.license_status(request_options=request_options)
        return _response.data


class AsyncDeploymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeploymentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeploymentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeploymentClient
        """
        return self._raw_client

    async def license_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeploymentLicenseStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeploymentLicenseStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.deployment.license_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.license_status(request_options=request_options)
        return _response.data
