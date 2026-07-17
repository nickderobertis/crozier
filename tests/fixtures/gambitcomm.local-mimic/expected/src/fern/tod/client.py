

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_tod import ConfigTod
from .raw_client import AsyncRawTodClient, RawTodClient


class TodClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTodClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTodClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTodClient
        """
        return self._raw_client

    def protocol_tod_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tod.protocol_tod_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tod_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_tod_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTod:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTod
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tod.protocol_tod_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tod_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_tod_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TOD statistics

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
        client.tod.protocol_tod_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tod_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_tod_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTod:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TOD tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTod
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tod.protocol_tod_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tod_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_tod_gettime(
        self,
        agent_num: int,
        server_addr: str,
        port_num: int,
        script_name: str,
        time_sec: int,
        num_retries: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Retrive time from server

        Parameters
        ----------
        agent_num : int
            Agent to show TOD return

        server_addr : str
            serverAddr

        port_num : int
            portNum

        script_name : str
            scriptName

        time_sec : int
            timeSec

        num_retries : int
            numRetries

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
        client.tod.protocol_tod_gettime(
            agent_num=1,
            server_addr="serverAddr",
            port_num=1,
            script_name="scriptName",
            time_sec=1,
            num_retries=1,
        )
        """
        _response = self._raw_client.protocol_tod_gettime(
            agent_num, server_addr, port_num, script_name, time_sec, num_retries, request_options=request_options
        )
        return _response.data

    def protocol_tod_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD configuration

        argument : str
            Parameter to set the TOD configuration

        value : str
            Value to set the TOD configuration

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
        client.tod.protocol_tod_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_tod_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_tod_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD tracing

        enable_or_not : str
            Value to set the TOD tracing

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
        client.tod.protocol_tod_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_tod_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_tod_get_stats_hdr(
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
        client.tod.protocol_tod_get_stats_hdr()
        """
        _response = self._raw_client.protocol_tod_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncTodClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTodClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTodClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTodClient
        """
        return self._raw_client

    async def protocol_tod_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.tod.protocol_tod_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tod_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTod:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTod
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
            await client.tod.protocol_tod_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tod_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TOD statistics

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
            await client.tod.protocol_tod_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tod_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTod:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TOD tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTod
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
            await client.tod.protocol_tod_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tod_gettime(
        self,
        agent_num: int,
        server_addr: str,
        port_num: int,
        script_name: str,
        time_sec: int,
        num_retries: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Retrive time from server

        Parameters
        ----------
        agent_num : int
            Agent to show TOD return

        server_addr : str
            serverAddr

        port_num : int
            portNum

        script_name : str
            scriptName

        time_sec : int
            timeSec

        num_retries : int
            numRetries

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
            await client.tod.protocol_tod_gettime(
                agent_num=1,
                server_addr="serverAddr",
                port_num=1,
                script_name="scriptName",
                time_sec=1,
                num_retries=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_gettime(
            agent_num, server_addr, port_num, script_name, time_sec, num_retries, request_options=request_options
        )
        return _response.data

    async def protocol_tod_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD configuration

        argument : str
            Parameter to set the TOD configuration

        value : str
            Value to set the TOD configuration

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
            await client.tod.protocol_tod_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_tod_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD tracing

        enable_or_not : str
            Value to set the TOD tracing

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
            await client.tod.protocol_tod_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_tod_get_stats_hdr(
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
            await client.tod.protocol_tod_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tod_get_stats_hdr(request_options=request_options)
        return _response.data
