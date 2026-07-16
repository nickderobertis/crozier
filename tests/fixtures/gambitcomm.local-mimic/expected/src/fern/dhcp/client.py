

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_dhcp import ConfigDhcp
from .raw_client import AsyncRawDhcpClient, RawDhcpClient


class DhcpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDhcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDhcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDhcpClient
        """
        return self._raw_client

    def protocol_dhcp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's DHCP configuration particulars

        Parameters
        ----------
        agent_num : int
            Agent to show the DHCP argument structure

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
        client.dhcp.protocol_dhcp_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_dhcp_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_dhcp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigDhcp:
        """
        Agent's DHCP configuration hwaddr,classid,add_options,script

        Parameters
        ----------
        agent_num : int
            Agent to show the DHCP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigDhcp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dhcp.protocol_dhcp_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_dhcp_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_dhcp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show DHCP statistics

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
        client.dhcp.protocol_dhcp_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_dhcp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_dhcp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigDhcp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether DHCP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigDhcp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dhcp.protocol_dhcp_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_dhcp_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_dhcp_params(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        DHCP-OFFER message parameters

        Parameters
        ----------
        agent_num : int
            Agent to show DHCP DHCP-OFFER message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dhcp.protocol_dhcp_params(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_dhcp_params(agent_num, request_options=request_options)
        return _response.data

    def protocol_dhcp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's DHCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the DHCP configuration

        argument : str
            Parameter to set the DHCP configuration

        value : str
            Value to set the DHCP configuration

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
        client.dhcp.protocol_dhcp_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_dhcp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_dhcp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the DHCP tracing

        enable_or_not : str
            Value to set the DHCP tracing

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
        client.dhcp.protocol_dhcp_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_dhcp_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_dhcp_get_stats_hdr(
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
        client.dhcp.protocol_dhcp_get_stats_hdr()
        """
        _response = self._raw_client.protocol_dhcp_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncDhcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDhcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDhcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDhcpClient
        """
        return self._raw_client

    async def protocol_dhcp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's DHCP configuration particulars

        Parameters
        ----------
        agent_num : int
            Agent to show the DHCP argument structure

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
            await client.dhcp.protocol_dhcp_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_dhcp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigDhcp:
        """
        Agent's DHCP configuration hwaddr,classid,add_options,script

        Parameters
        ----------
        agent_num : int
            Agent to show the DHCP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigDhcp
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
            await client.dhcp.protocol_dhcp_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_dhcp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show DHCP statistics

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
            await client.dhcp.protocol_dhcp_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_dhcp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigDhcp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether DHCP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigDhcp
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
            await client.dhcp.protocol_dhcp_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_dhcp_params(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        DHCP-OFFER message parameters

        Parameters
        ----------
        agent_num : int
            Agent to show DHCP DHCP-OFFER message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
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
            await client.dhcp.protocol_dhcp_params(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_params(agent_num, request_options=request_options)
        return _response.data

    async def protocol_dhcp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's DHCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the DHCP configuration

        argument : str
            Parameter to set the DHCP configuration

        value : str
            Value to set the DHCP configuration

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
            await client.dhcp.protocol_dhcp_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_dhcp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the DHCP tracing

        enable_or_not : str
            Value to set the DHCP tracing

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
            await client.dhcp.protocol_dhcp_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_dhcp_get_stats_hdr(
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
            await client.dhcp.protocol_dhcp_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_dhcp_get_stats_hdr(request_options=request_options)
        return _response.data
