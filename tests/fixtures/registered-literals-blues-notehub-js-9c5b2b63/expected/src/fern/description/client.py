

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.description_record import DescriptionRecord
from ..types.description_record_list import DescriptionRecordList
from .raw_client import AsyncRawDescriptionClient, RawDescriptionClient


OMIT = typing.cast(typing.Any, ...)


class DescriptionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDescriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDescriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDescriptionClient
        """
        return self._raw_client

    def list_global_descriptions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescriptionRecordList:
        """
        List metadata for all global description records.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecordList
            Description record metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.description.list_global_descriptions()
        """
        _response = self._raw_client.list_global_descriptions(request_options=request_options)
        return _response.data

    def get_global_description(
        self, description_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get a global description record. Returns the raw content with its stored Content-Type.

        Parameters
        ----------
        description_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The description content, returned with its stored Content-Type.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.description.get_global_description(
            description_name="descriptionName",
        )
        """
        with self._raw_client.get_global_description(description_name, request_options=request_options) as r:
            yield from r.data

    def set_global_description(
        self,
        description_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DescriptionRecord:
        """
        Create or replace a global description record, Blues staff only (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

        Parameters
        ----------
        description_name : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecord
            Description record created or updated.
        """
        _response = self._raw_client.set_global_description(
            description_name, request=request, request_options=request_options
        )
        return _response.data

    def delete_global_description(
        self, description_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a global description record by name (Blues staff only).

        Parameters
        ----------
        description_name : str

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
        client.description.delete_global_description(
            description_name="_health.qo",
        )
        """
        _response = self._raw_client.delete_global_description(description_name, request_options=request_options)
        return _response.data

    def list_project_descriptions(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescriptionRecordList:
        """
        List metadata for all description records in a project.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecordList
            Description record metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.description.list_project_descriptions(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.list_project_descriptions(project_or_product_uid, request_options=request_options)
        return _response.data

    def get_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Get a project description record. Returns the raw content with its stored Content-Type.

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The description content, returned with its stored Content-Type.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.description.get_project_description(
            project_or_product_uid="projectOrProductUID",
            description_name="descriptionName",
        )
        """
        with self._raw_client.get_project_description(
            project_or_product_uid, description_name, request_options=request_options
        ) as r:
            yield from r.data

    def set_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DescriptionRecord:
        """
        Create or replace a project description record (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecord
            Description record created or updated.
        """
        _response = self._raw_client.set_project_description(
            project_or_product_uid, description_name, request=request, request_options=request_options
        )
        return _response.data

    def delete_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a project description record by name.

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

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
        client.description.delete_project_description(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            description_name="_health.qo",
        )
        """
        _response = self._raw_client.delete_project_description(
            project_or_product_uid, description_name, request_options=request_options
        )
        return _response.data


class AsyncDescriptionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDescriptionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDescriptionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDescriptionClient
        """
        return self._raw_client

    async def list_global_descriptions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescriptionRecordList:
        """
        List metadata for all global description records.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecordList
            Description record metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.description.list_global_descriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_global_descriptions(request_options=request_options)
        return _response.data

    async def get_global_description(
        self, description_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a global description record. Returns the raw content with its stored Content-Type.

        Parameters
        ----------
        description_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The description content, returned with its stored Content-Type.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.description.get_global_description(
                description_name="descriptionName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_global_description(description_name, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def set_global_description(
        self,
        description_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DescriptionRecord:
        """
        Create or replace a global description record, Blues staff only (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

        Parameters
        ----------
        description_name : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecord
            Description record created or updated.
        """
        _response = await self._raw_client.set_global_description(
            description_name, request=request, request_options=request_options
        )
        return _response.data

    async def delete_global_description(
        self, description_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a global description record by name (Blues staff only).

        Parameters
        ----------
        description_name : str

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
            await client.description.delete_global_description(
                description_name="_health.qo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_global_description(description_name, request_options=request_options)
        return _response.data

    async def list_project_descriptions(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DescriptionRecordList:
        """
        List metadata for all description records in a project.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecordList
            Description record metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.description.list_project_descriptions(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_project_descriptions(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def get_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a project description record. Returns the raw content with its stored Content-Type.

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The description content, returned with its stored Content-Type.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.description.get_project_description(
                project_or_product_uid="projectOrProductUID",
                description_name="descriptionName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_project_description(
            project_or_product_uid, description_name, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def set_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DescriptionRecord:
        """
        Create or replace a project description record (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DescriptionRecord
            Description record created or updated.
        """
        _response = await self._raw_client.set_project_description(
            project_or_product_uid, description_name, request=request, request_options=request_options
        )
        return _response.data

    async def delete_project_description(
        self,
        project_or_product_uid: str,
        description_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a project description record by name.

        Parameters
        ----------
        project_or_product_uid : str

        description_name : str

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
            await client.description.delete_project_description(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                description_name="_health.qo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_description(
            project_or_product_uid, description_name, request_options=request_options
        )
        return _response.data
