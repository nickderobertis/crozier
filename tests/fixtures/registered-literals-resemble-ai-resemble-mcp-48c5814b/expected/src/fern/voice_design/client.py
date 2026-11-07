

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoiceDesignClient, RawVoiceDesignClient
from .types.create_voice_from_candidate_response import CreateVoiceFromCandidateResponse
from .types.generate_voice_design_response import GenerateVoiceDesignResponse


OMIT = typing.cast(typing.Any, ...)


class VoiceDesignClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoiceDesignClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoiceDesignClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoiceDesignClient
        """
        return self._raw_client

    def generate_voice_design(
        self, *, user_prompt: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateVoiceDesignResponse:
        """
        Generate three voice candidates from a text prompt

        Parameters
        ----------
        user_prompt : str
            Description of desired voice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateVoiceDesignResponse
            Voice candidates generated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_design.generate_voice_design(
            user_prompt="user_prompt",
        )
        """
        _response = self._raw_client.generate_voice_design(user_prompt=user_prompt, request_options=request_options)
        return _response.data

    def create_voice_from_candidate(
        self, *, uuid_: str, voice_sample_index: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateVoiceFromCandidateResponse:
        """
        Create a voice from a voice design candidate

        Parameters
        ----------
        uuid_ : str

        voice_sample_index : int

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceFromCandidateResponse
            Voice created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_design.create_voice_from_candidate(
            uuid_="uuid",
            voice_sample_index=1,
            name="name",
        )
        """
        _response = self._raw_client.create_voice_from_candidate(
            uuid_=uuid_, voice_sample_index=voice_sample_index, name=name, request_options=request_options
        )
        return _response.data


class AsyncVoiceDesignClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoiceDesignClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoiceDesignClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoiceDesignClient
        """
        return self._raw_client

    async def generate_voice_design(
        self, *, user_prompt: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateVoiceDesignResponse:
        """
        Generate three voice candidates from a text prompt

        Parameters
        ----------
        user_prompt : str
            Description of desired voice

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateVoiceDesignResponse
            Voice candidates generated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_design.generate_voice_design(
                user_prompt="user_prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_voice_design(
            user_prompt=user_prompt, request_options=request_options
        )
        return _response.data

    async def create_voice_from_candidate(
        self, *, uuid_: str, voice_sample_index: int, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateVoiceFromCandidateResponse:
        """
        Create a voice from a voice design candidate

        Parameters
        ----------
        uuid_ : str

        voice_sample_index : int

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceFromCandidateResponse
            Voice created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_design.create_voice_from_candidate(
                uuid_="uuid",
                voice_sample_index=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voice_from_candidate(
            uuid_=uuid_, voice_sample_index=voice_sample_index, name=name, request_options=request_options
        )
        return _response.data
