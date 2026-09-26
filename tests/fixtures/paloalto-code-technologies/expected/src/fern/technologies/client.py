

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_response import GetResponse
from ..types.ivcs_installed_app import IvcsInstalledApp
from ..types.ivcs_webhook import IvcsWebhook
from ..types.parsed_inventory import ParsedInventory
from .raw_client import AsyncRawTechnologiesClient, RawTechnologiesClient


class TechnologiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTechnologiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTechnologiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTechnologiesClient
        """
        return self._raw_client

    def get_apps(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[IvcsInstalledApp]:
        """
        Get an inventory of third-party applications (apps) found in your organization's version control system (VCS).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IvcsInstalledApp]
            apps

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.technologies.get_apps()
        """
        _response = self._raw_client.get_apps(request_options=request_options)
        return _response.data

    def get_webhooks(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[IvcsWebhook]:
        """
        Get an inventory of third-party webhooks found in your organization’s version control system (VCS).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IvcsWebhook]
            webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.technologies.get_webhooks()
        """
        _response = self._raw_client.get_webhooks(request_options=request_options)
        return _response.data

    def assets_inventory_get_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetResponse:
        """
        List all technologies and their sources

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponse
            Get assets inventory

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.technologies.assets_inventory_get_all()
        """
        _response = self._raw_client.assets_inventory_get_all(request_options=request_options)
        return _response.data

    def get_ci_inventory(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ParsedInventory]:
        """
        Get an inventory of all third-party services and tools used by an organization’s CI/CD pipeline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ParsedInventory]
            pipeline tools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.technologies.get_ci_inventory()
        """
        _response = self._raw_client.get_ci_inventory(request_options=request_options)
        return _response.data


class AsyncTechnologiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTechnologiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTechnologiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTechnologiesClient
        """
        return self._raw_client

    async def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IvcsInstalledApp]:
        """
        Get an inventory of third-party applications (apps) found in your organization's version control system (VCS).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IvcsInstalledApp]
            apps

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.technologies.get_apps()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps(request_options=request_options)
        return _response.data

    async def get_webhooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IvcsWebhook]:
        """
        Get an inventory of third-party webhooks found in your organization’s version control system (VCS).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IvcsWebhook]
            webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.technologies.get_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(request_options=request_options)
        return _response.data

    async def assets_inventory_get_all(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetResponse:
        """
        List all technologies and their sources

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetResponse
            Get assets inventory

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.technologies.assets_inventory_get_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.assets_inventory_get_all(request_options=request_options)
        return _response.data

    async def get_ci_inventory(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ParsedInventory]:
        """
        Get an inventory of all third-party services and tools used by an organization’s CI/CD pipeline.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ParsedInventory]
            pipeline tools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.technologies.get_ci_inventory()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ci_inventory(request_options=request_options)
        return _response.data
