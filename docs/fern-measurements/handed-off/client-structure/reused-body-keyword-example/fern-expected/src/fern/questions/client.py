

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.open_questions import OpenQuestions
from ..types.ticket import Ticket
from .raw_client import AsyncRawQuestionsClient, RawQuestionsClient


OMIT = typing.cast(typing.Any, ...)


class QuestionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQuestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQuestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQuestionsClient
        """
        return self._raw_client

    def list_open_questions(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenQuestions:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenQuestions
            The open questions.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.questions.list_open_questions()
        """
        _response = self._raw_client.list_open_questions(request_options=request_options)
        return _response.data

    def file_question(
        self,
        *,
        bench: str,
        question_bench: str,
        asked_by: str,
        urgent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        bench : str
            The bench the question is filed under.

        question_bench : str
            The bench the question is about.

        asked_by : str
            The grower asking.

        urgent : typing.Optional[bool]
            Whether a keeper should answer today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket
            The filed question's ticket.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.questions.file_question(
            bench="bench",
            question_bench="bench",
            asked_by="asked_by",
        )
        """
        _response = self._raw_client.file_question(
            bench=bench,
            question_bench=question_bench,
            asked_by=asked_by,
            urgent=urgent,
            request_options=request_options,
        )
        return _response.data


class AsyncQuestionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQuestionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQuestionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQuestionsClient
        """
        return self._raw_client

    async def list_open_questions(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenQuestions:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenQuestions
            The open questions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.questions.list_open_questions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_open_questions(request_options=request_options)
        return _response.data

    async def file_question(
        self,
        *,
        bench: str,
        question_bench: str,
        asked_by: str,
        urgent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        bench : str
            The bench the question is filed under.

        question_bench : str
            The bench the question is about.

        asked_by : str
            The grower asking.

        urgent : typing.Optional[bool]
            Whether a keeper should answer today.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket
            The filed question's ticket.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.questions.file_question(
                bench="bench",
                question_bench="bench",
                asked_by="asked_by",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_question(
            bench=bench,
            question_bench=question_bench,
            asked_by=asked_by,
            urgent=urgent,
            request_options=request_options,
        )
        return _response.data
