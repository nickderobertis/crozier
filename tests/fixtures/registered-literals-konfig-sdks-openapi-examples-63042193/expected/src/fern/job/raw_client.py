

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.job_cancel_with_number_response import JobCancelWithNumberResponse
from ..types.job_get_artifacts_response import JobGetArtifactsResponse
from ..types.job_get_details_response import JobGetDetailsResponse
from ..types.job_get_test_metadata_response import JobGetTestMetadataResponse
from pydantic import ValidationError


class RawJobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getdetails(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobGetDetailsResponse]:
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
        HttpResponse[JobGetDetailsResponse]
            Job details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/job/{encode_path_param(job_number)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetDetailsResponse,
                    parse_obj_as(
                        type_=JobGetDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancelwithnumber(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobCancelWithNumberResponse]:
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
        HttpResponse[JobCancelWithNumberResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/job/{encode_path_param(job_number)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobCancelWithNumberResponse,
                    parse_obj_as(
                        type_=JobCancelWithNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getartifacts(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobGetArtifactsResponse]:
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
        HttpResponse[JobGetArtifactsResponse]
            A paginated list of the job's artifacts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/{encode_path_param(job_number)}/artifacts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetArtifactsResponse,
                    parse_obj_as(
                        type_=JobGetArtifactsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def gettestmetadata(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobGetTestMetadataResponse]:
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
        HttpResponse[JobGetTestMetadataResponse]
            A paginated list of test results.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/{encode_path_param(job_number)}/tests",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetTestMetadataResponse,
                    parse_obj_as(
                        type_=JobGetTestMetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getdetails(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobGetDetailsResponse]:
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
        AsyncHttpResponse[JobGetDetailsResponse]
            Job details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/job/{encode_path_param(job_number)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetDetailsResponse,
                    parse_obj_as(
                        type_=JobGetDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancelwithnumber(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobCancelWithNumberResponse]:
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
        AsyncHttpResponse[JobCancelWithNumberResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/job/{encode_path_param(job_number)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobCancelWithNumberResponse,
                    parse_obj_as(
                        type_=JobCancelWithNumberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getartifacts(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobGetArtifactsResponse]:
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
        AsyncHttpResponse[JobGetArtifactsResponse]
            A paginated list of the job's artifacts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/{encode_path_param(job_number)}/artifacts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetArtifactsResponse,
                    parse_obj_as(
                        type_=JobGetArtifactsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def gettestmetadata(
        self, project_slug: str, job_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobGetTestMetadataResponse]:
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
        AsyncHttpResponse[JobGetTestMetadataResponse]
            A paginated list of test results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_slug)}/{encode_path_param(job_number)}/tests",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobGetTestMetadataResponse,
                    parse_obj_as(
                        type_=JobGetTestMetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
