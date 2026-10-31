

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.audio_reference import AudioReference
from ..types.base_response import BaseResponse
from .raw_client import AsyncRawSpeakerClient, RawSpeakerClient


OMIT = typing.cast(typing.Any, ...)


class SpeakerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpeakerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpeakerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpeakerClient
        """
        return self._raw_client

    def list_speakers(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        List all available speakers with optional pagination and detail control.

        - `detailed`: If true, returns complete metadata including references and embeddings.
        - `offset` / `limit`: Support for paginated speaker listing.

        Parameters
        ----------
        detailed : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.list_speakers()
        """
        _response = self._raw_client.list_speakers(
            detailed=detailed, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def refresh_speakers(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Force reload of all speaker metadata from disk.
        Use this when files are modified externally or newly added.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.refresh_speakers()
        """
        _response = self._raw_client.refresh_speakers(request_options=request_options)
        return _response.data

    def update_speakers(
        self,
        *,
        speakers: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Batch update multiple speakers by providing a list of speaker JSON configs.

        Each speaker must already exist (matched by ID).
        Will overwrite corresponding fields and persist changes to disk.

        Parameters
        ----------
        speakers : typing.Sequence[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.update_speakers(
            speakers=[{"key": "value"}],
        )
        """
        _response = self._raw_client.update_speakers(speakers=speakers, request_options=request_options)
        return _response.data

    def create_speaker(
        self,
        *,
        name: str,
        gender: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        wavs: typing.Optional[typing.Sequence[AudioReference]] = OMIT,
        save_file: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Create a new speaker profile with optional reference audios.

        - `name` is required and used as unique identifier.
        - `wavs` is a list of audio samples (base64-encoded) and reference texts for embedding.
        - `save_file`: If true, the speaker will be saved to disk and available after refresh.

        Parameters
        ----------
        name : str

        gender : typing.Optional[str]

        author : typing.Optional[str]

        desc : typing.Optional[str]

        version : typing.Optional[str]

        wavs : typing.Optional[typing.Sequence[AudioReference]]

        save_file : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.create_speaker(
            name="name",
        )
        """
        _response = self._raw_client.create_speaker(
            name=name,
            gender=gender,
            author=author,
            desc=desc,
            version=version,
            wavs=wavs,
            save_file=save_file,
            request_options=request_options,
        )
        return _response.data

    def update_speaker(
        self,
        *,
        json: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Update a single speaker's configuration by full JSON override.

        The speaker must already exist (matched by ID).
        Fields like name, gender, refs, etc., will be updated accordingly.

        Parameters
        ----------
        json : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.update_speaker()
        """
        _response = self._raw_client.update_speaker(json=json, request_options=request_options)
        return _response.data

    def speaker_detail(
        self,
        *,
        id: str,
        with_emb: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Fetch metadata of a specific speaker by ID.

        - `with_emb`: If true, includes embedding vectors and all reference data.

        Parameters
        ----------
        id : str

        with_emb : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.speaker.speaker_detail(
            id="id",
        )
        """
        _response = self._raw_client.speaker_detail(id=id, with_emb=with_emb, request_options=request_options)
        return _response.data


class AsyncSpeakerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpeakerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpeakerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpeakerClient
        """
        return self._raw_client

    async def list_speakers(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        List all available speakers with optional pagination and detail control.

        - `detailed`: If true, returns complete metadata including references and embeddings.
        - `offset` / `limit`: Support for paginated speaker listing.

        Parameters
        ----------
        detailed : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.list_speakers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_speakers(
            detailed=detailed, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def refresh_speakers(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Force reload of all speaker metadata from disk.
        Use this when files are modified externally or newly added.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.refresh_speakers()


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_speakers(request_options=request_options)
        return _response.data

    async def update_speakers(
        self,
        *,
        speakers: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Batch update multiple speakers by providing a list of speaker JSON configs.

        Each speaker must already exist (matched by ID).
        Will overwrite corresponding fields and persist changes to disk.

        Parameters
        ----------
        speakers : typing.Sequence[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.update_speakers(
                speakers=[{"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_speakers(speakers=speakers, request_options=request_options)
        return _response.data

    async def create_speaker(
        self,
        *,
        name: str,
        gender: typing.Optional[str] = OMIT,
        author: typing.Optional[str] = OMIT,
        desc: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        wavs: typing.Optional[typing.Sequence[AudioReference]] = OMIT,
        save_file: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Create a new speaker profile with optional reference audios.

        - `name` is required and used as unique identifier.
        - `wavs` is a list of audio samples (base64-encoded) and reference texts for embedding.
        - `save_file`: If true, the speaker will be saved to disk and available after refresh.

        Parameters
        ----------
        name : str

        gender : typing.Optional[str]

        author : typing.Optional[str]

        desc : typing.Optional[str]

        version : typing.Optional[str]

        wavs : typing.Optional[typing.Sequence[AudioReference]]

        save_file : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.create_speaker(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_speaker(
            name=name,
            gender=gender,
            author=author,
            desc=desc,
            version=version,
            wavs=wavs,
            save_file=save_file,
            request_options=request_options,
        )
        return _response.data

    async def update_speaker(
        self,
        *,
        json: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Update a single speaker's configuration by full JSON override.

        The speaker must already exist (matched by ID).
        Fields like name, gender, refs, etc., will be updated accordingly.

        Parameters
        ----------
        json : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.update_speaker()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_speaker(json=json, request_options=request_options)
        return _response.data

    async def speaker_detail(
        self,
        *,
        id: str,
        with_emb: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseResponse:
        """
        Fetch metadata of a specific speaker by ID.

        - `with_emb`: If true, includes embedding vectors and all reference data.

        Parameters
        ----------
        id : str

        with_emb : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.speaker.speaker_detail(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.speaker_detail(id=id, with_emb=with_emb, request_options=request_options)
        return _response.data
