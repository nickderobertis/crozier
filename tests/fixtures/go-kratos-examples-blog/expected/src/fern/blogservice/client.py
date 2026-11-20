

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_article_reply import CreateArticleReply
from ..types.delete_article_reply import DeleteArticleReply
from ..types.get_article_reply import GetArticleReply
from ..types.list_article_reply import ListArticleReply
from ..types.update_article_reply import UpdateArticleReply
from .raw_client import AsyncRawBlogserviceClient, RawBlogserviceClient


OMIT = typing.cast(typing.Any, ...)


class BlogserviceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBlogserviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBlogserviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBlogserviceClient
        """
        return self._raw_client

    def listarticle(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListArticleReply:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListArticleReply
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.blogservice.listarticle()
        """
        _response = self._raw_client.listarticle(request_options=request_options)
        return _response.data

    def createarticle(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateArticleReply:
        """
        Parameters
        ----------
        title : typing.Optional[str]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateArticleReply
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.blogservice.createarticle()
        """
        _response = self._raw_client.createarticle(title=title, content=content, request_options=request_options)
        return _response.data

    def getarticle(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> GetArticleReply:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArticleReply
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.blogservice.getarticle(
            id=1000000,
        )
        """
        _response = self._raw_client.getarticle(id, request_options=request_options)
        return _response.data

    def updatearticle(
        self,
        id_path_param: int,
        *,
        id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateArticleReply:
        """
        Parameters
        ----------
        id_path_param : int

        id : typing.Optional[int]

        title : typing.Optional[str]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateArticleReply
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.blogservice.updatearticle(
            id_path_param=1000000,
        )
        """
        _response = self._raw_client.updatearticle(
            id_path_param, id=id, title=title, content=content, request_options=request_options
        )
        return _response.data

    def deletearticle(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteArticleReply:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteArticleReply
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.blogservice.deletearticle(
            id=1000000,
        )
        """
        _response = self._raw_client.deletearticle(id, request_options=request_options)
        return _response.data


class AsyncBlogserviceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBlogserviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBlogserviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBlogserviceClient
        """
        return self._raw_client

    async def listarticle(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListArticleReply:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListArticleReply
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.blogservice.listarticle()


        asyncio.run(main())
        """
        _response = await self._raw_client.listarticle(request_options=request_options)
        return _response.data

    async def createarticle(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateArticleReply:
        """
        Parameters
        ----------
        title : typing.Optional[str]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateArticleReply
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.blogservice.createarticle()


        asyncio.run(main())
        """
        _response = await self._raw_client.createarticle(title=title, content=content, request_options=request_options)
        return _response.data

    async def getarticle(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> GetArticleReply:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArticleReply
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.blogservice.getarticle(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getarticle(id, request_options=request_options)
        return _response.data

    async def updatearticle(
        self,
        id_path_param: int,
        *,
        id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateArticleReply:
        """
        Parameters
        ----------
        id_path_param : int

        id : typing.Optional[int]

        title : typing.Optional[str]

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateArticleReply
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.blogservice.updatearticle(
                id_path_param=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatearticle(
            id_path_param, id=id, title=title, content=content, request_options=request_options
        )
        return _response.data

    async def deletearticle(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteArticleReply:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteArticleReply
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.blogservice.deletearticle(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletearticle(id, request_options=request_options)
        return _response.data
