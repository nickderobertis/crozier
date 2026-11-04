

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioEnhancementClient, RawAudioEnhancementClient
from .types.create_audio_enhancement_request_enhancement_engine import CreateAudioEnhancementRequestEnhancementEngine
from .types.create_audio_enhancement_response import CreateAudioEnhancementResponse
from .types.get_audio_enhancement_response import GetAudioEnhancementResponse
from .types.list_audio_enhancements_response import ListAudioEnhancementsResponse


OMIT = typing.cast(typing.Any, ...)


class AudioEnhancementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioEnhancementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioEnhancementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioEnhancementClient
        """
        return self._raw_client

    def list_audio_enhancements(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAudioEnhancementsResponse:
        """
        Returns a paginated list of all audio enhancements for your team, ordered by most recent first.

        Parameters
        ----------
        page : int
            Page number (starting from 1).

        page_size : typing.Optional[int]
            Items per page (10 to 1000). Default 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioEnhancementsResponse
            List of enhancements

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_enhancement.list_audio_enhancements(
            page=1,
        )
        """
        _response = self._raw_client.list_audio_enhancements(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_audio_enhancement(
        self,
        *,
        audio_file: core.File,
        enhancement_engine: typing.Optional[CreateAudioEnhancementRequestEnhancementEngine] = OMIT,
        remove_noise: typing.Optional[bool] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        studio_sound: typing.Optional[bool] = OMIT,
        enhancement_level: typing.Optional[float] = OMIT,
        loudness_target_level: typing.Optional[int] = OMIT,
        loudness_peak_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAudioEnhancementResponse:
        """
        Submit an audio file for enhancement. Processing happens asynchronously in the background.
        The API defaults to the v2 enhancement engine. The v1 engine is legacy and will be sunset in a future release.

        Parameters
        ----------
        audio_file : core.File
            See core.File for more documentation

        enhancement_engine : typing.Optional[CreateAudioEnhancementRequestEnhancementEngine]
            Enhancement engine to use. Default is v2.

        remove_noise : typing.Optional[bool]
            Remove background noise. Engine v2 only.

        normalize : typing.Optional[bool]
            Normalize audio levels. Engine v2 only.

        studio_sound : typing.Optional[bool]
            Apply studio-quality enhancement. Engine v2 only.

        enhancement_level : typing.Optional[float]
            Enhancement intensity (0.0 to 1.0). Engine v1 only (legacy).

        loudness_target_level : typing.Optional[int]
            Target loudness in LUFS. Engine v1 only (legacy).

        loudness_peak_limit : typing.Optional[int]
            Peak limit in dBTP. Engine v1 only (legacy).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAudioEnhancementResponse
            Enhancement job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_enhancement.create_audio_enhancement()
        """
        _response = self._raw_client.create_audio_enhancement(
            audio_file=audio_file,
            enhancement_engine=enhancement_engine,
            remove_noise=remove_noise,
            normalize=normalize,
            studio_sound=studio_sound,
            enhancement_level=enhancement_level,
            loudness_target_level=loudness_target_level,
            loudness_peak_limit=loudness_peak_limit,
            request_options=request_options,
        )
        return _response.data

    def get_audio_enhancement(
        self, enhancement_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioEnhancementResponse:
        """
        Poll this endpoint to check the status of an enhancement job and retrieve the download URL when complete.

        Parameters
        ----------
        enhancement_uuid : str
            The UUID returned from the create endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioEnhancementResponse
            Enhancement details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.audio_enhancement.get_audio_enhancement(
            enhancement_uuid="enhancement_uuid",
        )
        """
        _response = self._raw_client.get_audio_enhancement(enhancement_uuid, request_options=request_options)
        return _response.data


class AsyncAudioEnhancementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioEnhancementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioEnhancementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioEnhancementClient
        """
        return self._raw_client

    async def list_audio_enhancements(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAudioEnhancementsResponse:
        """
        Returns a paginated list of all audio enhancements for your team, ordered by most recent first.

        Parameters
        ----------
        page : int
            Page number (starting from 1).

        page_size : typing.Optional[int]
            Items per page (10 to 1000). Default 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAudioEnhancementsResponse
            List of enhancements

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_enhancement.list_audio_enhancements(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_audio_enhancements(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_audio_enhancement(
        self,
        *,
        audio_file: core.File,
        enhancement_engine: typing.Optional[CreateAudioEnhancementRequestEnhancementEngine] = OMIT,
        remove_noise: typing.Optional[bool] = OMIT,
        normalize: typing.Optional[bool] = OMIT,
        studio_sound: typing.Optional[bool] = OMIT,
        enhancement_level: typing.Optional[float] = OMIT,
        loudness_target_level: typing.Optional[int] = OMIT,
        loudness_peak_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAudioEnhancementResponse:
        """
        Submit an audio file for enhancement. Processing happens asynchronously in the background.
        The API defaults to the v2 enhancement engine. The v1 engine is legacy and will be sunset in a future release.

        Parameters
        ----------
        audio_file : core.File
            See core.File for more documentation

        enhancement_engine : typing.Optional[CreateAudioEnhancementRequestEnhancementEngine]
            Enhancement engine to use. Default is v2.

        remove_noise : typing.Optional[bool]
            Remove background noise. Engine v2 only.

        normalize : typing.Optional[bool]
            Normalize audio levels. Engine v2 only.

        studio_sound : typing.Optional[bool]
            Apply studio-quality enhancement. Engine v2 only.

        enhancement_level : typing.Optional[float]
            Enhancement intensity (0.0 to 1.0). Engine v1 only (legacy).

        loudness_target_level : typing.Optional[int]
            Target loudness in LUFS. Engine v1 only (legacy).

        loudness_peak_limit : typing.Optional[int]
            Peak limit in dBTP. Engine v1 only (legacy).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAudioEnhancementResponse
            Enhancement job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_enhancement.create_audio_enhancement()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_audio_enhancement(
            audio_file=audio_file,
            enhancement_engine=enhancement_engine,
            remove_noise=remove_noise,
            normalize=normalize,
            studio_sound=studio_sound,
            enhancement_level=enhancement_level,
            loudness_target_level=loudness_target_level,
            loudness_peak_limit=loudness_peak_limit,
            request_options=request_options,
        )
        return _response.data

    async def get_audio_enhancement(
        self, enhancement_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioEnhancementResponse:
        """
        Poll this endpoint to check the status of an enhancement job and retrieve the download URL when complete.

        Parameters
        ----------
        enhancement_uuid : str
            The UUID returned from the create endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioEnhancementResponse
            Enhancement details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.audio_enhancement.get_audio_enhancement(
                enhancement_uuid="enhancement_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_enhancement(enhancement_uuid, request_options=request_options)
        return _response.data
