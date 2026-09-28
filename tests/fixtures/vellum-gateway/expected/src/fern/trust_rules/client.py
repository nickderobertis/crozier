

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTrustRulesClient, RawTrustRulesClient
from .types.trust_rule_create_request_risk import TrustRuleCreateRequestRisk
from .types.trust_rule_create_request_scope import TrustRuleCreateRequestScope
from .types.trust_rule_create_response import TrustRuleCreateResponse
from .types.trust_rule_delete_response import TrustRuleDeleteResponse
from .types.trust_rule_reset_response import TrustRuleResetResponse
from .types.trust_rule_suggest_request_directory_scope_options_item import (
    TrustRuleSuggestRequestDirectoryScopeOptionsItem,
)
from .types.trust_rule_suggest_request_existing_rule import TrustRuleSuggestRequestExistingRule
from .types.trust_rule_suggest_request_intent import TrustRuleSuggestRequestIntent
from .types.trust_rule_suggest_request_risk_assessment import TrustRuleSuggestRequestRiskAssessment
from .types.trust_rule_suggest_request_scope_options_item import TrustRuleSuggestRequestScopeOptionsItem
from .types.trust_rule_suggest_response import TrustRuleSuggestResponse
from .types.trust_rule_update_request_risk import TrustRuleUpdateRequestRisk
from .types.trust_rule_update_response import TrustRuleUpdateResponse
from .types.trust_rules_list_response import TrustRulesListResponse


OMIT = typing.cast(typing.Any, ...)


class TrustRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrustRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrustRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrustRulesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        origin: typing.Optional[str] = None,
        tool: typing.Optional[str] = None,
        include_deleted: typing.Optional[str] = None,
        include_all: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRulesListResponse:
        """
        Returns trust rules, filtered to user-relevant rules by default. Pass include_all=true for the full set or origin/tool to filter.

        Parameters
        ----------
        origin : typing.Optional[str]
            Filter by origin (default | user_defined)

        tool : typing.Optional[str]
            Filter by tool name

        include_deleted : typing.Optional[str]
            "true" to include soft-deleted rules

        include_all : typing.Optional[str]
            "true" to disable the user-relevant filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRulesListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trust_rules.list()
        """
        _response = self._raw_client.list(
            origin=origin,
            tool=tool,
            include_deleted=include_deleted,
            include_all=include_all,
            request_options=request_options,
        )
        return _response.data

    def trust_rule_create(
        self,
        *,
        tool: str,
        pattern: str,
        risk: TrustRuleCreateRequestRisk,
        description: str,
        scope: typing.Optional[TrustRuleCreateRequestScope] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleCreateResponse:
        """
        Parameters
        ----------
        tool : str

        pattern : str

        risk : TrustRuleCreateRequestRisk

        description : str

        scope : typing.Optional[TrustRuleCreateRequestScope]
            Compatibility field. Trust rules apply workspace-wide: the engine matches on (tool, pattern) only, so a narrower scope cannot be honored and any value other than "everywhere" is rejected rather than stored broader than the consent it records.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleCreateResponse
            Successful response

        Examples
        --------
        from fern.trust_rules import TrustRuleCreateRequestRisk

        from fern import FernApi

        client = FernApi()
        client.trust_rules.trust_rule_create(
            tool="tool",
            pattern="pattern",
            risk=TrustRuleCreateRequestRisk.LOW,
            description="description",
        )
        """
        _response = self._raw_client.trust_rule_create(
            tool=tool, pattern=pattern, risk=risk, description=description, scope=scope, request_options=request_options
        )
        return _response.data

    def trust_rule_suggest(
        self,
        *,
        tool: str,
        command: str,
        risk_assessment: TrustRuleSuggestRequestRiskAssessment,
        scope_options: typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem],
        intent: TrustRuleSuggestRequestIntent,
        directory_scope_options: typing.Optional[
            typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem]
        ] = OMIT,
        existing_rule: typing.Optional[TrustRuleSuggestRequestExistingRule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleSuggestResponse:
        """
        LLM-backed suggestion for a rule matching the given tool invocation. Returns 503 when the daemon suggestion relay is unavailable.

        Parameters
        ----------
        tool : str

        command : str

        risk_assessment : TrustRuleSuggestRequestRiskAssessment

        scope_options : typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem]

        intent : TrustRuleSuggestRequestIntent

        directory_scope_options : typing.Optional[typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem]]

        existing_rule : typing.Optional[TrustRuleSuggestRequestExistingRule]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleSuggestResponse
            Successful response

        Examples
        --------
        from fern.trust_rules import (
            TrustRuleSuggestRequestIntent,
            TrustRuleSuggestRequestRiskAssessment,
            TrustRuleSuggestRequestScopeOptionsItem,
        )

        from fern import FernApi

        client = FernApi()
        client.trust_rules.trust_rule_suggest(
            tool="tool",
            command="command",
            risk_assessment=TrustRuleSuggestRequestRiskAssessment(
                risk="risk",
                reasoning="reasoning",
                reason_description="reasonDescription",
            ),
            scope_options=[
                TrustRuleSuggestRequestScopeOptionsItem(
                    pattern="pattern",
                    label="label",
                )
            ],
            intent=TrustRuleSuggestRequestIntent.AUTO_APPROVE,
        )
        """
        _response = self._raw_client.trust_rule_suggest(
            tool=tool,
            command=command,
            risk_assessment=risk_assessment,
            scope_options=scope_options,
            intent=intent,
            directory_scope_options=directory_scope_options,
            existing_rule=existing_rule,
            request_options=request_options,
        )
        return _response.data

    def trust_rule_delete(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustRuleDeleteResponse:
        """
        Soft-deletes the rule. Default-origin rules can be reset later.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trust_rules.trust_rule_delete(
            rule_id="rule_id",
        )
        """
        _response = self._raw_client.trust_rule_delete(rule_id, request_options=request_options)
        return _response.data

    def trust_rule_update(
        self,
        rule_id: str,
        *,
        risk: typing.Optional[TrustRuleUpdateRequestRisk] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleUpdateResponse:
        """
        Updates risk and/or description. Updating a default-origin rule marks it userModified.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        risk : typing.Optional[TrustRuleUpdateRequestRisk]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleUpdateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trust_rules.trust_rule_update(
            rule_id="rule_id",
        )
        """
        _response = self._raw_client.trust_rule_update(
            rule_id, risk=risk, description=description, request_options=request_options
        )
        return _response.data

    def trust_rule_reset(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustRuleResetResponse:
        """
        Restores a default-origin rule to its registry risk and description, clearing userModified and deleted.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleResetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trust_rules.trust_rule_reset(
            rule_id="rule_id",
        )
        """
        _response = self._raw_client.trust_rule_reset(rule_id, request_options=request_options)
        return _response.data


class AsyncTrustRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrustRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrustRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrustRulesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        origin: typing.Optional[str] = None,
        tool: typing.Optional[str] = None,
        include_deleted: typing.Optional[str] = None,
        include_all: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRulesListResponse:
        """
        Returns trust rules, filtered to user-relevant rules by default. Pass include_all=true for the full set or origin/tool to filter.

        Parameters
        ----------
        origin : typing.Optional[str]
            Filter by origin (default | user_defined)

        tool : typing.Optional[str]
            Filter by tool name

        include_deleted : typing.Optional[str]
            "true" to include soft-deleted rules

        include_all : typing.Optional[str]
            "true" to disable the user-relevant filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRulesListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            origin=origin,
            tool=tool,
            include_deleted=include_deleted,
            include_all=include_all,
            request_options=request_options,
        )
        return _response.data

    async def trust_rule_create(
        self,
        *,
        tool: str,
        pattern: str,
        risk: TrustRuleCreateRequestRisk,
        description: str,
        scope: typing.Optional[TrustRuleCreateRequestScope] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleCreateResponse:
        """
        Parameters
        ----------
        tool : str

        pattern : str

        risk : TrustRuleCreateRequestRisk

        description : str

        scope : typing.Optional[TrustRuleCreateRequestScope]
            Compatibility field. Trust rules apply workspace-wide: the engine matches on (tool, pattern) only, so a narrower scope cannot be honored and any value other than "everywhere" is rejected rather than stored broader than the consent it records.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.trust_rules import TrustRuleCreateRequestRisk

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.trust_rule_create(
                tool="tool",
                pattern="pattern",
                risk=TrustRuleCreateRequestRisk.LOW,
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trust_rule_create(
            tool=tool, pattern=pattern, risk=risk, description=description, scope=scope, request_options=request_options
        )
        return _response.data

    async def trust_rule_suggest(
        self,
        *,
        tool: str,
        command: str,
        risk_assessment: TrustRuleSuggestRequestRiskAssessment,
        scope_options: typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem],
        intent: TrustRuleSuggestRequestIntent,
        directory_scope_options: typing.Optional[
            typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem]
        ] = OMIT,
        existing_rule: typing.Optional[TrustRuleSuggestRequestExistingRule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleSuggestResponse:
        """
        LLM-backed suggestion for a rule matching the given tool invocation. Returns 503 when the daemon suggestion relay is unavailable.

        Parameters
        ----------
        tool : str

        command : str

        risk_assessment : TrustRuleSuggestRequestRiskAssessment

        scope_options : typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem]

        intent : TrustRuleSuggestRequestIntent

        directory_scope_options : typing.Optional[typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem]]

        existing_rule : typing.Optional[TrustRuleSuggestRequestExistingRule]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleSuggestResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.trust_rules import (
            TrustRuleSuggestRequestIntent,
            TrustRuleSuggestRequestRiskAssessment,
            TrustRuleSuggestRequestScopeOptionsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.trust_rule_suggest(
                tool="tool",
                command="command",
                risk_assessment=TrustRuleSuggestRequestRiskAssessment(
                    risk="risk",
                    reasoning="reasoning",
                    reason_description="reasonDescription",
                ),
                scope_options=[
                    TrustRuleSuggestRequestScopeOptionsItem(
                        pattern="pattern",
                        label="label",
                    )
                ],
                intent=TrustRuleSuggestRequestIntent.AUTO_APPROVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trust_rule_suggest(
            tool=tool,
            command=command,
            risk_assessment=risk_assessment,
            scope_options=scope_options,
            intent=intent,
            directory_scope_options=directory_scope_options,
            existing_rule=existing_rule,
            request_options=request_options,
        )
        return _response.data

    async def trust_rule_delete(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustRuleDeleteResponse:
        """
        Soft-deletes the rule. Default-origin rules can be reset later.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.trust_rule_delete(
                rule_id="rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trust_rule_delete(rule_id, request_options=request_options)
        return _response.data

    async def trust_rule_update(
        self,
        rule_id: str,
        *,
        risk: typing.Optional[TrustRuleUpdateRequestRisk] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrustRuleUpdateResponse:
        """
        Updates risk and/or description. Updating a default-origin rule marks it userModified.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        risk : typing.Optional[TrustRuleUpdateRequestRisk]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.trust_rule_update(
                rule_id="rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trust_rule_update(
            rule_id, risk=risk, description=description, request_options=request_options
        )
        return _response.data

    async def trust_rule_reset(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrustRuleResetResponse:
        """
        Restores a default-origin rule to its registry risk and description, clearing userModified and deleted.

        Parameters
        ----------
        rule_id : str
            The trust rule id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrustRuleResetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trust_rules.trust_rule_reset(
                rule_id="rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trust_rule_reset(rule_id, request_options=request_options)
        return _response.data
