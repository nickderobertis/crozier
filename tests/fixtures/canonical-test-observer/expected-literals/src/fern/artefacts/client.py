

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artefact_build_environment_review_decision import ArtefactBuildEnvironmentReviewDecision
from ..types.artefact_build_environment_review_response import ArtefactBuildEnvironmentReviewResponse
from ..types.artefact_build_response import ArtefactBuildResponse
from ..types.artefact_history_response import ArtefactHistoryResponse
from ..types.artefact_response import ArtefactResponse
from ..types.artefact_search_response import ArtefactSearchResponse
from ..types.artefact_status import ArtefactStatus
from ..types.artefact_version_response import ArtefactVersionResponse
from ..types.environment_review_patch import EnvironmentReviewPatch
from ..types.expected_environment_input import ExpectedEnvironmentInput
from ..types.family_name import FamilyName
from ..types.stage_name import StageName
from .raw_client import AsyncRawArtefactsClient, RawArtefactsClient


OMIT = typing.cast(typing.Any, ...)


class ArtefactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtefactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtefactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtefactsClient
        """
        return self._raw_client

    def get_artefacts(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactResponse]:
        """
        Get latest artefacts optionally by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_artefacts()
        """
        _response = self._raw_client.get_artefacts(family=family, request_options=request_options)
        return _response.data

    def search_artefacts(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactSearchResponse:
        """
        Search for artefacts by name with pagination support.

        Returns a list of distinct artefact names that match the search query.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for artefact names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactSearchResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.search_artefacts()
        """
        _response = self._raw_client.search_artefacts(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_artefact_history(
        self,
        *,
        name: str,
        family: FamilyName,
        track: typing.Optional[str] = None,
        stage: typing.Optional[StageName] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactHistoryResponse:
        """
        Get the versioning history of an artefact for a given name, family, and track,
        optionally filtered by stage, with pagination support.

        Returns a list of artefact versions along with their creation date.

        Parameters
        ----------
        name : str
            Artefact name

        family : FamilyName
            Artefact family

        track : typing.Optional[str]
            Artefact track

        stage : typing.Optional[StageName]
            Filter by stage

        limit : typing.Optional[int]
            Maximum number of results (defaults to 10 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactHistoryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_artefact_history(
            name="name",
            family="snap",
        )
        """
        _response = self._raw_client.get_artefact_history(
            name=name,
            family=family,
            track=track,
            stage=stage,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtefactResponse:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_artefact(
            artefact_id=1,
        )
        """
        _response = self._raw_client.get_artefact(artefact_id, request_options=request_options)
        return _response.data

    def delete_artefact(self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        artefact_id : int

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
        client.artefacts.delete_artefact(
            artefact_id=1,
        )
        """
        _response = self._raw_client.delete_artefact(artefact_id, request_options=request_options)
        return _response.data

    def patch_artefact(
        self,
        artefact_id: int,
        *,
        status: typing.Optional[ArtefactStatus] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        stage: typing.Optional[StageName] = OMIT,
        comment: typing.Optional[str] = OMIT,
        jira_issue: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        expected_environments: typing.Optional[typing.Sequence[ExpectedEnvironmentInput]] = OMIT,
        assignee_id: typing.Optional[int] = OMIT,
        assignee_email: typing.Optional[str] = OMIT,
        reviewer_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        reviewer_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactResponse:
        """
        Parameters
        ----------
        artefact_id : int

        status : typing.Optional[ArtefactStatus]

        archived : typing.Optional[bool]

        stage : typing.Optional[StageName]

        comment : typing.Optional[str]

        jira_issue : typing.Optional[str]

        attributes : typing.Optional[typing.Dict[str, typing.Any]]

        expected_environments : typing.Optional[typing.Sequence[ExpectedEnvironmentInput]]
            Expected environments, replacing the current set. Each environment is identified by name and architecture.

        assignee_id : typing.Optional[int]
            Legacy field. Mapped to reviewer_ids as a single-element list when reviewer_ids/reviewer_emails are not provided.

        assignee_email : typing.Optional[str]
            Legacy field. Mapped to reviewer_emails as a single-element list when reviewer_ids/reviewer_emails are not provided.

        reviewer_ids : typing.Optional[typing.Sequence[int]]
            Reviewer user IDs. Preferred over legacy assignee_id/assignee_email for setting assignees.

        reviewer_emails : typing.Optional[typing.Sequence[str]]
            Reviewer emails. Preferred over legacy assignee_id/assignee_email for setting assignees.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.patch_artefact(
            artefact_id=1,
        )
        """
        _response = self._raw_client.patch_artefact(
            artefact_id,
            status=status,
            archived=archived,
            stage=stage,
            comment=comment,
            jira_issue=jira_issue,
            attributes=attributes,
            expected_environments=expected_environments,
            assignee_id=assignee_id,
            assignee_email=assignee_email,
            reviewer_ids=reviewer_ids,
            reviewer_emails=reviewer_emails,
            request_options=request_options,
        )
        return _response.data

    def get_artefact_versions(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactVersionResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactVersionResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_artefact_versions(
            artefact_id=1,
        )
        """
        _response = self._raw_client.get_artefact_versions(artefact_id, request_options=request_options)
        return _response.data

    def get_environment_reviews(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildEnvironmentReviewResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_environment_reviews(
            artefact_id=1,
        )
        """
        _response = self._raw_client.get_environment_reviews(artefact_id, request_options=request_options)
        return _response.data

    def bulk_update_environment_reviews(
        self,
        artefact_id: int,
        *,
        request: typing.Sequence[EnvironmentReviewPatch],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request : typing.Sequence[EnvironmentReviewPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildEnvironmentReviewResponse]
            Successful Response

        Examples
        --------
        from fern import EnvironmentReviewPatch, FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.bulk_update_environment_reviews(
            artefact_id=1,
            request=[EnvironmentReviewPatch()],
        )
        """
        _response = self._raw_client.bulk_update_environment_reviews(
            artefact_id, request=request, request_options=request_options
        )
        return _response.data

    def update_environment_review(
        self,
        artefact_id: int,
        review_id: int,
        *,
        id: typing.Optional[int] = OMIT,
        review_decision: typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]] = OMIT,
        review_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactBuildEnvironmentReviewResponse:
        """
        Parameters
        ----------
        artefact_id : int

        review_id : int

        id : typing.Optional[int]

        review_decision : typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]]

        review_comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactBuildEnvironmentReviewResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.update_environment_review(
            artefact_id=1,
            review_id=1,
        )
        """
        _response = self._raw_client.update_environment_review(
            artefact_id,
            review_id,
            id=id,
            review_decision=review_decision,
            review_comment=review_comment,
            request_options=request_options,
        )
        return _response.data

    def get_artefact_builds(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactBuildResponse]:
        """
        Get latest artefact builds of an artefact together with their test executions

        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefacts.get_artefact_builds(
            artefact_id=1,
        )
        """
        _response = self._raw_client.get_artefact_builds(artefact_id, request_options=request_options)
        return _response.data


class AsyncArtefactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtefactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtefactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtefactsClient
        """
        return self._raw_client

    async def get_artefacts(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactResponse]:
        """
        Get latest artefacts optionally by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactResponse]
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
            await client.artefacts.get_artefacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefacts(family=family, request_options=request_options)
        return _response.data

    async def search_artefacts(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactSearchResponse:
        """
        Search for artefacts by name with pagination support.

        Returns a list of distinct artefact names that match the search query.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for artefact names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactSearchResponse
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
            await client.artefacts.search_artefacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_artefacts(
            q=q, families=families, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_artefact_history(
        self,
        *,
        name: str,
        family: FamilyName,
        track: typing.Optional[str] = None,
        stage: typing.Optional[StageName] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactHistoryResponse:
        """
        Get the versioning history of an artefact for a given name, family, and track,
        optionally filtered by stage, with pagination support.

        Returns a list of artefact versions along with their creation date.

        Parameters
        ----------
        name : str
            Artefact name

        family : FamilyName
            Artefact family

        track : typing.Optional[str]
            Artefact track

        stage : typing.Optional[StageName]
            Filter by stage

        limit : typing.Optional[int]
            Maximum number of results (defaults to 10 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactHistoryResponse
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
            await client.artefacts.get_artefact_history(
                name="name",
                family="snap",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact_history(
            name=name,
            family=family,
            track=track,
            stage=stage,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtefactResponse:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactResponse
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
            await client.artefacts.get_artefact(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact(artefact_id, request_options=request_options)
        return _response.data

    async def delete_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        artefact_id : int

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
            await client.artefacts.delete_artefact(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artefact(artefact_id, request_options=request_options)
        return _response.data

    async def patch_artefact(
        self,
        artefact_id: int,
        *,
        status: typing.Optional[ArtefactStatus] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        stage: typing.Optional[StageName] = OMIT,
        comment: typing.Optional[str] = OMIT,
        jira_issue: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        expected_environments: typing.Optional[typing.Sequence[ExpectedEnvironmentInput]] = OMIT,
        assignee_id: typing.Optional[int] = OMIT,
        assignee_email: typing.Optional[str] = OMIT,
        reviewer_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        reviewer_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactResponse:
        """
        Parameters
        ----------
        artefact_id : int

        status : typing.Optional[ArtefactStatus]

        archived : typing.Optional[bool]

        stage : typing.Optional[StageName]

        comment : typing.Optional[str]

        jira_issue : typing.Optional[str]

        attributes : typing.Optional[typing.Dict[str, typing.Any]]

        expected_environments : typing.Optional[typing.Sequence[ExpectedEnvironmentInput]]
            Expected environments, replacing the current set. Each environment is identified by name and architecture.

        assignee_id : typing.Optional[int]
            Legacy field. Mapped to reviewer_ids as a single-element list when reviewer_ids/reviewer_emails are not provided.

        assignee_email : typing.Optional[str]
            Legacy field. Mapped to reviewer_emails as a single-element list when reviewer_ids/reviewer_emails are not provided.

        reviewer_ids : typing.Optional[typing.Sequence[int]]
            Reviewer user IDs. Preferred over legacy assignee_id/assignee_email for setting assignees.

        reviewer_emails : typing.Optional[typing.Sequence[str]]
            Reviewer emails. Preferred over legacy assignee_id/assignee_email for setting assignees.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactResponse
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
            await client.artefacts.patch_artefact(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_artefact(
            artefact_id,
            status=status,
            archived=archived,
            stage=stage,
            comment=comment,
            jira_issue=jira_issue,
            attributes=attributes,
            expected_environments=expected_environments,
            assignee_id=assignee_id,
            assignee_email=assignee_email,
            reviewer_ids=reviewer_ids,
            reviewer_emails=reviewer_emails,
            request_options=request_options,
        )
        return _response.data

    async def get_artefact_versions(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactVersionResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactVersionResponse]
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
            await client.artefacts.get_artefact_versions(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact_versions(artefact_id, request_options=request_options)
        return _response.data

    async def get_environment_reviews(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildEnvironmentReviewResponse]
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
            await client.artefacts.get_environment_reviews(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_environment_reviews(artefact_id, request_options=request_options)
        return _response.data

    async def bulk_update_environment_reviews(
        self,
        artefact_id: int,
        *,
        request: typing.Sequence[EnvironmentReviewPatch],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request : typing.Sequence[EnvironmentReviewPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildEnvironmentReviewResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EnvironmentReviewPatch

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefacts.bulk_update_environment_reviews(
                artefact_id=1,
                request=[EnvironmentReviewPatch()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_environment_reviews(
            artefact_id, request=request, request_options=request_options
        )
        return _response.data

    async def update_environment_review(
        self,
        artefact_id: int,
        review_id: int,
        *,
        id: typing.Optional[int] = OMIT,
        review_decision: typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]] = OMIT,
        review_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactBuildEnvironmentReviewResponse:
        """
        Parameters
        ----------
        artefact_id : int

        review_id : int

        id : typing.Optional[int]

        review_decision : typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]]

        review_comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactBuildEnvironmentReviewResponse
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
            await client.artefacts.update_environment_review(
                artefact_id=1,
                review_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_environment_review(
            artefact_id,
            review_id,
            id=id,
            review_decision=review_decision,
            review_comment=review_comment,
            request_options=request_options,
        )
        return _response.data

    async def get_artefact_builds(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactBuildResponse]:
        """
        Get latest artefact builds of an artefact together with their test executions

        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactBuildResponse]
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
            await client.artefacts.get_artefact_builds(
                artefact_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact_builds(artefact_id, request_options=request_options)
        return _response.data
