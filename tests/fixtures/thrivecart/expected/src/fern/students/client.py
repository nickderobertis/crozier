

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStudentsClient, RawStudentsClient
from .types.create_student_response import CreateStudentResponse


OMIT = typing.cast(typing.Any, ...)


class StudentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStudentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStudentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStudentsClient
        """
        return self._raw_client

    def create_student(
        self,
        *,
        email: str,
        name: typing.Optional[str] = OMIT,
        course_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateStudentResponse:
        """
        Create or enroll a student in ThriveCart Learn courses.

        Parameters
        ----------
        email : str

        name : typing.Optional[str]

        course_id : typing.Optional[int]
            Course ID to enroll the student in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateStudentResponse
            Student enrollment result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.students.create_student(
            email="email",
        )
        """
        _response = self._raw_client.create_student(
            email=email, name=name, course_id=course_id, request_options=request_options
        )
        return _response.data


class AsyncStudentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStudentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStudentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStudentsClient
        """
        return self._raw_client

    async def create_student(
        self,
        *,
        email: str,
        name: typing.Optional[str] = OMIT,
        course_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateStudentResponse:
        """
        Create or enroll a student in ThriveCart Learn courses.

        Parameters
        ----------
        email : str

        name : typing.Optional[str]

        course_id : typing.Optional[int]
            Course ID to enroll the student in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateStudentResponse
            Student enrollment result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.students.create_student(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_student(
            email=email, name=name, course_id=course_id, request_options=request_options
        )
        return _response.data
