

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioEditClient, RawAudioEditClient
from .types.create_audio_edit_response import CreateAudioEditResponse
from .types.get_audio_edit_response import GetAudioEditResponse
from .types.list_audio_edits_response import ListAudioEditsResponse


OMIT = typing.cast(typing.Any, ...)


class AudioEditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioEditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioEditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioEditClient
        """
        return self._raw_client

    def list_audio_edits(
        self, *, page: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAudioEditsResponse:
        """
        Retrieve paginated list of audio edits

        Parameters
        ----------
        page : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioEditsResponse
            List of audio edits

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_edit.list_audio_edits(
            page=1,
        )
        """
        _response = self._raw_client.list_audio_edits(page=page, request_options=request_options)
        return _response.data

    def create_audio_edit(
        self,
        *,
        input_audio: core.File,
        original_transcript: str,
        target_transcript: str,
        voice_uuid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAudioEditResponse:
        """
        Edit audio segments using voice synthesis

        Parameters
        ----------
        input_audio : core.File
            See core.File for more documentation

        original_transcript : str
            Accurate transcript of the uploaded audio

        target_transcript : str
            Desired replacement text

        voice_uuid : str
            Voice used to render the edited segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAudioEditResponse
            Edit job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_edit.create_audio_edit(
            original_transcript="original_transcript",
            target_transcript="target_transcript",
            voice_uuid="voice_uuid",
        )
        """
        _response = self._raw_client.create_audio_edit(
            input_audio=input_audio,
            original_transcript=original_transcript,
            target_transcript=target_transcript,
            voice_uuid=voice_uuid,
            request_options=request_options,
        )
        return _response.data

    def get_audio_edit(
        self, audio_edit_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioEditResponse:
        """
        Get status and result of an audio edit

        Parameters
        ----------
        audio_edit_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioEditResponse
            Audio edit details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_edit.get_audio_edit(
            audio_edit_uuid="audio_edit_uuid",
        )
        """
        _response = self._raw_client.get_audio_edit(audio_edit_uuid, request_options=request_options)
        return _response.data


class AsyncAudioEditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioEditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioEditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioEditClient
        """
        return self._raw_client

    async def list_audio_edits(
        self, *, page: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAudioEditsResponse:
        """
        Retrieve paginated list of audio edits

        Parameters
        ----------
        page : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioEditsResponse
            List of audio edits

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_edit.list_audio_edits(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_audio_edits(page=page, request_options=request_options)
        return _response.data

    async def create_audio_edit(
        self,
        *,
        input_audio: core.File,
        original_transcript: str,
        target_transcript: str,
        voice_uuid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAudioEditResponse:
        """
        Edit audio segments using voice synthesis

        Parameters
        ----------
        input_audio : core.File
            See core.File for more documentation

        original_transcript : str
            Accurate transcript of the uploaded audio

        target_transcript : str
            Desired replacement text

        voice_uuid : str
            Voice used to render the edited segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAudioEditResponse
            Edit job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_edit.create_audio_edit(
                original_transcript="original_transcript",
                target_transcript="target_transcript",
                voice_uuid="voice_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_audio_edit(
            input_audio=input_audio,
            original_transcript=original_transcript,
            target_transcript=target_transcript,
            voice_uuid=voice_uuid,
            request_options=request_options,
        )
        return _response.data

    async def get_audio_edit(
        self, audio_edit_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioEditResponse:
        """
        Get status and result of an audio edit

        Parameters
        ----------
        audio_edit_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioEditResponse
            Audio edit details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_edit.get_audio_edit(
                audio_edit_uuid="audio_edit_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_edit(audio_edit_uuid, request_options=request_options)
        return _response.data
