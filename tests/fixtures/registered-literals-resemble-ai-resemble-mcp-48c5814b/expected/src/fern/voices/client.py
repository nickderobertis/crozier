

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoicesClient, RawVoicesClient
from .types.build_voice_response import BuildVoiceResponse
from .types.create_voice_request_voice_type import CreateVoiceRequestVoiceType
from .types.create_voice_response import CreateVoiceResponse
from .types.delete_voice_response import DeleteVoiceResponse
from .types.get_voice_response import GetVoiceResponse
from .types.list_voices_response import ListVoicesResponse


OMIT = typing.cast(typing.Any, ...)


class VoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoicesClient
        """
        return self._raw_client

    def list_voices(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListVoicesResponse:
        """
        Retrieve voice metadata

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVoicesResponse
            List of voices

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.list_voices(
            page=1,
        )
        """
        _response = self._raw_client.list_voices(
            page=page, page_size=page_size, advanced=advanced, request_options=request_options
        )
        return _response.data

    def create_voice(
        self,
        *,
        name: str,
        voice_type: typing.Optional[CreateVoiceRequestVoiceType] = OMIT,
        dataset_url: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVoiceResponse:
        """
        Create a new voice

        Parameters
        ----------
        name : str

        voice_type : typing.Optional[CreateVoiceRequestVoiceType]

        dataset_url : typing.Optional[str]

        callback_uri : typing.Optional[str]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceResponse
            Voice created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.create_voice(
            name="name",
        )
        """
        _response = self._raw_client.create_voice(
            name=name,
            voice_type=voice_type,
            dataset_url=dataset_url,
            callback_uri=callback_uri,
            language=language,
            request_options=request_options,
        )
        return _response.data

    def get_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetVoiceResponse:
        """
        Get voice details

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceResponse
            Voice details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.get_voice(
            voice_uuid="voice_uuid",
        )
        """
        _response = self._raw_client.get_voice(voice_uuid, request_options=request_options)
        return _response.data

    def delete_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteVoiceResponse:
        """
        Delete a voice

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceResponse
            Voice deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.delete_voice(
            voice_uuid="voice_uuid",
        )
        """
        _response = self._raw_client.delete_voice(voice_uuid, request_options=request_options)
        return _response.data

    def build_voice(
        self,
        voice_uuid: str,
        *,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildVoiceResponse:
        """
        Start voice training

        Parameters
        ----------
        voice_uuid : str

        fill : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildVoiceResponse
            Build started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voices.build_voice(
            voice_uuid="voice_uuid",
        )
        """
        _response = self._raw_client.build_voice(voice_uuid, fill=fill, request_options=request_options)
        return _response.data


class AsyncVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoicesClient
        """
        return self._raw_client

    async def list_voices(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListVoicesResponse:
        """
        Retrieve voice metadata

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVoicesResponse
            List of voices

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.list_voices(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_voices(
            page=page, page_size=page_size, advanced=advanced, request_options=request_options
        )
        return _response.data

    async def create_voice(
        self,
        *,
        name: str,
        voice_type: typing.Optional[CreateVoiceRequestVoiceType] = OMIT,
        dataset_url: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVoiceResponse:
        """
        Create a new voice

        Parameters
        ----------
        name : str

        voice_type : typing.Optional[CreateVoiceRequestVoiceType]

        dataset_url : typing.Optional[str]

        callback_uri : typing.Optional[str]

        language : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceResponse
            Voice created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.create_voice(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voice(
            name=name,
            voice_type=voice_type,
            dataset_url=dataset_url,
            callback_uri=callback_uri,
            language=language,
            request_options=request_options,
        )
        return _response.data

    async def get_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetVoiceResponse:
        """
        Get voice details

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceResponse
            Voice details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.get_voice(
                voice_uuid="voice_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_voice(voice_uuid, request_options=request_options)
        return _response.data

    async def delete_voice(
        self, voice_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteVoiceResponse:
        """
        Delete a voice

        Parameters
        ----------
        voice_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceResponse
            Voice deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.delete_voice(
                voice_uuid="voice_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_voice(voice_uuid, request_options=request_options)
        return _response.data

    async def build_voice(
        self,
        voice_uuid: str,
        *,
        fill: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildVoiceResponse:
        """
        Start voice training

        Parameters
        ----------
        voice_uuid : str

        fill : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildVoiceResponse
            Build started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voices.build_voice(
                voice_uuid="voice_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.build_voice(voice_uuid, fill=fill, request_options=request_options)
        return _response.data
