

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.analyze_commit_diff_response import AnalyzeCommitDiffResponse
from .raw_client import AsyncRawSdksClient, RawSdksClient


OMIT = typing.cast(typing.Any, ...)


class SdksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSdksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSdksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSdksClient
        """
        return self._raw_client

    def analyze_commit_diff(
        self,
        *,
        diff: str,
        language: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[str] = OMIT,
        prior_changelog: typing.Optional[str] = OMIT,
        spec_commit_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyzeCommitDiffResponse:
        """
        Analyzes a git diff and generates an AI-powered commit message with version bump recommendation.

        Parameters
        ----------
        diff : str
            The git diff to analyze for generating a commit message

        language : typing.Optional[str]
            The SDK programming language, e.g. 'typescript', 'python', 'java'. When provided, enables language-specific breaking change rules and behavioral analysis.

        previous_version : typing.Optional[str]
            The current published version before this change, e.g. '1.2.3'. Provided for context only — not included in the commit message.

        prior_changelog : typing.Optional[str]
            The last 3 changelog entries for this SDK. Used to match existing commit message style. Empty string or null if none.

        spec_commit_message : typing.Optional[str]
            The commit message from the API spec repository that triggered this SDK generation. Used as a hint for the intent of the change. Empty string or null if unavailable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyzeCommitDiffResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sdks.analyze_commit_diff(
            diff="diff",
        )
        """
        _response = self._raw_client.analyze_commit_diff(
            diff=diff,
            language=language,
            previous_version=previous_version,
            prior_changelog=prior_changelog,
            spec_commit_message=spec_commit_message,
            request_options=request_options,
        )
        return _response.data


class AsyncSdksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSdksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSdksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSdksClient
        """
        return self._raw_client

    async def analyze_commit_diff(
        self,
        *,
        diff: str,
        language: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[str] = OMIT,
        prior_changelog: typing.Optional[str] = OMIT,
        spec_commit_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyzeCommitDiffResponse:
        """
        Analyzes a git diff and generates an AI-powered commit message with version bump recommendation.

        Parameters
        ----------
        diff : str
            The git diff to analyze for generating a commit message

        language : typing.Optional[str]
            The SDK programming language, e.g. 'typescript', 'python', 'java'. When provided, enables language-specific breaking change rules and behavioral analysis.

        previous_version : typing.Optional[str]
            The current published version before this change, e.g. '1.2.3'. Provided for context only — not included in the commit message.

        prior_changelog : typing.Optional[str]
            The last 3 changelog entries for this SDK. Used to match existing commit message style. Empty string or null if none.

        spec_commit_message : typing.Optional[str]
            The commit message from the API spec repository that triggered this SDK generation. Used as a hint for the intent of the change. Empty string or null if unavailable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyzeCommitDiffResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sdks.analyze_commit_diff(
                diff="diff",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.analyze_commit_diff(
            diff=diff,
            language=language,
            previous_version=previous_version,
            prior_changelog=prior_changelog,
            spec_commit_message=spec_commit_message,
            request_options=request_options,
        )
        return _response.data
