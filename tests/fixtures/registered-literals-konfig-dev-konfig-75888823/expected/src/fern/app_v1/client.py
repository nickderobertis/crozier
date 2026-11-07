

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.app_name import AppName
from ..types.application import Application
from ..types.application_with_latest_deployment_and_build import ApplicationWithLatestDeploymentAndBuild
from ..types.auth_configuration import AuthConfiguration
from .raw_client import AsyncRawAppV1Client, RawAppV1Client


OMIT = typing.cast(typing.Any, ...)


class AppV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppV1Client
        """
        return self._raw_client

    def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationWithLatestDeploymentAndBuild]:
        """
        Returns an unsorted list of your organization’s [applications](https://hathora.dev/docs/concepts/hathora-entities#application). An application is uniquely identified by an `appId`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationWithLatestDeploymentAndBuild]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.app_v1.get_apps()
        """
        _response = self._raw_client.get_apps(request_options=request_options)
        return _response.data

    def create_app(
        self,
        *,
        auth_configuration: AuthConfiguration,
        app_name: AppName,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Application:
        """
        Create a new [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        auth_configuration : AuthConfiguration

        app_name : AppName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application


        Examples
        --------
        from fern import AuthConfiguration, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.app_v1.create_app(
            auth_configuration=AuthConfiguration(),
            app_name="minecraft",
        )
        """
        _response = self._raw_client.create_app(
            auth_configuration=auth_configuration, app_name=app_name, request_options=request_options
        )
        return _response.data

    def update_app(
        self,
        app_id: AppId,
        *,
        auth_configuration: AuthConfiguration,
        app_name: AppName,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Application:
        """
        Update data for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        auth_configuration : AuthConfiguration

        app_name : AppName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application
            Ok

        Examples
        --------
        from fern import AuthConfiguration, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.app_v1.update_app(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            auth_configuration=AuthConfiguration(),
            app_name="minecraft",
        )
        """
        _response = self._raw_client.update_app(
            app_id, auth_configuration=auth_configuration, app_name=app_name, request_options=request_options
        )
        return _response.data

    def get_app_info(self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None) -> Application:
        """
        Get details for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.app_v1.get_app_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_app_info(app_id, request_options=request_options)
        return _response.data

    def delete_app(self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`. Your organization will lose access to this application.

        Parameters
        ----------
        app_id : AppId

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
        )
        client.app_v1.delete_app(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.delete_app(app_id, request_options=request_options)
        return _response.data


class AsyncAppV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppV1Client
        """
        return self._raw_client

    async def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApplicationWithLatestDeploymentAndBuild]:
        """
        Returns an unsorted list of your organization’s [applications](https://hathora.dev/docs/concepts/hathora-entities#application). An application is uniquely identified by an `appId`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApplicationWithLatestDeploymentAndBuild]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.app_v1.get_apps()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_apps(request_options=request_options)
        return _response.data

    async def create_app(
        self,
        *,
        auth_configuration: AuthConfiguration,
        app_name: AppName,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Application:
        """
        Create a new [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        auth_configuration : AuthConfiguration

        app_name : AppName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AuthConfiguration

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.app_v1.create_app(
                auth_configuration=AuthConfiguration(),
                app_name="minecraft",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_app(
            auth_configuration=auth_configuration, app_name=app_name, request_options=request_options
        )
        return _response.data

    async def update_app(
        self,
        app_id: AppId,
        *,
        auth_configuration: AuthConfiguration,
        app_name: AppName,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Application:
        """
        Update data for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        auth_configuration : AuthConfiguration

        app_name : AppName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AuthConfiguration

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.app_v1.update_app(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                auth_configuration=AuthConfiguration(),
                app_name="minecraft",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_app(
            app_id, auth_configuration=auth_configuration, app_name=app_name, request_options=request_options
        )
        return _response.data

    async def get_app_info(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Application:
        """
        Get details for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Application
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.app_v1.get_app_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_info(app_id, request_options=request_options)
        return _response.data

    async def delete_app(self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`. Your organization will lose access to this application.

        Parameters
        ----------
        app_id : AppId

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
        )


        async def main() -> None:
            await client.app_v1.delete_app(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_app(app_id, request_options=request_options)
        return _response.data
