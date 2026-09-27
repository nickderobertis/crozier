

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLlmClient, RawLlmClient
from .types.get_mockserver_llm_optimisation_report_request_format import GetMockserverLlmOptimisationReportRequestFormat
from .types.put_mockserver_llm_diff_runs_request_after import PutMockserverLlmDiffRunsRequestAfter
from .types.put_mockserver_llm_diff_runs_request_before import PutMockserverLlmDiffRunsRequestBefore


OMIT = typing.cast(typing.Any, ...)


class LlmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLlmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLlmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLlmClient
        """
        return self._raw_client

    def retrieve_the_llm_optimisation_report(
        self,
        *,
        format: typing.Optional[GetMockserverLlmOptimisationReportRequestFormat] = None,
        session: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Analyses captured LLM traffic and reports optimisation signals (cost, latency, token usage, prompt and response characteristics) with an overall verdict. The report can also be emitted in evaluation-dataset formats for downstream tooling. An empty capture is a 200 with an empty report, not an error.

        Parameters
        ----------
        format : typing.Optional[GetMockserverLlmOptimisationReportRequestFormat]
            output format; defaults to json. The dataset formats also accept the aliases `evals` (openai-evals) and `finetune` (fine-tune), and underscores in place of hyphens.

        session : typing.Optional[str]
            restrict the report to a single captured session

        host : typing.Optional[str]
            restrict the report to a single upstream host

        provider : typing.Optional[str]
            restrict the report to a single LLM provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            optimisation report returned in the requested format

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.llm.retrieve_the_llm_optimisation_report()
        """
        _response = self._raw_client.retrieve_the_llm_optimisation_report(
            format=format, session=session, host=host, provider=provider, request_options=request_options
        )
        return _response.data

    def diff_two_captured_llm_agent_runs(
        self,
        *,
        before: typing.Optional[PutMockserverLlmDiffRunsRequestBefore] = OMIT,
        after: typing.Optional[PutMockserverLlmDiffRunsRequestAfter] = OMIT,
        normalization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Compares two captured agent runs, each selected by session, host and/or provider, and reports where they diverge. Normalization options control which incidental differences are ignored before comparing. The request body is optional — an empty body is treated as an empty filter on both sides.

        Parameters
        ----------
        before : typing.Optional[PutMockserverLlmDiffRunsRequestBefore]

        after : typing.Optional[PutMockserverLlmDiffRunsRequestAfter]

        normalization : typing.Optional[typing.Dict[str, typing.Any]]
            options controlling which incidental differences are ignored

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            diff of the two runs returned

        Examples
        --------
        from fern.llm import (
            PutMockserverLlmDiffRunsRequestAfter,
            PutMockserverLlmDiffRunsRequestBefore,
        )

        from fern import FernApi

        client = FernApi()
        client.llm.diff_two_captured_llm_agent_runs(
            before=PutMockserverLlmDiffRunsRequestBefore(
                session="run-1",
            ),
            after=PutMockserverLlmDiffRunsRequestAfter(
                session="run-2",
            ),
        )
        """
        _response = self._raw_client.diff_two_captured_llm_agent_runs(
            before=before, after=after, normalization=normalization, request_options=request_options
        )
        return _response.data


class AsyncLlmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLlmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLlmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLlmClient
        """
        return self._raw_client

    async def retrieve_the_llm_optimisation_report(
        self,
        *,
        format: typing.Optional[GetMockserverLlmOptimisationReportRequestFormat] = None,
        session: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Analyses captured LLM traffic and reports optimisation signals (cost, latency, token usage, prompt and response characteristics) with an overall verdict. The report can also be emitted in evaluation-dataset formats for downstream tooling. An empty capture is a 200 with an empty report, not an error.

        Parameters
        ----------
        format : typing.Optional[GetMockserverLlmOptimisationReportRequestFormat]
            output format; defaults to json. The dataset formats also accept the aliases `evals` (openai-evals) and `finetune` (fine-tune), and underscores in place of hyphens.

        session : typing.Optional[str]
            restrict the report to a single captured session

        host : typing.Optional[str]
            restrict the report to a single upstream host

        provider : typing.Optional[str]
            restrict the report to a single LLM provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            optimisation report returned in the requested format

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.llm.retrieve_the_llm_optimisation_report()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_llm_optimisation_report(
            format=format, session=session, host=host, provider=provider, request_options=request_options
        )
        return _response.data

    async def diff_two_captured_llm_agent_runs(
        self,
        *,
        before: typing.Optional[PutMockserverLlmDiffRunsRequestBefore] = OMIT,
        after: typing.Optional[PutMockserverLlmDiffRunsRequestAfter] = OMIT,
        normalization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Compares two captured agent runs, each selected by session, host and/or provider, and reports where they diverge. Normalization options control which incidental differences are ignored before comparing. The request body is optional — an empty body is treated as an empty filter on both sides.

        Parameters
        ----------
        before : typing.Optional[PutMockserverLlmDiffRunsRequestBefore]

        after : typing.Optional[PutMockserverLlmDiffRunsRequestAfter]

        normalization : typing.Optional[typing.Dict[str, typing.Any]]
            options controlling which incidental differences are ignored

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            diff of the two runs returned

        Examples
        --------
        import asyncio

        from fern.llm import (
            PutMockserverLlmDiffRunsRequestAfter,
            PutMockserverLlmDiffRunsRequestBefore,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.llm.diff_two_captured_llm_agent_runs(
                before=PutMockserverLlmDiffRunsRequestBefore(
                    session="run-1",
                ),
                after=PutMockserverLlmDiffRunsRequestAfter(
                    session="run-2",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diff_two_captured_llm_agent_runs(
            before=before, after=after, normalization=normalization, request_options=request_options
        )
        return _response.data
