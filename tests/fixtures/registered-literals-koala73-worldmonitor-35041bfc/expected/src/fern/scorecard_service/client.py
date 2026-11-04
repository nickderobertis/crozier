

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_bloc_scorecard_response import GetBlocScorecardResponse
from ..types.get_five_factor_scorecard_response import GetFiveFactorScorecardResponse
from ..types.list_five_factor_scorecards_response import ListFiveFactorScorecardsResponse
from .raw_client import AsyncRawScorecardServiceClient, RawScorecardServiceClient


class ScorecardServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScorecardServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScorecardServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScorecardServiceClient
        """
        return self._raw_client

    def get_five_factor_scorecard(
        self,
        *,
        country_code: str,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFiveFactorScorecardResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code for the requested scorecard.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFiveFactorScorecardResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )
        client.scorecard_service.get_five_factor_scorecard(
            country_code="US",
            jmespath="keys(@)",
        )
        """
        _response = self._raw_client.get_five_factor_scorecard(
            country_code=country_code, jmespath=jmespath, request_options=request_options
        )
        return _response.data

    def list_five_factor_scorecards(
        self, *, jmespath: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFiveFactorScorecardsResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFiveFactorScorecardsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )
        client.scorecard_service.list_five_factor_scorecards(
            jmespath="keys(@)",
        )
        """
        _response = self._raw_client.list_five_factor_scorecards(jmespath=jmespath, request_options=request_options)
        return _response.data

    def get_bloc_scorecard(
        self,
        *,
        preset: typing.Optional[str] = None,
        members: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBlocScorecardResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        preset : typing.Optional[str]
            Official bloc preset: USMCA, EU27, BRICS, GCC, ASEAN, or NATO. Values are case-sensitive. Omit when members is provided.

        members : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Custom list of 2-30 unique uppercase ISO 3166-1 alpha-2 members. Provide either preset or members; do not provide both.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlocScorecardResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )
        client.scorecard_service.get_bloc_scorecard(
            preset="NATO",
            jmespath="keys(@)",
        )
        """
        _response = self._raw_client.get_bloc_scorecard(
            preset=preset, members=members, jmespath=jmespath, request_options=request_options
        )
        return _response.data


class AsyncScorecardServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScorecardServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScorecardServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScorecardServiceClient
        """
        return self._raw_client

    async def get_five_factor_scorecard(
        self,
        *,
        country_code: str,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFiveFactorScorecardResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code for the requested scorecard.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFiveFactorScorecardResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.scorecard_service.get_five_factor_scorecard(
                country_code="US",
                jmespath="keys(@)",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_five_factor_scorecard(
            country_code=country_code, jmespath=jmespath, request_options=request_options
        )
        return _response.data

    async def list_five_factor_scorecards(
        self, *, jmespath: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFiveFactorScorecardsResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFiveFactorScorecardsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.scorecard_service.list_five_factor_scorecards(
                jmespath="keys(@)",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_five_factor_scorecards(
            jmespath=jmespath, request_options=request_options
        )
        return _response.data

    async def get_bloc_scorecard(
        self,
        *,
        preset: typing.Optional[str] = None,
        members: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetBlocScorecardResponse:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        preset : typing.Optional[str]
            Official bloc preset: USMCA, EU27, BRICS, GCC, ASEAN, or NATO. Values are case-sensitive. Omit when members is provided.

        members : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Custom list of 2-30 unique uppercase ISO 3166-1 alpha-2 members. Provide either preset or members; do not provide both.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlocScorecardResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.scorecard_service.get_bloc_scorecard(
                preset="NATO",
                jmespath="keys(@)",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bloc_scorecard(
            preset=preset, members=members, jmespath=jmespath, request_options=request_options
        )
        return _response.data
