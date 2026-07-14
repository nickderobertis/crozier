

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_snmptcp import ConfigSnmptcp
from ..types.ip_alias import IpAlias
from .raw_client import AsyncRawSnmptcpClient, RawSnmptcpClient


class SnmptcpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnmptcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnmptcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnmptcpClient
        """
        return self._raw_client

    def protocol_snmptcp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPTCP argument structure

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
        client.snmptcp.protocol_snmptcp_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmptcp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmptcp:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPTCP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmptcp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snmptcp.protocol_snmptcp_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmptcp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SNMPTCP statistics

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
        client.snmptcp.protocol_snmptcp_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmptcp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmptcp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SNMPTCP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmptcp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snmptcp.protocol_snmptcp_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmptcp_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
        client.snmptcp.protocol_snmptcp_ipalias_disable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_snmptcp_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
        client.snmptcp.protocol_snmptcp_ipalias_enable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_snmptcp_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
        client.snmptcp.protocol_snmptcp_ipalias_isenabled(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_snmptcp_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAlias]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snmptcp.protocol_snmptcp_ipalias_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmptcp_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmptcp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMPTCP configuration

        argument : str
            Parameter to set the SNMPTCP configuration

        value : str
            Value to set the SNMPTCP configuration

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
        client.snmptcp.protocol_snmptcp_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_snmptcp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_snmptcp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMPTCP tracing

        enable_or_not : str
            Value to set the SNMPTCP tracing

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
        client.snmptcp.protocol_snmptcp_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_snmptcp_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    def protocol_snmptcp_get_stats_hdr(
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
        client.snmptcp.protocol_snmptcp_get_stats_hdr()
        """
        _response = self._raw_client.protocol_snmptcp_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncSnmptcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnmptcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnmptcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnmptcpClient
        """
        return self._raw_client

    async def protocol_snmptcp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPTCP argument structure

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
            await client.snmptcp.protocol_snmptcp_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmptcp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmptcp:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPTCP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmptcp
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
            await client.snmptcp.protocol_snmptcp_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmptcp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SNMPTCP statistics

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
            await client.snmptcp.protocol_snmptcp_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmptcp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmptcp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SNMPTCP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmptcp
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
            await client.snmptcp.protocol_snmptcp_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmptcp_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
            await client.snmptcp.protocol_snmptcp_ipalias_disable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_snmptcp_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
            await client.snmptcp.protocol_snmptcp_ipalias_enable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_snmptcp_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        ipaddress : str

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
            await client.snmptcp.protocol_snmptcp_ipalias_isenabled(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_snmptcp_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SNMPTCP IP alias

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAlias]
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
            await client.snmptcp.protocol_snmptcp_ipalias_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmptcp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMPTCP configuration

        argument : str
            Parameter to set the SNMPTCP configuration

        value : str
            Value to set the SNMPTCP configuration

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
            await client.snmptcp.protocol_snmptcp_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_snmptcp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMPTCP tracing

        enable_or_not : str
            Value to set the SNMPTCP tracing

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
            await client.snmptcp.protocol_snmptcp_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_snmptcp_get_stats_hdr(
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
            await client.snmptcp.protocol_snmptcp_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmptcp_get_stats_hdr(request_options=request_options)
        return _response.data
