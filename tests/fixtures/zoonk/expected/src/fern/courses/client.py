

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.catalog_search_response import CatalogSearchResponse
from ..types.course_edition_response import CourseEditionResponse
from ..types.course_resource import CourseResource
from ..types.current_user_course_list_response import CurrentUserCourseListResponse
from ..types.language_course_list_response import LanguageCourseListResponse
from .raw_client import AsyncRawCoursesClient, RawCoursesClient
from .types.course_edition_request_language import CourseEditionRequestLanguage
from .types.get_course_edition_request_language import GetCourseEditionRequestLanguage
from .types.list_courses_request_category import ListCoursesRequestCategory
from .types.list_courses_response import ListCoursesResponse


OMIT = typing.cast(typing.Any, ...)


class CoursesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoursesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoursesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoursesClient
        """
        return self._raw_client

    def list_courses(
        self,
        *,
        language: str,
        category: typing.Optional[ListCoursesRequestCategory] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCoursesResponse:
        """
        Parameters
        ----------
        language : str
            Course language code

        category : typing.Optional[ListCoursesRequestCategory]
            Course category filter

        cursor : typing.Optional[str]
            Pagination cursor

        limit : typing.Optional[int]
            Results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCoursesResponse
            Paginated course results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.list_courses(
            language="en",
        )
        """
        _response = self._raw_client.list_courses(
            language=language, category=category, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def search_catalog(
        self, *, language: str, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CatalogSearchResponse:
        """
        Parameters
        ----------
        language : str
            Catalog language code

        query : str
            Search query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CatalogSearchResponse
            Bounded matching course and chapter resources

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.search_catalog(
            language="en",
            query="query",
        )
        """
        _response = self._raw_client.search_catalog(language=language, query=query, request_options=request_options)
        return _response.data

    def get_course(self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CourseResource:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseResource
            Published course metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.get_course(
            course_id="courseId",
        )
        """
        _response = self._raw_client.get_course(course_id, request_options=request_options)
        return _response.data

    def list_language_courses(
        self, *, language: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LanguageCourseListResponse:
        """
        Parameters
        ----------
        language : str
            Learner language code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageCourseListResponse
            Completed language courses

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.list_language_courses(
            language="en",
        )
        """
        _response = self._raw_client.list_language_courses(language=language, request_options=request_options)
        return _response.data

    def get_course_edition(
        self,
        course_id: str,
        *,
        language: GetCourseEditionRequestLanguage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourseEditionResponse:
        """
        Finds a course edition in the requested instructional language. Proven existing editions may be linked on demand; reading never runs identity models or creates generation requests.

        Parameters
        ----------
        course_id : str
            Course ID

        language : GetCourseEditionRequestLanguage
            Requested instructional language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseEditionResponse
            Available edition, existing generation, missing edition, or unsupported request

        Examples
        --------
        from fern.courses import GetCourseEditionRequestLanguage

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.get_course_edition(
            course_id="courseId",
            language=GetCourseEditionRequestLanguage.EN,
        )
        """
        _response = self._raw_client.get_course_edition(course_id, language=language, request_options=request_options)
        return _response.data

    def resolve_course_edition(
        self,
        course_id: str,
        *,
        language: CourseEditionRequestLanguage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourseEditionResponse:
        """
        Reuses an existing edition publicly. If none exists, authentication is required to resolve the source title through normal course identity search and prepare generation. A generation result identifies the course prompt to submit to POST /generations.

        Parameters
        ----------
        course_id : str
            Course ID

        language : CourseEditionRequestLanguage
            Requested instructional language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseEditionResponse
            Available edition, existing generation, missing edition, or unsupported request

        Examples
        --------
        from fern.courses import CourseEditionRequestLanguage

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.resolve_course_edition(
            course_id="courseId",
            language=CourseEditionRequestLanguage.EN,
        )
        """
        _response = self._raw_client.resolve_course_edition(
            course_id, language=language, request_options=request_options
        )
        return _response.data

    def list_current_user_courses(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrentUserCourseListResponse:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor

        limit : typing.Optional[int]
            Results per page

        query : typing.Optional[str]
            Filter enrolled courses by title or description, ignoring case

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserCourseListResponse
            Paginated learner course library

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.courses.list_current_user_courses()
        """
        _response = self._raw_client.list_current_user_courses(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def remove_current_user_course(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        course_id : str
            Course ID

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
        client.courses.remove_current_user_course(
            course_id="courseId",
        )
        """
        _response = self._raw_client.remove_current_user_course(course_id, request_options=request_options)
        return _response.data


class AsyncCoursesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoursesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoursesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoursesClient
        """
        return self._raw_client

    async def list_courses(
        self,
        *,
        language: str,
        category: typing.Optional[ListCoursesRequestCategory] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCoursesResponse:
        """
        Parameters
        ----------
        language : str
            Course language code

        category : typing.Optional[ListCoursesRequestCategory]
            Course category filter

        cursor : typing.Optional[str]
            Pagination cursor

        limit : typing.Optional[int]
            Results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCoursesResponse
            Paginated course results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.list_courses(
                language="en",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_courses(
            language=language, category=category, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def search_catalog(
        self, *, language: str, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CatalogSearchResponse:
        """
        Parameters
        ----------
        language : str
            Catalog language code

        query : str
            Search query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CatalogSearchResponse
            Bounded matching course and chapter resources

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.search_catalog(
                language="en",
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_catalog(
            language=language, query=query, request_options=request_options
        )
        return _response.data

    async def get_course(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourseResource:
        """
        Parameters
        ----------
        course_id : str
            Course ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseResource
            Published course metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.get_course(
                course_id="courseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_course(course_id, request_options=request_options)
        return _response.data

    async def list_language_courses(
        self, *, language: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LanguageCourseListResponse:
        """
        Parameters
        ----------
        language : str
            Learner language code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageCourseListResponse
            Completed language courses

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.list_language_courses(
                language="en",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_language_courses(language=language, request_options=request_options)
        return _response.data

    async def get_course_edition(
        self,
        course_id: str,
        *,
        language: GetCourseEditionRequestLanguage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourseEditionResponse:
        """
        Finds a course edition in the requested instructional language. Proven existing editions may be linked on demand; reading never runs identity models or creates generation requests.

        Parameters
        ----------
        course_id : str
            Course ID

        language : GetCourseEditionRequestLanguage
            Requested instructional language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseEditionResponse
            Available edition, existing generation, missing edition, or unsupported request

        Examples
        --------
        import asyncio

        from fern.courses import GetCourseEditionRequestLanguage

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.get_course_edition(
                course_id="courseId",
                language=GetCourseEditionRequestLanguage.EN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_course_edition(
            course_id, language=language, request_options=request_options
        )
        return _response.data

    async def resolve_course_edition(
        self,
        course_id: str,
        *,
        language: CourseEditionRequestLanguage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourseEditionResponse:
        """
        Reuses an existing edition publicly. If none exists, authentication is required to resolve the source title through normal course identity search and prepare generation. A generation result identifies the course prompt to submit to POST /generations.

        Parameters
        ----------
        course_id : str
            Course ID

        language : CourseEditionRequestLanguage
            Requested instructional language

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CourseEditionResponse
            Available edition, existing generation, missing edition, or unsupported request

        Examples
        --------
        import asyncio

        from fern.courses import CourseEditionRequestLanguage

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.resolve_course_edition(
                course_id="courseId",
                language=CourseEditionRequestLanguage.EN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_course_edition(
            course_id, language=language, request_options=request_options
        )
        return _response.data

    async def list_current_user_courses(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CurrentUserCourseListResponse:
        """
        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor

        limit : typing.Optional[int]
            Results per page

        query : typing.Optional[str]
            Filter enrolled courses by title or description, ignoring case

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CurrentUserCourseListResponse
            Paginated learner course library

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.courses.list_current_user_courses()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_current_user_courses(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def remove_current_user_course(
        self, course_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        course_id : str
            Course ID

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
            await client.courses.remove_current_user_course(
                course_id="courseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_current_user_course(course_id, request_options=request_options)
        return _response.data
