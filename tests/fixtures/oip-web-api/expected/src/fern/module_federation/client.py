

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.module_federation_dto import ModuleFederationDto
from .raw_client import AsyncRawModuleFederationClient, RawModuleFederationClient


OMIT = typing.cast(typing.Any, ...)


class ModuleFederationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModuleFederationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModuleFederationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModuleFederationClient
        """
        return self._raw_client

    def get_manifest_for_client_app(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ModuleFederationDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ModuleFederationDto]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.module_federation.get_manifest_for_client_app()
        """
        _response = self._raw_client.get_manifest_for_client_app(request_options=request_options)
        return _response.data

    def registry_module(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        remote_entry: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        export_module: typing.Optional[ModuleFederationDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            See 'name' in webpack.config.js

        remote_entry : typing.Optional[str]
            Remote entry

        base_url : typing.Optional[str]
            Base Url

        export_module : typing.Optional[ModuleFederationDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.module_federation.registry_module()
        """
        _response = self._raw_client.registry_module(
            name=name,
            remote_entry=remote_entry,
            base_url=base_url,
            export_module=export_module,
            request_options=request_options,
        )
        return _response.data


class AsyncModuleFederationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModuleFederationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModuleFederationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModuleFederationClient
        """
        return self._raw_client

    async def get_manifest_for_client_app(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ModuleFederationDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ModuleFederationDto]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.module_federation.get_manifest_for_client_app()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_manifest_for_client_app(request_options=request_options)
        return _response.data

    async def registry_module(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        remote_entry: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        export_module: typing.Optional[ModuleFederationDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            See 'name' in webpack.config.js

        remote_entry : typing.Optional[str]
            Remote entry

        base_url : typing.Optional[str]
            Base Url

        export_module : typing.Optional[ModuleFederationDto]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.module_federation.registry_module()


        asyncio.run(main())
        """
        _response = await self._raw_client.registry_module(
            name=name,
            remote_entry=remote_entry,
            base_url=base_url,
            export_module=export_module,
            request_options=request_options,
        )
        return _response.data
