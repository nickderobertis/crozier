

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feedback_query import FeedbackQuery
from ..types.feedback_settings import FeedbackSettings
from .raw_client import AsyncRawFeedbackClient, RawFeedbackClient


OMIT = typing.cast(typing.Any, ...)


class FeedbackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeedbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeedbackClient
        """
        return self._raw_client

    def send_feedback(
        self,
        *,
        queries: typing.Sequence[FeedbackQuery],
        primary: typing.Optional[FeedbackQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackSettings:
        """
        Parameters
        ----------
        queries : typing.Sequence[FeedbackQuery]

        primary : typing.Optional[FeedbackQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackSettings
            Accepted.

        Examples
        --------
        from fern import FeedbackQuery, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.feedback.send_feedback(
            queries=[FeedbackQuery()],
        )
        """
        _response = self._raw_client.send_feedback(queries=queries, primary=primary, request_options=request_options)
        return _response.data


class AsyncFeedbackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeedbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeedbackClient
        """
        return self._raw_client

    async def send_feedback(
        self,
        *,
        queries: typing.Sequence[FeedbackQuery],
        primary: typing.Optional[FeedbackQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackSettings:
        """
        Parameters
        ----------
        queries : typing.Sequence[FeedbackQuery]

        primary : typing.Optional[FeedbackQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackSettings
            Accepted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FeedbackQuery

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.feedback.send_feedback(
                queries=[FeedbackQuery()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_feedback(
            queries=queries, primary=primary, request_options=request_options
        )
        return _response.data
