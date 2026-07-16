

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFeedbackClient, RawFeedbackClient


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

    def feedback_details(self, feedback_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Feedback details

        Parameters
        ----------
        feedback_id : str

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
        client.feedback.feedback_details(
            feedback_id="feedback_id",
        )
        """
        _response = self._raw_client.feedback_details(feedback_id, request_options=request_options)
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

    async def feedback_details(
        self, feedback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Feedback details

        Parameters
        ----------
        feedback_id : str

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
            await client.feedback.feedback_details(
                feedback_id="feedback_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.feedback_details(feedback_id, request_options=request_options)
        return _response.data
