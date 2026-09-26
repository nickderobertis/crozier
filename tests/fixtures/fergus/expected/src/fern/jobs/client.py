

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.add_quote_response import AddQuoteResponse
from ..types.get_quote_by_id_quote_response import GetQuoteByIdQuoteResponse
from ..types.get_quotes_response import GetQuotesResponse
from ..types.job_financial_summary_response import JobFinancialSummaryResponse
from ..types.job_phase_response import JobPhaseResponse
from ..types.job_phases_response import JobPhasesResponse
from ..types.job_response import JobResponse
from ..types.jobs_response import JobsResponse
from ..types.update_quote_response import UpdateQuoteResponse
from .raw_client import AsyncRawJobsClient, RawJobsClient
from .types.get_jobs_job_id_quotes_request_filter_status import GetJobsJobIdQuotesRequestFilterStatus
from .types.get_jobs_job_id_quotes_request_sort_field import GetJobsJobIdQuotesRequestSortField
from .types.get_jobs_job_id_quotes_request_sort_order import GetJobsJobIdQuotesRequestSortOrder
from .types.get_jobs_request_filter_job_status import GetJobsRequestFilterJobStatus
from .types.get_jobs_request_filter_job_type import GetJobsRequestFilterJobType
from .types.get_jobs_request_sort_field import GetJobsRequestSortField
from .types.get_jobs_request_sort_order import GetJobsRequestSortOrder
from .types.post_jobs_job_id_quotes_request_sections_item import PostJobsJobIdQuotesRequestSectionsItem
from .types.post_jobs_request_job_type import PostJobsRequestJobType
from .types.put_jobs_job_id_quotes_quote_id_request_sections_item import PutJobsJobIdQuotesQuoteIdRequestSectionsItem
from .types.put_jobs_job_id_quotes_version_version_number_request_sections_item import (
    PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem,
)
from .types.put_jobs_job_id_request_body import PutJobsJobIdRequestBody


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def get_jobs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_job_no: typing.Optional[str] = None,
        filter_job_status: typing.Optional[GetJobsRequestFilterJobStatus] = None,
        filter_job_type: typing.Optional[GetJobsRequestFilterJobType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        sort_field: typing.Optional[GetJobsRequestSortField] = None,
        filter_show_on_hold: typing.Optional[bool] = None,
        filter_show_archived: typing.Optional[bool] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobsResponse:
        """
        Returns a list of jobs. The list can be filtered by job type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_job_no : typing.Optional[str]

        filter_job_status : typing.Optional[GetJobsRequestFilterJobStatus]

        filter_job_type : typing.Optional[GetJobsRequestFilterJobType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        sort_field : typing.Optional[GetJobsRequestSortField]

        filter_show_on_hold : typing.Optional[bool]

        filter_show_archived : typing.Optional[bool]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `description`
            - `longDescription`
            - `jobNo`
            - `customer.customerFullName`
            - `siteAddress.name`
            - `siteAddress.firstName`
            - `siteAddress.lastName`
            - `mainContact.firstName`
            - `mainContact.lastName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs()
        """
        _response = self._raw_client.get_jobs(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_job_no=filter_job_no,
            filter_job_status=filter_job_status,
            filter_job_type=filter_job_type,
            filter_customer_id=filter_customer_id,
            filter_site_id=filter_site_id,
            sort_field=sort_field,
            filter_show_on_hold=filter_show_on_hold,
            filter_show_archived=filter_show_archived,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def post_jobs(
        self,
        *,
        job_type: PostJobsRequestJobType,
        title: str,
        is_draft: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        customer_reference: typing.Optional[str] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Create a new job

        Parameters
        ----------
        job_type : PostJobsRequestJobType

        title : str

        is_draft : typing.Optional[bool]

        description : typing.Optional[str]

        customer_id : typing.Optional[float]

        customer_reference : typing.Optional[str]

        site_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Resource created successfully

        Examples
        --------
        from fern.jobs import PostJobsRequestJobType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.post_jobs(
            job_type=PostJobsRequestJobType.QUOTE,
            title="title",
        )
        """
        _response = self._raw_client.post_jobs(
            job_type=job_type,
            title=title,
            is_draft=is_draft,
            description=description,
            customer_id=customer_id,
            customer_reference=customer_reference,
            site_id=site_id,
            request_options=request_options,
        )
        return _response.data

    def get_jobs_job_id(self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None) -> JobResponse:
        """
        Returns a job by id

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id(
            job_id=1.1,
        )
        """
        _response = self._raw_client.get_jobs_job_id(job_id, request_options=request_options)
        return _response.data

    def put_jobs_job_id(
        self,
        job_id: float,
        *,
        request: PutJobsJobIdRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Updates a draft job

        Parameters
        ----------
        job_id : float

        request : PutJobsJobIdRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Resource created successfully

        Examples
        --------
        from fern.jobs import PutJobsJobIdRequestBodyTitle

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.put_jobs_job_id(
            job_id=1.1,
            request=PutJobsJobIdRequestBodyTitle(
                title="title",
            ),
        )
        """
        _response = self._raw_client.put_jobs_job_id(job_id, request=request, request_options=request_options)
        return _response.data

    def put_jobs_job_id_finalise(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobResponse:
        """
        Finalise a draft job.

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.put_jobs_job_id_finalise(
            job_id=1.1,
        )
        """
        _response = self._raw_client.put_jobs_job_id_finalise(job_id, request_options=request_options)
        return _response.data

    def get_jobs_job_id_phases(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhasesResponse:
        """
        Returns a list of job phases

        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhasesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_phases(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_jobs_job_id_phases(job_id, request_options=request_options)
        return _response.data

    def post_jobs_job_id_phases(
        self, job_id: str, *, title: str, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhaseResponse:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.post_jobs_job_id_phases(
            job_id="jobId",
            title="title",
            description="description",
        )
        """
        _response = self._raw_client.post_jobs_job_id_phases(
            job_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    def get_jobs_job_id_phases_job_phase_id(
        self, job_id: str, job_phase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhaseResponse:
        """
        Returns a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_phases_job_phase_id(
            job_id="jobId",
            job_phase_id="jobPhaseId",
        )
        """
        _response = self._raw_client.get_jobs_job_id_phases_job_phase_id(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    def put_jobs_job_id_phases_job_phase_id(
        self,
        job_id: str,
        job_phase_id: str,
        *,
        title: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobPhaseResponse:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.put_jobs_job_id_phases_job_phase_id(
            job_id="jobId",
            job_phase_id="jobPhaseId",
            title="title",
            description="description",
        )
        """
        _response = self._raw_client.put_jobs_job_id_phases_job_phase_id(
            job_id, job_phase_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    def post_jobs_job_id_phases_job_phase_id_void(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Void a job phase by JobId and Job PhaseId

        Parameters
        ----------
        job_id : float

        job_phase_id : float

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
        client.jobs.post_jobs_job_id_phases_job_phase_id_void(
            job_id=1.1,
            job_phase_id=1.1,
        )
        """
        _response = self._raw_client.post_jobs_job_id_phases_job_phase_id_void(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    def get_jobs_job_id_financial_summary(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobFinancialSummaryResponse:
        """
        Get a job financial summary

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobFinancialSummaryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_financial_summary(
            job_id=1.1,
        )
        """
        _response = self._raw_client.get_jobs_job_id_financial_summary(job_id, request_options=request_options)
        return _response.data

    def get_jobs_job_id_phases_job_phase_id_financial_summary(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobFinancialSummaryResponse:
        """
        Get a job phase financial summary

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobFinancialSummaryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_phases_job_phase_id_financial_summary(
            job_id=1.1,
            job_phase_id=1.1,
        )
        """
        _response = self._raw_client.get_jobs_job_id_phases_job_phase_id_financial_summary(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    def get_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsJobIdQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        include_combined_item_parents: typing.Optional[bool] = None,
        filter_status: typing.Optional[GetJobsJobIdQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsJobIdQuotesRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQuotesResponse:
        """
        Get all quotes for a job

        Parameters
        ----------
        job_id : str

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsJobIdQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        include_combined_item_parents : typing.Optional[bool]

        filter_status : typing.Optional[GetJobsJobIdQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsJobIdQuotesRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuotesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_quotes(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_jobs_job_id_quotes(
            job_id,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            include_combined_item_parents=include_combined_item_parents,
            filter_status=filter_status,
            sort_field=sort_field,
            request_options=request_options,
        )
        return _response.data

    def post_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        title: str,
        due_days: float,
        sections: typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
        description: typing.Optional[str] = OMIT,
        version_number: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddQuoteResponse:
        """
        Create a new quote

        Parameters
        ----------
        job_id : str

        title : str

        due_days : float

        sections : typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem]

        description : typing.Optional[str]

        version_number : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddQuoteResponse
            Resource created successfully

        Examples
        --------
        from fern.jobs import PostJobsJobIdQuotesRequestSectionsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.post_jobs_job_id_quotes(
            job_id="jobId",
            title="title",
            due_days=1.1,
            sections=[
                PostJobsJobIdQuotesRequestSectionsItem(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.post_jobs_job_id_quotes(
            job_id,
            title=title,
            due_days=due_days,
            sections=sections,
            description=description,
            version_number=version_number,
            request_options=request_options,
        )
        return _response.data

    def get_jobs_job_id_quotes_quote_id(
        self, job_id: float, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQuoteByIdQuoteResponse:
        """
        Get a quote

        Parameters
        ----------
        job_id : float

        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs_job_id_quotes_quote_id(
            job_id=1.1,
            quote_id=1.1,
        )
        """
        _response = self._raw_client.get_jobs_job_id_quotes_quote_id(job_id, quote_id, request_options=request_options)
        return _response.data

    def put_jobs_job_id_quotes_quote_id(
        self,
        job_id: float,
        quote_id: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateQuoteResponse:
        """
        Update a quote by ID

        Parameters
        ----------
        job_id : float

        quote_id : float

        sections : typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateQuoteResponse
            Successful Response

        Examples
        --------
        from fern.jobs import PutJobsJobIdQuotesQuoteIdRequestSectionsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.put_jobs_job_id_quotes_quote_id(
            job_id=1.1,
            quote_id=1.1,
            sections=[
                PutJobsJobIdQuotesQuoteIdRequestSectionsItem(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.put_jobs_job_id_quotes_quote_id(
            job_id, quote_id, sections=sections, title=title, description=description, request_options=request_options
        )
        return _response.data

    def put_jobs_job_id_quotes_version_version_number(
        self,
        job_id: float,
        version_number: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateQuoteResponse:
        """
        Update a quote by version number

        Parameters
        ----------
        job_id : float

        version_number : float

        sections : typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateQuoteResponse
            Successful Response

        Examples
        --------
        from fern.jobs import PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.put_jobs_job_id_quotes_version_version_number(
            job_id=1.1,
            version_number=1.1,
            sections=[
                PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.put_jobs_job_id_quotes_version_version_number(
            job_id,
            version_number,
            sections=sections,
            title=title,
            description=description,
            request_options=request_options,
        )
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def get_jobs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_job_no: typing.Optional[str] = None,
        filter_job_status: typing.Optional[GetJobsRequestFilterJobStatus] = None,
        filter_job_type: typing.Optional[GetJobsRequestFilterJobType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        sort_field: typing.Optional[GetJobsRequestSortField] = None,
        filter_show_on_hold: typing.Optional[bool] = None,
        filter_show_archived: typing.Optional[bool] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobsResponse:
        """
        Returns a list of jobs. The list can be filtered by job type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_job_no : typing.Optional[str]

        filter_job_status : typing.Optional[GetJobsRequestFilterJobStatus]

        filter_job_type : typing.Optional[GetJobsRequestFilterJobType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        sort_field : typing.Optional[GetJobsRequestSortField]

        filter_show_on_hold : typing.Optional[bool]

        filter_show_archived : typing.Optional[bool]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `description`
            - `longDescription`
            - `jobNo`
            - `customer.customerFullName`
            - `siteAddress.name`
            - `siteAddress.firstName`
            - `siteAddress.lastName`
            - `mainContact.firstName`
            - `mainContact.lastName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_job_no=filter_job_no,
            filter_job_status=filter_job_status,
            filter_job_type=filter_job_type,
            filter_customer_id=filter_customer_id,
            filter_site_id=filter_site_id,
            sort_field=sort_field,
            filter_show_on_hold=filter_show_on_hold,
            filter_show_archived=filter_show_archived,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def post_jobs(
        self,
        *,
        job_type: PostJobsRequestJobType,
        title: str,
        is_draft: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        customer_reference: typing.Optional[str] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Create a new job

        Parameters
        ----------
        job_type : PostJobsRequestJobType

        title : str

        is_draft : typing.Optional[bool]

        description : typing.Optional[str]

        customer_id : typing.Optional[float]

        customer_reference : typing.Optional[str]

        site_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern.jobs import PostJobsRequestJobType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.post_jobs(
                job_type=PostJobsRequestJobType.QUOTE,
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs(
            job_type=job_type,
            title=title,
            is_draft=is_draft,
            description=description,
            customer_id=customer_id,
            customer_reference=customer_reference,
            site_id=site_id,
            request_options=request_options,
        )
        return _response.data

    async def get_jobs_job_id(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobResponse:
        """
        Returns a job by id

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id(
                job_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id(job_id, request_options=request_options)
        return _response.data

    async def put_jobs_job_id(
        self,
        job_id: float,
        *,
        request: PutJobsJobIdRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResponse:
        """
        Updates a draft job

        Parameters
        ----------
        job_id : float

        request : PutJobsJobIdRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern.jobs import PutJobsJobIdRequestBodyTitle

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.put_jobs_job_id(
                job_id=1.1,
                request=PutJobsJobIdRequestBodyTitle(
                    title="title",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_jobs_job_id(job_id, request=request, request_options=request_options)
        return _response.data

    async def put_jobs_job_id_finalise(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobResponse:
        """
        Finalise a draft job.

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.put_jobs_job_id_finalise(
                job_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_jobs_job_id_finalise(job_id, request_options=request_options)
        return _response.data

    async def get_jobs_job_id_phases(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhasesResponse:
        """
        Returns a list of job phases

        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhasesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_phases(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_phases(job_id, request_options=request_options)
        return _response.data

    async def post_jobs_job_id_phases(
        self, job_id: str, *, title: str, description: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhaseResponse:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.post_jobs_job_id_phases(
                job_id="jobId",
                title="title",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_job_id_phases(
            job_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    async def get_jobs_job_id_phases_job_phase_id(
        self, job_id: str, job_phase_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobPhaseResponse:
        """
        Returns a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_phases_job_phase_id(
                job_id="jobId",
                job_phase_id="jobPhaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_phases_job_phase_id(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    async def put_jobs_job_id_phases_job_phase_id(
        self,
        job_id: str,
        job_phase_id: str,
        *,
        title: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobPhaseResponse:
        """
        Creates a job phase

        Parameters
        ----------
        job_id : str

        job_phase_id : str

        title : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobPhaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.put_jobs_job_id_phases_job_phase_id(
                job_id="jobId",
                job_phase_id="jobPhaseId",
                title="title",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_jobs_job_id_phases_job_phase_id(
            job_id, job_phase_id, title=title, description=description, request_options=request_options
        )
        return _response.data

    async def post_jobs_job_id_phases_job_phase_id_void(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Void a job phase by JobId and Job PhaseId

        Parameters
        ----------
        job_id : float

        job_phase_id : float

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
            await client.jobs.post_jobs_job_id_phases_job_phase_id_void(
                job_id=1.1,
                job_phase_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_job_id_phases_job_phase_id_void(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    async def get_jobs_job_id_financial_summary(
        self, job_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobFinancialSummaryResponse:
        """
        Get a job financial summary

        Parameters
        ----------
        job_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobFinancialSummaryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_financial_summary(
                job_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_financial_summary(job_id, request_options=request_options)
        return _response.data

    async def get_jobs_job_id_phases_job_phase_id_financial_summary(
        self, job_id: float, job_phase_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobFinancialSummaryResponse:
        """
        Get a job phase financial summary

        Parameters
        ----------
        job_id : float

        job_phase_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobFinancialSummaryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_phases_job_phase_id_financial_summary(
                job_id=1.1,
                job_phase_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_phases_job_phase_id_financial_summary(
            job_id, job_phase_id, request_options=request_options
        )
        return _response.data

    async def get_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetJobsJobIdQuotesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        include_combined_item_parents: typing.Optional[bool] = None,
        filter_status: typing.Optional[GetJobsJobIdQuotesRequestFilterStatus] = None,
        sort_field: typing.Optional[GetJobsJobIdQuotesRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetQuotesResponse:
        """
        Get all quotes for a job

        Parameters
        ----------
        job_id : str

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetJobsJobIdQuotesRequestSortOrder]

        page_cursor : typing.Optional[str]

        include_combined_item_parents : typing.Optional[bool]

        filter_status : typing.Optional[GetJobsJobIdQuotesRequestFilterStatus]

        sort_field : typing.Optional[GetJobsJobIdQuotesRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuotesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_quotes(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_quotes(
            job_id,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            include_combined_item_parents=include_combined_item_parents,
            filter_status=filter_status,
            sort_field=sort_field,
            request_options=request_options,
        )
        return _response.data

    async def post_jobs_job_id_quotes(
        self,
        job_id: str,
        *,
        title: str,
        due_days: float,
        sections: typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem],
        description: typing.Optional[str] = OMIT,
        version_number: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddQuoteResponse:
        """
        Create a new quote

        Parameters
        ----------
        job_id : str

        title : str

        due_days : float

        sections : typing.Sequence[PostJobsJobIdQuotesRequestSectionsItem]

        description : typing.Optional[str]

        version_number : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddQuoteResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern.jobs import PostJobsJobIdQuotesRequestSectionsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.post_jobs_job_id_quotes(
                job_id="jobId",
                title="title",
                due_days=1.1,
                sections=[
                    PostJobsJobIdQuotesRequestSectionsItem(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_jobs_job_id_quotes(
            job_id,
            title=title,
            due_days=due_days,
            sections=sections,
            description=description,
            version_number=version_number,
            request_options=request_options,
        )
        return _response.data

    async def get_jobs_job_id_quotes_quote_id(
        self, job_id: float, quote_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetQuoteByIdQuoteResponse:
        """
        Get a quote

        Parameters
        ----------
        job_id : float

        quote_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuoteByIdQuoteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs_job_id_quotes_quote_id(
                job_id=1.1,
                quote_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_job_id_quotes_quote_id(
            job_id, quote_id, request_options=request_options
        )
        return _response.data

    async def put_jobs_job_id_quotes_quote_id(
        self,
        job_id: float,
        quote_id: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateQuoteResponse:
        """
        Update a quote by ID

        Parameters
        ----------
        job_id : float

        quote_id : float

        sections : typing.Sequence[PutJobsJobIdQuotesQuoteIdRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateQuoteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.jobs import PutJobsJobIdQuotesQuoteIdRequestSectionsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.put_jobs_job_id_quotes_quote_id(
                job_id=1.1,
                quote_id=1.1,
                sections=[
                    PutJobsJobIdQuotesQuoteIdRequestSectionsItem(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_jobs_job_id_quotes_quote_id(
            job_id, quote_id, sections=sections, title=title, description=description, request_options=request_options
        )
        return _response.data

    async def put_jobs_job_id_quotes_version_version_number(
        self,
        job_id: float,
        version_number: float,
        *,
        sections: typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem],
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateQuoteResponse:
        """
        Update a quote by version number

        Parameters
        ----------
        job_id : float

        version_number : float

        sections : typing.Sequence[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem]

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateQuoteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.jobs import PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.put_jobs_job_id_quotes_version_version_number(
                job_id=1.1,
                version_number=1.1,
                sections=[
                    PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_jobs_job_id_quotes_version_version_number(
            job_id,
            version_number,
            sections=sections,
            title=title,
            description=description,
            request_options=request_options,
        )
        return _response.data
