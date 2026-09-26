

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sibling_discount import SiblingDiscount
from .raw_client import AsyncRawSiblingDiscountsClient, RawSiblingDiscountsClient
from .types.get_sibling_discounts_v3request_active_sibling_filter import GetSiblingDiscountsV3RequestActiveSiblingFilter
from .types.get_sibling_discounts_v3request_sibling_filter import GetSiblingDiscountsV3RequestSiblingFilter
from .types.get_sibling_discounts_v3request_sort_by import GetSiblingDiscountsV3RequestSortBy
from .types.get_sibling_discounts_v3request_status import GetSiblingDiscountsV3RequestStatus


class SiblingDiscountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSiblingDiscountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSiblingDiscountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSiblingDiscountsClient
        """
        return self._raw_client

    def get_sibling_discounts_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        status: typing.Optional[GetSiblingDiscountsV3RequestStatus] = None,
        sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter] = None,
        active_sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetSiblingDiscountsV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SiblingDiscount]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Students from families with siblings and resolved billing-plan discounts.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        status : typing.Optional[GetSiblingDiscountsV3RequestStatus]
            Optional status filter, case-insensitive.

        sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter]
            Optional sibling-family filter, case-insensitive.

        active_sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter]
            Require all siblings to be active, case-insensitive.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetSiblingDiscountsV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SiblingDiscount]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sibling_discounts.get_sibling_discounts_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_sibling_discounts_v3(
            company_id=company_id,
            school_id=school_id,
            status=status,
            sibling_filter=sibling_filter,
            active_sibling_filter=active_sibling_filter,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    def get_sibling_discounts_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SiblingDiscount:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiblingDiscount
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sibling_discounts.get_sibling_discounts_student_id_v3(
            student_id="student_id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_sibling_discounts_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data


class AsyncSiblingDiscountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSiblingDiscountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSiblingDiscountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSiblingDiscountsClient
        """
        return self._raw_client

    async def get_sibling_discounts_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        status: typing.Optional[GetSiblingDiscountsV3RequestStatus] = None,
        sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter] = None,
        active_sibling_filter: typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter] = None,
        has_alerts: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetSiblingDiscountsV3RequestSortBy] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SiblingDiscount]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Students from families with siblings and resolved billing-plan discounts.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        status : typing.Optional[GetSiblingDiscountsV3RequestStatus]
            Optional status filter, case-insensitive.

        sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter]
            Optional sibling-family filter, case-insensitive.

        active_sibling_filter : typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter]
            Require all siblings to be active, case-insensitive.

        has_alerts : typing.Optional[bool]
            Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetSiblingDiscountsV3RequestSortBy]
            Sort by a supported column with an _asc or _desc suffix.

        page : typing.Optional[int]
            One-based page number.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SiblingDiscount]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sibling_discounts.get_sibling_discounts_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sibling_discounts_v3(
            company_id=company_id,
            school_id=school_id,
            status=status,
            sibling_filter=sibling_filter,
            active_sibling_filter=active_sibling_filter,
            has_alerts=has_alerts,
            sort_by=sort_by,
            page=page,
            per_page=per_page,
            request_options=request_options,
        )
        return _response.data

    async def get_sibling_discounts_student_id_v3(
        self, student_id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SiblingDiscount:
        """
        The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.

        Parameters
        ----------
        student_id : str
            UUID identifying this student.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiblingDiscount
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sibling_discounts.get_sibling_discounts_student_id_v3(
                student_id="student_id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sibling_discounts_student_id_v3(
            student_id, company_id=company_id, request_options=request_options
        )
        return _response.data
