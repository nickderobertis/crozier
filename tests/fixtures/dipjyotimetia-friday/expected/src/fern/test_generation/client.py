

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.generate_response import GenerateResponse
from .raw_client import AsyncRawTestGenerationClient, RawTestGenerationClient


OMIT = typing.cast(typing.Any, ...)


class TestGenerationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestGenerationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestGenerationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestGenerationClient
        """
        return self._raw_client

    def generate_tests(
        self,
        *,
        jira_key: typing.Optional[str] = OMIT,
        gh_issue: typing.Optional[str] = OMIT,
        gh_repo: typing.Optional[str] = OMIT,
        confluence_id: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        output: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Parameters
        ----------
        jira_key : typing.Optional[str]

        gh_issue : typing.Optional[str]

        gh_repo : typing.Optional[str]

        confluence_id : typing.Optional[str]

        template : typing.Optional[str]

        output : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_generation.generate_tests()
        """
        _response = self._raw_client.generate_tests(
            jira_key=jira_key,
            gh_issue=gh_issue,
            gh_repo=gh_repo,
            confluence_id=confluence_id,
            template=template,
            output=output,
            request_options=request_options,
        )
        return _response.data


class AsyncTestGenerationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestGenerationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestGenerationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestGenerationClient
        """
        return self._raw_client

    async def generate_tests(
        self,
        *,
        jira_key: typing.Optional[str] = OMIT,
        gh_issue: typing.Optional[str] = OMIT,
        gh_repo: typing.Optional[str] = OMIT,
        confluence_id: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        output: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerateResponse:
        """
        Parameters
        ----------
        jira_key : typing.Optional[str]

        gh_issue : typing.Optional[str]

        gh_repo : typing.Optional[str]

        confluence_id : typing.Optional[str]

        template : typing.Optional[str]

        output : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_generation.generate_tests()


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_tests(
            jira_key=jira_key,
            gh_issue=gh_issue,
            gh_repo=gh_repo,
            confluence_id=confluence_id,
            template=template,
            output=output,
            request_options=request_options,
        )
        return _response.data
