

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.update_student_request import UpdateStudentRequest
from ..types.update_student_response import UpdateStudentResponse
from .raw_client import AsyncRawStudentsClient, RawStudentsClient
from .types.get_students_id_v3request_fields_item import GetStudentsIdV3RequestFieldsItem
from .types.get_students_id_v3response import GetStudentsIdV3Response
from .types.get_students_v3request_fields_item import GetStudentsV3RequestFieldsItem
from .types.get_students_v3response import GetStudentsV3Response


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

    def get_students_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]
        ] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStudentsV3Response:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns paginated students. The normal collection includes only Procare Desktop enrollment statuses configured as visible for the school. status defaults to active plus hold; all includes active, hold, inactive and graduate. Unknown status values also fall back to active plus hold.

        ids switches to a batch lookup of at most 200 UUIDs and requires school_id; this branch bypasses the normal status selection. Missing IDs are omitted. fields selects JSON properties, case-insensitively, and duplicate field names are removed.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional batch of at most 200 student UUIDs; requires school_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        status : typing.Optional[str]
            Normal collection: active, hold, inactive, graduate or all. Omitted/unrecognized values select active plus hold.

        fields : typing.Optional[typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Names are normalized to lowercase. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStudentsV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.students.get_students_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_students_v3(
            company_id=company_id,
            school_id=school_id,
            ids=ids,
            status=status,
            fields=fields,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStudentsIdV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. Returns the full student or the requested field projection. This item read does not apply the collection's session-school assignment check.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStudentsIdV3Response
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.students.get_students_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_students_id_v3(
            id, company_id=company_id, school_id=school_id, fields=fields, request_options=request_options
        )
        return _response.data

    def patch_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateStudentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStudentResponse:
        """
        Requires school_id assigned to the session and an authenticated user belonging to company_id. Attribution comes from that user; updated_by_email is accepted but ignored. At least one update property is required. Unknown properties return 400. Dates and room UUIDs may be cleared with null or an empty string; omission leaves them unchanged.

        Validation uses the resulting student state, including existing values:
        - transition_date_2 requires transition_date.
        - transition_room_override_id requires transition_date.
        - transition_room_2_id requires transition_date_2.
        - Effective start date must precede transition_date; transition_date must precede transition_date_2 when present; both transitions must precede the effective withdrawal date.
        - Specified room IDs must be active rooms in the student's school.

        Returns an update summary containing student_data, not the full GET representation. Unlike the shared write decoder, this handler does not enforce Content-Type. A post-update retrieval failure can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateStudentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStudentResponse
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.students.patch_students_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
            request={"transition_date": "2030-09-01"},
        )
        """
        _response = self._raw_client.patch_students_id_v3(
            id, company_id=company_id, school_id=school_id, request=request, request_options=request_options
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

    async def get_students_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]
        ] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStudentsV3Response:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns paginated students. The normal collection includes only Procare Desktop enrollment statuses configured as visible for the school. status defaults to active plus hold; all includes active, hold, inactive and graduate. Unknown status values also fall back to active plus hold.

        ids switches to a batch lookup of at most 200 UUIDs and requires school_id; this branch bypasses the normal status selection. Missing IDs are omitted. fields selects JSON properties, case-insensitively, and duplicate field names are removed.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional batch of at most 200 student UUIDs; requires school_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        status : typing.Optional[str]
            Normal collection: active, hold, inactive, graduate or all. Omitted/unrecognized values select active plus hold.

        fields : typing.Optional[typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Names are normalized to lowercase. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStudentsV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.students.get_students_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_students_v3(
            company_id=company_id,
            school_id=school_id,
            ids=ids,
            status=status,
            fields=fields,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        fields: typing.Optional[
            typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStudentsIdV3Response:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. Returns the full student or the requested field projection. This item read does not apply the collection's session-school assignment check.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        fields : typing.Optional[typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStudentsIdV3Response
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.students.get_students_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_students_id_v3(
            id, company_id=company_id, school_id=school_id, fields=fields, request_options=request_options
        )
        return _response.data

    async def patch_students_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: str,
        request: UpdateStudentRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStudentResponse:
        """
        Requires school_id assigned to the session and an authenticated user belonging to company_id. Attribution comes from that user; updated_by_email is accepted but ignored. At least one update property is required. Unknown properties return 400. Dates and room UUIDs may be cleared with null or an empty string; omission leaves them unchanged.

        Validation uses the resulting student state, including existing values:
        - transition_date_2 requires transition_date.
        - transition_room_override_id requires transition_date.
        - transition_room_2_id requires transition_date_2.
        - Effective start date must precede transition_date; transition_date must precede transition_date_2 when present; both transitions must precede the effective withdrawal date.
        - Specified room IDs must be active rooms in the student's school.

        Returns an update summary containing student_data, not the full GET representation. Unlike the shared write decoder, this handler does not enforce Content-Type. A post-update retrieval failure can return 404 or 500 after the write has executed.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        request : UpdateStudentRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStudentResponse
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.students.patch_students_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
                request={"transition_date": "2030-09-01"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_students_id_v3(
            id, company_id=company_id, school_id=school_id, request=request, request_options=request_options
        )
        return _response.data
