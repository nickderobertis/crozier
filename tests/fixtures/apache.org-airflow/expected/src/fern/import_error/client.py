

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.import_error import ImportError
from ..types.import_error_collection import ImportErrorCollection
from .raw_client import AsyncRawImportErrorClient, RawImportErrorClient


class ImportErrorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportErrorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportErrorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportErrorClient
        """
        return self._raw_client

    def get_import_errors(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportErrorCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportErrorCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_error.get_import_errors()
        """
        _response = self._raw_client.get_import_errors(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def get_import_error(
        self, import_error_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportError:
        """
        Parameters
        ----------
        import_error_id : int
            The import error ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportError
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_error.get_import_error(
            import_error_id=1,
        )
        """
        _response = self._raw_client.get_import_error(import_error_id, request_options=request_options)
        return _response.data


class AsyncImportErrorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportErrorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportErrorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportErrorClient
        """
        return self._raw_client

    async def get_import_errors(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportErrorCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportErrorCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_error.get_import_errors()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_import_errors(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def get_import_error(
        self, import_error_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportError:
        """
        Parameters
        ----------
        import_error_id : int
            The import error ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportError
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_error.get_import_error(
                import_error_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_import_error(import_error_id, request_options=request_options)
        return _response.data
