

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chapter_resource import ChapterResource
from ..types.course_chapter_list_response import CourseChapterListResponse
from .raw_client import AsyncRawChaptersClient, RawChaptersClient


class ChaptersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChaptersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChaptersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChaptersClient
        """
        return self._raw_client

    def get_chapter(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterResource:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterResource
            Published chapter metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chapters.get_chapter(
            chapter_id="chapterId",
        )
        """
        _response = self._raw_client.get_chapter(chapter_id, request_options=request_options)
        return _response.data

    def list_course_chapters(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseChapterListResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseChapterListResponse
            Complete published chapter resources in authored order

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chapters.list_course_chapters(
            course_id="courseId",
        )
        """
        _response = self._raw_client.list_course_chapters(course_id, request_options=request_options)
        return _response.data


class AsyncChaptersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChaptersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChaptersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChaptersClient
        """
        return self._raw_client

    async def get_chapter(
        self, chapter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChapterResource:
        """
        Parameters
        ----------
        chapter_id : str
            Chapter ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterResource
            Published chapter metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chapters.get_chapter(
                chapter_id="chapterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chapter(chapter_id, request_options=request_options)
        return _response.data

    async def list_course_chapters(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseChapterListResponse:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseChapterListResponse
            Complete published chapter resources in authored order

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chapters.list_course_chapters(
                course_id="courseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_course_chapters(course_id, request_options=request_options)
        return _response.data
