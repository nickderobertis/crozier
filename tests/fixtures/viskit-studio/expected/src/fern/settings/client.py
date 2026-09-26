

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.settings_response import SettingsResponse
from .raw_client import AsyncRawSettingsClient, RawSettingsClient
from .types.settings_update_default_locale import SettingsUpdateDefaultLocale


OMIT = typing.cast(typing.Any, ...)


class SettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSettingsClient
        """
        return self._raw_client

    def post_settings(
        self,
        *,
        brand_color: typing.Optional[str] = OMIT,
        default_locale: typing.Optional[SettingsUpdateDefaultLocale] = OMIT,
        export_preset: typing.Optional[str] = OMIT,
        monthly_cap_usd: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SettingsResponse:
        """
        Read-modify-write the 4 workspace-level options into config.yaml.

        Retries up to ``_MAX_CHECKSUM_RETRIES`` times if the config drifted
        underneath us (concurrent provider save).  Inode-changed is treated
        identically to checksum-mismatch.

        Parameters
        ----------
        brand_color : typing.Optional[str]

        default_locale : typing.Optional[SettingsUpdateDefaultLocale]

        export_preset : typing.Optional[str]

        monthly_cap_usd : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.post_settings()
        """
        _response = self._raw_client.post_settings(
            brand_color=brand_color,
            default_locale=default_locale,
            export_preset=export_preset,
            monthly_cap_usd=monthly_cap_usd,
            request_options=request_options,
        )
        return _response.data


class AsyncSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSettingsClient
        """
        return self._raw_client

    async def post_settings(
        self,
        *,
        brand_color: typing.Optional[str] = OMIT,
        default_locale: typing.Optional[SettingsUpdateDefaultLocale] = OMIT,
        export_preset: typing.Optional[str] = OMIT,
        monthly_cap_usd: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SettingsResponse:
        """
        Read-modify-write the 4 workspace-level options into config.yaml.

        Retries up to ``_MAX_CHECKSUM_RETRIES`` times if the config drifted
        underneath us (concurrent provider save).  Inode-changed is treated
        identically to checksum-mismatch.

        Parameters
        ----------
        brand_color : typing.Optional[str]

        default_locale : typing.Optional[SettingsUpdateDefaultLocale]

        export_preset : typing.Optional[str]

        monthly_cap_usd : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.post_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_settings(
            brand_color=brand_color,
            default_locale=default_locale,
            export_preset=export_preset,
            monthly_cap_usd=monthly_cap_usd,
            request_options=request_options,
        )
        return _response.data
