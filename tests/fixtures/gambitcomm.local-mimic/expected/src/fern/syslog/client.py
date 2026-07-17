

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_syslog import ConfigSyslog
from .raw_client import AsyncRawSyslogClient, RawSyslogClient


OMIT = typing.cast(typing.Any, ...)


class SyslogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSyslogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSyslogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSyslogClient
        """
        return self._raw_client

    def protocol_syslog_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SYSLOG argument structure

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
        client.syslog.protocol_syslog_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_syslog_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_syslog_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSyslog:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SYSLOG configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSyslog
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.syslog.protocol_syslog_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_syslog_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_syslog_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SYSLOG statistics

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
        client.syslog.protocol_syslog_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_syslog_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_syslog_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSyslog:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SYSLOG tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSyslog
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.syslog.protocol_syslog_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_syslog_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_syslog_get_attr(
        self, agent_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be server , sequence , separator , hostname , timestamp

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        attr : str
            Attribute

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
        client.syslog.protocol_syslog_get_attr(
            agent_num=1,
            attr="attr",
        )
        """
        _response = self._raw_client.protocol_syslog_get_attr(agent_num, attr, request_options=request_options)
        return _response.data

    def protocol_syslog_send(
        self,
        agent_num: int,
        pri: int,
        *,
        hostname: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        separator: typing.Optional[str] = OMIT,
        sequence: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        pri : int
            Message Priority

        hostname : typing.Optional[str]

        message : typing.Optional[str]

        separator : typing.Optional[str]

        sequence : typing.Optional[str]

        timestamp : typing.Optional[str]

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
        client.syslog.protocol_syslog_send(
            agent_num=1,
            pri=1,
        )
        """
        _response = self._raw_client.protocol_syslog_send(
            agent_num,
            pri,
            hostname=hostname,
            message=message,
            separator=separator,
            sequence=sequence,
            timestamp=timestamp,
            request_options=request_options,
        )
        return _response.data

    def protocol_syslog_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG configuration

        argument : str
            Parameter to set the SYSLOG configuration

        value : str
            Value to set the SYSLOG configuration

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
        client.syslog.protocol_syslog_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_syslog_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_syslog_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        enable_or_not : str
            Value to set the SYSLOG tracing

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
        client.syslog.protocol_syslog_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_syslog_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    def protocol_syslog_set_attr(
        self, agent_num: int, attr: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be server , sequence , separator , hostname , timestamp

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        attr : str
            Attribute

        value : str

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
        client.syslog.protocol_syslog_set_attr(
            agent_num=1,
            attr="attr",
            value="value",
        )
        """
        _response = self._raw_client.protocol_syslog_set_attr(agent_num, attr, value, request_options=request_options)
        return _response.data

    def protocol_syslog_get_stats_hdr(
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
        client.syslog.protocol_syslog_get_stats_hdr()
        """
        _response = self._raw_client.protocol_syslog_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncSyslogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSyslogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSyslogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSyslogClient
        """
        return self._raw_client

    async def protocol_syslog_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SYSLOG argument structure

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
            await client.syslog.protocol_syslog_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_syslog_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSyslog:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SYSLOG configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSyslog
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
            await client.syslog.protocol_syslog_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_syslog_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SYSLOG statistics

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
            await client.syslog.protocol_syslog_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_syslog_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSyslog:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SYSLOG tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSyslog
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
            await client.syslog.protocol_syslog_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_syslog_get_attr(
        self, agent_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be server , sequence , separator , hostname , timestamp

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        attr : str
            Attribute

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
            await client.syslog.protocol_syslog_get_attr(
                agent_num=1,
                attr="attr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_attr(agent_num, attr, request_options=request_options)
        return _response.data

    async def protocol_syslog_send(
        self,
        agent_num: int,
        pri: int,
        *,
        hostname: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        separator: typing.Optional[str] = OMIT,
        sequence: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        pri : int
            Message Priority

        hostname : typing.Optional[str]

        message : typing.Optional[str]

        separator : typing.Optional[str]

        sequence : typing.Optional[str]

        timestamp : typing.Optional[str]

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
            await client.syslog.protocol_syslog_send(
                agent_num=1,
                pri=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_send(
            agent_num,
            pri,
            hostname=hostname,
            message=message,
            separator=separator,
            sequence=sequence,
            timestamp=timestamp,
            request_options=request_options,
        )
        return _response.data

    async def protocol_syslog_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG configuration

        argument : str
            Parameter to set the SYSLOG configuration

        value : str
            Value to set the SYSLOG configuration

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
            await client.syslog.protocol_syslog_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_syslog_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        enable_or_not : str
            Value to set the SYSLOG tracing

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
            await client.syslog.protocol_syslog_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_syslog_set_attr(
        self, agent_num: int, attr: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be server , sequence , separator , hostname , timestamp

        Parameters
        ----------
        agent_num : int
            Agent to set the SYSLOG tracing

        attr : str
            Attribute

        value : str

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
            await client.syslog.protocol_syslog_set_attr(
                agent_num=1,
                attr="attr",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_set_attr(
            agent_num, attr, value, request_options=request_options
        )
        return _response.data

    async def protocol_syslog_get_stats_hdr(
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
            await client.syslog.protocol_syslog_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_syslog_get_stats_hdr(request_options=request_options)
        return _response.data
