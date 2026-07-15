

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_telnet import ConfigTelnet
from ..types.ip_alias import IpAlias
from ..types.telnet_user import TelnetUser
from .raw_client import AsyncRawTelnetClient, RawTelnetClient


class TelnetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTelnetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTelnetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTelnetClient
        """
        return self._raw_client

    def protocol_telnet_connection_logon(
        self,
        agent_num: int,
        connection_id: int,
        user: str,
        password: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Logon change allows (hidden) commands for a different access mode to run.

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        user : str

        password : str

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
        client.telnet.protocol_telnet_connection_logon(
            agent_num=1,
            connection_id=1,
            user="user",
            password="password",
        )
        """
        _response = self._raw_client.protocol_telnet_connection_logon(
            agent_num, connection_id, user, password, request_options=request_options
        )
        return _response.data

    def protocol_telnet_connection_request(
        self,
        agent_num: int,
        connection_id: int,
        command: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Equivalent of the command typed in by the user.

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        command : str

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
        client.telnet.protocol_telnet_connection_request(
            agent_num=1,
            connection_id=1,
            command="command",
        )
        """
        _response = self._raw_client.protocol_telnet_connection_request(
            agent_num, connection_id, command, request_options=request_options
        )
        return _response.data

    def protocol_telnet_connection_signal(
        self,
        agent_num: int,
        connection_id: int,
        signal_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Signal name is either connect or idle

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        signal_name : str

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
        client.telnet.protocol_telnet_connection_signal(
            agent_num=1,
            connection_id=1,
            signal_name="signalName",
        )
        """
        _response = self._raw_client.protocol_telnet_connection_signal(
            agent_num, connection_id, signal_name, request_options=request_options
        )
        return _response.data

    def protocol_telnet_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TELNET argument structure

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
        client.telnet.protocol_telnet_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTelnet:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TELNET configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTelnet
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.telnet.protocol_telnet_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
        client.telnet.protocol_telnet_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTelnet:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TELNET tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTelnet
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.telnet.protocol_telnet_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
        client.telnet.protocol_telnet_ipalias_disable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_telnet_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_telnet_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
        client.telnet.protocol_telnet_ipalias_enable(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_telnet_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_telnet_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
        client.telnet.protocol_telnet_ipalias_isenabled(
            agent_num=1,
            ipaddress="ipaddress",
            port=1,
        )
        """
        _response = self._raw_client.protocol_telnet_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    def protocol_telnet_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
        client.telnet.protocol_telnet_ipalias_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_connections(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        IDs of all connected connections

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET configuration

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
        client.telnet.protocol_telnet_server_get_connections(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_connections(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_keymap(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Keymap file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
        client.telnet.protocol_telnet_server_get_keymap(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_keymap(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_rulesdb(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Rules db file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
        client.telnet.protocol_telnet_server_get_rulesdb(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_rulesdb(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_state(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Return 1 means accepting connections, 0 not

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
        client.telnet.protocol_telnet_server_get_state(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_state(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_userdb(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        User db file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
        client.telnet.protocol_telnet_server_get_userdb(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_userdb(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_server_get_users(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TelnetUser]:
        """
        List of users

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelnetUser]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.telnet.protocol_telnet_server_get_users(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_telnet_server_get_users(agent_num, request_options=request_options)
        return _response.data

    def protocol_telnet_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TELNET configuration

        argument : str
            Parameter to set the TELNET configuration

        value : str
            Value to set the TELNET configuration

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
        client.telnet.protocol_telnet_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_telnet_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_telnet_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TELNET tracing

        enable_or_not : str
            Value to set the TELNET tracing

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
        client.telnet.protocol_telnet_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_telnet_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    def protocol_telnet_get_stats_hdr(
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
        client.telnet.protocol_telnet_get_stats_hdr()
        """
        _response = self._raw_client.protocol_telnet_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncTelnetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTelnetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTelnetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTelnetClient
        """
        return self._raw_client

    async def protocol_telnet_connection_logon(
        self,
        agent_num: int,
        connection_id: int,
        user: str,
        password: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Logon change allows (hidden) commands for a different access mode to run.

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        user : str

        password : str

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
            await client.telnet.protocol_telnet_connection_logon(
                agent_num=1,
                connection_id=1,
                user="user",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_connection_logon(
            agent_num, connection_id, user, password, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_connection_request(
        self,
        agent_num: int,
        connection_id: int,
        command: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Equivalent of the command typed in by the user.

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        command : str

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
            await client.telnet.protocol_telnet_connection_request(
                agent_num=1,
                connection_id=1,
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_connection_request(
            agent_num, connection_id, command, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_connection_signal(
        self,
        agent_num: int,
        connection_id: int,
        signal_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Signal name is either connect or idle

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET connection

        connection_id : int

        signal_name : str

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
            await client.telnet.protocol_telnet_connection_signal(
                agent_num=1,
                connection_id=1,
                signal_name="signalName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_connection_signal(
            agent_num, connection_id, signal_name, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TELNET argument structure

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
            await client.telnet.protocol_telnet_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTelnet:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TELNET configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTelnet
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
            await client.telnet.protocol_telnet_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
            await client.telnet.protocol_telnet_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTelnet:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TELNET tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTelnet
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
            await client.telnet.protocol_telnet_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_ipalias_disable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
            await client.telnet.protocol_telnet_ipalias_disable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_ipalias_disable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_ipalias_enable(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
            await client.telnet.protocol_telnet_ipalias_enable(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_ipalias_enable(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_ipalias_isenabled(
        self, agent_num: int, ipaddress: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
            await client.telnet.protocol_telnet_ipalias_isenabled(
                agent_num=1,
                ipaddress="ipaddress",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_ipalias_isenabled(
            agent_num, ipaddress, port, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_ipalias_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

        Parameters
        ----------
        agent_num : int
            Agent to manipulate TELNET IP alias

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
            await client.telnet.protocol_telnet_ipalias_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_ipalias_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_server_get_connections(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        IDs of all connected connections

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET configuration

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
            await client.telnet.protocol_telnet_server_get_connections(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_connections(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_server_get_keymap(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Keymap file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
            await client.telnet.protocol_telnet_server_get_keymap(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_keymap(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_server_get_rulesdb(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Rules db file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
            await client.telnet.protocol_telnet_server_get_rulesdb(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_rulesdb(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_server_get_state(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Return 1 means accepting connections, 0 not

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
            await client.telnet.protocol_telnet_server_get_state(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_state(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_server_get_userdb(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        User db file name

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET statistics

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
            await client.telnet.protocol_telnet_server_get_userdb(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_userdb(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_server_get_users(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TelnetUser]:
        """
        List of users

        Parameters
        ----------
        agent_num : int
            Agent to show TELNET configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelnetUser]
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
            await client.telnet.protocol_telnet_server_get_users(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_server_get_users(agent_num, request_options=request_options)
        return _response.data

    async def protocol_telnet_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TELNET configuration

        argument : str
            Parameter to set the TELNET configuration

        value : str
            Value to set the TELNET configuration

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
            await client.telnet.protocol_telnet_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TELNET tracing

        enable_or_not : str
            Value to set the TELNET tracing

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
            await client.telnet.protocol_telnet_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_telnet_get_stats_hdr(
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
            await client.telnet.protocol_telnet_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_telnet_get_stats_hdr(request_options=request_options)
        return _response.data
