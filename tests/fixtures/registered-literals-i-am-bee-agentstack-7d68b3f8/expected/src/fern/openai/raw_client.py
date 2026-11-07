

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
from ..types.chat_completion_audio_param import ChatCompletionAudioParam
from ..types.chat_completion_function_tool_param import ChatCompletionFunctionToolParam
from ..types.chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from ..types.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from ..types.http_validation_error import HttpValidationError
from ..types.open_ai_page_model import OpenAiPageModel
from ..types.openai_types_chat_completion_create_params_function import OpenaiTypesChatCompletionCreateParamsFunction
from ..types.web_search_options import WebSearchOptions
from .types.chat_completion_request_function_call import ChatCompletionRequestFunctionCall
from .types.chat_completion_request_messages_item import ChatCompletionRequestMessagesItem
from .types.chat_completion_request_modalities_item import ChatCompletionRequestModalitiesItem
from .types.chat_completion_request_model import ChatCompletionRequestModel
from .types.chat_completion_request_reasoning_effort import ChatCompletionRequestReasoningEffort
from .types.chat_completion_request_response_format import ChatCompletionRequestResponseFormat
from .types.chat_completion_request_service_tier import ChatCompletionRequestServiceTier
from .types.chat_completion_request_stop import ChatCompletionRequestStop
from .types.chat_completion_request_tool_choice import ChatCompletionRequestToolChoice
from .types.embeddings_request_encoding_format import EmbeddingsRequestEncodingFormat
from .types.embeddings_request_input import EmbeddingsRequestInput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOpenaiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_chat_completion(
        self,
        *,
        messages: typing.Sequence[ChatCompletionRequestMessagesItem],
        model: ChatCompletionRequestModel,
        audio: typing.Optional[ChatCompletionAudioParam] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        function_call: typing.Optional[ChatCompletionRequestFunctionCall] = OMIT,
        functions: typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]] = OMIT,
        logit_bias: typing.Optional[typing.Dict[str, typing.Optional[int]]] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        modalities: typing.Optional[typing.Sequence[ChatCompletionRequestModalitiesItem]] = OMIT,
        n: typing.Optional[int] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        prediction: typing.Optional[ChatCompletionPredictionContentParam] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        reasoning_effort: typing.Optional[ChatCompletionRequestReasoningEffort] = OMIT,
        response_format: typing.Optional[ChatCompletionRequestResponseFormat] = OMIT,
        seed: typing.Optional[int] = OMIT,
        service_tier: typing.Optional[ChatCompletionRequestServiceTier] = OMIT,
        stop: typing.Optional[ChatCompletionRequestStop] = OMIT,
        store: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[ChatCompletionStreamOptionsParam] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        tool_choice: typing.Optional[ChatCompletionRequestToolChoice] = OMIT,
        tools: typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        user: typing.Optional[str] = OMIT,
        web_search_options: typing.Optional[WebSearchOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        messages : typing.Sequence[ChatCompletionRequestMessagesItem]

        model : ChatCompletionRequestModel

        audio : typing.Optional[ChatCompletionAudioParam]

        frequency_penalty : typing.Optional[float]

        function_call : typing.Optional[ChatCompletionRequestFunctionCall]

        functions : typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]]

        logit_bias : typing.Optional[typing.Dict[str, typing.Optional[int]]]

        logprobs : typing.Optional[bool]

        max_completion_tokens : typing.Optional[int]

        max_tokens : typing.Optional[int]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        modalities : typing.Optional[typing.Sequence[ChatCompletionRequestModalitiesItem]]

        n : typing.Optional[int]

        parallel_tool_calls : typing.Optional[bool]

        prediction : typing.Optional[ChatCompletionPredictionContentParam]

        presence_penalty : typing.Optional[float]

        reasoning_effort : typing.Optional[ChatCompletionRequestReasoningEffort]

        response_format : typing.Optional[ChatCompletionRequestResponseFormat]

        seed : typing.Optional[int]

        service_tier : typing.Optional[ChatCompletionRequestServiceTier]

        stop : typing.Optional[ChatCompletionRequestStop]

        store : typing.Optional[bool]

        stream : typing.Optional[bool]

        stream_options : typing.Optional[ChatCompletionStreamOptionsParam]

        temperature : typing.Optional[float]

        tool_choice : typing.Optional[ChatCompletionRequestToolChoice]

        tools : typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]]

        top_logprobs : typing.Optional[int]

        top_p : typing.Optional[float]

        user : typing.Optional[str]

        web_search_options : typing.Optional[WebSearchOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/openai/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatCompletionRequestMessagesItem], direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=ChatCompletionRequestModel, direction="write"
                ),
                "audio": convert_and_respect_annotation_metadata(
                    object_=audio, annotation=typing.Optional[ChatCompletionAudioParam], direction="write"
                ),
                "frequency_penalty": frequency_penalty,
                "function_call": convert_and_respect_annotation_metadata(
                    object_=function_call,
                    annotation=typing.Optional[ChatCompletionRequestFunctionCall],
                    direction="write",
                ),
                "functions": convert_and_respect_annotation_metadata(
                    object_=functions,
                    annotation=typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]],
                    direction="write",
                ),
                "logit_bias": logit_bias,
                "logprobs": logprobs,
                "max_completion_tokens": max_completion_tokens,
                "max_tokens": max_tokens,
                "metadata": metadata,
                "modalities": modalities,
                "n": n,
                "parallel_tool_calls": parallel_tool_calls,
                "prediction": convert_and_respect_annotation_metadata(
                    object_=prediction,
                    annotation=typing.Optional[ChatCompletionPredictionContentParam],
                    direction="write",
                ),
                "presence_penalty": presence_penalty,
                "reasoning_effort": reasoning_effort,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format,
                    annotation=typing.Optional[ChatCompletionRequestResponseFormat],
                    direction="write",
                ),
                "seed": seed,
                "service_tier": service_tier,
                "stop": convert_and_respect_annotation_metadata(
                    object_=stop, annotation=typing.Optional[ChatCompletionRequestStop], direction="write"
                ),
                "store": store,
                "stream": stream,
                "stream_options": convert_and_respect_annotation_metadata(
                    object_=stream_options,
                    annotation=typing.Optional[ChatCompletionStreamOptionsParam],
                    direction="write",
                ),
                "temperature": temperature,
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=typing.Optional[ChatCompletionRequestToolChoice], direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]],
                    direction="write",
                ),
                "top_logprobs": top_logprobs,
                "top_p": top_p,
                "user": user,
                "web_search_options": convert_and_respect_annotation_metadata(
                    object_=web_search_options, annotation=typing.Optional[WebSearchOptions], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def create_embedding(
        self,
        *,
        model: str,
        input: EmbeddingsRequestInput,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        model : str

        input : EmbeddingsRequestInput

        encoding_format : typing.Optional[EmbeddingsRequestEncodingFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/openai/embeddings",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbeddingsRequestInput, direction="write"
                ),
                "encoding_format": encoding_format,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[OpenAiPageModel]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAiPageModel]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/openai/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAiPageModel,
                    parse_obj_as(
                        type_=OpenAiPageModel,
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


class AsyncRawOpenaiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_chat_completion(
        self,
        *,
        messages: typing.Sequence[ChatCompletionRequestMessagesItem],
        model: ChatCompletionRequestModel,
        audio: typing.Optional[ChatCompletionAudioParam] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        function_call: typing.Optional[ChatCompletionRequestFunctionCall] = OMIT,
        functions: typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]] = OMIT,
        logit_bias: typing.Optional[typing.Dict[str, typing.Optional[int]]] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        modalities: typing.Optional[typing.Sequence[ChatCompletionRequestModalitiesItem]] = OMIT,
        n: typing.Optional[int] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        prediction: typing.Optional[ChatCompletionPredictionContentParam] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        reasoning_effort: typing.Optional[ChatCompletionRequestReasoningEffort] = OMIT,
        response_format: typing.Optional[ChatCompletionRequestResponseFormat] = OMIT,
        seed: typing.Optional[int] = OMIT,
        service_tier: typing.Optional[ChatCompletionRequestServiceTier] = OMIT,
        stop: typing.Optional[ChatCompletionRequestStop] = OMIT,
        store: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[ChatCompletionStreamOptionsParam] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        tool_choice: typing.Optional[ChatCompletionRequestToolChoice] = OMIT,
        tools: typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        user: typing.Optional[str] = OMIT,
        web_search_options: typing.Optional[WebSearchOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        messages : typing.Sequence[ChatCompletionRequestMessagesItem]

        model : ChatCompletionRequestModel

        audio : typing.Optional[ChatCompletionAudioParam]

        frequency_penalty : typing.Optional[float]

        function_call : typing.Optional[ChatCompletionRequestFunctionCall]

        functions : typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]]

        logit_bias : typing.Optional[typing.Dict[str, typing.Optional[int]]]

        logprobs : typing.Optional[bool]

        max_completion_tokens : typing.Optional[int]

        max_tokens : typing.Optional[int]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        modalities : typing.Optional[typing.Sequence[ChatCompletionRequestModalitiesItem]]

        n : typing.Optional[int]

        parallel_tool_calls : typing.Optional[bool]

        prediction : typing.Optional[ChatCompletionPredictionContentParam]

        presence_penalty : typing.Optional[float]

        reasoning_effort : typing.Optional[ChatCompletionRequestReasoningEffort]

        response_format : typing.Optional[ChatCompletionRequestResponseFormat]

        seed : typing.Optional[int]

        service_tier : typing.Optional[ChatCompletionRequestServiceTier]

        stop : typing.Optional[ChatCompletionRequestStop]

        store : typing.Optional[bool]

        stream : typing.Optional[bool]

        stream_options : typing.Optional[ChatCompletionStreamOptionsParam]

        temperature : typing.Optional[float]

        tool_choice : typing.Optional[ChatCompletionRequestToolChoice]

        tools : typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]]

        top_logprobs : typing.Optional[int]

        top_p : typing.Optional[float]

        user : typing.Optional[str]

        web_search_options : typing.Optional[WebSearchOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/openai/chat/completions",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatCompletionRequestMessagesItem], direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=ChatCompletionRequestModel, direction="write"
                ),
                "audio": convert_and_respect_annotation_metadata(
                    object_=audio, annotation=typing.Optional[ChatCompletionAudioParam], direction="write"
                ),
                "frequency_penalty": frequency_penalty,
                "function_call": convert_and_respect_annotation_metadata(
                    object_=function_call,
                    annotation=typing.Optional[ChatCompletionRequestFunctionCall],
                    direction="write",
                ),
                "functions": convert_and_respect_annotation_metadata(
                    object_=functions,
                    annotation=typing.Optional[typing.Sequence[OpenaiTypesChatCompletionCreateParamsFunction]],
                    direction="write",
                ),
                "logit_bias": logit_bias,
                "logprobs": logprobs,
                "max_completion_tokens": max_completion_tokens,
                "max_tokens": max_tokens,
                "metadata": metadata,
                "modalities": modalities,
                "n": n,
                "parallel_tool_calls": parallel_tool_calls,
                "prediction": convert_and_respect_annotation_metadata(
                    object_=prediction,
                    annotation=typing.Optional[ChatCompletionPredictionContentParam],
                    direction="write",
                ),
                "presence_penalty": presence_penalty,
                "reasoning_effort": reasoning_effort,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format,
                    annotation=typing.Optional[ChatCompletionRequestResponseFormat],
                    direction="write",
                ),
                "seed": seed,
                "service_tier": service_tier,
                "stop": convert_and_respect_annotation_metadata(
                    object_=stop, annotation=typing.Optional[ChatCompletionRequestStop], direction="write"
                ),
                "store": store,
                "stream": stream,
                "stream_options": convert_and_respect_annotation_metadata(
                    object_=stream_options,
                    annotation=typing.Optional[ChatCompletionStreamOptionsParam],
                    direction="write",
                ),
                "temperature": temperature,
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=typing.Optional[ChatCompletionRequestToolChoice], direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[ChatCompletionFunctionToolParam]],
                    direction="write",
                ),
                "top_logprobs": top_logprobs,
                "top_p": top_p,
                "user": user,
                "web_search_options": convert_and_respect_annotation_metadata(
                    object_=web_search_options, annotation=typing.Optional[WebSearchOptions], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def create_embedding(
        self,
        *,
        model: str,
        input: EmbeddingsRequestInput,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        model : str

        input : EmbeddingsRequestInput

        encoding_format : typing.Optional[EmbeddingsRequestEncodingFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/openai/embeddings",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbeddingsRequestInput, direction="write"
                ),
                "encoding_format": encoding_format,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def list_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OpenAiPageModel]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAiPageModel]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/openai/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAiPageModel,
                    parse_obj_as(
                        type_=OpenAiPageModel,
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
