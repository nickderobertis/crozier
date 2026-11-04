

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contributor_basic_out import ContributorBasicOut
from ..types.story_out import StoryOut
from ..types.tile_gradient_out import TileGradientOut
from .raw_client import AsyncRawMockClient, RawMockClient


OMIT = typing.cast(typing.Any, ...)


class MockClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMockClient
        """
        return self._raw_client

    def list_contributors(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ContributorBasicOut]:
        """
        Get all contributors with basic info: name, country, series_id, and mosaic_url only

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContributorBasicOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.list_contributors()
        """
        _response = self._raw_client.list_contributors(request_options=request_options)
        return _response.data

    def get_contributor(
        self, contributor_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorBasicOut:
        """
        Get a specific contributor with basic info: name, country, series_id, and mosaic_url only

        Parameters
        ----------
        contributor_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorBasicOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.get_contributor(
            contributor_id=1,
        )
        """
        _response = self._raw_client.get_contributor(contributor_id, request_options=request_options)
        return _response.data

    def list_stories(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[StoryOut]:
        """
        Get all stories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StoryOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.list_stories()
        """
        _response = self._raw_client.list_stories(request_options=request_options)
        return _response.data

    def create_story(
        self,
        *,
        title: str,
        name: str,
        occupation: str,
        story: str,
        image: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StoryOut:
        """
        Create a new story with image upload

        Parameters
        ----------
        title : str

        name : str

        occupation : str

        story : str

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoryOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.create_story(
            title="title",
            name="name",
            occupation="occupation",
            story="story",
        )
        """
        _response = self._raw_client.create_story(
            title=title, name=name, occupation=occupation, story=story, image=image, request_options=request_options
        )
        return _response.data

    def list_tile_gradients(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TileGradientOut]:
        """
        Get all tile gradients

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TileGradientOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.list_tile_gradients()
        """
        _response = self._raw_client.list_tile_gradients(request_options=request_options)
        return _response.data

    def create_tile_gradient(
        self, *, border: str, from_: str, glow: str, to: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TileGradientOut:
        """
        Create a new tile gradient

        Parameters
        ----------
        border : str

        from_ : str

        glow : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileGradientOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mock.create_tile_gradient(
            border="border",
            from_="from",
            glow="glow",
            to="to",
        )
        """
        _response = self._raw_client.create_tile_gradient(
            border=border, from_=from_, glow=glow, to=to, request_options=request_options
        )
        return _response.data


class AsyncMockClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMockClient
        """
        return self._raw_client

    async def list_contributors(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ContributorBasicOut]:
        """
        Get all contributors with basic info: name, country, series_id, and mosaic_url only

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContributorBasicOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.list_contributors()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_contributors(request_options=request_options)
        return _response.data

    async def get_contributor(
        self, contributor_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContributorBasicOut:
        """
        Get a specific contributor with basic info: name, country, series_id, and mosaic_url only

        Parameters
        ----------
        contributor_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContributorBasicOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.get_contributor(
                contributor_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contributor(contributor_id, request_options=request_options)
        return _response.data

    async def list_stories(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[StoryOut]:
        """
        Get all stories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StoryOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.list_stories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_stories(request_options=request_options)
        return _response.data

    async def create_story(
        self,
        *,
        title: str,
        name: str,
        occupation: str,
        story: str,
        image: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StoryOut:
        """
        Create a new story with image upload

        Parameters
        ----------
        title : str

        name : str

        occupation : str

        story : str

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoryOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.create_story(
                title="title",
                name="name",
                occupation="occupation",
                story="story",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_story(
            title=title, name=name, occupation=occupation, story=story, image=image, request_options=request_options
        )
        return _response.data

    async def list_tile_gradients(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TileGradientOut]:
        """
        Get all tile gradients

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TileGradientOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.list_tile_gradients()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tile_gradients(request_options=request_options)
        return _response.data

    async def create_tile_gradient(
        self, *, border: str, from_: str, glow: str, to: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TileGradientOut:
        """
        Create a new tile gradient

        Parameters
        ----------
        border : str

        from_ : str

        glow : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileGradientOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mock.create_tile_gradient(
                border="border",
                from_="from",
                glow="glow",
                to="to",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tile_gradient(
            border=border, from_=from_, glow=glow, to=to, request_options=request_options
        )
        return _response.data
