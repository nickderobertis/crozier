

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chapter_completion_response import ChapterCompletionResponse
from ..types.course_completion_response import CourseCompletionResponse
from ..types.course_continuation_list_response import CourseContinuationListResponse
from ..types.current_user_activity_response import CurrentUserActivityResponse
from ..types.current_user_energy_response import CurrentUserEnergyResponse
from ..types.current_user_level_response import CurrentUserLevelResponse
from ..types.current_user_progress_response import CurrentUserProgressResponse
from ..types.current_user_progress_snapshot_response import CurrentUserProgressSnapshotResponse
from ..types.current_user_score_patterns_response import CurrentUserScorePatternsResponse
from ..types.current_user_score_response import CurrentUserScoreResponse
from ..types.lesson_completion_response import LessonCompletionResponse
from ..types.lesson_visibility_hidden_lesson_kinds_item import LessonVisibilityHiddenLessonKindsItem
from ..types.lesson_visibility_output import LessonVisibilityOutput
from ..types.next_lesson_response import NextLessonResponse
from .raw_client import AsyncRawProgressClient, RawProgressClient
from .types.lesson_completion_request_answers_value import LessonCompletionRequestAnswersValue
from .types.lesson_completion_request_step_timings_value import LessonCompletionRequestStepTimingsValue


OMIT = typing.cast(typing.Any, ...)


class ProgressClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProgressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProgressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProgressClient
        """
        return self._raw_client

    def list_current_user_course_continuations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseContinuationListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseContinuationListResponse
            Current continuation targets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.list_current_user_course_continuations()
        """
        _response = self._raw_client.list_current_user_course_continuations(request_options=request_options)
        return _response.data

    def get_current_user_lesson_visibility(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonVisibilityOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonVisibilityOutput
            Current lesson visibility preferences

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_lesson_visibility()
        """
        _response = self._raw_client.get_current_user_lesson_visibility(request_options=request_options)
        return _response.data

    def update_current_user_lesson_visibility(
        self,
        *,
        hidden_lesson_kinds: typing.Sequence[LessonVisibilityHiddenLessonKindsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonVisibilityOutput:
        """
        Parameters
        ----------
        hidden_lesson_kinds : typing.Sequence[LessonVisibilityHiddenLessonKindsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonVisibilityOutput
            Updated lesson visibility preferences

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.update_current_user_lesson_visibility(
            hidden_lesson_kinds=["alphabet"],
        )
        """
        _response = self._raw_client.update_current_user_lesson_visibility(
            hidden_lesson_kinds=hidden_lesson_kinds, request_options=request_options
        )
        return _response.data

    def create_lesson_completion(
        self,
        lesson_id: str,
        *,
        answers: typing.Dict[str, LessonCompletionRequestAnswersValue],
        started_at: float,
        step_timings: typing.Dict[str, LessonCompletionRequestStepTimingsValue],
        time_zone: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonCompletionResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        answers : typing.Dict[str, LessonCompletionRequestAnswersValue]

        started_at : float

        step_timings : typing.Dict[str, LessonCompletionRequestStepTimingsValue]

        time_zone : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonCompletionResponse
            Authoritative completion rewards and progress

        Examples
        --------
        from fern.progress import (
            LessonCompletionRequestAnswersValue_FillBlank,
            LessonCompletionRequestStepTimingsValue,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.create_lesson_completion(
            lesson_id="lessonId",
            answers={
                "key": LessonCompletionRequestAnswersValue_FillBlank(
                    user_answers=["userAnswers"],
                )
            },
            started_at=1.1,
            step_timings={
                "key": LessonCompletionRequestStepTimingsValue(
                    answered_at=1.1,
                    day_of_week=1,
                    duration_seconds=1.1,
                    hour_of_day=1,
                )
            },
            time_zone="timeZone",
        )
        """
        _response = self._raw_client.create_lesson_completion(
            lesson_id,
            answers=answers,
            started_at=started_at,
            step_timings=step_timings,
            time_zone=time_zone,
            request_options=request_options,
        )
        return _response.data

    def create_lesson_start(self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

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
        client.progress.create_lesson_start(
            lesson_id="lessonId",
        )
        """
        _response = self._raw_client.create_lesson_start(lesson_id, request_options=request_options)
        return _response.data

    def get_current_user_progress(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserProgressResponse:
        """
        Compact progress totals for Home and overview surfaces. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserProgressResponse
            Current learner progress summary

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_progress()
        """
        _response = self._raw_client.get_current_user_progress(request_options=request_options)
        return _response.data

    def get_current_user_activity(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserActivityResponse:
        """
        Lifetime activity totals and a bounded 53-week completion calendar. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserActivityResponse
            Current learner activity

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_activity()
        """
        _response = self._raw_client.get_current_user_activity(request_options=request_options)
        return _response.data

    def get_current_user_energy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserEnergyResponse:
        """
        Current Energy, a bounded 53-week timeline, and lifetime insights. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserEnergyResponse
            Current learner Energy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_energy()
        """
        _response = self._raw_client.get_current_user_energy(request_options=request_options)
        return _response.data

    def get_current_user_level(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserLevelResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserLevelResponse
            Current learner belt and level

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_level()
        """
        _response = self._raw_client.get_current_user_level(request_options=request_options)
        return _response.data

    def get_current_user_score(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserScoreResponse:
        """
        Weighted Score and bounded 90-day weekly history. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserScoreResponse
            Current learner Score

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_score()
        """
        _response = self._raw_client.get_current_user_score(request_options=request_options)
        return _response.data

    def get_current_user_score_patterns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserScorePatternsResponse:
        """
        Complete weekday and daypart breakdowns for the bounded 90-day Score window. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserScorePatternsResponse
            Current learner Score patterns

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_score_patterns()
        """
        _response = self._raw_client.get_current_user_score_patterns(request_options=request_options)
        return _response.data

    def get_current_user_progress_snapshot(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserProgressSnapshotResponse:
        """
        Pre-completion milestone facts used by interactive lesson players. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserProgressSnapshotResponse
            Current learner player progress snapshot

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_current_user_progress_snapshot()
        """
        _response = self._raw_client.get_current_user_progress_snapshot(request_options=request_options)
        return _response.data

    def get_chapter_next_lesson(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NextLessonResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NextLessonResponse
            Next lesson to complete

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_chapter_next_lesson(
            chapter_id="chapterId",
        )
        """
        _response = self._raw_client.get_chapter_next_lesson(chapter_id, request_options=request_options)
        return _response.data

    def get_chapter_progress(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterCompletionResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterCompletionResponse
            Lesson completion status for a chapter

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_chapter_progress(
            chapter_id="chapterId",
        )
        """
        _response = self._raw_client.get_chapter_progress(chapter_id, request_options=request_options)
        return _response.data

    def get_course_next_lesson(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NextLessonResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NextLessonResponse
            Next lesson to complete

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_course_next_lesson(
            course_id="courseId",
        )
        """
        _response = self._raw_client.get_course_next_lesson(course_id, request_options=request_options)
        return _response.data

    def get_course_progress(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseCompletionResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseCompletionResponse
            Chapter completion status for a course

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.progress.get_course_progress(
            course_id="courseId",
        )
        """
        _response = self._raw_client.get_course_progress(course_id, request_options=request_options)
        return _response.data


class AsyncProgressClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProgressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProgressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProgressClient
        """
        return self._raw_client

    async def list_current_user_course_continuations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseContinuationListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseContinuationListResponse
            Current continuation targets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.list_current_user_course_continuations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_current_user_course_continuations(request_options=request_options)
        return _response.data

    async def get_current_user_lesson_visibility(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LessonVisibilityOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonVisibilityOutput
            Current lesson visibility preferences

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_lesson_visibility()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_lesson_visibility(request_options=request_options)
        return _response.data

    async def update_current_user_lesson_visibility(
        self,
        *,
        hidden_lesson_kinds: typing.Sequence[LessonVisibilityHiddenLessonKindsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonVisibilityOutput:
        """
        Parameters
        ----------
        hidden_lesson_kinds : typing.Sequence[LessonVisibilityHiddenLessonKindsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonVisibilityOutput
            Updated lesson visibility preferences

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.update_current_user_lesson_visibility(
                hidden_lesson_kinds=["alphabet"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_current_user_lesson_visibility(
            hidden_lesson_kinds=hidden_lesson_kinds, request_options=request_options
        )
        return _response.data

    async def create_lesson_completion(
        self,
        lesson_id: str,
        *,
        answers: typing.Dict[str, LessonCompletionRequestAnswersValue],
        started_at: float,
        step_timings: typing.Dict[str, LessonCompletionRequestStepTimingsValue],
        time_zone: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LessonCompletionResponse:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

        answers : typing.Dict[str, LessonCompletionRequestAnswersValue]

        started_at : float

        step_timings : typing.Dict[str, LessonCompletionRequestStepTimingsValue]

        time_zone : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LessonCompletionResponse
            Authoritative completion rewards and progress

        Examples
        --------
        import asyncio

        from fern.progress import (
            LessonCompletionRequestAnswersValue_FillBlank,
            LessonCompletionRequestStepTimingsValue,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.create_lesson_completion(
                lesson_id="lessonId",
                answers={
                    "key": LessonCompletionRequestAnswersValue_FillBlank(
                        user_answers=["userAnswers"],
                    )
                },
                started_at=1.1,
                step_timings={
                    "key": LessonCompletionRequestStepTimingsValue(
                        answered_at=1.1,
                        day_of_week=1,
                        duration_seconds=1.1,
                        hour_of_day=1,
                    )
                },
                time_zone="timeZone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lesson_completion(
            lesson_id,
            answers=answers,
            started_at=started_at,
            step_timings=step_timings,
            time_zone=time_zone,
            request_options=request_options,
        )
        return _response.data

    async def create_lesson_start(
        self, lesson_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        lesson_id : str
            Lesson ID

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
            await client.progress.create_lesson_start(
                lesson_id="lessonId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lesson_start(lesson_id, request_options=request_options)
        return _response.data

    async def get_current_user_progress(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserProgressResponse:
        """
        Compact progress totals for Home and overview surfaces. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserProgressResponse
            Current learner progress summary

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_progress()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_progress(request_options=request_options)
        return _response.data

    async def get_current_user_activity(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserActivityResponse:
        """
        Lifetime activity totals and a bounded 53-week completion calendar. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserActivityResponse
            Current learner activity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_activity()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_activity(request_options=request_options)
        return _response.data

    async def get_current_user_energy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserEnergyResponse:
        """
        Current Energy, a bounded 53-week timeline, and lifetime insights. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserEnergyResponse
            Current learner Energy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_energy()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_energy(request_options=request_options)
        return _response.data

    async def get_current_user_level(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserLevelResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserLevelResponse
            Current learner belt and level

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_level()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_level(request_options=request_options)
        return _response.data

    async def get_current_user_score(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserScoreResponse:
        """
        Weighted Score and bounded 90-day weekly history. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserScoreResponse
            Current learner Score

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_score()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_score(request_options=request_options)
        return _response.data

    async def get_current_user_score_patterns(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserScorePatternsResponse:
        """
        Complete weekday and daypart breakdowns for the bounded 90-day Score window. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserScorePatternsResponse
            Current learner Score patterns

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_score_patterns()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_score_patterns(request_options=request_options)
        return _response.data

    async def get_current_user_progress_snapshot(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CurrentUserProgressSnapshotResponse:
        """
        Pre-completion milestone facts used by interactive lesson players. Calendar boundaries use the validated timezone resolved from the request and fall back to UTC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserProgressSnapshotResponse
            Current learner player progress snapshot

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_current_user_progress_snapshot()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_progress_snapshot(request_options=request_options)
        return _response.data

    async def get_chapter_next_lesson(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NextLessonResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NextLessonResponse
            Next lesson to complete

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_chapter_next_lesson(
                chapter_id="chapterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chapter_next_lesson(chapter_id, request_options=request_options)
        return _response.data

    async def get_chapter_progress(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterCompletionResponse:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterCompletionResponse
            Lesson completion status for a chapter

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_chapter_progress(
                chapter_id="chapterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chapter_progress(chapter_id, request_options=request_options)
        return _response.data

    async def get_course_next_lesson(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NextLessonResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NextLessonResponse
            Next lesson to complete

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_course_next_lesson(
                course_id="courseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_course_next_lesson(course_id, request_options=request_options)
        return _response.data

    async def get_course_progress(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseCompletionResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseCompletionResponse
            Chapter completion status for a course

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.progress.get_course_progress(
                course_id="courseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_course_progress(course_id, request_options=request_options)
        return _response.data
