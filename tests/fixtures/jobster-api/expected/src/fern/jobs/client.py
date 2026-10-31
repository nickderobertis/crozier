

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_input_job_type import JobInputJobType
from ..types.job_input_status import JobInputStatus
from .raw_client import AsyncRawJobsClient, RawJobsClient
from .types.get_jobs_request_job_type import GetJobsRequestJobType
from .types.get_jobs_request_sort import GetJobsRequestSort
from .types.get_jobs_request_status import GetJobsRequestStatus


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

    def list_the_authenticated_users_jobs(
        self,
        *,
        search: typing.Optional[str] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        job_type: typing.Optional[GetJobsRequestJobType] = None,
        sort: typing.Optional[GetJobsRequestSort] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        status : typing.Optional[GetJobsRequestStatus]

        job_type : typing.Optional[GetJobsRequestJobType]

        sort : typing.Optional[GetJobsRequestSort]

        page : typing.Optional[int]

        limit : typing.Optional[int]

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
        client.jobs.list_the_authenticated_users_jobs()
        """
        _response = self._raw_client.list_the_authenticated_users_jobs(
            search=search,
            status=status,
            job_type=job_type,
            sort=sort,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def create_a_job(
        self,
        *,
        company: str,
        position: str,
        status: typing.Optional[JobInputStatus] = OMIT,
        job_type: typing.Optional[JobInputJobType] = OMIT,
        job_location: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Not currently idempotent; a repeated request creates another job.

        Parameters
        ----------
        company : str

        position : str

        status : typing.Optional[JobInputStatus]

        job_type : typing.Optional[JobInputJobType]

        job_location : typing.Optional[str]

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
        client.jobs.create_a_job(
            company="company",
            position="position",
        )
        """
        _response = self._raw_client.create_a_job(
            company=company,
            position=position,
            status=status,
            job_type=job_type,
            job_location=job_location,
            request_options=request_options,
        )
        return _response.data

    def get_status_totals_and_monthly_application_counts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
        client.jobs.get_status_totals_and_monthly_application_counts()
        """
        _response = self._raw_client.get_status_totals_and_monthly_application_counts(request_options=request_options)
        return _response.data

    def get_one_owned_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.jobs.get_one_owned_job(
            id="id",
        )
        """
        _response = self._raw_client.get_one_owned_job(id, request_options=request_options)
        return _response.data

    def delete_one_owned_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.jobs.delete_one_owned_job(
            id="id",
        )
        """
        _response = self._raw_client.delete_one_owned_job(id, request_options=request_options)
        return _response.data

    def update_one_owned_job(
        self,
        id: str,
        *,
        company: str,
        position: str,
        status: typing.Optional[JobInputStatus] = OMIT,
        job_type: typing.Optional[JobInputJobType] = OMIT,
        job_location: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        company : str

        position : str

        status : typing.Optional[JobInputStatus]

        job_type : typing.Optional[JobInputJobType]

        job_location : typing.Optional[str]

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
        client.jobs.update_one_owned_job(
            id="id",
            company="company",
            position="position",
        )
        """
        _response = self._raw_client.update_one_owned_job(
            id,
            company=company,
            position=position,
            status=status,
            job_type=job_type,
            job_location=job_location,
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

    async def list_the_authenticated_users_jobs(
        self,
        *,
        search: typing.Optional[str] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        job_type: typing.Optional[GetJobsRequestJobType] = None,
        sort: typing.Optional[GetJobsRequestSort] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        status : typing.Optional[GetJobsRequestStatus]

        job_type : typing.Optional[GetJobsRequestJobType]

        sort : typing.Optional[GetJobsRequestSort]

        page : typing.Optional[int]

        limit : typing.Optional[int]

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
            await client.jobs.list_the_authenticated_users_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_authenticated_users_jobs(
            search=search,
            status=status,
            job_type=job_type,
            sort=sort,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def create_a_job(
        self,
        *,
        company: str,
        position: str,
        status: typing.Optional[JobInputStatus] = OMIT,
        job_type: typing.Optional[JobInputJobType] = OMIT,
        job_location: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Not currently idempotent; a repeated request creates another job.

        Parameters
        ----------
        company : str

        position : str

        status : typing.Optional[JobInputStatus]

        job_type : typing.Optional[JobInputJobType]

        job_location : typing.Optional[str]

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
            await client.jobs.create_a_job(
                company="company",
                position="position",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_job(
            company=company,
            position=position,
            status=status,
            job_type=job_type,
            job_location=job_location,
            request_options=request_options,
        )
        return _response.data

    async def get_status_totals_and_monthly_application_counts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            await client.jobs.get_status_totals_and_monthly_application_counts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status_totals_and_monthly_application_counts(
            request_options=request_options
        )
        return _response.data

    async def get_one_owned_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.jobs.get_one_owned_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_one_owned_job(id, request_options=request_options)
        return _response.data

    async def delete_one_owned_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.jobs.delete_one_owned_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_one_owned_job(id, request_options=request_options)
        return _response.data

    async def update_one_owned_job(
        self,
        id: str,
        *,
        company: str,
        position: str,
        status: typing.Optional[JobInputStatus] = OMIT,
        job_type: typing.Optional[JobInputJobType] = OMIT,
        job_location: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        company : str

        position : str

        status : typing.Optional[JobInputStatus]

        job_type : typing.Optional[JobInputJobType]

        job_location : typing.Optional[str]

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
            await client.jobs.update_one_owned_job(
                id="id",
                company="company",
                position="position",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_one_owned_job(
            id,
            company=company,
            position=position,
            status=status,
            job_type=job_type,
            job_location=job_location,
            request_options=request_options,
        )
        return _response.data
