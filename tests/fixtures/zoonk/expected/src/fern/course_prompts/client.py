

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.course_prompt_generation_response import CoursePromptGenerationResponse
from ..types.resolve_course_prompt_request import ResolveCoursePromptRequest
from ..types.resolve_course_prompt_response import ResolveCoursePromptResponse
from .raw_client import AsyncRawCoursePromptsClient, RawCoursePromptsClient


OMIT = typing.cast(typing.Any, ...)


class CoursePromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoursePromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoursePromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoursePromptsClient
        """
        return self._raw_client

    def create_course_prompt(
        self, *, request: ResolveCoursePromptRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ResolveCoursePromptResponse:
        """
        Classifies and stores topic prompts publicly, returning existing courses and unsupported outcomes without authentication. Authentication is required before a prompt can create a generation request.

        Parameters
        ----------
        request : ResolveCoursePromptRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolveCoursePromptResponse
            Course, generation, or classification outcome

        Examples
        --------
        from fern import FernApi, ResolveCoursePromptRequest_Topic

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.course_prompts.create_course_prompt(
            request=ResolveCoursePromptRequest_Topic(
                language="language",
                prompt="prompt",
            ),
        )
        """
        _response = self._raw_client.create_course_prompt(request=request, request_options=request_options)
        return _response.data

    def get_course_prompt(
        self, course_prompt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoursePromptGenerationResponse:
        """
        Parameters
        ----------
        course_prompt_id : str
            Course prompt ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoursePromptGenerationResponse
            Course prompt generation state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.course_prompts.get_course_prompt(
            course_prompt_id="coursePromptId",
        )
        """
        _response = self._raw_client.get_course_prompt(course_prompt_id, request_options=request_options)
        return _response.data


class AsyncCoursePromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoursePromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoursePromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoursePromptsClient
        """
        return self._raw_client

    async def create_course_prompt(
        self, *, request: ResolveCoursePromptRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> ResolveCoursePromptResponse:
        """
        Classifies and stores topic prompts publicly, returning existing courses and unsupported outcomes without authentication. Authentication is required before a prompt can create a generation request.

        Parameters
        ----------
        request : ResolveCoursePromptRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolveCoursePromptResponse
            Course, generation, or classification outcome

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ResolveCoursePromptRequest_Topic

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.course_prompts.create_course_prompt(
                request=ResolveCoursePromptRequest_Topic(
                    language="language",
                    prompt="prompt",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_course_prompt(request=request, request_options=request_options)
        return _response.data

    async def get_course_prompt(
        self, course_prompt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoursePromptGenerationResponse:
        """
        Parameters
        ----------
        course_prompt_id : str
            Course prompt ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoursePromptGenerationResponse
            Course prompt generation state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.course_prompts.get_course_prompt(
                course_prompt_id="coursePromptId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_course_prompt(course_prompt_id, request_options=request_options)
        return _response.data
