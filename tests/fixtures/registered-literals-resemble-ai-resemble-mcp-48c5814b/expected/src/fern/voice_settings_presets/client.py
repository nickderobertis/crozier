

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoiceSettingsPresetsClient, RawVoiceSettingsPresetsClient
from .types.create_voice_settings_preset_response import CreateVoiceSettingsPresetResponse
from .types.delete_voice_settings_preset_response import DeleteVoiceSettingsPresetResponse
from .types.get_voice_settings_preset_response import GetVoiceSettingsPresetResponse
from .types.list_voice_settings_presets_response import ListVoiceSettingsPresetsResponse
from .types.update_voice_settings_preset_response import UpdateVoiceSettingsPresetResponse


OMIT = typing.cast(typing.Any, ...)


class VoiceSettingsPresetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoiceSettingsPresetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoiceSettingsPresetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoiceSettingsPresetsClient
        """
        return self._raw_client

    def list_voice_settings_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListVoiceSettingsPresetsResponse:
        """
        List all voice settings presets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVoiceSettingsPresetsResponse
            List of presets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_settings_presets.list_voice_settings_presets()
        """
        _response = self._raw_client.list_voice_settings_presets(request_options=request_options)
        return _response.data

    def create_voice_settings_preset(
        self,
        *,
        name: str,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVoiceSettingsPresetResponse:
        """
        Create a new voice settings preset (max 5 per user)

        Parameters
        ----------
        name : str
            Preset name (unique, max 30 characters)

        pace : typing.Optional[float]
            Speech pace/speed

        temperature : typing.Optional[float]
            Voice variation

        pitch : typing.Optional[float]
            Voice pitch adjustment

        use_hd : typing.Optional[bool]
            Use HD quality

        exaggeration : typing.Optional[float]
            Emotional exaggeration

        description : typing.Optional[str]
            Voice style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceSettingsPresetResponse
            Preset created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_settings_presets.create_voice_settings_preset(
            name="name",
        )
        """
        _response = self._raw_client.create_voice_settings_preset(
            name=name,
            pace=pace,
            temperature=temperature,
            pitch=pitch,
            use_hd=use_hd,
            exaggeration=exaggeration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetVoiceSettingsPresetResponse:
        """
        Get preset details

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceSettingsPresetResponse
            Preset details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_settings_presets.get_voice_settings_preset(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_voice_settings_preset(uuid_, request_options=request_options)
        return _response.data

    def delete_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteVoiceSettingsPresetResponse:
        """
        Delete a preset

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceSettingsPresetResponse
            Preset deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_settings_presets.delete_voice_settings_preset(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.delete_voice_settings_preset(uuid_, request_options=request_options)
        return _response.data

    def update_voice_settings_preset(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateVoiceSettingsPresetResponse:
        """
        Update a preset

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        pace : typing.Optional[float]

        temperature : typing.Optional[float]

        pitch : typing.Optional[float]

        use_hd : typing.Optional[bool]

        exaggeration : typing.Optional[float]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateVoiceSettingsPresetResponse
            Preset updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.voice_settings_presets.update_voice_settings_preset(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.update_voice_settings_preset(
            uuid_,
            name=name,
            pace=pace,
            temperature=temperature,
            pitch=pitch,
            use_hd=use_hd,
            exaggeration=exaggeration,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncVoiceSettingsPresetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoiceSettingsPresetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoiceSettingsPresetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoiceSettingsPresetsClient
        """
        return self._raw_client

    async def list_voice_settings_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListVoiceSettingsPresetsResponse:
        """
        List all voice settings presets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVoiceSettingsPresetsResponse
            List of presets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_settings_presets.list_voice_settings_presets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_voice_settings_presets(request_options=request_options)
        return _response.data

    async def create_voice_settings_preset(
        self,
        *,
        name: str,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateVoiceSettingsPresetResponse:
        """
        Create a new voice settings preset (max 5 per user)

        Parameters
        ----------
        name : str
            Preset name (unique, max 30 characters)

        pace : typing.Optional[float]
            Speech pace/speed

        temperature : typing.Optional[float]
            Voice variation

        pitch : typing.Optional[float]
            Voice pitch adjustment

        use_hd : typing.Optional[bool]
            Use HD quality

        exaggeration : typing.Optional[float]
            Emotional exaggeration

        description : typing.Optional[str]
            Voice style prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateVoiceSettingsPresetResponse
            Preset created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_settings_presets.create_voice_settings_preset(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voice_settings_preset(
            name=name,
            pace=pace,
            temperature=temperature,
            pitch=pitch,
            use_hd=use_hd,
            exaggeration=exaggeration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetVoiceSettingsPresetResponse:
        """
        Get preset details

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceSettingsPresetResponse
            Preset details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_settings_presets.get_voice_settings_preset(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_voice_settings_preset(uuid_, request_options=request_options)
        return _response.data

    async def delete_voice_settings_preset(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteVoiceSettingsPresetResponse:
        """
        Delete a preset

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteVoiceSettingsPresetResponse
            Preset deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_settings_presets.delete_voice_settings_preset(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_voice_settings_preset(uuid_, request_options=request_options)
        return _response.data

    async def update_voice_settings_preset(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        pace: typing.Optional[float] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        use_hd: typing.Optional[bool] = OMIT,
        exaggeration: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateVoiceSettingsPresetResponse:
        """
        Update a preset

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        pace : typing.Optional[float]

        temperature : typing.Optional[float]

        pitch : typing.Optional[float]

        use_hd : typing.Optional[bool]

        exaggeration : typing.Optional[float]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateVoiceSettingsPresetResponse
            Preset updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.voice_settings_presets.update_voice_settings_preset(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_voice_settings_preset(
            uuid_,
            name=name,
            pace=pace,
            temperature=temperature,
            pitch=pitch,
            use_hd=use_hd,
            exaggeration=exaggeration,
            description=description,
            request_options=request_options,
        )
        return _response.data
