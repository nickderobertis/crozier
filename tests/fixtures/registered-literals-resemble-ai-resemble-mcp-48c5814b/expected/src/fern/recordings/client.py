

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRecordingsClient, RawRecordingsClient
from .types.create_recording_response import CreateRecordingResponse
from .types.delete_recording_response import DeleteRecordingResponse
from .types.get_recording_response import GetRecordingResponse
from .types.list_recordings_response import ListRecordingsResponse
from .types.update_recording_response import UpdateRecordingResponse


OMIT = typing.cast(typing.Any, ...)


class RecordingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecordingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecordingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecordingsClient
        """
        return self._raw_client

    def list_recordings(
        self,
        voice_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRecordingsResponse:
        """
        List all recordings for a voice

        Parameters
        ----------
        voice_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRecordingsResponse
            List of recordings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recordings.list_recordings(
            voice_uuid="voice_uuid",
            page=1,
        )
        """
        _response = self._raw_client.list_recordings(
            voice_uuid, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_recording(
        self,
        voice_uuid: str,
        *,
        file: core.File,
        name: str,
        text: str,
        emotion: str,
        is_active: bool,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRecordingResponse:
        """
        Upload a new recording for voice training

        Parameters
        ----------
        voice_uuid : str

        file : core.File
            See core.File for more documentation

        name : str
            Display name

        text : str
            Transcript of the clip

        emotion : str
            Emotion label

        is_active : bool
            Include in training

        fill : typing.Optional[bool]
            Include for Resemble Fill

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRecordingResponse
            Recording created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recordings.create_recording(
            voice_uuid="voice_uuid",
            name="name",
            text="text",
            emotion="emotion",
            is_active=True,
        )
        """
        _response = self._raw_client.create_recording(
            voice_uuid,
            file=file,
            name=name,
            text=text,
            emotion=emotion,
            is_active=is_active,
            fill=fill,
            request_options=request_options,
        )
        return _response.data

    def get_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRecordingResponse:
        """
        Get recording details

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRecordingResponse
            Recording details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recordings.get_recording(
            voice_uuid="voice_uuid",
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.get_recording(voice_uuid, recording_id, request_options=request_options)
        return _response.data

    def delete_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRecordingResponse:
        """
        Delete a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRecordingResponse
            Recording deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recordings.delete_recording(
            voice_uuid="voice_uuid",
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.delete_recording(voice_uuid, recording_id, request_options=request_options)
        return _response.data

    def update_recording(
        self,
        voice_uuid: str,
        recording_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        emotion: typing.Optional[str] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRecordingResponse:
        """
        Update a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        name : typing.Optional[str]

        text : typing.Optional[str]

        emotion : typing.Optional[str]

        is_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRecordingResponse
            Recording updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.recordings.update_recording(
            voice_uuid="voice_uuid",
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.update_recording(
            voice_uuid,
            recording_id,
            name=name,
            text=text,
            emotion=emotion,
            is_active=is_active,
            request_options=request_options,
        )
        return _response.data


class AsyncRecordingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecordingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecordingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecordingsClient
        """
        return self._raw_client

    async def list_recordings(
        self,
        voice_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRecordingsResponse:
        """
        List all recordings for a voice

        Parameters
        ----------
        voice_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRecordingsResponse
            List of recordings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recordings.list_recordings(
                voice_uuid="voice_uuid",
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_recordings(
            voice_uuid, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_recording(
        self,
        voice_uuid: str,
        *,
        file: core.File,
        name: str,
        text: str,
        emotion: str,
        is_active: bool,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRecordingResponse:
        """
        Upload a new recording for voice training

        Parameters
        ----------
        voice_uuid : str

        file : core.File
            See core.File for more documentation

        name : str
            Display name

        text : str
            Transcript of the clip

        emotion : str
            Emotion label

        is_active : bool
            Include in training

        fill : typing.Optional[bool]
            Include for Resemble Fill

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRecordingResponse
            Recording created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recordings.create_recording(
                voice_uuid="voice_uuid",
                name="name",
                text="text",
                emotion="emotion",
                is_active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_recording(
            voice_uuid,
            file=file,
            name=name,
            text=text,
            emotion=emotion,
            is_active=is_active,
            fill=fill,
            request_options=request_options,
        )
        return _response.data

    async def get_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRecordingResponse:
        """
        Get recording details

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRecordingResponse
            Recording details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recordings.get_recording(
                voice_uuid="voice_uuid",
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recording(voice_uuid, recording_id, request_options=request_options)
        return _response.data

    async def delete_recording(
        self, voice_uuid: str, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRecordingResponse:
        """
        Delete a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRecordingResponse
            Recording deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recordings.delete_recording(
                voice_uuid="voice_uuid",
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_recording(voice_uuid, recording_id, request_options=request_options)
        return _response.data

    async def update_recording(
        self,
        voice_uuid: str,
        recording_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        emotion: typing.Optional[str] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRecordingResponse:
        """
        Update a recording

        Parameters
        ----------
        voice_uuid : str

        recording_id : str

        name : typing.Optional[str]

        text : typing.Optional[str]

        emotion : typing.Optional[str]

        is_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRecordingResponse
            Recording updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.recordings.update_recording(
                voice_uuid="voice_uuid",
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_recording(
            voice_uuid,
            recording_id,
            name=name,
            text=text,
            emotion=emotion,
            is_active=is_active,
            request_options=request_options,
        )
        return _response.data
