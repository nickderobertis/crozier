

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.any import Any
from ..types.done import Done
from ..types.global_config_import_body import GlobalConfigImportBody
from .raw_client import AsyncRawImportExportClient, RawImportExportClient


OMIT = typing.cast(typing.Any, ...)


class ImportExportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportExportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportExportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportExportClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_import_export_controller_full_export(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_export()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_export(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_import_export_controller_full_import(
        self, *, request: GlobalConfigImportBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : GlobalConfigImportBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_import(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_import(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
        self, *, request: GlobalConfigImportBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : GlobalConfigImportBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncImportExportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportExportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportExportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportExportClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_import_export_controller_full_export(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_export()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_export(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_import_export_controller_full_import(
        self, *, request: GlobalConfigImportBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : GlobalConfigImportBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_import(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_import(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
        self, *, request: GlobalConfigImportBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : GlobalConfigImportBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_export.otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_import_export_controller_full_import_from_file(
            request=request, request_options=request_options
        )
        return _response.data
