

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_tag_response import PaginatedTagResponse
from .raw_client import AsyncRawTagClient, RawTagClient
from .types.tag import Tag


OMIT = typing.cast(typing.Any, ...)


class TagClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagClient
        """
        return self._raw_client

    def get_all_tags(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTagResponse:
        """
        Retrieves tags known in the system in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTagResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.get_all_tags()
        """
        _response = self._raw_client.get_all_tags(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_tag(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Create a tag

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the tag

        name : typing.Optional[str]
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.create_tag(
            name="testtag",
        )
        """
        _response = self._raw_client.create_tag(id=id, name=name, request_options=request_options)
        return _response.data

    def get_tag(self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tag:
        """
        Get a single tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.get_tag(
            tag_id="TagID",
        )
        """
        _response = self._raw_client.get_tag(tag_id, request_options=request_options)
        return _response.data

    def update_tag(
        self,
        tag_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Update a tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

        id : typing.Optional[str]
            ID of the tag

        name : typing.Optional[str]
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.update_tag(
            tag_id="TagID",
            name="testtag",
        )
        """
        _response = self._raw_client.update_tag(tag_id, id=id, name=name, request_options=request_options)
        return _response.data

    def delete_tag(self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

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
        client.tag.delete_tag(
            tag_id="TagID",
        )
        """
        _response = self._raw_client.delete_tag(tag_id, request_options=request_options)
        return _response.data


class AsyncTagClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagClient
        """
        return self._raw_client

    async def get_all_tags(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTagResponse:
        """
        Retrieves tags known in the system in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTagResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.get_all_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_tags(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_tag(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Create a tag

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the tag

        name : typing.Optional[str]
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.create_tag(
                name="testtag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag(id=id, name=name, request_options=request_options)
        return _response.data

    async def get_tag(self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tag:
        """
        Get a single tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.get_tag(
                tag_id="TagID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag(tag_id, request_options=request_options)
        return _response.data

    async def update_tag(
        self,
        tag_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Update a tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

        id : typing.Optional[str]
            ID of the tag

        name : typing.Optional[str]
            Name of the tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.update_tag(
                tag_id="TagID",
                name="testtag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag(tag_id, id=id, name=name, request_options=request_options)
        return _response.data

    async def delete_tag(self, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a tag

        Parameters
        ----------
        tag_id : str
            UUID of a tag

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
            await client.tag.delete_tag(
                tag_id="TagID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(tag_id, request_options=request_options)
        return _response.data
