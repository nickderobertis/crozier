

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_ipmi import ConfigIpmi
from .raw_client import AsyncRawIpmiClient, RawIpmiClient


class IpmiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpmiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpmiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpmiClient
        """
        return self._raw_client

    def protocol_ipmi_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the IPMI argument structure

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
        client.ipmi.protocol_ipmi_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ipmi_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_ipmi_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigIpmi:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the IPMI configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigIpmi
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ipmi.protocol_ipmi_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ipmi_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_ipmi_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show IPMI statistics

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
        client.ipmi.protocol_ipmi_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ipmi_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_ipmi_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigIpmi:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether IPMI tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigIpmi
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ipmi.protocol_ipmi_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_ipmi_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_ipmi_get_attr(
        self, agent_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

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
        client.ipmi.protocol_ipmi_get_attr(
            agent_num=1,
            attr="attr",
        )
        """
        _response = self._raw_client.protocol_ipmi_get_attr(agent_num, attr, request_options=request_options)
        return _response.data

    def protocol_ipmi_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI configuration

        argument : str
            Parameter to set the IPMI configuration

        value : str
            Value to set the IPMI configuration

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
        client.ipmi.protocol_ipmi_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_ipmi_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_ipmi_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

        enable_or_not : str
            Value to set the IPMI tracing

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
        client.ipmi.protocol_ipmi_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_ipmi_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_ipmi_set_attr(
        self, agent_num: int, attr: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

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
        client.ipmi.protocol_ipmi_set_attr(
            agent_num=1,
            attr="attr",
            value="value",
        )
        """
        _response = self._raw_client.protocol_ipmi_set_attr(agent_num, attr, value, request_options=request_options)
        return _response.data

    def protocol_ipmi_get_stats_hdr(
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
        client.ipmi.protocol_ipmi_get_stats_hdr()
        """
        _response = self._raw_client.protocol_ipmi_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncIpmiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpmiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpmiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpmiClient
        """
        return self._raw_client

    async def protocol_ipmi_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the IPMI argument structure

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
            await client.ipmi.protocol_ipmi_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ipmi_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigIpmi:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the IPMI configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigIpmi
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
            await client.ipmi.protocol_ipmi_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ipmi_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show IPMI statistics

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
            await client.ipmi.protocol_ipmi_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ipmi_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigIpmi:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether IPMI tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigIpmi
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
            await client.ipmi.protocol_ipmi_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_ipmi_get_attr(
        self, agent_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

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
            await client.ipmi.protocol_ipmi_get_attr(
                agent_num=1,
                attr="attr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_attr(agent_num, attr, request_options=request_options)
        return _response.data

    async def protocol_ipmi_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI configuration

        argument : str
            Parameter to set the IPMI configuration

        value : str
            Value to set the IPMI configuration

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
            await client.ipmi.protocol_ipmi_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_ipmi_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

        enable_or_not : str
            Value to set the IPMI tracing

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
            await client.ipmi.protocol_ipmi_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_ipmi_set_attr(
        self, agent_num: int, attr: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

        Parameters
        ----------
        agent_num : int
            Agent to set the IPMI tracing

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
            await client.ipmi.protocol_ipmi_set_attr(
                agent_num=1,
                attr="attr",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_set_attr(
            agent_num, attr, value, request_options=request_options
        )
        return _response.data

    async def protocol_ipmi_get_stats_hdr(
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
            await client.ipmi.protocol_ipmi_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_ipmi_get_stats_hdr(request_options=request_options)
        return _response.data
