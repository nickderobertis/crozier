

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item import Item
from ..types.section import Section
from ..types.section_result import SectionResult
from ..types.write_result import WriteResult
from .raw_client import AsyncRawSectionsClient, RawSectionsClient
from .types.update_section_response import UpdateSectionResponse


OMIT = typing.cast(typing.Any, ...)


class SectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSectionsClient
        """
        return self._raw_client

    def add_section(
        self,
        filename: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SectionResult:
        """
        Appends a new section. A `name` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        name : str
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SectionResult
            Section added

        Examples
        --------
        from fern import FernApi, Item

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sections.add_section(
            filename="conf.yml",
            name="Monitoring",
            icon="fas fa-chart-line",
            items=[
                Item(
                    title="title",
                )
            ],
        )
        """
        _response = self._raw_client.add_section(
            filename,
            name=name,
            icon=icon,
            display_data=display_data,
            items=items,
            widgets=widgets,
            filtered_items=filtered_items,
            request_options=request_options,
        )
        return _response.data

    def get_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Section:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Section
            Section

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sections.get_section(
            filename="conf.yml",
            sid="0",
        )
        """
        _response = self._raw_client.get_section(filename, sid, request_options=request_options)
        return _response.data

    def delete_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WriteResult:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sections.delete_section(
            filename="conf.yml",
            sid="0",
        )
        """
        _response = self._raw_client.delete_section(filename, sid, request_options=request_options)
        return _response.data

    def update_section(
        self,
        filename: str,
        sid: str,
        *,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSectionResponse:
        """
        Shallow-merges the supplied fields. Sending `items` replaces the whole array.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        name : typing.Optional[str]
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSectionResponse
            Updated section

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sections.update_section(
            filename="conf.yml",
            sid="0",
            name="Renamed Section",
        )
        """
        _response = self._raw_client.update_section(
            filename,
            sid,
            name=name,
            icon=icon,
            display_data=display_data,
            items=items,
            widgets=widgets,
            filtered_items=filtered_items,
            request_options=request_options,
        )
        return _response.data


class AsyncSectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSectionsClient
        """
        return self._raw_client

    async def add_section(
        self,
        filename: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SectionResult:
        """
        Appends a new section. A `name` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        name : str
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SectionResult
            Section added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Item

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sections.add_section(
                filename="conf.yml",
                name="Monitoring",
                icon="fas fa-chart-line",
                items=[
                    Item(
                        title="title",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_section(
            filename,
            name=name,
            icon=icon,
            display_data=display_data,
            items=items,
            widgets=widgets,
            filtered_items=filtered_items,
            request_options=request_options,
        )
        return _response.data

    async def get_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Section:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Section
            Section

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sections.get_section(
                filename="conf.yml",
                sid="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_section(filename, sid, request_options=request_options)
        return _response.data

    async def delete_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WriteResult:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sections.delete_section(
                filename="conf.yml",
                sid="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_section(filename, sid, request_options=request_options)
        return _response.data

    async def update_section(
        self,
        filename: str,
        sid: str,
        *,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSectionResponse:
        """
        Shallow-merges the supplied fields. Sending `items` replaces the whole array.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        name : typing.Optional[str]
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSectionResponse
            Updated section

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sections.update_section(
                filename="conf.yml",
                sid="0",
                name="Renamed Section",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_section(
            filename,
            sid,
            name=name,
            icon=icon,
            display_data=display_data,
            items=items,
            widgets=widgets,
            filtered_items=filtered_items,
            request_options=request_options,
        )
        return _response.data
