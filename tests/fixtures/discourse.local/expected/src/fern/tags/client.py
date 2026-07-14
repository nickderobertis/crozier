

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTagsClient, RawTagsClient
from .types.create_tag_group_response import CreateTagGroupResponse
from .types.get_tag_group_response import GetTagGroupResponse
from .types.get_tag_response import GetTagResponse
from .types.list_tag_groups_response import ListTagGroupsResponse
from .types.list_tags_response import ListTagsResponse
from .types.update_tag_group_response import UpdateTagGroupResponse


OMIT = typing.cast(typing.Any, ...)


class TagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagsClient
        """
        return self._raw_client

    def get_tag(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetTagResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTagResponse
            notifications

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.get_tag(
            name="name",
        )
        """
        _response = self._raw_client.get_tag(name, request_options=request_options)
        return _response.data

    def list_tag_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListTagGroupsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTagGroupsResponse
            tags

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.list_tag_groups()
        """
        _response = self._raw_client.list_tag_groups(request_options=request_options)
        return _response.data

    def create_tag_group(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTagGroupResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTagGroupResponse
            tag group created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.create_tag_group(
            name="name",
        )
        """
        _response = self._raw_client.create_tag_group(name=name, request_options=request_options)
        return _response.data

    def get_tag_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetTagGroupResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTagGroupResponse
            notifications

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.get_tag_group(
            id="id",
        )
        """
        _response = self._raw_client.get_tag_group(id, request_options=request_options)
        return _response.data

    def update_tag_group(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateTagGroupResponse:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTagGroupResponse
            Tag group updated

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.update_tag_group(
            id="id",
        )
        """
        _response = self._raw_client.update_tag_group(id, name=name, request_options=request_options)
        return _response.data

    def list_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListTagsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTagsResponse
            notifications

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.list_tags()
        """
        _response = self._raw_client.list_tags(request_options=request_options)
        return _response.data


class AsyncTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagsClient
        """
        return self._raw_client

    async def get_tag(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetTagResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTagResponse
            notifications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.get_tag(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag(name, request_options=request_options)
        return _response.data

    async def list_tag_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListTagGroupsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTagGroupsResponse
            tags

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.list_tag_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tag_groups(request_options=request_options)
        return _response.data

    async def create_tag_group(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateTagGroupResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTagGroupResponse
            tag group created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.create_tag_group(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag_group(name=name, request_options=request_options)
        return _response.data

    async def get_tag_group(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTagGroupResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTagGroupResponse
            notifications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.get_tag_group(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag_group(id, request_options=request_options)
        return _response.data

    async def update_tag_group(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateTagGroupResponse:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTagGroupResponse
            Tag group updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.update_tag_group(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag_group(id, name=name, request_options=request_options)
        return _response.data

    async def list_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListTagsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTagsResponse
            notifications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.list_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(request_options=request_options)
        return _response.data
