

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_cancel_with_number_response import JobCancelWithNumberResponse
from ..types.job_get_artifacts_response import JobGetArtifactsResponse
from ..types.job_get_details_response import JobGetDetailsResponse
from ..types.job_get_test_metadata_response import JobGetTestMetadataResponse
from .raw_client import AsyncRawJobClient, RawJobClient


class JobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobClient
        """
        return self._raw_client

    def getdetails(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetDetailsResponse:
        """
        Returns job details.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetDetailsResponse
            Job details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.job.getdetails(
            project_slug="project-slug",
            job_number="job-number",
        )
        """
        _response = self._raw_client.getdetails(project_slug, job_number, request_options=request_options)
        return _response.data

    def cancelwithnumber(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobCancelWithNumberResponse:
        """
        Cancel job with a given job number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobCancelWithNumberResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.job.cancelwithnumber(
            project_slug="project-slug",
            job_number="job-number",
        )
        """
        _response = self._raw_client.cancelwithnumber(project_slug, job_number, request_options=request_options)
        return _response.data

    def getartifacts(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetArtifactsResponse:
        """
        Returns a job's artifacts.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetArtifactsResponse
            A paginated list of the job's artifacts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.job.getartifacts(
            project_slug="project-slug",
            job_number="job-number",
        )
        """
        _response = self._raw_client.getartifacts(project_slug, job_number, request_options=request_options)
        return _response.data

    def gettestmetadata(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetTestMetadataResponse:
        """
        Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetTestMetadataResponse
            A paginated list of test results.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.job.gettestmetadata(
            project_slug="project-slug",
            job_number="job-number",
        )
        """
        _response = self._raw_client.gettestmetadata(project_slug, job_number, request_options=request_options)
        return _response.data


class AsyncJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobClient
        """
        return self._raw_client

    async def getdetails(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetDetailsResponse:
        """
        Returns job details.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetDetailsResponse
            Job details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.job.getdetails(
                project_slug="project-slug",
                job_number="job-number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdetails(project_slug, job_number, request_options=request_options)
        return _response.data

    async def cancelwithnumber(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobCancelWithNumberResponse:
        """
        Cancel job with a given job number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobCancelWithNumberResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.job.cancelwithnumber(
                project_slug="project-slug",
                job_number="job-number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelwithnumber(project_slug, job_number, request_options=request_options)
        return _response.data

    async def getartifacts(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetArtifactsResponse:
        """
        Returns a job's artifacts.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetArtifactsResponse
            A paginated list of the job's artifacts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.job.getartifacts(
                project_slug="project-slug",
                job_number="job-number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getartifacts(project_slug, job_number, request_options=request_options)
        return _response.data

    async def gettestmetadata(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobGetTestMetadataResponse:
        """
        Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        job_number : typing.Any
            The number of the job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobGetTestMetadataResponse
            A paginated list of test results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.job.gettestmetadata(
                project_slug="project-slug",
                job_number="job-number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettestmetadata(project_slug, job_number, request_options=request_options)
        return _response.data
