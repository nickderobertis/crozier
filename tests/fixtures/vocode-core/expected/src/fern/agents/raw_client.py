

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agent import Agent
from ..types.agent_page import AgentPage
from ..types.agent_params_actions_item import AgentParamsActionsItem
from ..types.agent_params_deepgram_keywords_value import AgentParamsDeepgramKeywordsValue
from ..types.agent_params_endpointing_sensitivity import AgentParamsEndpointingSensitivity
from ..types.agent_params_ivr_navigation_mode import AgentParamsIvrNavigationMode
from ..types.agent_params_openai_account_connection import AgentParamsOpenaiAccountConnection
from ..types.agent_params_prompt import AgentParamsPrompt
from ..types.agent_params_vector_database import AgentParamsVectorDatabase
from ..types.agent_params_voice import AgentParamsVoice
from ..types.agent_params_webhook import AgentParamsWebhook
from ..types.agent_update_params_actions import AgentUpdateParamsActions
from ..types.agent_update_params_ask_if_human_present_on_idle import AgentUpdateParamsAskIfHumanPresentOnIdle
from ..types.agent_update_params_context_endpoint import AgentUpdateParamsContextEndpoint
from ..types.agent_update_params_conversation_speed import AgentUpdateParamsConversationSpeed
from ..types.agent_update_params_deepgram_keywords import AgentUpdateParamsDeepgramKeywords
from ..types.agent_update_params_endpointing_sensitivity import AgentUpdateParamsEndpointingSensitivity
from ..types.agent_update_params_idle_time_seconds import AgentUpdateParamsIdleTimeSeconds
from ..types.agent_update_params_initial_message import AgentUpdateParamsInitialMessage
from ..types.agent_update_params_initial_message_delay import AgentUpdateParamsInitialMessageDelay
from ..types.agent_update_params_interrupt_sensitivity import AgentUpdateParamsInterruptSensitivity
from ..types.agent_update_params_ivr_navigation_mode import AgentUpdateParamsIvrNavigationMode
from ..types.agent_update_params_language import AgentUpdateParamsLanguage
from ..types.agent_update_params_llm_fallback import AgentUpdateParamsLlmFallback
from ..types.agent_update_params_name import AgentUpdateParamsName
from ..types.agent_update_params_noise_suppression import AgentUpdateParamsNoiseSuppression
from ..types.agent_update_params_openai_account_connection import AgentUpdateParamsOpenaiAccountConnection
from ..types.agent_update_params_openai_model_name_override import AgentUpdateParamsOpenaiModelNameOverride
from ..types.agent_update_params_prompt import AgentUpdateParamsPrompt
from ..types.agent_update_params_run_do_not_call_detection import AgentUpdateParamsRunDoNotCallDetection
from ..types.agent_update_params_vector_database import AgentUpdateParamsVectorDatabase
from ..types.agent_update_params_voice import AgentUpdateParamsVoice
from ..types.agent_update_params_webhook import AgentUpdateParamsWebhook
from ..types.http_validation_error import HttpValidationError
from ..types.internal_llm_fallback import InternalLlmFallback
from ..types.interrupt_sensitivity import InterruptSensitivity
from ..types.language import Language
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_agent(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Agent]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Agent]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_agents(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentPage,
                    parse_obj_as(
                        type_=AgentPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_agent(
        self,
        *,
        prompt: AgentParamsPrompt,
        voice: AgentParamsVoice,
        name: typing.Optional[str] = OMIT,
        language: typing.Optional[Language] = OMIT,
        actions: typing.Optional[typing.Sequence[AgentParamsActionsItem]] = OMIT,
        initial_message: typing.Optional[str] = OMIT,
        webhook: typing.Optional[AgentParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[InterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        noise_suppression: typing.Optional[bool] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[float] = OMIT,
        initial_message_delay: typing.Optional[float] = OMIT,
        openai_model_name_override: typing.Optional[str] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[bool] = OMIT,
        openai_account_connection: typing.Optional[AgentParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        llm_fallback: typing.Optional[InternalLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]] = OMIT,
        idle_time_seconds: typing.Optional[int] = OMIT,
        llm_temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Agent]:
        """
        Parameters
        ----------
        prompt : AgentParamsPrompt

        voice : AgentParamsVoice

        name : typing.Optional[str]

        language : typing.Optional[Language]

        actions : typing.Optional[typing.Sequence[AgentParamsActionsItem]]

        initial_message : typing.Optional[str]

        webhook : typing.Optional[AgentParamsWebhook]

        vector_database : typing.Optional[AgentParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[InterruptSensitivity]

        context_endpoint : typing.Optional[str]

        noise_suppression : typing.Optional[bool]

        endpointing_sensitivity : typing.Optional[AgentParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentParamsIvrNavigationMode]

        conversation_speed : typing.Optional[float]

        initial_message_delay : typing.Optional[float]

        openai_model_name_override : typing.Optional[str]

        ask_if_human_present_on_idle : typing.Optional[bool]

        openai_account_connection : typing.Optional[AgentParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[bool]

        llm_fallback : typing.Optional[InternalLlmFallback]

        deepgram_keywords : typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]]

        idle_time_seconds : typing.Optional[int]

        llm_temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Agent]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/create",
            method="POST",
            json={
                "name": name,
                "prompt": convert_and_respect_annotation_metadata(
                    object_=prompt, annotation=AgentParamsPrompt, direction="write"
                ),
                "language": language,
                "actions": convert_and_respect_annotation_metadata(
                    object_=actions, annotation=typing.Sequence[AgentParamsActionsItem], direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=AgentParamsVoice, direction="write"
                ),
                "initial_message": initial_message,
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=typing.Optional[AgentParamsWebhook], direction="write"
                ),
                "vector_database": convert_and_respect_annotation_metadata(
                    object_=vector_database, annotation=typing.Optional[AgentParamsVectorDatabase], direction="write"
                ),
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": convert_and_respect_annotation_metadata(
                    object_=openai_account_connection,
                    annotation=typing.Optional[AgentParamsOpenaiAccountConnection],
                    direction="write",
                ),
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": convert_and_respect_annotation_metadata(
                    object_=llm_fallback, annotation=typing.Optional[InternalLlmFallback], direction="write"
                ),
                "deepgram_keywords": convert_and_respect_annotation_metadata(
                    object_=deepgram_keywords,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]],
                    direction="write",
                ),
                "idle_time_seconds": idle_time_seconds,
                "llm_temperature": llm_temperature,
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
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_agent(
        self,
        *,
        id: str,
        name: typing.Optional[AgentUpdateParamsName] = OMIT,
        prompt: typing.Optional[AgentUpdateParamsPrompt] = OMIT,
        language: typing.Optional[AgentUpdateParamsLanguage] = OMIT,
        actions: typing.Optional[AgentUpdateParamsActions] = OMIT,
        voice: typing.Optional[AgentUpdateParamsVoice] = OMIT,
        initial_message: typing.Optional[AgentUpdateParamsInitialMessage] = OMIT,
        webhook: typing.Optional[AgentUpdateParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentUpdateParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[AgentUpdateParamsInterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[AgentUpdateParamsContextEndpoint] = OMIT,
        noise_suppression: typing.Optional[AgentUpdateParamsNoiseSuppression] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentUpdateParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentUpdateParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[AgentUpdateParamsConversationSpeed] = OMIT,
        initial_message_delay: typing.Optional[AgentUpdateParamsInitialMessageDelay] = OMIT,
        openai_model_name_override: typing.Optional[AgentUpdateParamsOpenaiModelNameOverride] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle] = OMIT,
        openai_account_connection: typing.Optional[AgentUpdateParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[AgentUpdateParamsRunDoNotCallDetection] = OMIT,
        llm_fallback: typing.Optional[AgentUpdateParamsLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[AgentUpdateParamsDeepgramKeywords] = OMIT,
        idle_time_seconds: typing.Optional[AgentUpdateParamsIdleTimeSeconds] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Agent]:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[AgentUpdateParamsName]

        prompt : typing.Optional[AgentUpdateParamsPrompt]

        language : typing.Optional[AgentUpdateParamsLanguage]

        actions : typing.Optional[AgentUpdateParamsActions]

        voice : typing.Optional[AgentUpdateParamsVoice]

        initial_message : typing.Optional[AgentUpdateParamsInitialMessage]

        webhook : typing.Optional[AgentUpdateParamsWebhook]

        vector_database : typing.Optional[AgentUpdateParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[AgentUpdateParamsInterruptSensitivity]

        context_endpoint : typing.Optional[AgentUpdateParamsContextEndpoint]

        noise_suppression : typing.Optional[AgentUpdateParamsNoiseSuppression]

        endpointing_sensitivity : typing.Optional[AgentUpdateParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentUpdateParamsIvrNavigationMode]

        conversation_speed : typing.Optional[AgentUpdateParamsConversationSpeed]

        initial_message_delay : typing.Optional[AgentUpdateParamsInitialMessageDelay]

        openai_model_name_override : typing.Optional[AgentUpdateParamsOpenaiModelNameOverride]

        ask_if_human_present_on_idle : typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle]

        openai_account_connection : typing.Optional[AgentUpdateParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[AgentUpdateParamsRunDoNotCallDetection]

        llm_fallback : typing.Optional[AgentUpdateParamsLlmFallback]

        deepgram_keywords : typing.Optional[AgentUpdateParamsDeepgramKeywords]

        idle_time_seconds : typing.Optional[AgentUpdateParamsIdleTimeSeconds]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Agent]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "name": convert_and_respect_annotation_metadata(
                    object_=name, annotation=typing.Optional[AgentUpdateParamsName], direction="write"
                ),
                "prompt": convert_and_respect_annotation_metadata(
                    object_=prompt, annotation=AgentUpdateParamsPrompt, direction="write"
                ),
                "language": convert_and_respect_annotation_metadata(
                    object_=language, annotation=AgentUpdateParamsLanguage, direction="write"
                ),
                "actions": convert_and_respect_annotation_metadata(
                    object_=actions, annotation=AgentUpdateParamsActions, direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=AgentUpdateParamsVoice, direction="write"
                ),
                "initial_message": convert_and_respect_annotation_metadata(
                    object_=initial_message,
                    annotation=typing.Optional[AgentUpdateParamsInitialMessage],
                    direction="write",
                ),
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=typing.Optional[AgentUpdateParamsWebhook], direction="write"
                ),
                "vector_database": convert_and_respect_annotation_metadata(
                    object_=vector_database,
                    annotation=typing.Optional[AgentUpdateParamsVectorDatabase],
                    direction="write",
                ),
                "interrupt_sensitivity": convert_and_respect_annotation_metadata(
                    object_=interrupt_sensitivity, annotation=AgentUpdateParamsInterruptSensitivity, direction="write"
                ),
                "context_endpoint": convert_and_respect_annotation_metadata(
                    object_=context_endpoint,
                    annotation=typing.Optional[AgentUpdateParamsContextEndpoint],
                    direction="write",
                ),
                "noise_suppression": convert_and_respect_annotation_metadata(
                    object_=noise_suppression, annotation=AgentUpdateParamsNoiseSuppression, direction="write"
                ),
                "endpointing_sensitivity": convert_and_respect_annotation_metadata(
                    object_=endpointing_sensitivity,
                    annotation=AgentUpdateParamsEndpointingSensitivity,
                    direction="write",
                ),
                "ivr_navigation_mode": convert_and_respect_annotation_metadata(
                    object_=ivr_navigation_mode, annotation=AgentUpdateParamsIvrNavigationMode, direction="write"
                ),
                "conversation_speed": convert_and_respect_annotation_metadata(
                    object_=conversation_speed, annotation=AgentUpdateParamsConversationSpeed, direction="write"
                ),
                "initial_message_delay": convert_and_respect_annotation_metadata(
                    object_=initial_message_delay, annotation=AgentUpdateParamsInitialMessageDelay, direction="write"
                ),
                "openai_model_name_override": convert_and_respect_annotation_metadata(
                    object_=openai_model_name_override,
                    annotation=typing.Optional[AgentUpdateParamsOpenaiModelNameOverride],
                    direction="write",
                ),
                "ask_if_human_present_on_idle": convert_and_respect_annotation_metadata(
                    object_=ask_if_human_present_on_idle,
                    annotation=AgentUpdateParamsAskIfHumanPresentOnIdle,
                    direction="write",
                ),
                "openai_account_connection": convert_and_respect_annotation_metadata(
                    object_=openai_account_connection,
                    annotation=typing.Optional[AgentUpdateParamsOpenaiAccountConnection],
                    direction="write",
                ),
                "run_do_not_call_detection": convert_and_respect_annotation_metadata(
                    object_=run_do_not_call_detection,
                    annotation=AgentUpdateParamsRunDoNotCallDetection,
                    direction="write",
                ),
                "llm_fallback": convert_and_respect_annotation_metadata(
                    object_=llm_fallback, annotation=typing.Optional[AgentUpdateParamsLlmFallback], direction="write"
                ),
                "deepgram_keywords": convert_and_respect_annotation_metadata(
                    object_=deepgram_keywords,
                    annotation=typing.Optional[AgentUpdateParamsDeepgramKeywords],
                    direction="write",
                ),
                "idle_time_seconds": convert_and_respect_annotation_metadata(
                    object_=idle_time_seconds,
                    annotation=typing.Optional[AgentUpdateParamsIdleTimeSeconds],
                    direction="write",
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
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_agent(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Agent]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Agent]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_agents(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentPage,
                    parse_obj_as(
                        type_=AgentPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_agent(
        self,
        *,
        prompt: AgentParamsPrompt,
        voice: AgentParamsVoice,
        name: typing.Optional[str] = OMIT,
        language: typing.Optional[Language] = OMIT,
        actions: typing.Optional[typing.Sequence[AgentParamsActionsItem]] = OMIT,
        initial_message: typing.Optional[str] = OMIT,
        webhook: typing.Optional[AgentParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[InterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[str] = OMIT,
        noise_suppression: typing.Optional[bool] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[float] = OMIT,
        initial_message_delay: typing.Optional[float] = OMIT,
        openai_model_name_override: typing.Optional[str] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[bool] = OMIT,
        openai_account_connection: typing.Optional[AgentParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        llm_fallback: typing.Optional[InternalLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]] = OMIT,
        idle_time_seconds: typing.Optional[int] = OMIT,
        llm_temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Agent]:
        """
        Parameters
        ----------
        prompt : AgentParamsPrompt

        voice : AgentParamsVoice

        name : typing.Optional[str]

        language : typing.Optional[Language]

        actions : typing.Optional[typing.Sequence[AgentParamsActionsItem]]

        initial_message : typing.Optional[str]

        webhook : typing.Optional[AgentParamsWebhook]

        vector_database : typing.Optional[AgentParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[InterruptSensitivity]

        context_endpoint : typing.Optional[str]

        noise_suppression : typing.Optional[bool]

        endpointing_sensitivity : typing.Optional[AgentParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentParamsIvrNavigationMode]

        conversation_speed : typing.Optional[float]

        initial_message_delay : typing.Optional[float]

        openai_model_name_override : typing.Optional[str]

        ask_if_human_present_on_idle : typing.Optional[bool]

        openai_account_connection : typing.Optional[AgentParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[bool]

        llm_fallback : typing.Optional[InternalLlmFallback]

        deepgram_keywords : typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]]

        idle_time_seconds : typing.Optional[int]

        llm_temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Agent]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/create",
            method="POST",
            json={
                "name": name,
                "prompt": convert_and_respect_annotation_metadata(
                    object_=prompt, annotation=AgentParamsPrompt, direction="write"
                ),
                "language": language,
                "actions": convert_and_respect_annotation_metadata(
                    object_=actions, annotation=typing.Sequence[AgentParamsActionsItem], direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=AgentParamsVoice, direction="write"
                ),
                "initial_message": initial_message,
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=typing.Optional[AgentParamsWebhook], direction="write"
                ),
                "vector_database": convert_and_respect_annotation_metadata(
                    object_=vector_database, annotation=typing.Optional[AgentParamsVectorDatabase], direction="write"
                ),
                "interrupt_sensitivity": interrupt_sensitivity,
                "context_endpoint": context_endpoint,
                "noise_suppression": noise_suppression,
                "endpointing_sensitivity": endpointing_sensitivity,
                "ivr_navigation_mode": ivr_navigation_mode,
                "conversation_speed": conversation_speed,
                "initial_message_delay": initial_message_delay,
                "openai_model_name_override": openai_model_name_override,
                "ask_if_human_present_on_idle": ask_if_human_present_on_idle,
                "openai_account_connection": convert_and_respect_annotation_metadata(
                    object_=openai_account_connection,
                    annotation=typing.Optional[AgentParamsOpenaiAccountConnection],
                    direction="write",
                ),
                "run_do_not_call_detection": run_do_not_call_detection,
                "llm_fallback": convert_and_respect_annotation_metadata(
                    object_=llm_fallback, annotation=typing.Optional[InternalLlmFallback], direction="write"
                ),
                "deepgram_keywords": convert_and_respect_annotation_metadata(
                    object_=deepgram_keywords,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[AgentParamsDeepgramKeywordsValue]]],
                    direction="write",
                ),
                "idle_time_seconds": idle_time_seconds,
                "llm_temperature": llm_temperature,
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
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_agent(
        self,
        *,
        id: str,
        name: typing.Optional[AgentUpdateParamsName] = OMIT,
        prompt: typing.Optional[AgentUpdateParamsPrompt] = OMIT,
        language: typing.Optional[AgentUpdateParamsLanguage] = OMIT,
        actions: typing.Optional[AgentUpdateParamsActions] = OMIT,
        voice: typing.Optional[AgentUpdateParamsVoice] = OMIT,
        initial_message: typing.Optional[AgentUpdateParamsInitialMessage] = OMIT,
        webhook: typing.Optional[AgentUpdateParamsWebhook] = OMIT,
        vector_database: typing.Optional[AgentUpdateParamsVectorDatabase] = OMIT,
        interrupt_sensitivity: typing.Optional[AgentUpdateParamsInterruptSensitivity] = OMIT,
        context_endpoint: typing.Optional[AgentUpdateParamsContextEndpoint] = OMIT,
        noise_suppression: typing.Optional[AgentUpdateParamsNoiseSuppression] = OMIT,
        endpointing_sensitivity: typing.Optional[AgentUpdateParamsEndpointingSensitivity] = OMIT,
        ivr_navigation_mode: typing.Optional[AgentUpdateParamsIvrNavigationMode] = OMIT,
        conversation_speed: typing.Optional[AgentUpdateParamsConversationSpeed] = OMIT,
        initial_message_delay: typing.Optional[AgentUpdateParamsInitialMessageDelay] = OMIT,
        openai_model_name_override: typing.Optional[AgentUpdateParamsOpenaiModelNameOverride] = OMIT,
        ask_if_human_present_on_idle: typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle] = OMIT,
        openai_account_connection: typing.Optional[AgentUpdateParamsOpenaiAccountConnection] = OMIT,
        run_do_not_call_detection: typing.Optional[AgentUpdateParamsRunDoNotCallDetection] = OMIT,
        llm_fallback: typing.Optional[AgentUpdateParamsLlmFallback] = OMIT,
        deepgram_keywords: typing.Optional[AgentUpdateParamsDeepgramKeywords] = OMIT,
        idle_time_seconds: typing.Optional[AgentUpdateParamsIdleTimeSeconds] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Agent]:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[AgentUpdateParamsName]

        prompt : typing.Optional[AgentUpdateParamsPrompt]

        language : typing.Optional[AgentUpdateParamsLanguage]

        actions : typing.Optional[AgentUpdateParamsActions]

        voice : typing.Optional[AgentUpdateParamsVoice]

        initial_message : typing.Optional[AgentUpdateParamsInitialMessage]

        webhook : typing.Optional[AgentUpdateParamsWebhook]

        vector_database : typing.Optional[AgentUpdateParamsVectorDatabase]

        interrupt_sensitivity : typing.Optional[AgentUpdateParamsInterruptSensitivity]

        context_endpoint : typing.Optional[AgentUpdateParamsContextEndpoint]

        noise_suppression : typing.Optional[AgentUpdateParamsNoiseSuppression]

        endpointing_sensitivity : typing.Optional[AgentUpdateParamsEndpointingSensitivity]

        ivr_navigation_mode : typing.Optional[AgentUpdateParamsIvrNavigationMode]

        conversation_speed : typing.Optional[AgentUpdateParamsConversationSpeed]

        initial_message_delay : typing.Optional[AgentUpdateParamsInitialMessageDelay]

        openai_model_name_override : typing.Optional[AgentUpdateParamsOpenaiModelNameOverride]

        ask_if_human_present_on_idle : typing.Optional[AgentUpdateParamsAskIfHumanPresentOnIdle]

        openai_account_connection : typing.Optional[AgentUpdateParamsOpenaiAccountConnection]

        run_do_not_call_detection : typing.Optional[AgentUpdateParamsRunDoNotCallDetection]

        llm_fallback : typing.Optional[AgentUpdateParamsLlmFallback]

        deepgram_keywords : typing.Optional[AgentUpdateParamsDeepgramKeywords]

        idle_time_seconds : typing.Optional[AgentUpdateParamsIdleTimeSeconds]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Agent]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "name": convert_and_respect_annotation_metadata(
                    object_=name, annotation=typing.Optional[AgentUpdateParamsName], direction="write"
                ),
                "prompt": convert_and_respect_annotation_metadata(
                    object_=prompt, annotation=AgentUpdateParamsPrompt, direction="write"
                ),
                "language": convert_and_respect_annotation_metadata(
                    object_=language, annotation=AgentUpdateParamsLanguage, direction="write"
                ),
                "actions": convert_and_respect_annotation_metadata(
                    object_=actions, annotation=AgentUpdateParamsActions, direction="write"
                ),
                "voice": convert_and_respect_annotation_metadata(
                    object_=voice, annotation=AgentUpdateParamsVoice, direction="write"
                ),
                "initial_message": convert_and_respect_annotation_metadata(
                    object_=initial_message,
                    annotation=typing.Optional[AgentUpdateParamsInitialMessage],
                    direction="write",
                ),
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=typing.Optional[AgentUpdateParamsWebhook], direction="write"
                ),
                "vector_database": convert_and_respect_annotation_metadata(
                    object_=vector_database,
                    annotation=typing.Optional[AgentUpdateParamsVectorDatabase],
                    direction="write",
                ),
                "interrupt_sensitivity": convert_and_respect_annotation_metadata(
                    object_=interrupt_sensitivity, annotation=AgentUpdateParamsInterruptSensitivity, direction="write"
                ),
                "context_endpoint": convert_and_respect_annotation_metadata(
                    object_=context_endpoint,
                    annotation=typing.Optional[AgentUpdateParamsContextEndpoint],
                    direction="write",
                ),
                "noise_suppression": convert_and_respect_annotation_metadata(
                    object_=noise_suppression, annotation=AgentUpdateParamsNoiseSuppression, direction="write"
                ),
                "endpointing_sensitivity": convert_and_respect_annotation_metadata(
                    object_=endpointing_sensitivity,
                    annotation=AgentUpdateParamsEndpointingSensitivity,
                    direction="write",
                ),
                "ivr_navigation_mode": convert_and_respect_annotation_metadata(
                    object_=ivr_navigation_mode, annotation=AgentUpdateParamsIvrNavigationMode, direction="write"
                ),
                "conversation_speed": convert_and_respect_annotation_metadata(
                    object_=conversation_speed, annotation=AgentUpdateParamsConversationSpeed, direction="write"
                ),
                "initial_message_delay": convert_and_respect_annotation_metadata(
                    object_=initial_message_delay, annotation=AgentUpdateParamsInitialMessageDelay, direction="write"
                ),
                "openai_model_name_override": convert_and_respect_annotation_metadata(
                    object_=openai_model_name_override,
                    annotation=typing.Optional[AgentUpdateParamsOpenaiModelNameOverride],
                    direction="write",
                ),
                "ask_if_human_present_on_idle": convert_and_respect_annotation_metadata(
                    object_=ask_if_human_present_on_idle,
                    annotation=AgentUpdateParamsAskIfHumanPresentOnIdle,
                    direction="write",
                ),
                "openai_account_connection": convert_and_respect_annotation_metadata(
                    object_=openai_account_connection,
                    annotation=typing.Optional[AgentUpdateParamsOpenaiAccountConnection],
                    direction="write",
                ),
                "run_do_not_call_detection": convert_and_respect_annotation_metadata(
                    object_=run_do_not_call_detection,
                    annotation=AgentUpdateParamsRunDoNotCallDetection,
                    direction="write",
                ),
                "llm_fallback": convert_and_respect_annotation_metadata(
                    object_=llm_fallback, annotation=typing.Optional[AgentUpdateParamsLlmFallback], direction="write"
                ),
                "deepgram_keywords": convert_and_respect_annotation_metadata(
                    object_=deepgram_keywords,
                    annotation=typing.Optional[AgentUpdateParamsDeepgramKeywords],
                    direction="write",
                ),
                "idle_time_seconds": convert_and_respect_annotation_metadata(
                    object_=idle_time_seconds,
                    annotation=typing.Optional[AgentUpdateParamsIdleTimeSeconds],
                    direction="write",
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
                    Agent,
                    parse_obj_as(
                        type_=Agent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
