

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.add_analysis_archive_result import AddAnalysisArchiveResult
from ..types.analysis_archive_rules import AnalysisArchiveRules
from ..types.analysis_archive_transition_rule import AnalysisArchiveTransitionRule
from ..types.analysis_archive_transition_rule_exclude import AnalysisArchiveTransitionRuleExclude
from ..types.analysis_archive_transition_rule_transition import AnalysisArchiveTransitionRuleTransition
from ..types.archive_summary import ArchiveSummary
from ..types.archived_analyses import ArchivedAnalyses
from ..types.archived_analysis import ArchivedAnalysis
from ..types.image_analysis_references import ImageAnalysisReferences
from ..types.image_selector import ImageSelector
from .raw_client import AsyncRawArchivesClient, RawArchivesClient


OMIT = typing.cast(typing.Any, ...)


class ArchivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArchivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArchivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArchivesClient
        """
        return self._raw_client

    def list_archives(self, *, request_options: typing.Optional[RequestOptions] = None) -> ArchiveSummary:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchiveSummary
            Archive summary listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.list_archives()
        """
        _response = self._raw_client.list_archives(request_options=request_options)
        return _response.data

    def list_analysis_archive(self, *, request_options: typing.Optional[RequestOptions] = None) -> ArchivedAnalyses:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivedAnalyses
            Image analysis archive listing for the requesting account (not the whole system)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.list_analysis_archive()
        """
        _response = self._raw_client.list_analysis_archive(request_options=request_options)
        return _response.data

    def archive_image_analysis(
        self, *, request: ImageAnalysisReferences, request_options: typing.Optional[RequestOptions] = None
    ) -> AddAnalysisArchiveResult:
        """
        Parameters
        ----------
        request : ImageAnalysisReferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddAnalysisArchiveResult
            Archive statuses

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.archive_image_analysis(
            request=["string"],
        )
        """
        _response = self._raw_client.archive_image_analysis(request=request, request_options=request_options)
        return _response.data

    def get_archived_analysis(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArchivedAnalysis:
        """
        Returns the archive metadata record identifying the image and tags for the analysis in the archive.

        Parameters
        ----------
        image_digest : str
            The image digest to identify the image analysis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivedAnalysis
            Archived Image

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.get_archived_analysis(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.get_archived_analysis(image_digest, request_options=request_options)
        return _response.data

    def delete_archived_analysis(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs a synchronous archive deletion

        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.delete_archived_analysis(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.delete_archived_analysis(
            image_digest, force=force, request_options=request_options
        )
        return _response.data

    def list_analysis_archive_rules(
        self, *, system_global: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AnalysisArchiveRules:
        """
        Parameters
        ----------
        system_global : typing.Optional[bool]
            If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveRules
            Archive transition rules

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.list_analysis_archive_rules()
        """
        _response = self._raw_client.list_analysis_archive_rules(
            system_global=system_global, request_options=request_options
        )
        return _response.data

    def create_analysis_archive_rule(
        self,
        *,
        transition: AnalysisArchiveTransitionRuleTransition,
        analysis_age_days: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        exclude: typing.Optional[AnalysisArchiveTransitionRuleExclude] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_images_per_account: typing.Optional[int] = OMIT,
        rule_id: typing.Optional[str] = OMIT,
        selector: typing.Optional[ImageSelector] = OMIT,
        system_global: typing.Optional[bool] = OMIT,
        tag_versions_newer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalysisArchiveTransitionRule:
        """
        Parameters
        ----------
        transition : AnalysisArchiveTransitionRuleTransition
            The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.

        analysis_age_days : typing.Optional[int]
            Matches if the analysis is strictly older than this number of days

        created_at : typing.Optional[dt.datetime]

        exclude : typing.Optional[AnalysisArchiveTransitionRuleExclude]

        last_updated : typing.Optional[dt.datetime]

        max_images_per_account : typing.Optional[int]
            This is the maximum number of image analyses an account can have. Can only be set on system_global rules

        rule_id : typing.Optional[str]
            Unique identifier for archive rule

        selector : typing.Optional[ImageSelector]

        system_global : typing.Optional[bool]
            True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them

        tag_versions_newer : typing.Optional[int]
            Number of images mapped to the tag that are newer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveTransitionRule
            Archive transition rule

        Examples
        --------
        from fern import AnalysisArchiveTransitionRuleTransition, FernApi

        client = FernApi()
        client.archives.create_analysis_archive_rule(
            transition=AnalysisArchiveTransitionRuleTransition.ARCHIVE,
        )
        """
        _response = self._raw_client.create_analysis_archive_rule(
            transition=transition,
            analysis_age_days=analysis_age_days,
            created_at=created_at,
            exclude=exclude,
            last_updated=last_updated,
            max_images_per_account=max_images_per_account,
            rule_id=rule_id,
            selector=selector,
            system_global=system_global,
            tag_versions_newer=tag_versions_newer,
            request_options=request_options,
        )
        return _response.data

    def get_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnalysisArchiveTransitionRule:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveTransitionRule
            Archive transition rule

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.get_analysis_archive_rule(
            rule_id="ruleId",
        )
        """
        _response = self._raw_client.get_analysis_archive_rule(rule_id, request_options=request_options)
        return _response.data

    def delete_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.archives.delete_analysis_archive_rule(
            rule_id="ruleId",
        )
        """
        _response = self._raw_client.delete_analysis_archive_rule(rule_id, request_options=request_options)
        return _response.data


class AsyncArchivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArchivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArchivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArchivesClient
        """
        return self._raw_client

    async def list_archives(self, *, request_options: typing.Optional[RequestOptions] = None) -> ArchiveSummary:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchiveSummary
            Archive summary listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.list_archives()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_archives(request_options=request_options)
        return _response.data

    async def list_analysis_archive(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArchivedAnalyses:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivedAnalyses
            Image analysis archive listing for the requesting account (not the whole system)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.list_analysis_archive()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_analysis_archive(request_options=request_options)
        return _response.data

    async def archive_image_analysis(
        self, *, request: ImageAnalysisReferences, request_options: typing.Optional[RequestOptions] = None
    ) -> AddAnalysisArchiveResult:
        """
        Parameters
        ----------
        request : ImageAnalysisReferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddAnalysisArchiveResult
            Archive statuses

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.archive_image_analysis(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_image_analysis(request=request, request_options=request_options)
        return _response.data

    async def get_archived_analysis(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArchivedAnalysis:
        """
        Returns the archive metadata record identifying the image and tags for the analysis in the archive.

        Parameters
        ----------
        image_digest : str
            The image digest to identify the image analysis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArchivedAnalysis
            Archived Image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.get_archived_analysis(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_archived_analysis(image_digest, request_options=request_options)
        return _response.data

    async def delete_archived_analysis(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs a synchronous archive deletion

        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.delete_archived_analysis(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_archived_analysis(
            image_digest, force=force, request_options=request_options
        )
        return _response.data

    async def list_analysis_archive_rules(
        self, *, system_global: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AnalysisArchiveRules:
        """
        Parameters
        ----------
        system_global : typing.Optional[bool]
            If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveRules
            Archive transition rules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.list_analysis_archive_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_analysis_archive_rules(
            system_global=system_global, request_options=request_options
        )
        return _response.data

    async def create_analysis_archive_rule(
        self,
        *,
        transition: AnalysisArchiveTransitionRuleTransition,
        analysis_age_days: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        exclude: typing.Optional[AnalysisArchiveTransitionRuleExclude] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_images_per_account: typing.Optional[int] = OMIT,
        rule_id: typing.Optional[str] = OMIT,
        selector: typing.Optional[ImageSelector] = OMIT,
        system_global: typing.Optional[bool] = OMIT,
        tag_versions_newer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalysisArchiveTransitionRule:
        """
        Parameters
        ----------
        transition : AnalysisArchiveTransitionRuleTransition
            The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.

        analysis_age_days : typing.Optional[int]
            Matches if the analysis is strictly older than this number of days

        created_at : typing.Optional[dt.datetime]

        exclude : typing.Optional[AnalysisArchiveTransitionRuleExclude]

        last_updated : typing.Optional[dt.datetime]

        max_images_per_account : typing.Optional[int]
            This is the maximum number of image analyses an account can have. Can only be set on system_global rules

        rule_id : typing.Optional[str]
            Unique identifier for archive rule

        selector : typing.Optional[ImageSelector]

        system_global : typing.Optional[bool]
            True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them

        tag_versions_newer : typing.Optional[int]
            Number of images mapped to the tag that are newer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveTransitionRule
            Archive transition rule

        Examples
        --------
        import asyncio

        from fern import AnalysisArchiveTransitionRuleTransition, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.create_analysis_archive_rule(
                transition=AnalysisArchiveTransitionRuleTransition.ARCHIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_analysis_archive_rule(
            transition=transition,
            analysis_age_days=analysis_age_days,
            created_at=created_at,
            exclude=exclude,
            last_updated=last_updated,
            max_images_per_account=max_images_per_account,
            rule_id=rule_id,
            selector=selector,
            system_global=system_global,
            tag_versions_newer=tag_versions_newer,
            request_options=request_options,
        )
        return _response.data

    async def get_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AnalysisArchiveTransitionRule:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalysisArchiveTransitionRule
            Archive transition rule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.get_analysis_archive_rule(
                rule_id="ruleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_analysis_archive_rule(rule_id, request_options=request_options)
        return _response.data

    async def delete_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.archives.delete_analysis_archive_rule(
                rule_id="ruleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_analysis_archive_rule(rule_id, request_options=request_options)
        return _response.data
