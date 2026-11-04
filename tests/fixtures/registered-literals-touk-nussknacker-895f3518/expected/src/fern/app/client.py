

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.build_info_dto import BuildInfoDto
from ..types.health_check_process_success_response_dto import HealthCheckProcessSuccessResponseDto
from ..types.leader_response_dto import LeaderResponseDto
from ..types.map_string import MapString
from ..types.scenario_parameters_combination_with_engine_errors import ScenarioParametersCombinationWithEngineErrors
from .raw_client import AsyncRawAppClient, RawAppClient


class AppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppClient
        """
        return self._raw_client

    def get_api_app_healthcheck(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_healthcheck()
        """
        _response = self._raw_client.get_api_app_healthcheck(request_options=request_options)
        return _response.data

    def get_api_app_leader(self, *, request_options: typing.Optional[RequestOptions] = None) -> LeaderResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaderResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_leader()
        """
        _response = self._raw_client.get_api_app_leader(request_options=request_options)
        return _response.data

    def get_api_app_buildinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> BuildInfoDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildInfoDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_buildinfo()
        """
        _response = self._raw_client.get_api_app_buildinfo(request_options=request_options)
        return _response.data

    def post_api_app_processingtype_reload(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.app.post_api_app_processingtype_reload()
        """
        _response = self._raw_client.post_api_app_processingtype_reload(request_options=request_options)
        return _response.data

    def post_api_app_model_reload(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.app.post_api_app_model_reload()
        """
        _response = self._raw_client.post_api_app_model_reload(request_options=request_options)
        return _response.data

    def get_api_app_healthcheck_process_deployment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_healthcheck_process_deployment()
        """
        _response = self._raw_client.get_api_app_healthcheck_process_deployment(request_options=request_options)
        return _response.data

    def get_api_app_healthcheck_process_validation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_healthcheck_process_validation()
        """
        _response = self._raw_client.get_api_app_healthcheck_process_validation(request_options=request_options)
        return _response.data

    def get_api_app_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_config()
        """
        _response = self._raw_client.get_api_app_config(request_options=request_options)
        return _response.data

    def get_api_app_config_categorieswithprocessingtype(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MapString:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MapString


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_app_config_categorieswithprocessingtype()
        """
        _response = self._raw_client.get_api_app_config_categorieswithprocessingtype(request_options=request_options)
        return _response.data

    def get_api_scenarioparameterscombinations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioParametersCombinationWithEngineErrors:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioParametersCombinationWithEngineErrors


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.app.get_api_scenarioparameterscombinations()
        """
        _response = self._raw_client.get_api_scenarioparameterscombinations(request_options=request_options)
        return _response.data


class AsyncAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppClient
        """
        return self._raw_client

    async def get_api_app_healthcheck(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


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
            await client.app.get_api_app_healthcheck()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_healthcheck(request_options=request_options)
        return _response.data

    async def get_api_app_leader(self, *, request_options: typing.Optional[RequestOptions] = None) -> LeaderResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LeaderResponseDto


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
            await client.app.get_api_app_leader()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_leader(request_options=request_options)
        return _response.data

    async def get_api_app_buildinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> BuildInfoDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildInfoDto


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
            await client.app.get_api_app_buildinfo()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_buildinfo(request_options=request_options)
        return _response.data

    async def post_api_app_processingtype_reload(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.app.post_api_app_processingtype_reload()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_app_processingtype_reload(request_options=request_options)
        return _response.data

    async def post_api_app_model_reload(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.app.post_api_app_model_reload()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_app_model_reload(request_options=request_options)
        return _response.data

    async def get_api_app_healthcheck_process_deployment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


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
            await client.app.get_api_app_healthcheck_process_deployment()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_healthcheck_process_deployment(request_options=request_options)
        return _response.data

    async def get_api_app_healthcheck_process_validation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckProcessSuccessResponseDto:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckProcessSuccessResponseDto


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
            await client.app.get_api_app_healthcheck_process_validation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_healthcheck_process_validation(request_options=request_options)
        return _response.data

    async def get_api_app_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


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
            await client.app.get_api_app_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_config(request_options=request_options)
        return _response.data

    async def get_api_app_config_categorieswithprocessingtype(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MapString:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MapString


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
            await client.app.get_api_app_config_categorieswithprocessingtype()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_app_config_categorieswithprocessingtype(
            request_options=request_options
        )
        return _response.data

    async def get_api_scenarioparameterscombinations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioParametersCombinationWithEngineErrors:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioParametersCombinationWithEngineErrors


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
            await client.app.get_api_scenarioparameterscombinations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_scenarioparameterscombinations(request_options=request_options)
        return _response.data
