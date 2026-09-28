

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAdminSessionsClient, RawAdminSessionsClient


class AdminSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminSessionsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_users_controller_sessions(
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
        client.admin_sessions.otoroshi_controllers_adminapi_users_controller_sessions()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_sessions(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_discard_all_sessions(
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
        client.admin_sessions.otoroshi_controllers_adminapi_users_controller_discard_all_sessions()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_all_sessions(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_users_controller_discard_session(
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
        client.admin_sessions.otoroshi_controllers_adminapi_users_controller_discard_session(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_session(
            id, request_options=request_options
        )
        return _response.data


class AsyncAdminSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminSessionsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_users_controller_sessions(
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
            await client.admin_sessions.otoroshi_controllers_adminapi_users_controller_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_sessions(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_discard_all_sessions(
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
            await client.admin_sessions.otoroshi_controllers_adminapi_users_controller_discard_all_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_all_sessions(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_users_controller_discard_session(
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
            await client.admin_sessions.otoroshi_controllers_adminapi_users_controller_discard_session(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_users_controller_discard_session(
            id, request_options=request_options
        )
        return _response.data
