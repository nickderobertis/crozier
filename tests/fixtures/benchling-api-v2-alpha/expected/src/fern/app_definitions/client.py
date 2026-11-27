

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_client_secret import AppClientSecret
from .raw_client import AsyncRawAppDefinitionsClient, RawAppDefinitionsClient


class AppDefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppDefinitionsClient
        """
        return self._raw_client

    def regenerate_benchling_app_definition_client_secret(
        self, app_def_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppClientSecret:
        """
        Regenerate the oauth2 client key for the given app definition. Note that this will invalidate the previous key, and the value returned by this call can't be retrieved from Benchling.

        Parameters
        ----------
        app_def_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClientSecret
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app_definitions.regenerate_benchling_app_definition_client_secret(
            app_def_id="appdef_e59sjL23Pqn30xHg",
        )
        """
        _response = self._raw_client.regenerate_benchling_app_definition_client_secret(
            app_def_id, request_options=request_options
        )
        return _response.data


class AsyncAppDefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppDefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppDefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppDefinitionsClient
        """
        return self._raw_client

    async def regenerate_benchling_app_definition_client_secret(
        self, app_def_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AppClientSecret:
        """
        Regenerate the oauth2 client key for the given app definition. Note that this will invalidate the previous key, and the value returned by this call can't be retrieved from Benchling.

        Parameters
        ----------
        app_def_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClientSecret
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app_definitions.regenerate_benchling_app_definition_client_secret(
                app_def_id="appdef_e59sjL23Pqn30xHg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.regenerate_benchling_app_definition_client_secret(
            app_def_id, request_options=request_options
        )
        return _response.data
