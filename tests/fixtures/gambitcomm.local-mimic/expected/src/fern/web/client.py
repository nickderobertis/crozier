

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_web import ConfigWeb
from .raw_client import AsyncRawWebClient, RawWebClient


class WebClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebClient
        """
        return self._raw_client

    def protocol_web_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB argument structure

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
        client.web.protocol_web_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_web_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_web_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigWeb:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigWeb
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.web.protocol_web_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_web_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_web_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show WEB statistics

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
        client.web.protocol_web_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_web_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_web_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigWeb:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether WEB tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigWeb
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.web.protocol_web_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_web_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_web_port_add(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add port

        Parameters
        ----------
        agent_num : int
            Agent to add WEB port

        port : int
            TCP port

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
        client.web.protocol_web_port_add(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_web_port_add(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_web_port_exists(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Check the port. 1 means existing, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show WEB configuration

        port : int
            TCP port

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
        client.web.protocol_web_port_exists(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_web_port_exists(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_web_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove port

        Parameters
        ----------
        agent_num : int
            Agent to remove WEB port

        port : int
            TCP port

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
        client.web.protocol_web_port_remove(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_web_port_remove(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_web_port_set(
        self,
        agent_num: int,
        port: int,
        protocol: str,
        version: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Set port

        Parameters
        ----------
        agent_num : int
            Agent to set WEB port

        port : int
            TCP port

        protocol : str
            Encryption or related protocol

        version : str
            Encryption or related protocol version

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
        client.web.protocol_web_port_set(
            agent_num=1,
            port=1,
            protocol="protocol",
            version="version",
        )
        """
        _response = self._raw_client.protocol_web_port_set(
            agent_num, port, protocol, version, request_options=request_options
        )
        return _response.data

    def protocol_web_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start port

        Parameters
        ----------
        agent_num : int
            Agent to start WEB port

        port : int
            TCP port

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
        client.web.protocol_web_port_start(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_web_port_start(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_web_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop port

        Parameters
        ----------
        agent_num : int
            Agent to stop WEB port

        port : int
            TCP port

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
        client.web.protocol_web_port_stop(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.protocol_web_port_stop(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_web_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB configuration

        argument : str
            Parameter to set the WEB configuration

        value : str
            Value to set the WEB configuration

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
        client.web.protocol_web_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_web_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_web_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB tracing

        enable_or_not : str
            Value to set the WEB tracing

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
        client.web.protocol_web_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_web_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_web_get_stats_hdr(
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
        client.web.protocol_web_get_stats_hdr()
        """
        _response = self._raw_client.protocol_web_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncWebClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebClient
        """
        return self._raw_client

    async def protocol_web_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB argument structure

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
            await client.web.protocol_web_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_web_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigWeb:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigWeb
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
            await client.web.protocol_web_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_web_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show WEB statistics

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
            await client.web.protocol_web_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_web_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigWeb:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether WEB tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigWeb
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
            await client.web.protocol_web_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_web_port_add(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add port

        Parameters
        ----------
        agent_num : int
            Agent to add WEB port

        port : int
            TCP port

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
            await client.web.protocol_web_port_add(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_add(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_web_port_exists(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Check the port. 1 means existing, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show WEB configuration

        port : int
            TCP port

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
            await client.web.protocol_web_port_exists(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_exists(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_web_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove port

        Parameters
        ----------
        agent_num : int
            Agent to remove WEB port

        port : int
            TCP port

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
            await client.web.protocol_web_port_remove(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_remove(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_web_port_set(
        self,
        agent_num: int,
        port: int,
        protocol: str,
        version: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Set port

        Parameters
        ----------
        agent_num : int
            Agent to set WEB port

        port : int
            TCP port

        protocol : str
            Encryption or related protocol

        version : str
            Encryption or related protocol version

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
            await client.web.protocol_web_port_set(
                agent_num=1,
                port=1,
                protocol="protocol",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_set(
            agent_num, port, protocol, version, request_options=request_options
        )
        return _response.data

    async def protocol_web_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start port

        Parameters
        ----------
        agent_num : int
            Agent to start WEB port

        port : int
            TCP port

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
            await client.web.protocol_web_port_start(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_start(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_web_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop port

        Parameters
        ----------
        agent_num : int
            Agent to stop WEB port

        port : int
            TCP port

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
            await client.web.protocol_web_port_stop(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_port_stop(agent_num, port, request_options=request_options)
        return _response.data

    async def protocol_web_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB configuration

        argument : str
            Parameter to set the WEB configuration

        value : str
            Value to set the WEB configuration

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
            await client.web.protocol_web_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_web_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB tracing

        enable_or_not : str
            Value to set the WEB tracing

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
            await client.web.protocol_web_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_web_get_stats_hdr(
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
            await client.web.protocol_web_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_web_get_stats_hdr(request_options=request_options)
        return _response.data
