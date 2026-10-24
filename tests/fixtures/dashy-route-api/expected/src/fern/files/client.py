

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_config import AppConfig
from ..types.config import Config
from ..types.file_list import FileList
from ..types.page import Page
from ..types.page_info import PageInfo
from ..types.section import Section
from ..types.write_result import WriteResult
from .raw_client import AsyncRawFilesClient, RawFilesClient


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def list_config_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> FileList:
        """
        Lists every YAML config file in the user-data directory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Config files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.list_config_files()
        """
        _response = self._raw_client.list_config_files(request_options=request_options)
        return _response.data

    def get_config_file(self, filename: str, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Returns the parsed config file as JSON.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Parsed config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.get_config_file(
            filename="conf.yml",
        )
        """
        _response = self._raw_client.get_config_file(filename, request_options=request_options)
        return _response.data

    def replace_config_file(
        self,
        filename: str,
        *,
        page_info: typing.Optional[PageInfo] = OMIT,
        app_config: typing.Optional[AppConfig] = OMIT,
        sections: typing.Optional[typing.Sequence[Section]] = OMIT,
        pages: typing.Optional[typing.Sequence[Page]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WriteResult:
        """
        Overwrites the whole file. Writes to `conf.yml` are validated against the
        config schema; sub-pages are not. A timestamped backup is taken first.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        page_info : typing.Optional[PageInfo]

        app_config : typing.Optional[AppConfig]

        sections : typing.Optional[typing.Sequence[Section]]

        pages : typing.Optional[typing.Sequence[Page]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        from fern import FernApi, PageInfo, Section

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.replace_config_file(
            filename="conf.yml",
            page_info=PageInfo(
                title="My Dashboard",
            ),
            sections=[
                Section(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.replace_config_file(
            filename,
            page_info=page_info,
            app_config=app_config,
            sections=sections,
            pages=pages,
            request_options=request_options,
        )
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def list_config_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> FileList:
        """
        Lists every YAML config file in the user-data directory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileList
            Config files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.list_config_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_config_files(request_options=request_options)
        return _response.data

    async def get_config_file(
        self, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Config:
        """
        Returns the parsed config file as JSON.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Parsed config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.get_config_file(
                filename="conf.yml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config_file(filename, request_options=request_options)
        return _response.data

    async def replace_config_file(
        self,
        filename: str,
        *,
        page_info: typing.Optional[PageInfo] = OMIT,
        app_config: typing.Optional[AppConfig] = OMIT,
        sections: typing.Optional[typing.Sequence[Section]] = OMIT,
        pages: typing.Optional[typing.Sequence[Page]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WriteResult:
        """
        Overwrites the whole file. Writes to `conf.yml` are validated against the
        config schema; sub-pages are not. A timestamped backup is taken first.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        page_info : typing.Optional[PageInfo]

        app_config : typing.Optional[AppConfig]

        sections : typing.Optional[typing.Sequence[Section]]

        pages : typing.Optional[typing.Sequence[Page]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PageInfo, Section

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.replace_config_file(
                filename="conf.yml",
                page_info=PageInfo(
                    title="My Dashboard",
                ),
                sections=[
                    Section(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_config_file(
            filename,
            page_info=page_info,
            app_config=app_config,
            sections=sections,
            pages=pages,
            request_options=request_options,
        )
        return _response.data
