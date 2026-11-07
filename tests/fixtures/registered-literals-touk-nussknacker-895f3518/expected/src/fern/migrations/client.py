

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_version import ApiVersion
from ..types.migrate_scenario_request_dto import MigrateScenarioRequestDto
from .raw_client import AsyncRawMigrationsClient, RawMigrationsClient


OMIT = typing.cast(typing.Any, ...)


class MigrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMigrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMigrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMigrationsClient
        """
        return self._raw_client

    def post_api_migrate(
        self, *, request: MigrateScenarioRequestDto, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MigrateScenarioRequestDto

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
        client.migrations.post_api_migrate(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_api_migrate(request=request, request_options=request_options)
        return _response.data

    def get_api_migration_scenario_description_version(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiVersion:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiVersion


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.migrations.get_api_migration_scenario_description_version()
        """
        _response = self._raw_client.get_api_migration_scenario_description_version(request_options=request_options)
        return _response.data


class AsyncMigrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMigrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMigrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMigrationsClient
        """
        return self._raw_client

    async def post_api_migrate(
        self, *, request: MigrateScenarioRequestDto, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MigrateScenarioRequestDto

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
            await client.migrations.post_api_migrate(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_migrate(request=request, request_options=request_options)
        return _response.data

    async def get_api_migration_scenario_description_version(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiVersion:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiVersion


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
            await client.migrations.get_api_migration_scenario_description_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_migration_scenario_description_version(
            request_options=request_options
        )
        return _response.data
