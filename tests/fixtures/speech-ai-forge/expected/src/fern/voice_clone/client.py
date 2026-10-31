

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoiceCloneClient, RawVoiceCloneClient


OMIT = typing.cast(typing.Any, ...)


class VoiceCloneClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoiceCloneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoiceCloneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoiceCloneClient
        """
        return self._raw_client

    def voice_clone(
        self,
        *,
        src_audio: core.File,
        ref_spk: typing.Optional[str] = None,
        spk_emotion: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        tau: typing.Optional[float] = None,
        format: typing.Optional[str] = None,
        ref_audio: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Voice cloning API

        **Deprecated**
        This API is deprecated and will be removed in the future.
        Please use the `TTS API` instead.

        Parameters
        ----------
        src_audio : core.File
            See core.File for more documentation

        ref_spk : typing.Optional[str]

        spk_emotion : typing.Optional[str]

        model : typing.Optional[str]

        tau : typing.Optional[float]

        format : typing.Optional[str]

        ref_audio : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.voice_clone.voice_clone()
        """
        _response = self._raw_client.voice_clone(
            src_audio=src_audio,
            ref_spk=ref_spk,
            spk_emotion=spk_emotion,
            model=model,
            tau=tau,
            format=format,
            ref_audio=ref_audio,
            request_options=request_options,
        )
        return _response.data


class AsyncVoiceCloneClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoiceCloneClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoiceCloneClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoiceCloneClient
        """
        return self._raw_client

    async def voice_clone(
        self,
        *,
        src_audio: core.File,
        ref_spk: typing.Optional[str] = None,
        spk_emotion: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        tau: typing.Optional[float] = None,
        format: typing.Optional[str] = None,
        ref_audio: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Voice cloning API

        **Deprecated**
        This API is deprecated and will be removed in the future.
        Please use the `TTS API` instead.

        Parameters
        ----------
        src_audio : core.File
            See core.File for more documentation

        ref_spk : typing.Optional[str]

        spk_emotion : typing.Optional[str]

        model : typing.Optional[str]

        tau : typing.Optional[float]

        format : typing.Optional[str]

        ref_audio : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.voice_clone.voice_clone()


        asyncio.run(main())
        """
        _response = await self._raw_client.voice_clone(
            src_audio=src_audio,
            ref_spk=ref_spk,
            spk_emotion=spk_emotion,
            model=model,
            tau=tau,
            format=format,
            ref_audio=ref_audio,
            request_options=request_options,
        )
        return _response.data
