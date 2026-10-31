

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.execution_metadata import ExecutionMetadata
from ..types.family_name import FamilyName
from ..types.http_validation_error import HttpValidationError
from ..types.issue_response import IssueResponse
from ..types.issue_source import IssueSource
from ..types.issue_status import IssueStatus
from ..types.issues_get_response import IssuesGetResponse
from ..types.minimal_issue_test_result_attachment_rule_response import MinimalIssueTestResultAttachmentRuleResponse
from ..types.test_result_search_filters import TestResultSearchFilters
from ..types.test_result_status import TestResultStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIssuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        test_results : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        attachment_rule : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attach",
            method="POST",
            json={
                "test_results": test_results,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "attachment_rule": attachment_rule,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        test_results : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        attachment_rule : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/detach",
            method="POST",
            json={
                "test_results": test_results,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "attachment_rule": attachment_rule,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_attachment_rule(
        self,
        issue_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        families: typing.Optional[typing.Sequence[FamilyName]] = OMIT,
        artefacts: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_versions: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_stages: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_tracks: typing.Optional[typing.Sequence[str]] = OMIT,
        environment_names: typing.Optional[typing.Sequence[str]] = OMIT,
        test_plans: typing.Optional[typing.Sequence[str]] = OMIT,
        test_case_names: typing.Optional[typing.Sequence[str]] = OMIT,
        template_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        test_result_statuses: typing.Optional[typing.Sequence[TestResultStatus]] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MinimalIssueTestResultAttachmentRuleResponse]:
        """
        Parameters
        ----------
        issue_id : int

        enabled : typing.Optional[bool]

        families : typing.Optional[typing.Sequence[FamilyName]]

        artefacts : typing.Optional[typing.Sequence[str]]

        artefact_versions : typing.Optional[typing.Sequence[str]]

        artefact_stages : typing.Optional[typing.Sequence[str]]

        artefact_tracks : typing.Optional[typing.Sequence[str]]

        environment_names : typing.Optional[typing.Sequence[str]]

        test_plans : typing.Optional[typing.Sequence[str]]

        test_case_names : typing.Optional[typing.Sequence[str]]

        template_ids : typing.Optional[typing.Sequence[str]]

        test_result_statuses : typing.Optional[typing.Sequence[TestResultStatus]]

        execution_metadata : typing.Optional[ExecutionMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MinimalIssueTestResultAttachmentRuleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules",
            method="POST",
            json={
                "enabled": enabled,
                "families": families,
                "artefacts": artefacts,
                "artefact_versions": artefact_versions,
                "artefact_stages": artefact_stages,
                "artefact_tracks": artefact_tracks,
                "environment_names": environment_names,
                "test_plans": test_plans,
                "test_case_names": test_case_names,
                "template_ids": template_ids,
                "test_result_statuses": test_result_statuses,
                "execution_metadata": execution_metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MinimalIssueTestResultAttachmentRuleResponse,
                    parse_obj_as(
                        type_=MinimalIssueTestResultAttachmentRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_attachment_rule(
        self, issue_id: int, attachment_rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules/{encode_path_param(attachment_rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_attachment_rule(
        self,
        issue_id: int,
        attachment_rule_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MinimalIssueTestResultAttachmentRuleResponse]:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MinimalIssueTestResultAttachmentRuleResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules/{encode_path_param(attachment_rule_id)}",
            method="PATCH",
            json={
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MinimalIssueTestResultAttachmentRuleResponse,
                    parse_obj_as(
                        type_=MinimalIssueTestResultAttachmentRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_issues(
        self,
        *,
        source: typing.Optional[IssueSource] = None,
        project: typing.Optional[str] = None,
        status: typing.Optional[typing.Sequence[IssueStatus]] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssuesGetResponse]:
        """
        Parameters
        ----------
        source : typing.Optional[IssueSource]
            Filter by issue source (e.g., github, jira, launchpad)

        project : typing.Optional[str]
            Filter by project name

        status : typing.Optional[typing.Sequence[IssueStatus]]
            Filter by issue status. Accepts multiple values

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact family (e.g., snap, deb, charm, image)

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        q : typing.Optional[str]
            Search term for issue source, project, keys, title, and status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssuesGetResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/issues",
            method="GET",
            params={
                "source": source,
                "project": project,
                "status": status,
                "families": families,
                "limit": limit,
                "offset": offset,
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssuesGetResponse,
                    parse_obj_as(
                        type_=IssuesGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_update_issue(
        self,
        *,
        url: str,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[IssueStatus] = OMIT,
        auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        url : str

        title : typing.Optional[str]

        status : typing.Optional[IssueStatus]

        auto_rerun_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/issues",
            method="PUT",
            json={
                "title": title,
                "status": status,
                "auto_rerun_enabled": auto_rerun_enabled,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_issue(
        self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_issue(
        self,
        issue_id: int,
        *,
        title: typing.Optional[str] = None,
        status: typing.Optional[IssueStatus] = None,
        auto_rerun_enabled: typing.Optional[bool] = None,
        issue_patch_request_title: typing.Optional[str] = OMIT,
        issue_patch_request_status: typing.Optional[IssueStatus] = OMIT,
        issue_patch_request_auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        title : typing.Optional[str]

        status : typing.Optional[IssueStatus]

        auto_rerun_enabled : typing.Optional[bool]

        issue_patch_request_title : typing.Optional[str]

        issue_patch_request_status : typing.Optional[IssueStatus]

        issue_patch_request_auto_rerun_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}",
            method="PATCH",
            params={
                "title": title,
                "status": status,
                "auto_rerun_enabled": auto_rerun_enabled,
            },
            json={
                "title": issue_patch_request_title,
                "status": issue_patch_request_status,
                "auto_rerun_enabled": issue_patch_request_auto_rerun_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIssuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        test_results : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        attachment_rule : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attach",
            method="POST",
            json={
                "test_results": test_results,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "attachment_rule": attachment_rule,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        test_results : typing.Optional[typing.Sequence[int]]

        test_results_filters : typing.Optional[TestResultSearchFilters]

        attachment_rule : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/detach",
            method="POST",
            json={
                "test_results": test_results,
                "test_results_filters": convert_and_respect_annotation_metadata(
                    object_=test_results_filters, annotation=typing.Optional[TestResultSearchFilters], direction="write"
                ),
                "attachment_rule": attachment_rule,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_attachment_rule(
        self,
        issue_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        families: typing.Optional[typing.Sequence[FamilyName]] = OMIT,
        artefacts: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_versions: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_stages: typing.Optional[typing.Sequence[str]] = OMIT,
        artefact_tracks: typing.Optional[typing.Sequence[str]] = OMIT,
        environment_names: typing.Optional[typing.Sequence[str]] = OMIT,
        test_plans: typing.Optional[typing.Sequence[str]] = OMIT,
        test_case_names: typing.Optional[typing.Sequence[str]] = OMIT,
        template_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        test_result_statuses: typing.Optional[typing.Sequence[TestResultStatus]] = OMIT,
        execution_metadata: typing.Optional[ExecutionMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MinimalIssueTestResultAttachmentRuleResponse]:
        """
        Parameters
        ----------
        issue_id : int

        enabled : typing.Optional[bool]

        families : typing.Optional[typing.Sequence[FamilyName]]

        artefacts : typing.Optional[typing.Sequence[str]]

        artefact_versions : typing.Optional[typing.Sequence[str]]

        artefact_stages : typing.Optional[typing.Sequence[str]]

        artefact_tracks : typing.Optional[typing.Sequence[str]]

        environment_names : typing.Optional[typing.Sequence[str]]

        test_plans : typing.Optional[typing.Sequence[str]]

        test_case_names : typing.Optional[typing.Sequence[str]]

        template_ids : typing.Optional[typing.Sequence[str]]

        test_result_statuses : typing.Optional[typing.Sequence[TestResultStatus]]

        execution_metadata : typing.Optional[ExecutionMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MinimalIssueTestResultAttachmentRuleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules",
            method="POST",
            json={
                "enabled": enabled,
                "families": families,
                "artefacts": artefacts,
                "artefact_versions": artefact_versions,
                "artefact_stages": artefact_stages,
                "artefact_tracks": artefact_tracks,
                "environment_names": environment_names,
                "test_plans": test_plans,
                "test_case_names": test_case_names,
                "template_ids": template_ids,
                "test_result_statuses": test_result_statuses,
                "execution_metadata": execution_metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MinimalIssueTestResultAttachmentRuleResponse,
                    parse_obj_as(
                        type_=MinimalIssueTestResultAttachmentRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_attachment_rule(
        self, issue_id: int, attachment_rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules/{encode_path_param(attachment_rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_attachment_rule(
        self,
        issue_id: int,
        attachment_rule_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MinimalIssueTestResultAttachmentRuleResponse]:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MinimalIssueTestResultAttachmentRuleResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}/attachment-rules/{encode_path_param(attachment_rule_id)}",
            method="PATCH",
            json={
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MinimalIssueTestResultAttachmentRuleResponse,
                    parse_obj_as(
                        type_=MinimalIssueTestResultAttachmentRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_issues(
        self,
        *,
        source: typing.Optional[IssueSource] = None,
        project: typing.Optional[str] = None,
        status: typing.Optional[typing.Sequence[IssueStatus]] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssuesGetResponse]:
        """
        Parameters
        ----------
        source : typing.Optional[IssueSource]
            Filter by issue source (e.g., github, jira, launchpad)

        project : typing.Optional[str]
            Filter by project name

        status : typing.Optional[typing.Sequence[IssueStatus]]
            Filter by issue status. Accepts multiple values

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact family (e.g., snap, deb, charm, image)

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        q : typing.Optional[str]
            Search term for issue source, project, keys, title, and status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssuesGetResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/issues",
            method="GET",
            params={
                "source": source,
                "project": project,
                "status": status,
                "families": families,
                "limit": limit,
                "offset": offset,
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssuesGetResponse,
                    parse_obj_as(
                        type_=IssuesGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_update_issue(
        self,
        *,
        url: str,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[IssueStatus] = OMIT,
        auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        url : str

        title : typing.Optional[str]

        status : typing.Optional[IssueStatus]

        auto_rerun_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/issues",
            method="PUT",
            json={
                "title": title,
                "status": status,
                "auto_rerun_enabled": auto_rerun_enabled,
                "url": url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_issue(
        self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_issue(
        self,
        issue_id: int,
        *,
        title: typing.Optional[str] = None,
        status: typing.Optional[IssueStatus] = None,
        auto_rerun_enabled: typing.Optional[bool] = None,
        issue_patch_request_title: typing.Optional[str] = OMIT,
        issue_patch_request_status: typing.Optional[IssueStatus] = OMIT,
        issue_patch_request_auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueResponse]:
        """
        Parameters
        ----------
        issue_id : int

        title : typing.Optional[str]

        status : typing.Optional[IssueStatus]

        auto_rerun_enabled : typing.Optional[bool]

        issue_patch_request_title : typing.Optional[str]

        issue_patch_request_status : typing.Optional[IssueStatus]

        issue_patch_request_auto_rerun_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/issues/{encode_path_param(issue_id)}",
            method="PATCH",
            params={
                "title": title,
                "status": status,
                "auto_rerun_enabled": auto_rerun_enabled,
            },
            json={
                "title": issue_patch_request_title,
                "status": issue_patch_request_status,
                "auto_rerun_enabled": issue_patch_request_auto_rerun_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueResponse,
                    parse_obj_as(
                        type_=IssueResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
