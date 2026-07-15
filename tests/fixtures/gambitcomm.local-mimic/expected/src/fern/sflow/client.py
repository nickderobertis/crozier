

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_sflow import ConfigSflow
from .raw_client import AsyncRawSflowClient, RawSflowClient


class SflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSflowClient
        """
        return self._raw_client

    def protocol_sflow_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SFLOW argument structure

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
        client.sflow.protocol_sflow_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSflow:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SFLOW configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSflow
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sflow.protocol_sflow_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SFLOW statistics

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
        client.sflow.protocol_sflow_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSflow:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SFLOW tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSflow
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.sflow.protocol_sflow_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_halt(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Halt SFLOW traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
        client.sflow.protocol_sflow_halt(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_halt(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_reload(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Reload SFLOW configuration before resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
        client.sflow.protocol_sflow_reload(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_reload(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_resume(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
        client.sflow.protocol_sflow_resume(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_sflow_resume(agent_num, request_options=request_options)
        return _response.data

    def protocol_sflow_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW configuration

        argument : str
            Parameter to set the SFLOW configuration

        value : str
            Value to set the SFLOW configuration

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
        client.sflow.protocol_sflow_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_sflow_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_sflow_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW tracing

        enable_or_not : str
            Value to set the SFLOW tracing

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
        client.sflow.protocol_sflow_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_sflow_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_sflow_get_stats_hdr(
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
        client.sflow.protocol_sflow_get_stats_hdr()
        """
        _response = self._raw_client.protocol_sflow_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncSflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSflowClient
        """
        return self._raw_client

    async def protocol_sflow_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SFLOW argument structure

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
            await client.sflow.protocol_sflow_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSflow:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the SFLOW configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSflow
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
            await client.sflow.protocol_sflow_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show SFLOW statistics

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
            await client.sflow.protocol_sflow_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSflow:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether SFLOW tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSflow
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
            await client.sflow.protocol_sflow_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_halt(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Halt SFLOW traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
            await client.sflow.protocol_sflow_halt(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_halt(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_reload(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Reload SFLOW configuration before resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
            await client.sflow.protocol_sflow_reload(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_reload(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_resume(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Resuming traffic

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW

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
            await client.sflow.protocol_sflow_resume(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_resume(agent_num, request_options=request_options)
        return _response.data

    async def protocol_sflow_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW configuration

        argument : str
            Parameter to set the SFLOW configuration

        value : str
            Value to set the SFLOW configuration

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
            await client.sflow.protocol_sflow_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_sflow_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the SFLOW tracing

        enable_or_not : str
            Value to set the SFLOW tracing

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
            await client.sflow.protocol_sflow_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_sflow_get_stats_hdr(
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
            await client.sflow.protocol_sflow_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_sflow_get_stats_hdr(request_options=request_options)
        return _response.data
