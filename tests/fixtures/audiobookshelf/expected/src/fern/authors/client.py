

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.author import Author
from ..types.author_asin import AuthorAsin
from ..types.author_description import AuthorDescription
from ..types.author_id import AuthorId
from ..types.author_image_path import AuthorImagePath
from ..types.author_name import AuthorName
from ..types.author_search_name import AuthorSearchName
from ..types.image_format import ImageFormat
from ..types.image_height import ImageHeight
from ..types.image_raw import ImageRaw
from ..types.image_url import ImageUrl
from ..types.image_width import ImageWidth
from ..types.region import Region
from .raw_client import AsyncRawAuthorsClient, RawAuthorsClient
from .types.match_author_by_id_response import MatchAuthorByIdResponse
from .types.update_author_by_id_response import UpdateAuthorByIdResponse


OMIT = typing.cast(typing.Any, ...)


class AuthorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorsClient
        """
        return self._raw_client

    def get_author_by_id(
        self,
        id: AuthorId,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Author:
        """
        Get an author by ID. The author's books and series can be included in the response.

        Parameters
        ----------
        id : AuthorId
            Author ID

        include : typing.Optional[str]
            A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Author
            getAuthorById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.get_author_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            include="items,series",
        )
        """
        _response = self._raw_client.get_author_by_id(id, include=include, request_options=request_options)
        return _response.data

    def delete_author_by_id(self, id: AuthorId, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Delete an author by ID. This will remove the author from all books.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            deleteAuthorById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.delete_author_by_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_author_by_id(id, request_options=request_options)
        return _response.data

    def update_author_by_id(
        self,
        id: AuthorId,
        *,
        name: typing.Optional[AuthorName] = OMIT,
        description: typing.Optional[AuthorDescription] = OMIT,
        image_path: typing.Optional[AuthorImagePath] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAuthorByIdResponse:
        """
        Update an author by ID. The author's name and description can be updated. This endpoint will merge two authors if the new author name matches another author name in the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        name : typing.Optional[AuthorName]

        description : typing.Optional[AuthorDescription]

        image_path : typing.Optional[AuthorImagePath]

        asin : typing.Optional[AuthorAsin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAuthorByIdResponse
            updateAuthorById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.update_author_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.update_author_by_id(
            id, name=name, description=description, image_path=image_path, asin=asin, request_options=request_options
        )
        return _response.data

    def get_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Get an author image by author ID. The image will be returned in the requested format and size.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            getAuthorImageById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.get_author_image_by_id(
            id="id",
        )
        """
        with self._raw_client.get_author_image_by_id(id, token=token, ts=ts, request_options=request_options) as r:
            yield from r.data

    def add_author_image_by_id(
        self,
        id: AuthorId,
        *,
        request: ImageUrl,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Add an author image to the server. The image will be downloaded from the provided URL and stored on the server.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request : ImageUrl

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            addAuthorImageById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.add_author_image_by_id(
            id="id",
            request="string",
        )
        """
        with self._raw_client.add_author_image_by_id(
            id, request=request, token=token, ts=ts, request_options=request_options
        ) as r:
            yield from r.data

    def delete_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an author image by author ID. This will remove the image from the server and the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

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
        client.authors.delete_author_image_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.delete_author_image_by_id(id, token=token, ts=ts, request_options=request_options)
        return _response.data

    def update_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        width: typing.Optional[ImageWidth] = OMIT,
        height: typing.Optional[ImageHeight] = OMIT,
        format: typing.Optional[ImageFormat] = OMIT,
        raw: typing.Optional[ImageRaw] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Update an author image by author ID. The image will be resized if the width, height, or format is provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        width : typing.Optional[ImageWidth]

        height : typing.Optional[ImageHeight]

        format : typing.Optional[ImageFormat]

        raw : typing.Optional[ImageRaw]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            updateAuthorImageById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.update_author_image_by_id(
            id="id",
        )
        """
        with self._raw_client.update_author_image_by_id(
            id, token=token, ts=ts, width=width, height=height, format=format, raw=raw, request_options=request_options
        ) as r:
            yield from r.data

    def match_author_by_id(
        self,
        id: AuthorId,
        *,
        q: typing.Optional[AuthorSearchName] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MatchAuthorByIdResponse:
        """
        Match the author against Audible using quick match. Quick match updates the author's description and image (if no image already existed) with information from audible. Either `asin` or `q` must be provided, with `asin` taking priority if both are provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        q : typing.Optional[AuthorSearchName]

        asin : typing.Optional[AuthorAsin]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MatchAuthorByIdResponse
            matchAuthorById OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authors.match_author_by_id(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.match_author_by_id(
            id, q=q, asin=asin, region=region, request_options=request_options
        )
        return _response.data


class AsyncAuthorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorsClient
        """
        return self._raw_client

    async def get_author_by_id(
        self,
        id: AuthorId,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Author:
        """
        Get an author by ID. The author's books and series can be included in the response.

        Parameters
        ----------
        id : AuthorId
            Author ID

        include : typing.Optional[str]
            A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Author
            getAuthorById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.get_author_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                include="items,series",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_author_by_id(id, include=include, request_options=request_options)
        return _response.data

    async def delete_author_by_id(
        self, id: AuthorId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Delete an author by ID. This will remove the author from all books.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            deleteAuthorById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.delete_author_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_author_by_id(id, request_options=request_options)
        return _response.data

    async def update_author_by_id(
        self,
        id: AuthorId,
        *,
        name: typing.Optional[AuthorName] = OMIT,
        description: typing.Optional[AuthorDescription] = OMIT,
        image_path: typing.Optional[AuthorImagePath] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAuthorByIdResponse:
        """
        Update an author by ID. The author's name and description can be updated. This endpoint will merge two authors if the new author name matches another author name in the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        name : typing.Optional[AuthorName]

        description : typing.Optional[AuthorDescription]

        image_path : typing.Optional[AuthorImagePath]

        asin : typing.Optional[AuthorAsin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAuthorByIdResponse
            updateAuthorById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.update_author_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_author_by_id(
            id, name=name, description=description, image_path=image_path, asin=asin, request_options=request_options
        )
        return _response.data

    async def get_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Get an author image by author ID. The image will be returned in the requested format and size.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            getAuthorImageById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.get_author_image_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_author_image_by_id(
            id, token=token, ts=ts, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def add_author_image_by_id(
        self,
        id: AuthorId,
        *,
        request: ImageUrl,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Add an author image to the server. The image will be downloaded from the provided URL and stored on the server.

        Parameters
        ----------
        id : AuthorId
            Author ID

        request : ImageUrl

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            addAuthorImageById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.add_author_image_by_id(
                id="id",
                request="string",
            )


        asyncio.run(main())
        """
        async with self._raw_client.add_author_image_by_id(
            id, request=request, token=token, ts=ts, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an author image by author ID. This will remove the image from the server and the database.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

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
            await client.authors.delete_author_image_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_author_image_by_id(
            id, token=token, ts=ts, request_options=request_options
        )
        return _response.data

    async def update_author_image_by_id(
        self,
        id: AuthorId,
        *,
        token: typing.Optional[str] = None,
        ts: typing.Optional[int] = None,
        width: typing.Optional[ImageWidth] = OMIT,
        height: typing.Optional[ImageHeight] = OMIT,
        format: typing.Optional[ImageFormat] = OMIT,
        raw: typing.Optional[ImageRaw] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Update an author image by author ID. The image will be resized if the width, height, or format is provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        token : typing.Optional[str]
            API token

        ts : typing.Optional[int]
            Updated at value

        width : typing.Optional[ImageWidth]

        height : typing.Optional[ImageHeight]

        format : typing.Optional[ImageFormat]

        raw : typing.Optional[ImageRaw]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            updateAuthorImageById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.update_author_image_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.update_author_image_by_id(
            id, token=token, ts=ts, width=width, height=height, format=format, raw=raw, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def match_author_by_id(
        self,
        id: AuthorId,
        *,
        q: typing.Optional[AuthorSearchName] = OMIT,
        asin: typing.Optional[AuthorAsin] = OMIT,
        region: typing.Optional[Region] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MatchAuthorByIdResponse:
        """
        Match the author against Audible using quick match. Quick match updates the author's description and image (if no image already existed) with information from audible. Either `asin` or `q` must be provided, with `asin` taking priority if both are provided.

        Parameters
        ----------
        id : AuthorId
            Author ID

        q : typing.Optional[AuthorSearchName]

        asin : typing.Optional[AuthorAsin]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MatchAuthorByIdResponse
            matchAuthorById OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authors.match_author_by_id(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.match_author_by_id(
            id, q=q, asin=asin, region=region, request_options=request_options
        )
        return _response.data
