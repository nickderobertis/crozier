

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.rule import Rule
from ..types.rule_section import RuleSection
from .types.get_api_rule_sections_index_request_index import GetApiRuleSectionsIndexRequestIndex
from .types.get_api_rules_index_request_index import GetApiRulesIndexRequestIndex


class RawRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_rule_section_by_index(
        self, index: GetApiRuleSectionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RuleSection]:
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
        HttpResponse[RuleSection]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/rule-sections/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RuleSection,
                    parse_obj_as(
                        type_=RuleSection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_rule_by_index(
        self, index: GetApiRulesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Rule]:
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
        HttpResponse[Rule]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/rules/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_rule_section_by_index(
        self, index: GetApiRuleSectionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RuleSection]:
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
        AsyncHttpResponse[RuleSection]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/rule-sections/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RuleSection,
                    parse_obj_as(
                        type_=RuleSection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_rule_by_index(
        self, index: GetApiRulesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Rule]:
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
        AsyncHttpResponse[Rule]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/rules/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
