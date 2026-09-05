

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.color_str import ColorStr
from ..types.description_safe_str import DescriptionSafeStr
from ..types.envelope_list_tag_get import EnvelopeListTagGet
from ..types.envelope_list_tag_group_get import EnvelopeListTagGroupGet
from ..types.envelope_tag_get import EnvelopeTagGet
from ..types.group_id_int import GroupIdInt
from ..types.name_safe_str import NameSafeStr
from .raw_client import AsyncRawTagsClient, RawTagsClient


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

    def list_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTagGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.list_tags()
        """
        _response = self._raw_client.list_tags(request_options=request_options)
        return _response.data

    def create_tag(
        self,
        *,
        name: NameSafeStr,
        color: ColorStr,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Parameters
        ----------
        name : NameSafeStr

        color : ColorStr

        description : typing.Optional[DescriptionSafeStr]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.create_tag(
            name="name",
            color="color",
        )
        """
        _response = self._raw_client.create_tag(
            name=name, color=color, description=description, priority=priority, request_options=request_options
        )
        return _response.data

    def delete_tag(self, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.delete_tag(
            tag_id=1,
        )
        """
        _response = self._raw_client.delete_tag(tag_id, request_options=request_options)
        return _response.data

    def update_tag(
        self,
        tag_id: int,
        *,
        name: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        color: typing.Optional[ColorStr] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Parameters
        ----------
        tag_id : int

        name : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        color : typing.Optional[ColorStr]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.update_tag(
            tag_id=1,
        )
        """
        _response = self._raw_client.update_tag(
            tag_id, name=name, description=description, color=color, priority=priority, request_options=request_options
        )
        return _response.data

    def list_tag_groups(
        self, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListTagGroupGet:
        """
        Lists all groups associated to this tag

        Parameters
        ----------
        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.list_tag_groups(
            tag_id=1,
        )
        """
        _response = self._raw_client.list_tag_groups(tag_id, request_options=request_options)
        return _response.data

    def create_tag_group(
        self,
        tag_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Shares tag `tag_id` with an organization or user with `group_id` providing access-rights to it

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.create_tag_group(
            tag_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.create_tag_group(
            tag_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def replace_tag_group(
        self,
        tag_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListTagGroupGet:
        """
        Replace access rights on tag for associated organization or user with `group_id`

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGroupGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.replace_tag_group(
            tag_id=1,
            group_id=1,
            read=True,
            write=True,
            delete=True,
        )
        """
        _response = self._raw_client.replace_tag_group(
            tag_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    def delete_tag_group(
        self, tag_id: int, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete access rights on tag to an associated organization or user with `group_id`

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tags.delete_tag_group(
            tag_id=1,
            group_id=1,
        )
        """
        _response = self._raw_client.delete_tag_group(tag_id, group_id, request_options=request_options)
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

    async def list_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> EnvelopeListTagGet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGet
            Successful Response

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

    async def create_tag(
        self,
        *,
        name: NameSafeStr,
        color: ColorStr,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Parameters
        ----------
        name : NameSafeStr

        color : ColorStr

        description : typing.Optional[DescriptionSafeStr]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.create_tag(
                name="name",
                color="color",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag(
            name=name, color=color, description=description, priority=priority, request_options=request_options
        )
        return _response.data

    async def delete_tag(self, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.delete_tag(
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(tag_id, request_options=request_options)
        return _response.data

    async def update_tag(
        self,
        tag_id: int,
        *,
        name: typing.Optional[NameSafeStr] = OMIT,
        description: typing.Optional[DescriptionSafeStr] = OMIT,
        color: typing.Optional[ColorStr] = OMIT,
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Parameters
        ----------
        tag_id : int

        name : typing.Optional[NameSafeStr]

        description : typing.Optional[DescriptionSafeStr]

        color : typing.Optional[ColorStr]

        priority : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.update_tag(
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag(
            tag_id, name=name, description=description, color=color, priority=priority, request_options=request_options
        )
        return _response.data

    async def list_tag_groups(
        self, tag_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListTagGroupGet:
        """
        Lists all groups associated to this tag

        Parameters
        ----------
        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.list_tag_groups(
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tag_groups(tag_id, request_options=request_options)
        return _response.data

    async def create_tag_group(
        self,
        tag_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTagGet:
        """
        Shares tag `tag_id` with an organization or user with `group_id` providing access-rights to it

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTagGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.create_tag_group(
                tag_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag_group(
            tag_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def replace_tag_group(
        self,
        tag_id: int,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListTagGroupGet:
        """
        Replace access rights on tag for associated organization or user with `group_id`

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGroupGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.replace_tag_group(
                tag_id=1,
                group_id=1,
                read=True,
                write=True,
                delete=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_tag_group(
            tag_id, group_id, read=read, write=write, delete=delete, request_options=request_options
        )
        return _response.data

    async def delete_tag_group(
        self, tag_id: int, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete access rights on tag to an associated organization or user with `group_id`

        Parameters
        ----------
        tag_id : int

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tags.delete_tag_group(
                tag_id=1,
                group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag_group(tag_id, group_id, request_options=request_options)
        return _response.data
