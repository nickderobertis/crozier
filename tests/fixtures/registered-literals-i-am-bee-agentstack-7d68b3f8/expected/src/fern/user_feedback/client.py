

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_result_user_feedback_response import PaginatedResultUserFeedbackResponse
from .raw_client import AsyncRawUserFeedbackClient, RawUserFeedbackClient


OMIT = typing.cast(typing.Any, ...)


class UserFeedbackClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserFeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserFeedbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserFeedbackClient
        """
        return self._raw_client

    def list_user_feedback(
        self,
        *,
        provider_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultUserFeedbackResponse:
        """
        Parameters
        ----------
        provider_id : typing.Optional[str]

        limit : typing.Optional[int]

        after_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultUserFeedbackResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_feedback.list_user_feedback()
        """
        _response = self._raw_client.list_user_feedback(
            provider_id=provider_id, limit=limit, after_cursor=after_cursor, request_options=request_options
        )
        return _response.data

    def user_feedback(
        self,
        *,
        provider_id: str,
        task_id: str,
        context_id: str,
        rating: int,
        message: str,
        comment_tags: typing.Optional[typing.Sequence[str]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        provider_id : str

        task_id : str

        context_id : str

        rating : int
            Rating thats either 1 or -1

        message : str

        comment_tags : typing.Optional[typing.Sequence[str]]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_feedback.user_feedback(
            provider_id="provider_id",
            task_id="task_id",
            context_id="context_id",
            rating=1,
            message="message",
        )
        """
        _response = self._raw_client.user_feedback(
            provider_id=provider_id,
            task_id=task_id,
            context_id=context_id,
            rating=rating,
            message=message,
            comment_tags=comment_tags,
            comment=comment,
            request_options=request_options,
        )
        return _response.data


class AsyncUserFeedbackClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserFeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserFeedbackClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserFeedbackClient
        """
        return self._raw_client

    async def list_user_feedback(
        self,
        *,
        provider_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        after_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultUserFeedbackResponse:
        """
        Parameters
        ----------
        provider_id : typing.Optional[str]

        limit : typing.Optional[int]

        after_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultUserFeedbackResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_feedback.list_user_feedback()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_feedback(
            provider_id=provider_id, limit=limit, after_cursor=after_cursor, request_options=request_options
        )
        return _response.data

    async def user_feedback(
        self,
        *,
        provider_id: str,
        task_id: str,
        context_id: str,
        rating: int,
        message: str,
        comment_tags: typing.Optional[typing.Sequence[str]] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        provider_id : str

        task_id : str

        context_id : str

        rating : int
            Rating thats either 1 or -1

        message : str

        comment_tags : typing.Optional[typing.Sequence[str]]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_feedback.user_feedback(
                provider_id="provider_id",
                task_id="task_id",
                context_id="context_id",
                rating=1,
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_feedback(
            provider_id=provider_id,
            task_id=task_id,
            context_id=context_id,
            rating=rating,
            message=message,
            comment_tags=comment_tags,
            comment=comment,
            request_options=request_options,
        )
        return _response.data
