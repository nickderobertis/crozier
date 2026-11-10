

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.theme import Theme
from ..types.theme_rules_item import ThemeRulesItem
from .raw_client import AsyncRawThemesClient, RawThemesClient


OMIT = typing.cast(typing.Any, ...)


class ThemesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemesClient
        """
        return self._raw_client

    def return_a_list_of_all_themes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Theme]:
        """
        Returns all themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Theme]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.return_a_list_of_all_themes()
        """
        _response = self._raw_client.return_a_list_of_all_themes(request_options=request_options)
        return _response.data

    def creates_a_new_theme(
        self,
        *,
        uuid_: str,
        name: str,
        rules: typing.Sequence[ThemeRulesItem],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new theme.

        Parameters
        ----------
        uuid_ : str

        name : str

        rules : typing.Sequence[ThemeRulesItem]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ThemeRulesItem

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.creates_a_new_theme(
            uuid_="00000000-0000-0000-0000-000000000000",
            name="Theme name",
            rules=[
                ThemeRulesItem(
                    text="#000000",
                    background="#000000",
                    border="#000000",
                    shape="0",
                    border_width="0px",
                    filter_type="type",
                    filter_value="filterValue",
                )
            ],
        )
        """
        _response = self._raw_client.creates_a_new_theme(
            uuid_=uuid_, name=name, rules=rules, id=id, request_options=request_options
        )
        return _response.data

    def updates_theme_configuration(
        self,
        theme_id: str,
        *,
        uuid_: str,
        name: str,
        rules: typing.Sequence[ThemeRulesItem],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Theme:
        """
        Updates theme configuration for the specified theme ID.

        Parameters
        ----------
        theme_id : str
            Selected theme ID.

        uuid_ : str

        name : str

        rules : typing.Sequence[ThemeRulesItem]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            Successful operation.

        Examples
        --------
        from fern import FernApi, ThemeRulesItem

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.updates_theme_configuration(
            theme_id="themeId",
            uuid_="00000000-0000-0000-0000-000000000000",
            name="Theme name",
            rules=[
                ThemeRulesItem(
                    text="#000000",
                    background="#000000",
                    border="#000000",
                    shape="0",
                    border_width="0px",
                    filter_type="type",
                    filter_value="filterValue",
                )
            ],
        )
        """
        _response = self._raw_client.updates_theme_configuration(
            theme_id, uuid_=uuid_, name=name, rules=rules, id=id, request_options=request_options
        )
        return _response.data

    def deletes_the_theme(self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Deletes the theme with the provided theme ID.

        Parameters
        ----------
        theme_id : str
            Theme ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.deletes_the_theme(
            theme_id="themeId",
        )
        """
        _response = self._raw_client.deletes_the_theme(theme_id, request_options=request_options)
        return _response.data

    def imports_new_theme_from_a_zip_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Imports new theme from the provided zip file into the local DB.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.imports_new_theme_from_a_zip_file()
        """
        _response = self._raw_client.imports_new_theme_from_a_zip_file(request_options=request_options)
        return _response.data

    def returns_a_zip_file_containing_the_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a zip file containing the theme.

        Parameters
        ----------
        theme_id : str
            Selected theme ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.themes.returns_a_zip_file_containing_the_theme(
            theme_id="themeId",
        )
        """
        _response = self._raw_client.returns_a_zip_file_containing_the_theme(theme_id, request_options=request_options)
        return _response.data


class AsyncThemesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemesClient
        """
        return self._raw_client

    async def return_a_list_of_all_themes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Theme]:
        """
        Returns all themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Theme]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.return_a_list_of_all_themes()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_all_themes(request_options=request_options)
        return _response.data

    async def creates_a_new_theme(
        self,
        *,
        uuid_: str,
        name: str,
        rules: typing.Sequence[ThemeRulesItem],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new theme.

        Parameters
        ----------
        uuid_ : str

        name : str

        rules : typing.Sequence[ThemeRulesItem]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ThemeRulesItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.creates_a_new_theme(
                uuid_="00000000-0000-0000-0000-000000000000",
                name="Theme name",
                rules=[
                    ThemeRulesItem(
                        text="#000000",
                        background="#000000",
                        border="#000000",
                        shape="0",
                        border_width="0px",
                        filter_type="type",
                        filter_value="filterValue",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_theme(
            uuid_=uuid_, name=name, rules=rules, id=id, request_options=request_options
        )
        return _response.data

    async def updates_theme_configuration(
        self,
        theme_id: str,
        *,
        uuid_: str,
        name: str,
        rules: typing.Sequence[ThemeRulesItem],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Theme:
        """
        Updates theme configuration for the specified theme ID.

        Parameters
        ----------
        theme_id : str
            Selected theme ID.

        uuid_ : str

        name : str

        rules : typing.Sequence[ThemeRulesItem]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ThemeRulesItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.updates_theme_configuration(
                theme_id="themeId",
                uuid_="00000000-0000-0000-0000-000000000000",
                name="Theme name",
                rules=[
                    ThemeRulesItem(
                        text="#000000",
                        background="#000000",
                        border="#000000",
                        shape="0",
                        border_width="0px",
                        filter_type="type",
                        filter_value="filterValue",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_theme_configuration(
            theme_id, uuid_=uuid_, name=name, rules=rules, id=id, request_options=request_options
        )
        return _response.data

    async def deletes_the_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Deletes the theme with the provided theme ID.

        Parameters
        ----------
        theme_id : str
            Theme ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.deletes_the_theme(
                theme_id="themeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_theme(theme_id, request_options=request_options)
        return _response.data

    async def imports_new_theme_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Theme:
        """
        Imports new theme from the provided zip file into the local DB.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.imports_new_theme_from_a_zip_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_theme_from_a_zip_file(request_options=request_options)
        return _response.data

    async def returns_a_zip_file_containing_the_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a zip file containing the theme.

        Parameters
        ----------
        theme_id : str
            Selected theme ID.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.themes.returns_a_zip_file_containing_the_theme(
                theme_id="themeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_zip_file_containing_the_theme(
            theme_id, request_options=request_options
        )
        return _response.data
