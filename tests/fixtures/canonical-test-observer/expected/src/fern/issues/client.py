

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.execution_metadata import ExecutionMetadata
from ..types.family_name import FamilyName
from ..types.issue_response import IssueResponse
from ..types.issue_source import IssueSource
from ..types.issue_status import IssueStatus
from ..types.issues_get_response import IssuesGetResponse
from ..types.minimal_issue_test_result_attachment_rule_response import MinimalIssueTestResultAttachmentRuleResponse
from ..types.test_result_search_filters import TestResultSearchFilters
from ..types.test_result_status import TestResultStatus
from .raw_client import AsyncRawIssuesClient, RawIssuesClient


OMIT = typing.cast(typing.Any, ...)


class IssuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIssuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIssuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIssuesClient
        """
        return self._raw_client

    def add_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.add_issue_attachments(
            issue_id=1,
        )
        """
        _response = self._raw_client.add_issue_attachments(
            issue_id,
            test_results=test_results,
            test_results_filters=test_results_filters,
            attachment_rule=attachment_rule,
            request_options=request_options,
        )
        return _response.data

    def remove_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.remove_issue_attachments(
            issue_id=1,
        )
        """
        _response = self._raw_client.remove_issue_attachments(
            issue_id,
            test_results=test_results,
            test_results_filters=test_results_filters,
            attachment_rule=attachment_rule,
            request_options=request_options,
        )
        return _response.data

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
    ) -> MinimalIssueTestResultAttachmentRuleResponse:
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
        MinimalIssueTestResultAttachmentRuleResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.post_attachment_rule(
            issue_id=1,
        )
        """
        _response = self._raw_client.post_attachment_rule(
            issue_id,
            enabled=enabled,
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            environment_names=environment_names,
            test_plans=test_plans,
            test_case_names=test_case_names,
            template_ids=template_ids,
            test_result_statuses=test_result_statuses,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    def delete_attachment_rule(
        self, issue_id: int, attachment_rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.delete_attachment_rule(
            issue_id=1,
            attachment_rule_id=1,
        )
        """
        _response = self._raw_client.delete_attachment_rule(
            issue_id, attachment_rule_id, request_options=request_options
        )
        return _response.data

    def patch_attachment_rule(
        self,
        issue_id: int,
        attachment_rule_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MinimalIssueTestResultAttachmentRuleResponse:
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
        MinimalIssueTestResultAttachmentRuleResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.patch_attachment_rule(
            issue_id=1,
            attachment_rule_id=1,
        )
        """
        _response = self._raw_client.patch_attachment_rule(
            issue_id, attachment_rule_id, enabled=enabled, request_options=request_options
        )
        return _response.data

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
    ) -> IssuesGetResponse:
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
        IssuesGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.get_issues()
        """
        _response = self._raw_client.get_issues(
            source=source,
            project=project,
            status=status,
            families=families,
            limit=limit,
            offset=offset,
            q=q,
            request_options=request_options,
        )
        return _response.data

    def create_or_update_issue(
        self,
        *,
        url: str,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[IssueStatus] = OMIT,
        auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.create_or_update_issue(
            url="url",
        )
        """
        _response = self._raw_client.create_or_update_issue(
            url=url, title=title, status=status, auto_rerun_enabled=auto_rerun_enabled, request_options=request_options
        )
        return _response.data

    def get_issue(self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> IssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.get_issue(
            issue_id=1,
        )
        """
        _response = self._raw_client.get_issue(issue_id, request_options=request_options)
        return _response.data

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
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.issues.patch_issue(
            issue_id=1,
        )
        """
        _response = self._raw_client.patch_issue(
            issue_id,
            title=title,
            status=status,
            auto_rerun_enabled=auto_rerun_enabled,
            issue_patch_request_title=issue_patch_request_title,
            issue_patch_request_status=issue_patch_request_status,
            issue_patch_request_auto_rerun_enabled=issue_patch_request_auto_rerun_enabled,
            request_options=request_options,
        )
        return _response.data


class AsyncIssuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIssuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIssuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIssuesClient
        """
        return self._raw_client

    async def add_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.add_issue_attachments(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_issue_attachments(
            issue_id,
            test_results=test_results,
            test_results_filters=test_results_filters,
            attachment_rule=attachment_rule,
            request_options=request_options,
        )
        return _response.data

    async def remove_issue_attachments(
        self,
        issue_id: int,
        *,
        test_results: typing.Optional[typing.Sequence[int]] = OMIT,
        test_results_filters: typing.Optional[TestResultSearchFilters] = OMIT,
        attachment_rule: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.remove_issue_attachments(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_issue_attachments(
            issue_id,
            test_results=test_results,
            test_results_filters=test_results_filters,
            attachment_rule=attachment_rule,
            request_options=request_options,
        )
        return _response.data

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
    ) -> MinimalIssueTestResultAttachmentRuleResponse:
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
        MinimalIssueTestResultAttachmentRuleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.post_attachment_rule(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_attachment_rule(
            issue_id,
            enabled=enabled,
            families=families,
            artefacts=artefacts,
            artefact_versions=artefact_versions,
            artefact_stages=artefact_stages,
            artefact_tracks=artefact_tracks,
            environment_names=environment_names,
            test_plans=test_plans,
            test_case_names=test_case_names,
            template_ids=template_ids,
            test_result_statuses=test_result_statuses,
            execution_metadata=execution_metadata,
            request_options=request_options,
        )
        return _response.data

    async def delete_attachment_rule(
        self, issue_id: int, attachment_rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        issue_id : int

        attachment_rule_id : int

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
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.delete_attachment_rule(
                issue_id=1,
                attachment_rule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_attachment_rule(
            issue_id, attachment_rule_id, request_options=request_options
        )
        return _response.data

    async def patch_attachment_rule(
        self,
        issue_id: int,
        attachment_rule_id: int,
        *,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MinimalIssueTestResultAttachmentRuleResponse:
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
        MinimalIssueTestResultAttachmentRuleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.patch_attachment_rule(
                issue_id=1,
                attachment_rule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_attachment_rule(
            issue_id, attachment_rule_id, enabled=enabled, request_options=request_options
        )
        return _response.data

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
    ) -> IssuesGetResponse:
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
        IssuesGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.get_issues()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_issues(
            source=source,
            project=project,
            status=status,
            families=families,
            limit=limit,
            offset=offset,
            q=q,
            request_options=request_options,
        )
        return _response.data

    async def create_or_update_issue(
        self,
        *,
        url: str,
        title: typing.Optional[str] = OMIT,
        status: typing.Optional[IssueStatus] = OMIT,
        auto_rerun_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.create_or_update_issue(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_issue(
            url=url, title=title, status=status, auto_rerun_enabled=auto_rerun_enabled, request_options=request_options
        )
        return _response.data

    async def get_issue(
        self, issue_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IssueResponse:
        """
        Parameters
        ----------
        issue_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.get_issue(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_issue(issue_id, request_options=request_options)
        return _response.data

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
    ) -> IssueResponse:
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
        IssueResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.issues.patch_issue(
                issue_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_issue(
            issue_id,
            title=title,
            status=status,
            auto_rerun_enabled=auto_rerun_enabled,
            issue_patch_request_title=issue_patch_request_title,
            issue_patch_request_status=issue_patch_request_status,
            issue_patch_request_auto_rerun_enabled=issue_patch_request_auto_rerun_enabled,
            request_options=request_options,
        )
        return _response.data
