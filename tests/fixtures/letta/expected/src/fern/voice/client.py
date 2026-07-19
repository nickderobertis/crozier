

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoiceClient, RawVoiceClient


OMIT = typing.cast(typing.Any, ...)


class VoiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoiceClient
        """
        return self._raw_client

    def create_voice_chat_completions(
        self,
        agent_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        DEPRECATED: This voice-beta endpoint has been deprecated.

        The voice functionality has been integrated into the main chat completions endpoint.
        Please use the standard /v1/agents/{agent_id}/messages endpoint instead.

        This endpoint will be removed in a future version.

        Parameters
        ----------
        agent_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice.create_voice_chat_completions(
            agent_id="agent_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_voice_chat_completions(
            agent_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncVoiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoiceClient
        """
        return self._raw_client

    async def create_voice_chat_completions(
        self,
        agent_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        DEPRECATED: This voice-beta endpoint has been deprecated.

        The voice functionality has been integrated into the main chat completions endpoint.
        Please use the standard /v1/agents/{agent_id}/messages endpoint instead.

        This endpoint will be removed in a future version.

        Parameters
        ----------
        agent_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice.create_voice_chat_completions(
                agent_id="agent_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voice_chat_completions(
            agent_id, request=request, request_options=request_options
        )
        return _response.data
