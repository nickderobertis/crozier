

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClusterClient, RawClusterClient


OMIT = typing.cast(typing.Any, ...)


class ClusterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClusterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClusterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClusterClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_create_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_create_session(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_create_session(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_update_state(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_update_state(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_update_state(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_state_ws(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_state_ws()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_state_ws(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_read_state(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_read_state()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_read_state(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_relay_routing(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_relay_routing(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_relay_routing(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_get_cluster_members(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_get_cluster_members()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_get_cluster_members(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_live_cluster(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_live_cluster()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_live_cluster(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_create_login_token(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request : typing.Dict[str, typing.Any]

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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_create_login_token(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_create_login_token(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_get_user_token(
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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_get_user_token(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_get_user_token(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_cluster_controller_set_user_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.cluster.otoroshi_controllers_adminapi_cluster_controller_set_user_token(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_cluster_controller_set_user_token(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncClusterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClusterClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClusterClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClusterClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_is_session_valid(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_create_session(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_create_session(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_create_session(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_update_state(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_update_state(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_update_state(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_state_ws(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_state_ws()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_state_ws(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_read_state(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_read_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_read_state(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_relay_routing(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_relay_routing(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_relay_routing(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_get_cluster_members(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_get_cluster_members()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_get_cluster_members(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_live_cluster(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_live_cluster()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_live_cluster(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_create_login_token(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request : typing.Dict[str, typing.Any]

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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_create_login_token(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_create_login_token(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_get_user_token(
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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_get_user_token(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_get_user_token(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_cluster_controller_set_user_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.cluster.otoroshi_controllers_adminapi_cluster_controller_set_user_token(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_cluster_controller_set_user_token(
            request=request, request_options=request_options
        )
        return _response.data
