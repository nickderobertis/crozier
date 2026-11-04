

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDuetsClient, RawDuetsClient
from .types.create_duet_voice_pair_response import CreateDuetVoicePairResponse
from .types.create_duet_voice_response import CreateDuetVoiceResponse
from .types.delete_duet_voice_response import DeleteDuetVoiceResponse
from .types.generate_duet_request_script_item import GenerateDuetRequestScriptItem
from .types.generate_duet_response import GenerateDuetResponse
from .types.list_duet_voice_pairs_response import ListDuetVoicePairsResponse
from .types.list_duet_voices_response import ListDuetVoicesResponse
from .types.update_duet_voice_response import UpdateDuetVoiceResponse


OMIT = typing.cast(typing.Any, ...)


class DuetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDuetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDuetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDuetsClient
        """
        return self._raw_client

    def list_duet_voices(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListDuetVoicesResponse:
        """
        Returns default and custom duet voices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDuetVoicesResponse
            List of duet voices

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.list_duet_voices()
        """
        _response = self._raw_client.list_duet_voices(request_options=request_options)
        return _response.data

    def create_duet_voice(
        self,
        *,
        name: str,
        audio: core.File,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDuetVoiceResponse:
        """
        Create a custom voice for duet generation

        Parameters
        ----------
        name : str
            Voice name

        audio : core.File
            See core.File for more documentation

        style_prompt : typing.Optional[str]
            Optional style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDuetVoiceResponse
            Duet voice created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.create_duet_voice(
            name="name",
        )
        """
        _response = self._raw_client.create_duet_voice(
            name=name, audio=audio, style_prompt=style_prompt, request_options=request_options
        )
        return _response.data

    def update_duet_voice(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDuetVoiceResponse:
        """
        Update a custom duet voice (default voices cannot be modified)

        Parameters
        ----------
        id : int

        name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDuetVoiceResponse
            Duet voice updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.update_duet_voice(
            id=1,
        )
        """
        _response = self._raw_client.update_duet_voice(
            id, name=name, style_prompt=style_prompt, request_options=request_options
        )
        return _response.data

    def delete_duet_voice(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDuetVoiceResponse:
        """
        Delete a custom duet voice (default voices cannot be deleted)

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDuetVoiceResponse
            Duet voice deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.delete_duet_voice(
            id=1,
        )
        """
        _response = self._raw_client.delete_duet_voice(id, request_options=request_options)
        return _response.data

    def list_duet_voice_pairs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListDuetVoicePairsResponse:
        """
        List all voice pairs for duet generation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDuetVoicePairsResponse
            List of voice pairs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.list_duet_voice_pairs()
        """
        _response = self._raw_client.list_duet_voice_pairs(request_options=request_options)
        return _response.data

    def create_duet_voice_pair(
        self,
        *,
        voice1id: int,
        voice2id: int,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDuetVoicePairResponse:
        """
        Create a voice pair for duet generation

        Parameters
        ----------
        voice1id : int
            ID of first voice

        voice2id : int
            ID of second voice

        name : typing.Optional[str]
            Optional pair name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDuetVoicePairResponse
            Voice pair created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.create_duet_voice_pair(
            voice1id=1,
            voice2id=1,
        )
        """
        _response = self._raw_client.create_duet_voice_pair(
            voice1id=voice1id, voice2id=voice2id, name=name, request_options=request_options
        )
        return _response.data

    def generate_duet(
        self,
        *,
        voice_pair_id: int,
        script: typing.Sequence[GenerateDuetRequestScriptItem],
        title: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateDuetResponse:
        """
        Generate conversational audio with two speakers

        Parameters
        ----------
        voice_pair_id : int
            Voice pair ID to use

        script : typing.Sequence[GenerateDuetRequestScriptItem]

        title : typing.Optional[str]
            Optional title for the duet

        callback_uri : typing.Optional[str]
            Webhook URL for completion notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateDuetResponse
            Duet generation job created

        Examples
        --------
        from fern.duets import GenerateDuetRequestScriptItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.duets.generate_duet(
            voice_pair_id=1,
            script=[
                GenerateDuetRequestScriptItem(
                    speaker=1,
                    text="text",
                )
            ],
        )
        """
        _response = self._raw_client.generate_duet(
            voice_pair_id=voice_pair_id,
            script=script,
            title=title,
            callback_uri=callback_uri,
            request_options=request_options,
        )
        return _response.data


class AsyncDuetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDuetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDuetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDuetsClient
        """
        return self._raw_client

    async def list_duet_voices(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListDuetVoicesResponse:
        """
        Returns default and custom duet voices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDuetVoicesResponse
            List of duet voices

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.list_duet_voices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_duet_voices(request_options=request_options)
        return _response.data

    async def create_duet_voice(
        self,
        *,
        name: str,
        audio: core.File,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDuetVoiceResponse:
        """
        Create a custom voice for duet generation

        Parameters
        ----------
        name : str
            Voice name

        audio : core.File
            See core.File for more documentation

        style_prompt : typing.Optional[str]
            Optional style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDuetVoiceResponse
            Duet voice created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.create_duet_voice(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_duet_voice(
            name=name, audio=audio, style_prompt=style_prompt, request_options=request_options
        )
        return _response.data

    async def update_duet_voice(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDuetVoiceResponse:
        """
        Update a custom duet voice (default voices cannot be modified)

        Parameters
        ----------
        id : int

        name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDuetVoiceResponse
            Duet voice updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.update_duet_voice(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_duet_voice(
            id, name=name, style_prompt=style_prompt, request_options=request_options
        )
        return _response.data

    async def delete_duet_voice(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDuetVoiceResponse:
        """
        Delete a custom duet voice (default voices cannot be deleted)

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDuetVoiceResponse
            Duet voice deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.delete_duet_voice(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_duet_voice(id, request_options=request_options)
        return _response.data

    async def list_duet_voice_pairs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListDuetVoicePairsResponse:
        """
        List all voice pairs for duet generation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListDuetVoicePairsResponse
            List of voice pairs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.list_duet_voice_pairs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_duet_voice_pairs(request_options=request_options)
        return _response.data

    async def create_duet_voice_pair(
        self,
        *,
        voice1id: int,
        voice2id: int,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDuetVoicePairResponse:
        """
        Create a voice pair for duet generation

        Parameters
        ----------
        voice1id : int
            ID of first voice

        voice2id : int
            ID of second voice

        name : typing.Optional[str]
            Optional pair name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDuetVoicePairResponse
            Voice pair created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.create_duet_voice_pair(
                voice1id=1,
                voice2id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_duet_voice_pair(
            voice1id=voice1id, voice2id=voice2id, name=name, request_options=request_options
        )
        return _response.data

    async def generate_duet(
        self,
        *,
        voice_pair_id: int,
        script: typing.Sequence[GenerateDuetRequestScriptItem],
        title: typing.Optional[str] = OMIT,
        callback_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateDuetResponse:
        """
        Generate conversational audio with two speakers

        Parameters
        ----------
        voice_pair_id : int
            Voice pair ID to use

        script : typing.Sequence[GenerateDuetRequestScriptItem]

        title : typing.Optional[str]
            Optional title for the duet

        callback_uri : typing.Optional[str]
            Webhook URL for completion notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateDuetResponse
            Duet generation job created

        Examples
        --------
        import asyncio

        from fern.duets import GenerateDuetRequestScriptItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.duets.generate_duet(
                voice_pair_id=1,
                script=[
                    GenerateDuetRequestScriptItem(
                        speaker=1,
                        text="text",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_duet(
            voice_pair_id=voice_pair_id,
            script=script,
            title=title,
            callback_uri=callback_uri,
            request_options=request_options,
        )
        return _response.data
