

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAppsSessionsClient, RawAppsSessionsClient


class AppsSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppsSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppsSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppsSessionsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_users_controller_private_apps_sessions(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apps_sessions.otoroshi_controllers_adminapi_users_controller_private_apps_sessions()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_private_apps_sessions(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apps_sessions.otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.apps_sessions.otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
            id, request_options=request_options
        )
        return _response.data


class AsyncAppsSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppsSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppsSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppsSessionsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_users_controller_private_apps_sessions(
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
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apps_sessions.otoroshi_controllers_adminapi_users_controller_private_apps_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_private_apps_sessions(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions(
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
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apps_sessions.otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_all_private_apps_sessions(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.apps_sessions.otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_private_apps_session(
            id, request_options=request_options
        )
        return _response.data
