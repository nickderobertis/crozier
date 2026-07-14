

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.rule import Rule
from ..types.rule_section import RuleSection
from .raw_client import AsyncRawRulesClient, RawRulesClient
from .types.get_api_rule_sections_index_request_index import GetApiRuleSectionsIndexRequestIndex
from .types.get_api_rules_index_request_index import GetApiRulesIndexRequestIndex


class RulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRulesClient
        """
        return self._raw_client

    def get_a_rule_section_by_index(
        self, index: GetApiRuleSectionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RuleSection:
        """
        Rule sections represent a sub-heading and text that can be found underneath a rule heading in the SRD.

        Parameters
        ----------
        index : GetApiRuleSectionsIndexRequestIndex
            The `index` of the rule section to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RuleSection
            OK

        Examples
        --------
        from fern.rules import GetApiRuleSectionsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.rules.get_a_rule_section_by_index(
            index=GetApiRuleSectionsIndexRequestIndex.ABILITY_CHECKS,
        )
        """
        _response = self._raw_client.get_a_rule_section_by_index(index, request_options=request_options)
        return _response.data

    def get_a_rule_by_index(
        self, index: GetApiRulesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Rule:
        """
        # Rule

        Rules are pages in the SRD that document the mechanics of Dungeons and Dragons.
        Rules have descriptions which is the text directly underneath the rule heading
        in the SRD. Rules also have subsections for each heading underneath the rule in the SRD.

        Parameters
        ----------
        index : GetApiRulesIndexRequestIndex
            The `index` of the rule to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            OK

        Examples
        --------
        from fern.rules import GetApiRulesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.rules.get_a_rule_by_index(
            index=GetApiRulesIndexRequestIndex.ADVENTURING,
        )
        """
        _response = self._raw_client.get_a_rule_by_index(index, request_options=request_options)
        return _response.data


class AsyncRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRulesClient
        """
        return self._raw_client

    async def get_a_rule_section_by_index(
        self, index: GetApiRuleSectionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RuleSection:
        """
        Rule sections represent a sub-heading and text that can be found underneath a rule heading in the SRD.

        Parameters
        ----------
        index : GetApiRuleSectionsIndexRequestIndex
            The `index` of the rule section to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RuleSection
            OK

        Examples
        --------
        import asyncio

        from fern.rules import GetApiRuleSectionsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.rules.get_a_rule_section_by_index(
                index=GetApiRuleSectionsIndexRequestIndex.ABILITY_CHECKS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_rule_section_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_rule_by_index(
        self, index: GetApiRulesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Rule:
        """
        # Rule

        Rules are pages in the SRD that document the mechanics of Dungeons and Dragons.
        Rules have descriptions which is the text directly underneath the rule heading
        in the SRD. Rules also have subsections for each heading underneath the rule in the SRD.

        Parameters
        ----------
        index : GetApiRulesIndexRequestIndex
            The `index` of the rule to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            OK

        Examples
        --------
        import asyncio

        from fern.rules import GetApiRulesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.rules.get_a_rule_by_index(
                index=GetApiRulesIndexRequestIndex.ADVENTURING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_rule_by_index(index, request_options=request_options)
        return _response.data
