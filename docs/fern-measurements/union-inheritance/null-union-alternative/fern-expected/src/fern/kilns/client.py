

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKilnsClient, RawKilnsClient
from .types.adjust_kiln_settings_request_changes_item import AdjustKilnSettingsRequestChangesItem
from .types.register_kiln_request_settings_value import RegisterKilnRequestSettingsValue


OMIT = typing.cast(typing.Any, ...)


class KilnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKilnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKilnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKilnsClient
        """
        return self._raw_client

    def register_kiln(
        self,
        *,
        name: str,
        settings: typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        settings : typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.kilns.register_kiln(
            name="name",
        )
        """
        _response = self._raw_client.register_kiln(name=name, settings=settings, request_options=request_options)
        return _response.data

    def adjust_kiln_settings(
        self,
        kiln_id: str,
        *,
        changes: typing.Sequence[AdjustKilnSettingsRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        kiln_id : str

        changes : typing.Sequence[AdjustKilnSettingsRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.kilns import AdjustKilnSettingsRequestChangesItem

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.kilns.adjust_kiln_settings(
            kiln_id="kilnId",
            changes=[
                AdjustKilnSettingsRequestChangesItem(
                    setting="setting",
                )
            ],
        )
        """
        _response = self._raw_client.adjust_kiln_settings(kiln_id, changes=changes, request_options=request_options)
        return _response.data


class AsyncKilnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKilnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKilnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKilnsClient
        """
        return self._raw_client

    async def register_kiln(
        self,
        *,
        name: str,
        settings: typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        name : str

        settings : typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.kilns.register_kiln(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_kiln(name=name, settings=settings, request_options=request_options)
        return _response.data

    async def adjust_kiln_settings(
        self,
        kiln_id: str,
        *,
        changes: typing.Sequence[AdjustKilnSettingsRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        kiln_id : str

        changes : typing.Sequence[AdjustKilnSettingsRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.kilns import AdjustKilnSettingsRequestChangesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.kilns.adjust_kiln_settings(
                kiln_id="kilnId",
                changes=[
                    AdjustKilnSettingsRequestChangesItem(
                        setting="setting",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adjust_kiln_settings(
            kiln_id, changes=changes, request_options=request_options
        )
        return _response.data
