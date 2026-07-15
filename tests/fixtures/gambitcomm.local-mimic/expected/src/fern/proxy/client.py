

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_proxy import ConfigProxy
from .raw_client import AsyncRawProxyClient, RawProxyClient


class ProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProxyClient
        """
        return self._raw_client

    def protocol_proxy_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the PROXY argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_proxy_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_proxy_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProxy:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the PROXY configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProxy
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_proxy_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_proxy_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show PROXY statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_proxy_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_proxy_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProxy:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether PROXY tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProxy
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_proxy_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_proxy_port_add(
        self,
        agent_num: int,
        port: int,
        target: str,
        target_port: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Additional proxy target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        target : str

        target_port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_add(
            agent_num=1,
            port=1,
            target="target",
            target_port=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_add(
            agent_num, port, target, target_port, request_options=request_options
        )
        return _response.data

    def protocol_proxy_port_isstarted(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Check individual target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_isstarted(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_isstarted(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_proxy_port_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_proxy_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove proxy target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_remove(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_remove(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_proxy_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start additional target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_start(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_start(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_proxy_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop additional target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_port_stop(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_proxy_port_stop(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_proxy_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the PROXY configuration

        argument : str
            Parameter to set the PROXY configuration

        value : str
            Value to set the PROXY configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_proxy_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_proxy_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the PROXY tracing

        enable_or_not : str
            Value to set the PROXY tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_proxy_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_proxy_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The headers of statistics fields

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.proxy.protocol_proxy_get_stats_hdr()
        """
        _response = self._raw_client.protocol_proxy_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProxyClient
        """
        return self._raw_client

    async def protocol_proxy_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the PROXY argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_proxy_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProxy:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the PROXY configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProxy
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_proxy_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show PROXY statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_proxy_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProxy:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether PROXY tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProxy
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_proxy_port_add(
        self,
        agent_num: int,
        port: int,
        target: str,
        target_port: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Additional proxy target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        target : str

        target_port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_add(
                agent_num=1,
                port=1,
                target="target",
                target_port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_add(
            agent_num, port, target, target_port, request_options=request_options
        )
        return _response.data

    async def protocol_proxy_port_isstarted(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Check individual target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_isstarted(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_isstarted(
            agent_num, port, request_options=request_options
        )
        return _response.data

    async def protocol_proxy_port_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_proxy_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove proxy target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_remove(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_remove(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_proxy_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start additional target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_start(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_start(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_proxy_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop additional target

        Parameters
        ----------
        agent_num : int
            Agent to manipulate PROXY target

        port : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_port_stop(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_port_stop(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_proxy_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the PROXY configuration

        argument : str
            Parameter to set the PROXY configuration

        value : str
            Value to set the PROXY configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_proxy_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the PROXY tracing

        enable_or_not : str
            Value to set the PROXY tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_proxy_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The headers of statistics fields

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.proxy.protocol_proxy_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_proxy_get_stats_hdr(request_options=request_options)
        return _response.data
