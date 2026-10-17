

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.statuses_response import StatusesResponse
from .raw_client import AsyncRawStatusesClient, RawStatusesClient


OMIT = typing.cast(typing.Any, ...)


class StatusesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatusesClient
        """
        return self._raw_client

    def get_statuses_user_timeline(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        規定のアカウントのタイムライン(home)を取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.statuses.get_statuses_user_timeline()
        """
        _response = self._raw_client.get_statuses_user_timeline(request_options=request_options)
        return _response.data

    def get_statuses_mentions_timeline(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        規定のアカウントに対するメンションを取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.statuses.get_statuses_mentions_timeline()
        """
        _response = self._raw_client.get_statuses_mentions_timeline(request_options=request_options)
        return _response.data

    def get_statuses_hash(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusesResponse:
        """
        規定のハッシュタグで検索した結果を取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.statuses.get_statuses_hash()
        """
        _response = self._raw_client.get_statuses_hash(request_options=request_options)
        return _response.data

    def post_statuses_update(
        self,
        *,
        status: typing.Optional[str] = OMIT,
        media_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        in_reply_to_tweet_id: typing.Optional[str] = OMIT,
        quote_tweet_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusesResponse:
        """
        ツイート投稿する

        Parameters
        ----------
        status : typing.Optional[str]
            ツイート本文

        media_ids : typing.Optional[typing.Sequence[str]]
            事前にアップロードした画像・動画のID

        in_reply_to_tweet_id : typing.Optional[str]
            リプライ先のツイートID

        quote_tweet_id : typing.Optional[str]
            引用RTの引用元ツイートID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse
            ツイート投稿後のstatuses/user_timelineに相当するもの

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.statuses.post_statuses_update(
            status="走者乙ｗｗｗｗｗｗｗｗｗｗｗｗ\nｗｗｗｗｗ\nｗｗｗｗｗｗｗｗｗｗｗｗｗｗ",
            media_ids=["710511363345354753"],
        )
        """
        _response = self._raw_client.post_statuses_update(
            status=status,
            media_ids=media_ids,
            in_reply_to_tweet_id=in_reply_to_tweet_id,
            quote_tweet_id=quote_tweet_id,
            request_options=request_options,
        )
        return _response.data

    def post_statuses_destroy_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        指定したIDのツイートを削除する。

        Parameters
        ----------
        id : str
            削除対象のツイートID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse
            処理実行後のstatuses/user_timelineに相当するもの

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            auth="YOUR_AUTH",
        )
        client.statuses.post_statuses_destroy_id(
            id="id",
        )
        """
        _response = self._raw_client.post_statuses_destroy_id(id, request_options=request_options)
        return _response.data


class AsyncStatusesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatusesClient
        """
        return self._raw_client

    async def get_statuses_user_timeline(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        規定のアカウントのタイムライン(home)を取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.statuses.get_statuses_user_timeline()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_statuses_user_timeline(request_options=request_options)
        return _response.data

    async def get_statuses_mentions_timeline(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        規定のアカウントに対するメンションを取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.statuses.get_statuses_mentions_timeline()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_statuses_mentions_timeline(request_options=request_options)
        return _response.data

    async def get_statuses_hash(self, *, request_options: typing.Optional[RequestOptions] = None) -> StatusesResponse:
        """
        規定のハッシュタグで検索した結果を取得する。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.statuses.get_statuses_hash()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_statuses_hash(request_options=request_options)
        return _response.data

    async def post_statuses_update(
        self,
        *,
        status: typing.Optional[str] = OMIT,
        media_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        in_reply_to_tweet_id: typing.Optional[str] = OMIT,
        quote_tweet_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StatusesResponse:
        """
        ツイート投稿する

        Parameters
        ----------
        status : typing.Optional[str]
            ツイート本文

        media_ids : typing.Optional[typing.Sequence[str]]
            事前にアップロードした画像・動画のID

        in_reply_to_tweet_id : typing.Optional[str]
            リプライ先のツイートID

        quote_tweet_id : typing.Optional[str]
            引用RTの引用元ツイートID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse
            ツイート投稿後のstatuses/user_timelineに相当するもの

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.statuses.post_statuses_update(
                status="走者乙ｗｗｗｗｗｗｗｗｗｗｗｗ\nｗｗｗｗｗ\nｗｗｗｗｗｗｗｗｗｗｗｗｗｗ",
                media_ids=["710511363345354753"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_statuses_update(
            status=status,
            media_ids=media_ids,
            in_reply_to_tweet_id=in_reply_to_tweet_id,
            quote_tweet_id=quote_tweet_id,
            request_options=request_options,
        )
        return _response.data

    async def post_statuses_destroy_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusesResponse:
        """
        指定したIDのツイートを削除する。

        Parameters
        ----------
        id : str
            削除対象のツイートID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusesResponse
            処理実行後のstatuses/user_timelineに相当するもの

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            auth="YOUR_AUTH",
        )


        async def main() -> None:
            await client.statuses.post_statuses_destroy_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_statuses_destroy_id(id, request_options=request_options)
        return _response.data
