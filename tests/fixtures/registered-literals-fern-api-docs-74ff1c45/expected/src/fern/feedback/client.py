

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_feedback_response import CreateFeedbackResponse
from ..types.get_feedback_response import GetFeedbackResponse
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
        self,
        domain_path_param: str,
        *,
        conversation_id: str,
        query_id: str,
        domain: str,
        is_helpful: bool,
        feedback_message: typing.Optional[str] = OMIT,
        user_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFeedbackResponse:
        """
        Parameters
        ----------
        domain_path_param : str

        conversation_id : str
            The ID of the conversation

        query_id : str
            The ID of the query

        domain : str
            The domain of the conversation

        is_helpful : bool
            Whether the conversation was helpful

        feedback_message : typing.Optional[str]
            The feedback message from the user

        user_email : typing.Optional[str]
            The email of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFeedbackResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feedback.create_feedback(
            domain_path_param="domain",
            conversation_id="conversation_id",
            query_id="query_id",
            domain="domain",
            is_helpful=True,
        )
        """
        _response = self._raw_client.create_feedback(
            domain_path_param,
            conversation_id=conversation_id,
            query_id=query_id,
            domain=domain,
            is_helpful=is_helpful,
            feedback_message=feedback_message,
            user_email=user_email,
            request_options=request_options,
        )
        return _response.data

    def get_feedback_by_id(
        self, domain: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFeedbackResponse:
        """
        Parameters
        ----------
        domain : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFeedbackResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.feedback.get_feedback_by_id(
            domain="domain",
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.get_feedback_by_id(domain, conversation_id, request_options=request_options)
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
        self,
        domain_path_param: str,
        *,
        conversation_id: str,
        query_id: str,
        domain: str,
        is_helpful: bool,
        feedback_message: typing.Optional[str] = OMIT,
        user_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateFeedbackResponse:
        """
        Parameters
        ----------
        domain_path_param : str

        conversation_id : str
            The ID of the conversation

        query_id : str
            The ID of the query

        domain : str
            The domain of the conversation

        is_helpful : bool
            Whether the conversation was helpful

        feedback_message : typing.Optional[str]
            The feedback message from the user

        user_email : typing.Optional[str]
            The email of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateFeedbackResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feedback.create_feedback(
                domain_path_param="domain",
                conversation_id="conversation_id",
                query_id="query_id",
                domain="domain",
                is_helpful=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_feedback(
            domain_path_param,
            conversation_id=conversation_id,
            query_id=query_id,
            domain=domain,
            is_helpful=is_helpful,
            feedback_message=feedback_message,
            user_email=user_email,
            request_options=request_options,
        )
        return _response.data

    async def get_feedback_by_id(
        self, domain: str, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFeedbackResponse:
        """
        Parameters
        ----------
        domain : str

        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFeedbackResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.feedback.get_feedback_by_id(
                domain="domain",
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feedback_by_id(domain, conversation_id, request_options=request_options)
        return _response.data
