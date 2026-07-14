

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_netflow import ConfigNetflow
from .raw_client import AsyncRawNetflowClient, RawNetflowClient


class NetflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetflowClient
        """
        return self._raw_client

    def protocol_netflow_change_dfs(
        self, agent_num: int, interval: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Interval in msec .

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        interval : int
            NETFLOW export interval

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
        client.netflow.protocol_netflow_change_dfs(
            agent_num=1,
            interval=1,
        )
        """
        _response = self._raw_client.protocol_netflow_change_dfs(agent_num, interval, request_options=request_options)
        return _response.data

    def protocol_netflow_change_tfs(
        self, agent_num: int, interval: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Interval in msec .

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        interval : int
            NETFLOW export interval

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
        client.netflow.protocol_netflow_change_tfs(
            agent_num=1,
            interval=1,
        )
        """
        _response = self._raw_client.protocol_netflow_change_tfs(agent_num, interval, request_options=request_options)
        return _response.data

    def protocol_netflow_change_attr(
        self,
        agent_num: int,
        flowset_uid: int,
        field_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Change attributes

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        flowset_uid : int

        field_num : int

        attr : str

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
        client.netflow.protocol_netflow_change_attr(
            agent_num=1,
            flowset_uid=1,
            field_num=1,
            attr="attr",
            value="value",
        )
        """
        _response = self._raw_client.protocol_netflow_change_attr(
            agent_num, flowset_uid, field_num, attr, value, request_options=request_options
        )
        return _response.data

    def protocol_netflow_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Optional[typing.Any]]]:
        """
        Show list of NETFLOW exports

        Parameters
        ----------
        agent_num : int
            Agent to show NETFLOW statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Optional[typing.Any]]]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.netflow.protocol_netflow_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the NETFLOW argument structure

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
        client.netflow.protocol_netflow_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigNetflow:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the NETFLOW configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigNetflow
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.netflow.protocol_netflow_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show NETFLOW statistics

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
        client.netflow.protocol_netflow_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigNetflow:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether NETFLOW tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigNetflow
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.netflow.protocol_netflow_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_halt(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Halt NETFLOW traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
        client.netflow.protocol_netflow_halt(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_halt(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_reload(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Reload NETFLOW configuration before resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
        client.netflow.protocol_netflow_reload(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_reload(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_resume(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
        client.netflow.protocol_netflow_resume(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_netflow_resume(agent_num, request_options=request_options)
        return _response.data

    def protocol_netflow_set_collector(
        self, agent_num: int, collector_ip: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Allow changing collector without stopping agent

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        collector_ip : str
            file name to load config

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
        client.netflow.protocol_netflow_set_collector(
            agent_num=1,
            collector_ip="collectorIP",
        )
        """
        _response = self._raw_client.protocol_netflow_set_collector(
            agent_num, collector_ip, request_options=request_options
        )
        return _response.data

    def protocol_netflow_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW configuration

        argument : str
            Parameter to set the NETFLOW configuration

        value : str
            Value to set the NETFLOW configuration

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
        client.netflow.protocol_netflow_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_netflow_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_netflow_set_file_name(
        self, agent_num: int, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Allow reloading the configuration file for an agent without stopping agent

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        file_name : str
            file name to load config

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
        client.netflow.protocol_netflow_set_file_name(
            agent_num=1,
            file_name="fileName",
        )
        """
        _response = self._raw_client.protocol_netflow_set_file_name(
            agent_num, file_name, request_options=request_options
        )
        return _response.data

    def protocol_netflow_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW tracing

        enable_or_not : str
            Value to set the NETFLOW tracing

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
        client.netflow.protocol_netflow_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_netflow_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    def protocol_netflow_get_stats_hdr(
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
        client.netflow.protocol_netflow_get_stats_hdr()
        """
        _response = self._raw_client.protocol_netflow_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncNetflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetflowClient
        """
        return self._raw_client

    async def protocol_netflow_change_dfs(
        self, agent_num: int, interval: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Interval in msec .

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        interval : int
            NETFLOW export interval

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
            await client.netflow.protocol_netflow_change_dfs(
                agent_num=1,
                interval=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_change_dfs(
            agent_num, interval, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_change_tfs(
        self, agent_num: int, interval: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Interval in msec .

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        interval : int
            NETFLOW export interval

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
            await client.netflow.protocol_netflow_change_tfs(
                agent_num=1,
                interval=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_change_tfs(
            agent_num, interval, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_change_attr(
        self,
        agent_num: int,
        flowset_uid: int,
        field_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Change attributes

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        flowset_uid : int

        field_num : int

        attr : str

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
            await client.netflow.protocol_netflow_change_attr(
                agent_num=1,
                flowset_uid=1,
                field_num=1,
                attr="attr",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_change_attr(
            agent_num, flowset_uid, field_num, attr, value, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Optional[typing.Any]]]:
        """
        Show list of NETFLOW exports

        Parameters
        ----------
        agent_num : int
            Agent to show NETFLOW statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Optional[typing.Any]]]
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
            await client.netflow.protocol_netflow_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the NETFLOW argument structure

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
            await client.netflow.protocol_netflow_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigNetflow:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the NETFLOW configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigNetflow
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
            await client.netflow.protocol_netflow_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show NETFLOW statistics

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
            await client.netflow.protocol_netflow_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigNetflow:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether NETFLOW tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigNetflow
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
            await client.netflow.protocol_netflow_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_halt(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Halt NETFLOW traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
            await client.netflow.protocol_netflow_halt(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_halt(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_reload(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Reload NETFLOW configuration before resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
            await client.netflow.protocol_netflow_reload(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_reload(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_resume(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

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
            await client.netflow.protocol_netflow_resume(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_resume(agent_num, request_options=request_options)
        return _response.data

    async def protocol_netflow_set_collector(
        self, agent_num: int, collector_ip: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Allow changing collector without stopping agent

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        collector_ip : str
            file name to load config

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
            await client.netflow.protocol_netflow_set_collector(
                agent_num=1,
                collector_ip="collectorIP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_set_collector(
            agent_num, collector_ip, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW configuration

        argument : str
            Parameter to set the NETFLOW configuration

        value : str
            Value to set the NETFLOW configuration

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
            await client.netflow.protocol_netflow_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_set_file_name(
        self, agent_num: int, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Allow reloading the configuration file for an agent without stopping agent

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW

        file_name : str
            file name to load config

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
            await client.netflow.protocol_netflow_set_file_name(
                agent_num=1,
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_set_file_name(
            agent_num, file_name, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the NETFLOW tracing

        enable_or_not : str
            Value to set the NETFLOW tracing

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
            await client.netflow.protocol_netflow_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_netflow_get_stats_hdr(
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
            await client.netflow.protocol_netflow_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_netflow_get_stats_hdr(request_options=request_options)
        return _response.data
