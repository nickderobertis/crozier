

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.prompts_get_response import PromptsGetResponse
from ..types.prompts_prompt_name_post_response import PromptsPromptNamePostResponse
from ..types.prompts_refresh_post_response import PromptsRefreshPostResponse
from ..types.prompts_sources_post_response import PromptsSourcesPostResponse
from .raw_client import AsyncRawPromptsClient, RawPromptsClient
from .types.prompts_sources_post_request_files_item import PromptsSourcesPostRequestFilesItem


OMIT = typing.cast(typing.Any, ...)


class PromptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPromptsClient
        """
        return self._raw_client

    def list_all_available_prompts(
        self,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsGetResponse:
        """
        List all available prompts

        Parameters
        ----------
        source : typing.Optional[str]
            Enumerate a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). An unknown/evicted identifier returns 400 with re-upload guidance. Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prompts.list_all_available_prompts()
        """
        _response = self._raw_client.list_all_available_prompts(
            source=source, repo=repo, path=path, branch=branch, request_options=request_options
        )
        return _response.data

    def force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptsRefreshPostResponse:
        """
        Force-refresh the prompts cache by pulling latest from the git repository

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsRefreshPostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prompts.force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository()
        """
        _response = self._raw_client.force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
            request_options=request_options
        )
        return _response.data

    def ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
        self,
        *,
        source: str,
        files: typing.Sequence[PromptsSourcesPostRequestFilesItem],
        content_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsSourcesPostResponse:
        """
        Ingest (upload) a skill source the server caches and renders via POST /api/v1/prompts/:promptName?source=<identifier> with no git clone (PRD #647)

        Parameters
        ----------
        source : str
            Stable source identifier (e.g., "local:team-dev" or a git URL the server cannot reach)

        files : typing.Sequence[PromptsSourcesPostRequestFilesItem]
            Uploaded files with base64-encoded content

        content_hash : typing.Optional[str]
            CLI-computed content hash (enables future re-upload dedup)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsSourcesPostResponse
            Successful response

        Examples
        --------
        from fern.prompts import PromptsSourcesPostRequestFilesItem

        from fern import FernApi

        client = FernApi()
        client.prompts.ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
            source="source",
            files=[
                PromptsSourcesPostRequestFilesItem(
                    path="path",
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
            source=source, files=files, content_hash=content_hash, request_options=request_options
        )
        return _response.data

    def get_a_prompt_with_rendered_template_arguments(
        self,
        prompt_name: str,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        arguments: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsPromptNamePostResponse:
        """
        Get a prompt with rendered template arguments

        Parameters
        ----------
        prompt_name : str
            Name of the prompt

        source : typing.Optional[str]
            Render a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        arguments : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsPromptNamePostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prompts.get_a_prompt_with_rendered_template_arguments(
            prompt_name="promptName",
        )
        """
        _response = self._raw_client.get_a_prompt_with_rendered_template_arguments(
            prompt_name,
            source=source,
            repo=repo,
            path=path,
            branch=branch,
            arguments=arguments,
            request_options=request_options,
        )
        return _response.data


class AsyncPromptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPromptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPromptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPromptsClient
        """
        return self._raw_client

    async def list_all_available_prompts(
        self,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsGetResponse:
        """
        List all available prompts

        Parameters
        ----------
        source : typing.Optional[str]
            Enumerate a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). An unknown/evicted identifier returns 400 with re-upload guidance. Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prompts.list_all_available_prompts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_available_prompts(
            source=source, repo=repo, path=path, branch=branch, request_options=request_options
        )
        return _response.data

    async def force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PromptsRefreshPostResponse:
        """
        Force-refresh the prompts cache by pulling latest from the git repository

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsRefreshPostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prompts.force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository()


        asyncio.run(main())
        """
        _response = await self._raw_client.force_refresh_the_prompts_cache_by_pulling_latest_from_the_git_repository(
            request_options=request_options
        )
        return _response.data

    async def ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
        self,
        *,
        source: str,
        files: typing.Sequence[PromptsSourcesPostRequestFilesItem],
        content_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsSourcesPostResponse:
        """
        Ingest (upload) a skill source the server caches and renders via POST /api/v1/prompts/:promptName?source=<identifier> with no git clone (PRD #647)

        Parameters
        ----------
        source : str
            Stable source identifier (e.g., "local:team-dev" or a git URL the server cannot reach)

        files : typing.Sequence[PromptsSourcesPostRequestFilesItem]
            Uploaded files with base64-encoded content

        content_hash : typing.Optional[str]
            CLI-computed content hash (enables future re-upload dedup)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsSourcesPostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.prompts import PromptsSourcesPostRequestFilesItem

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prompts.ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
                source="source",
                files=[
                    PromptsSourcesPostRequestFilesItem(
                        path="path",
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest_upload_a_skill_source_the_server_caches_and_renders_via_post_api_v1prompts_prompt_name_source_identifier_with_no_git_clone_prd647(
            source=source, files=files, content_hash=content_hash, request_options=request_options
        )
        return _response.data

    async def get_a_prompt_with_rendered_template_arguments(
        self,
        prompt_name: str,
        *,
        source: typing.Optional[str] = None,
        repo: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        branch: typing.Optional[str] = None,
        arguments: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PromptsPromptNamePostResponse:
        """
        Get a prompt with rendered template arguments

        Parameters
        ----------
        prompt_name : str
            Name of the prompt

        source : typing.Optional[str]
            Render a previously-ingested (CLI-uploaded) source by its identifier with no git clone (PRD #647). Takes precedence over repo/path/branch.

        repo : typing.Optional[str]
            Per-request git repository URL override (PRD #581)

        path : typing.Optional[str]
            Subdirectory within the override repo (PRD #621)

        branch : typing.Optional[str]
            Branch of the override repo (PRD #621)

        arguments : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PromptsPromptNamePostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prompts.get_a_prompt_with_rendered_template_arguments(
                prompt_name="promptName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_prompt_with_rendered_template_arguments(
            prompt_name,
            source=source,
            repo=repo,
            path=path,
            branch=branch,
            arguments=arguments,
            request_options=request_options,
        )
        return _response.data
