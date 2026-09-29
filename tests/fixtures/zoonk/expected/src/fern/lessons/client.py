

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chapter_lesson_list_response import ChapterLessonListResponse
from ..types.lesson_content_response import LessonContentResponse
from ..types.lesson_preload_response import LessonPreloadResponse
from ..types.lesson_question import LessonQuestion
from ..types.lesson_question_context_input import LessonQuestionContextInput
from ..types.lesson_question_thread import LessonQuestionThread
from ..types.lesson_resource import LessonResource
from ..types.lesson_successor_response import LessonSuccessorResponse
from .raw_client import AsyncRawLessonsClient, RawLessonsClient
from .types.get_lesson_question_thread_request_context_kind import GetLessonQuestionThreadRequestContextKind


OMIT = typing.cast(typing.Any, ...)


class LessonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLessonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLessonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLessonsClient
        """
        return self._raw_client

    def list_chapter_lessons(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterLessonListResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterLessonListResponse
            Complete published lesson resources in authored order

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.list_chapter_lessons(
            chapter_id="chapterId",
        )
        """
        _response = self._raw_client.list_chapter_lessons(chapter_id, request_options=request_options)
        return _response.data

    def get_lesson(self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> LessonResource:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonResource
            Published lesson metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.get_lesson(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.get_lesson(lesson_id, request_options=request_options)
        return _response.data

    def get_lesson_content(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonContentResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonContentResponse
            Playable lesson content or a generation outcome

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.get_lesson_content(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.get_lesson_content(lesson_id, request_options=request_options)
        return _response.data

    def get_lesson_successor(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonSuccessorResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonSuccessorResponse
            The next published lesson in course order

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.get_lesson_successor(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.get_lesson_successor(lesson_id, request_options=request_options)
        return _response.data

    def create_lesson_preload(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonPreloadResponse:
        """
        Derives a small generation lookahead from the current lesson. Clients cannot select workflow target IDs.

        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonPreloadResponse
            Derived generation workflows accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.create_lesson_preload(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.create_lesson_preload(lesson_id, request_options=request_options)
        return _response.data

    def get_lesson_question_thread(
        self,
        lesson_id: str,
        *,
        context_kind: typing.Optional[GetLessonQuestionThreadRequestContextKind] = None,
        cursor: typing.Optional[str] = None,
        step_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[LessonQuestionThread]:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        context_kind : typing.Optional[GetLessonQuestionThreadRequestContextKind]
            Filter by context kind; use lesson for the completion conversation

        cursor : typing.Optional[str]
            Opaque cursor returned in nextCursor

        step_id : typing.Optional[str]
            Return questions and answer explanations for this step only; pagination uses the same filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[LessonQuestionThread]
            Up to 50 lesson questions ordered chronologically within the page; omitting the cursor returns the newest page, or null before the first question

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.get_lesson_question_thread(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.get_lesson_question_thread(
            lesson_id, context_kind=context_kind, cursor=cursor, step_id=step_id, request_options=request_options
        )
        return _response.data

    def create_lesson_question(
        self,
        lesson_id: str,
        *,
        context: LessonQuestionContextInput,
        question: str,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonQuestion:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        context : LessonQuestionContextInput

        question : str

        request_id : str
            Client-generated idempotency key reused for exact request retries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonQuestion
            Durable pending lesson question

        Examples
        --------
        from fern import FernApi, LessonQuestionContextInput_Lesson

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.create_lesson_question(
            lesson_id="lessonId",
            context=LessonQuestionContextInput_Lesson(),
            question="question",
            request_id="requestId",
        )
        """
        _response = self._raw_client.create_lesson_question(
            lesson_id, context=context, question=question, request_id=request_id, request_options=request_options
        )
        return _response.data

    def get_lesson_question(
        self, question_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonQuestion:
        """
        Parameters
        ----------
        question_id : str
            Lesson question ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonQuestion
            Current learner-owned lesson question

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lessons.get_lesson_question(
            question_id="questionId",
        )
        """
        _response = self._raw_client.get_lesson_question(question_id, request_options=request_options)
        return _response.data

    def create_lesson_question_answer(
        self, question_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[str]:
        """
        Claims a pending or failed question and returns one grounded answer as an AI SDK UI message stream.

        Parameters
        ----------
        question_id : str
            Lesson question ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Lesson question answer streamed as AI SDK UI message events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.lessons.create_lesson_question_answer(
            question_id="questionId",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.create_lesson_question_answer(question_id, request_options=request_options) as r:
            yield from r.data


class AsyncLessonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLessonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLessonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLessonsClient
        """
        return self._raw_client

    async def list_chapter_lessons(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterLessonListResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterLessonListResponse
            Complete published lesson resources in authored order

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.list_chapter_lessons(
                chapter_id="chapterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chapter_lessons(chapter_id, request_options=request_options)
        return _response.data

    async def get_lesson(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonResource:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonResource
            Published lesson metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.get_lesson(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lesson(lesson_id, request_options=request_options)
        return _response.data

    async def get_lesson_content(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonContentResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonContentResponse
            Playable lesson content or a generation outcome

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.get_lesson_content(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lesson_content(lesson_id, request_options=request_options)
        return _response.data

    async def get_lesson_successor(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonSuccessorResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonSuccessorResponse
            The next published lesson in course order

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.get_lesson_successor(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lesson_successor(lesson_id, request_options=request_options)
        return _response.data

    async def create_lesson_preload(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonPreloadResponse:
        """
        Derives a small generation lookahead from the current lesson. Clients cannot select workflow target IDs.

        Parameters
        ----------
        lesson_id : str
            Lesson ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonPreloadResponse
            Derived generation workflows accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.create_lesson_preload(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lesson_preload(lesson_id, request_options=request_options)
        return _response.data

    async def get_lesson_question_thread(
        self,
        lesson_id: str,
        *,
        context_kind: typing.Optional[GetLessonQuestionThreadRequestContextKind] = None,
        cursor: typing.Optional[str] = None,
        step_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[LessonQuestionThread]:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        context_kind : typing.Optional[GetLessonQuestionThreadRequestContextKind]
            Filter by context kind; use lesson for the completion conversation

        cursor : typing.Optional[str]
            Opaque cursor returned in nextCursor

        step_id : typing.Optional[str]
            Return questions and answer explanations for this step only; pagination uses the same filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[LessonQuestionThread]
            Up to 50 lesson questions ordered chronologically within the page; omitting the cursor returns the newest page, or null before the first question

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.get_lesson_question_thread(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lesson_question_thread(
            lesson_id, context_kind=context_kind, cursor=cursor, step_id=step_id, request_options=request_options
        )
        return _response.data

    async def create_lesson_question(
        self,
        lesson_id: str,
        *,
        context: LessonQuestionContextInput,
        question: str,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonQuestion:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        context : LessonQuestionContextInput

        question : str

        request_id : str
            Client-generated idempotency key reused for exact request retries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonQuestion
            Durable pending lesson question

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LessonQuestionContextInput_Lesson

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.create_lesson_question(
                lesson_id="lessonId",
                context=LessonQuestionContextInput_Lesson(),
                question="question",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lesson_question(
            lesson_id, context=context, question=question, request_id=request_id, request_options=request_options
        )
        return _response.data

    async def get_lesson_question(
        self, question_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonQuestion:
        """
        Parameters
        ----------
        question_id : str
            Lesson question ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonQuestion
            Current learner-owned lesson question

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lessons.get_lesson_question(
                question_id="questionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lesson_question(question_id, request_options=request_options)
        return _response.data

    async def create_lesson_question_answer(
        self, question_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Claims a pending or failed question and returns one grounded answer as an AI SDK UI message stream.

        Parameters
        ----------
        question_id : str
            Lesson question ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Lesson question answer streamed as AI SDK UI message events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.lessons.create_lesson_question_answer(
                question_id="questionId",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.create_lesson_question_answer(question_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
