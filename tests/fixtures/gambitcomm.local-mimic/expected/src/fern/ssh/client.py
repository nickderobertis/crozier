

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_ssh import ConfigSsh
from ..types.ip_alias import IpAlias
from .raw_client import AsyncRawSshClient, RawSshClient


class SshClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSshClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSshClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSshClient
        """
        return self._raw_client

    def protocol_ssh_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SSH argument structure

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
        client.ssh.protocol_ssh_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ssh_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_ssh_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSsh:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SSH configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSsh
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ssh.protocol_ssh_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ssh_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_ssh_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SSH statistics

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
        client.ssh.protocol_ssh_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ssh_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_ssh_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSsh:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SSH tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSsh
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ssh.protocol_ssh_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ssh_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_ssh_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
        client.ssh.protocol_ssh_ipalias_disable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_ssh_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_ssh_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
        client.ssh.protocol_ssh_ipalias_enable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_ssh_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_ssh_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
        client.ssh.protocol_ssh_ipalias_isenabled(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_ssh_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_ssh_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
        client.ssh.protocol_ssh_ipalias_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ssh_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_ssh_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SSH configuration

        argument : str
            Parameter to set the SSH configuration

        value : str
            Value to set the SSH configuration

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
        client.ssh.protocol_ssh_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_ssh_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_ssh_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SSH tracing

        enable_or_not : str
            Value to set the SSH tracing

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
        client.ssh.protocol_ssh_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_ssh_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_ssh_get_stats_hdr(
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
        client.ssh.protocol_ssh_get_stats_hdr()
        """
        _response = self._raw_client.protocol_ssh_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncSshClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSshClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSshClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSshClient
        """
        return self._raw_client

    async def protocol_ssh_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SSH argument structure

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
            await client.ssh.protocol_ssh_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ssh_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSsh:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SSH configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSsh
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
            await client.ssh.protocol_ssh_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ssh_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SSH statistics

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
            await client.ssh.protocol_ssh_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ssh_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSsh:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SSH tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSsh
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
            await client.ssh.protocol_ssh_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ssh_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
            await client.ssh.protocol_ssh_ipalias_disable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_ssh_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
            await client.ssh.protocol_ssh_ipalias_enable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_ssh_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
            await client.ssh.protocol_ssh_ipalias_isenabled(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_ssh_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate SSH IP alias

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
            await client.ssh.protocol_ssh_ipalias_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ssh_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SSH configuration

        argument : str
            Parameter to set the SSH configuration

        value : str
            Value to set the SSH configuration

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
            await client.ssh.protocol_ssh_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_ssh_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SSH tracing

        enable_or_not : str
            Value to set the SSH tracing

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
            await client.ssh.protocol_ssh_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_ssh_get_stats_hdr(
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
            await client.ssh.protocol_ssh_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ssh_get_stats_hdr(request_options=request_options)
        return _response.data
