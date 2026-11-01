

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSourceInputSwitchClient, RawSourceInputSwitchClient
from .types.set_player_cmd_switch_mode_request_mode import SetPlayerCmdSwitchModeRequestMode


class SourceInputSwitchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceInputSwitchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceInputSwitchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceInputSwitchClient
        """
        return self._raw_client

    def set_player_cmd_switch_mode(
        self, mode: SetPlayerCmdSwitchModeRequestMode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:switchmode:%s

        the mode can be the text as below:
        - line-in (it refers to aux-in too)
        - bluetooth
        - optical
        - udisk
        - wifi
        - HDMI

        Parameters
        ----------
        mode : SetPlayerCmdSwitchModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern.source_input_switch import SetPlayerCmdSwitchModeRequestMode

        from fern import FernApi

        client = FernApi()
        client.source_input_switch.set_player_cmd_switch_mode(
            mode=SetPlayerCmdSwitchModeRequestMode.LINE_IN,
        )
        """
        _response = self._raw_client.set_player_cmd_switch_mode(mode, request_options=request_options)
        return _response.data


class AsyncSourceInputSwitchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceInputSwitchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceInputSwitchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceInputSwitchClient
        """
        return self._raw_client

    async def set_player_cmd_switch_mode(
        self, mode: SetPlayerCmdSwitchModeRequestMode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:switchmode:%s

        the mode can be the text as below:
        - line-in (it refers to aux-in too)
        - bluetooth
        - optical
        - udisk
        - wifi
        - HDMI

        Parameters
        ----------
        mode : SetPlayerCmdSwitchModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern.source_input_switch import SetPlayerCmdSwitchModeRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.source_input_switch.set_player_cmd_switch_mode(
                mode=SetPlayerCmdSwitchModeRequestMode.LINE_IN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_switch_mode(mode, request_options=request_options)
        return _response.data
