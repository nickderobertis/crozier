

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tag import Tag
from ..types.tag_set import TagSet
from .raw_client import AsyncRawTagClient, RawTagClient


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

    def list_tags(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        tag_set: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Tag]:
        """
        Retrieve tags.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        tag_set : typing.Optional[str]
            Restrict results to tags belonging to this tag set.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            A list of tags

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.list_tags()
        """
        _response = self._raw_client.list_tags(
            owned_by=owned_by, tag_set=tag_set, url_words=url_words, request_options=request_options
        )
        return _response.data

    def create_a_new_tag(
        self,
        *,
        name: str,
        colour: typing.Optional[str] = OMIT,
        tag_set: typing.Optional[TagSet] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Parameters
        ----------
        name : str

        colour : typing.Optional[str]

        tag_set : typing.Optional[TagSet]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.create_a_new_tag(
            name="name",
        )
        """
        _response = self._raw_client.create_a_new_tag(
            name=name, colour=colour, tag_set=tag_set, url_words=url_words, request_options=request_options
        )
        return _response.data

    def retrieve_a_single_tag_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tag:
        """
        Parameters
        ----------
        id : str
            Id of the tag to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            The tag

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.retrieve_a_single_tag_by_id(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_a_single_tag_by_id(id, request_options=request_options)
        return _response.data

    def list_tag_sets(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TagSet]:
        """
        Retrieve tag sets.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagSet]
            A list of tag sets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.list_tag_sets()
        """
        _response = self._raw_client.list_tag_sets(
            owned_by=owned_by, url_words=url_words, request_options=request_options
        )
        return _response.data

    def create_a_new_tag_set(
        self, *, name: str, url_words: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TagSet:
        """
        Parameters
        ----------
        name : str

        url_words : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagSet
            Tagset created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.create_a_new_tag_set(
            name="name",
            url_words="urlWords",
        )
        """
        _response = self._raw_client.create_a_new_tag_set(
            name=name, url_words=url_words, request_options=request_options
        )
        return _response.data

    def retrieve_a_single_tag_set_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TagSet:
        """
        Parameters
        ----------
        id : str
            Id of the tag set to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagSet
            The tag set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.retrieve_a_single_tag_set_by_id(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_a_single_tag_set_by_id(id, request_options=request_options)
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

    async def list_tags(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        tag_set: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Tag]:
        """
        Retrieve tags.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        tag_set : typing.Optional[str]
            Restrict results to tags belonging to this tag set.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tag]
            A list of tags

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.list_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(
            owned_by=owned_by, tag_set=tag_set, url_words=url_words, request_options=request_options
        )
        return _response.data

    async def create_a_new_tag(
        self,
        *,
        name: str,
        colour: typing.Optional[str] = OMIT,
        tag_set: typing.Optional[TagSet] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Parameters
        ----------
        name : str

        colour : typing.Optional[str]

        tag_set : typing.Optional[TagSet]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Tag created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.create_a_new_tag(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_tag(
            name=name, colour=colour, tag_set=tag_set, url_words=url_words, request_options=request_options
        )
        return _response.data

    async def retrieve_a_single_tag_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tag:
        """
        Parameters
        ----------
        id : str
            Id of the tag to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            The tag

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.retrieve_a_single_tag_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_tag_by_id(id, request_options=request_options)
        return _response.data

    async def list_tag_sets(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TagSet]:
        """
        Retrieve tag sets.

        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to those owned by this user.

        url_words : typing.Optional[str]
            Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TagSet]
            A list of tag sets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.list_tag_sets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tag_sets(
            owned_by=owned_by, url_words=url_words, request_options=request_options
        )
        return _response.data

    async def create_a_new_tag_set(
        self, *, name: str, url_words: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TagSet:
        """
        Parameters
        ----------
        name : str

        url_words : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagSet
            Tagset created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.create_a_new_tag_set(
                name="name",
                url_words="urlWords",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_tag_set(
            name=name, url_words=url_words, request_options=request_options
        )
        return _response.data

    async def retrieve_a_single_tag_set_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TagSet:
        """
        Parameters
        ----------
        id : str
            Id of the tag set to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagSet
            The tag set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.retrieve_a_single_tag_set_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_tag_set_by_id(id, request_options=request_options)
        return _response.data
