

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTunnelsClient, RawTunnelsClient


OMIT = typing.cast(typing.Any, ...)


class TunnelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTunnelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTunnelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTunnelsClient
        """
        return self._raw_client

    def otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint(
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
        client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint()
        """
        _response = self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_tunnel_tunnel_controller_infos(
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
        client.tunnels.otoroshi_next_tunnel_tunnel_controller_infos()
        """
        _response = self._raw_client.otoroshi_next_tunnel_tunnel_controller_infos(request_options=request_options)
        return _response.data

    def otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
        self, tunnel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        tunnel_id : str
            the tunnelId parameter

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
        client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
            tunnel_id="tunnelId",
        )
        """
        _response = self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
            tunnel_id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
        self,
        tunnel_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        tunnel_id : str
            the tunnelId parameter

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
        client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
            tunnel_id="tunnelId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
            tunnel_id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_tunnel_tunnel_controller_tunnel_infos(
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
        client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_infos()
        """
        _response = self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_infos(
            request_options=request_options
        )
        return _response.data


class AsyncTunnelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTunnelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTunnelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTunnelsClient
        """
        return self._raw_client

    async def otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint(
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
            await client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_endpoint(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_tunnel_tunnel_controller_infos(
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
            await client.tunnels.otoroshi_next_tunnel_tunnel_controller_infos()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_tunnel_tunnel_controller_infos(request_options=request_options)
        return _response.data

    async def otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
        self, tunnel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        tunnel_id : str
            the tunnelId parameter

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
            await client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
                tunnel_id="tunnelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_relay_ws(
            tunnel_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
        self,
        tunnel_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        tunnel_id : str
            the tunnelId parameter

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
            await client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
                tunnel_id="tunnelId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_relay(
            tunnel_id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_tunnel_tunnel_controller_tunnel_infos(
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
            await client.tunnels.otoroshi_next_tunnel_tunnel_controller_tunnel_infos()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_tunnel_tunnel_controller_tunnel_infos(
            request_options=request_options
        )
        return _response.data
