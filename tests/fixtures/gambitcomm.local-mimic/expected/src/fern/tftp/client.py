

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_tftp import ConfigTftp
from .raw_client import AsyncRawTftpClient, RawTftpClient


class TftpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTftpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTftpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTftpClient
        """
        return self._raw_client

    def protocol_tftp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's TFTP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TFTP argument structure

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
        client.tftp.protocol_tftp_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tftp_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_tftp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTftp:
        """
        Agent's TFTP configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TFTP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTftp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tftp.protocol_tftp_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tftp_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_tftp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

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
        client.tftp.protocol_tftp_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tftp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_tftp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTftp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TFTP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTftp
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tftp.protocol_tftp_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_tftp_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_tftp_session_read(
        self, agent_num: int, srcfile: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Session ID is returned

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

        srcfile : str
            File name to retrieve from server

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
        client.tftp.protocol_tftp_session_read(
            agent_num=1,
            srcfile="srcfile",
        )
        """
        _response = self._raw_client.protocol_tftp_session_read(agent_num, srcfile, request_options=request_options)
        return _response.data

    def protocol_tftp_session_write(
        self, agent_num: int, srcfile: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Session ID is returned

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

        srcfile : str
            File name to upload to server

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
        client.tftp.protocol_tftp_session_write(
            agent_num=1,
            srcfile="srcfile",
        )
        """
        _response = self._raw_client.protocol_tftp_session_write(agent_num, srcfile, request_options=request_options)
        return _response.data

    def protocol_tftp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TFTP configuration

        Parameters
        ----------
        agent_num : int
            Agent to set the TFTP configuration

        argument : str
            Parameter to set the TFTP configuration

        value : str
            Value to set the TFTP configuration

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
        client.tftp.protocol_tftp_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_tftp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_tftp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TFTP tracing

        enable_or_not : str
            Value to set the TFTP tracing

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
        client.tftp.protocol_tftp_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_tftp_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_tftp_session_get_parameter(
        self,
        agent_num: int,
        session_id: str,
        parameter: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameter is server , port , or dstfile

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP parameter

        session_id : str
            SessionID

        parameter : str
            Parameter to show

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
        client.tftp.protocol_tftp_session_get_parameter(
            agent_num=1,
            session_id="sessionID",
            parameter="parameter",
        )
        """
        _response = self._raw_client.protocol_tftp_session_get_parameter(
            agent_num, session_id, parameter, request_options=request_options
        )
        return _response.data

    def protocol_tftp_session_set_parameter(
        self,
        agent_num: int,
        session_id: str,
        parameter: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameter is server , port , or dstfile

        Parameters
        ----------
        agent_num : int
            Agent to set TFTP parameter

        session_id : str
            SessionID

        parameter : str
            Parameter to set

        value : str
            Value to set

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
        client.tftp.protocol_tftp_session_set_parameter(
            agent_num=1,
            session_id="sessionID",
            parameter="parameter",
            value="value",
        )
        """
        _response = self._raw_client.protocol_tftp_session_set_parameter(
            agent_num, session_id, parameter, value, request_options=request_options
        )
        return _response.data

    def protocol_tftp_session_start(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start uploading or downloading the file

        Parameters
        ----------
        agent_num : int
            Agent to start TFTP transaction

        session_id : str
            SessionID

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
        client.tftp.protocol_tftp_session_start(
            agent_num=1,
            session_id="sessionID",
        )
        """
        _response = self._raw_client.protocol_tftp_session_start(agent_num, session_id, request_options=request_options)
        return _response.data

    def protocol_tftp_session_status(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Status includes running state, bytes transfered, and time elapsed

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP transaction

        session_id : str
            SessionID

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
        client.tftp.protocol_tftp_session_status(
            agent_num=1,
            session_id="sessionID",
        )
        """
        _response = self._raw_client.protocol_tftp_session_status(
            agent_num, session_id, request_options=request_options
        )
        return _response.data

    def protocol_tftp_session_stop(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop uploading or downloading the file

        Parameters
        ----------
        agent_num : int
            Agent to stop TFTP transaction

        session_id : str
            SessionID

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
        client.tftp.protocol_tftp_session_stop(
            agent_num=1,
            session_id="sessionID",
        )
        """
        _response = self._raw_client.protocol_tftp_session_stop(agent_num, session_id, request_options=request_options)
        return _response.data

    def protocol_tftp_get_stats_hdr(
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
        client.tftp.protocol_tftp_get_stats_hdr()
        """
        _response = self._raw_client.protocol_tftp_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncTftpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTftpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTftpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTftpClient
        """
        return self._raw_client

    async def protocol_tftp_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Agent's TFTP configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the TFTP argument structure

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
            await client.tftp.protocol_tftp_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tftp_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTftp:
        """
        Agent's TFTP configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TFTP configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTftp
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
            await client.tftp.protocol_tftp_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tftp_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

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
            await client.tftp.protocol_tftp_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tftp_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigTftp:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TFTP tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigTftp
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
            await client.tftp.protocol_tftp_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_tftp_session_read(
        self, agent_num: int, srcfile: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Session ID is returned

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

        srcfile : str
            File name to retrieve from server

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
            await client.tftp.protocol_tftp_session_read(
                agent_num=1,
                srcfile="srcfile",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_read(
            agent_num, srcfile, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_write(
        self, agent_num: int, srcfile: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Session ID is returned

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP statistics

        srcfile : str
            File name to upload to server

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
            await client.tftp.protocol_tftp_session_write(
                agent_num=1,
                srcfile="srcfile",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_write(
            agent_num, srcfile, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's TFTP configuration

        Parameters
        ----------
        agent_num : int
            Agent to set the TFTP configuration

        argument : str
            Parameter to set the TFTP configuration

        value : str
            Value to set the TFTP configuration

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
            await client.tftp.protocol_tftp_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TFTP tracing

        enable_or_not : str
            Value to set the TFTP tracing

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
            await client.tftp.protocol_tftp_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_get_parameter(
        self,
        agent_num: int,
        session_id: str,
        parameter: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameter is server , port , or dstfile

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP parameter

        session_id : str
            SessionID

        parameter : str
            Parameter to show

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
            await client.tftp.protocol_tftp_session_get_parameter(
                agent_num=1,
                session_id="sessionID",
                parameter="parameter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_get_parameter(
            agent_num, session_id, parameter, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_set_parameter(
        self,
        agent_num: int,
        session_id: str,
        parameter: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameter is server , port , or dstfile

        Parameters
        ----------
        agent_num : int
            Agent to set TFTP parameter

        session_id : str
            SessionID

        parameter : str
            Parameter to set

        value : str
            Value to set

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
            await client.tftp.protocol_tftp_session_set_parameter(
                agent_num=1,
                session_id="sessionID",
                parameter="parameter",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_set_parameter(
            agent_num, session_id, parameter, value, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_start(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Start uploading or downloading the file

        Parameters
        ----------
        agent_num : int
            Agent to start TFTP transaction

        session_id : str
            SessionID

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
            await client.tftp.protocol_tftp_session_start(
                agent_num=1,
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_start(
            agent_num, session_id, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_status(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Status includes running state, bytes transfered, and time elapsed

        Parameters
        ----------
        agent_num : int
            Agent to show TFTP transaction

        session_id : str
            SessionID

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
            await client.tftp.protocol_tftp_session_status(
                agent_num=1,
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_status(
            agent_num, session_id, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_session_stop(
        self, agent_num: int, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stop uploading or downloading the file

        Parameters
        ----------
        agent_num : int
            Agent to stop TFTP transaction

        session_id : str
            SessionID

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
            await client.tftp.protocol_tftp_session_stop(
                agent_num=1,
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_session_stop(
            agent_num, session_id, request_options=request_options
        )
        return _response.data

    async def protocol_tftp_get_stats_hdr(
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
            await client.tftp.protocol_tftp_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_tftp_get_stats_hdr(request_options=request_options)
        return _response.data
