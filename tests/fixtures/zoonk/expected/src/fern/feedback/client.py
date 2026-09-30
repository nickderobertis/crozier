

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feedback_response import FeedbackResponse
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

    def create_feedback(
        self, *, email: str, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedbackResponse:
        """
        Parameters
        ----------
        email : str
            Reply-to email address

        message : str
            Feedback or contact message body

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponse
            Feedback received

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feedback.create_feedback(
            email="email",
            message="message",
        )
        """
        _response = self._raw_client.create_feedback(email=email, message=message, request_options=request_options)
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

    async def create_feedback(
        self, *, email: str, message: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FeedbackResponse:
        """
        Parameters
        ----------
        email : str
            Reply-to email address

        message : str
            Feedback or contact message body

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponse
            Feedback received

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feedback.create_feedback(
                email="email",
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_feedback(
            email=email, message=message, request_options=request_options
        )
        return _response.data
