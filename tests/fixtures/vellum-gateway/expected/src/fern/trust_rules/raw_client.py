

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTrustRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        origin: typing.Optional[str] = None,
        tool: typing.Optional[str] = None,
        include_deleted: typing.Optional[str] = None,
        include_all: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrustRulesListResponse]:
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
        HttpResponse[TrustRulesListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trust-rules",
            method="GET",
            params={
                "origin": origin,
                "tool": tool,
                "include_deleted": include_deleted,
                "include_all": include_all,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRulesListResponse,
                    parse_obj_as(
                        type_=TrustRulesListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trust_rule_create(
        self,
        *,
        tool: str,
        pattern: str,
        risk: TrustRuleCreateRequestRisk,
        description: str,
        scope: typing.Optional[TrustRuleCreateRequestScope] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrustRuleCreateResponse]:
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
        HttpResponse[TrustRuleCreateResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trust-rules",
            method="POST",
            json={
                "tool": tool,
                "pattern": pattern,
                "risk": risk,
                "description": description,
                "scope": scope,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleCreateResponse,
                    parse_obj_as(
                        type_=TrustRuleCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TrustRuleSuggestResponse]:
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
        HttpResponse[TrustRuleSuggestResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trust-rules/suggest",
            method="POST",
            json={
                "tool": tool,
                "command": command,
                "riskAssessment": convert_and_respect_annotation_metadata(
                    object_=risk_assessment, annotation=TrustRuleSuggestRequestRiskAssessment, direction="write"
                ),
                "scopeOptions": convert_and_respect_annotation_metadata(
                    object_=scope_options,
                    annotation=typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem],
                    direction="write",
                ),
                "directoryScopeOptions": convert_and_respect_annotation_metadata(
                    object_=directory_scope_options,
                    annotation=typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem],
                    direction="write",
                ),
                "intent": intent,
                "existingRule": convert_and_respect_annotation_metadata(
                    object_=existing_rule, annotation=TrustRuleSuggestRequestExistingRule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleSuggestResponse,
                    parse_obj_as(
                        type_=TrustRuleSuggestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trust_rule_delete(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrustRuleDeleteResponse]:
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
        HttpResponse[TrustRuleDeleteResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleDeleteResponse,
                    parse_obj_as(
                        type_=TrustRuleDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trust_rule_update(
        self,
        rule_id: str,
        *,
        risk: typing.Optional[TrustRuleUpdateRequestRisk] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrustRuleUpdateResponse]:
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
        HttpResponse[TrustRuleUpdateResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}",
            method="PATCH",
            json={
                "risk": risk,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleUpdateResponse,
                    parse_obj_as(
                        type_=TrustRuleUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trust_rule_reset(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrustRuleResetResponse]:
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
        HttpResponse[TrustRuleResetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}/reset",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleResetResponse,
                    parse_obj_as(
                        type_=TrustRuleResetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTrustRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        origin: typing.Optional[str] = None,
        tool: typing.Optional[str] = None,
        include_deleted: typing.Optional[str] = None,
        include_all: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrustRulesListResponse]:
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
        AsyncHttpResponse[TrustRulesListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trust-rules",
            method="GET",
            params={
                "origin": origin,
                "tool": tool,
                "include_deleted": include_deleted,
                "include_all": include_all,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRulesListResponse,
                    parse_obj_as(
                        type_=TrustRulesListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trust_rule_create(
        self,
        *,
        tool: str,
        pattern: str,
        risk: TrustRuleCreateRequestRisk,
        description: str,
        scope: typing.Optional[TrustRuleCreateRequestScope] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrustRuleCreateResponse]:
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
        AsyncHttpResponse[TrustRuleCreateResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trust-rules",
            method="POST",
            json={
                "tool": tool,
                "pattern": pattern,
                "risk": risk,
                "description": description,
                "scope": scope,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleCreateResponse,
                    parse_obj_as(
                        type_=TrustRuleCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TrustRuleSuggestResponse]:
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
        AsyncHttpResponse[TrustRuleSuggestResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trust-rules/suggest",
            method="POST",
            json={
                "tool": tool,
                "command": command,
                "riskAssessment": convert_and_respect_annotation_metadata(
                    object_=risk_assessment, annotation=TrustRuleSuggestRequestRiskAssessment, direction="write"
                ),
                "scopeOptions": convert_and_respect_annotation_metadata(
                    object_=scope_options,
                    annotation=typing.Sequence[TrustRuleSuggestRequestScopeOptionsItem],
                    direction="write",
                ),
                "directoryScopeOptions": convert_and_respect_annotation_metadata(
                    object_=directory_scope_options,
                    annotation=typing.Sequence[TrustRuleSuggestRequestDirectoryScopeOptionsItem],
                    direction="write",
                ),
                "intent": intent,
                "existingRule": convert_and_respect_annotation_metadata(
                    object_=existing_rule, annotation=TrustRuleSuggestRequestExistingRule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleSuggestResponse,
                    parse_obj_as(
                        type_=TrustRuleSuggestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trust_rule_delete(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrustRuleDeleteResponse]:
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
        AsyncHttpResponse[TrustRuleDeleteResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleDeleteResponse,
                    parse_obj_as(
                        type_=TrustRuleDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trust_rule_update(
        self,
        rule_id: str,
        *,
        risk: typing.Optional[TrustRuleUpdateRequestRisk] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrustRuleUpdateResponse]:
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
        AsyncHttpResponse[TrustRuleUpdateResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}",
            method="PATCH",
            json={
                "risk": risk,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleUpdateResponse,
                    parse_obj_as(
                        type_=TrustRuleUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trust_rule_reset(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrustRuleResetResponse]:
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
        AsyncHttpResponse[TrustRuleResetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/trust-rules/{encode_path_param(rule_id)}/reset",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrustRuleResetResponse,
                    parse_obj_as(
                        type_=TrustRuleResetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
