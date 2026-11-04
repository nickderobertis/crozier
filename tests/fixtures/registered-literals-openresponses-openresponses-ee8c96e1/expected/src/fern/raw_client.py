

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.create_response_body_input import CreateResponseBodyInput
from .types.create_response_body_reasoning import CreateResponseBodyReasoning
from .types.create_response_body_service_tier import CreateResponseBodyServiceTier
from .types.create_response_body_stream_options import CreateResponseBodyStreamOptions
from .types.create_response_body_text import CreateResponseBodyText
from .types.create_response_body_tool_choice import CreateResponseBodyToolChoice
from .types.create_response_body_truncation import CreateResponseBodyTruncation
from .types.include_enum import IncludeEnum
from .types.response_resource import ResponseResource
from .types.responses_tool_param import ResponsesToolParam
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def createresponse(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        input: typing.Optional[CreateResponseBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        include: typing.Optional[typing.Sequence[IncludeEnum]] = OMIT,
        tools: typing.Optional[typing.Sequence[ResponsesToolParam]] = OMIT,
        tool_choice: typing.Optional[CreateResponseBodyToolChoice] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        text: typing.Optional[CreateResponseBodyText] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[CreateResponseBodyStreamOptions] = OMIT,
        background: typing.Optional[bool] = OMIT,
        max_output_tokens: typing.Optional[int] = OMIT,
        max_tool_calls: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[CreateResponseBodyReasoning] = OMIT,
        safety_identifier: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        truncation: typing.Optional[CreateResponseBodyTruncation] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        store: typing.Optional[bool] = OMIT,
        service_tier: typing.Optional[CreateResponseBodyServiceTier] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseResource]:
        """
        Creates a response.

        Parameters
        ----------
        model : typing.Optional[str]
            The model to use for this request, e.g. 'gpt-5.2'.

        input : typing.Optional[CreateResponseBodyInput]
            Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.

        previous_response_id : typing.Optional[str]
            The ID of the response to use as the prior turn for this request.

        include : typing.Optional[typing.Sequence[IncludeEnum]]

        tools : typing.Optional[typing.Sequence[ResponsesToolParam]]
            A list of tools that the model may call while generating the response.

        tool_choice : typing.Optional[CreateResponseBodyToolChoice]
            Controls which tool the model should use, if any.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
                    Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.

        text : typing.Optional[CreateResponseBodyText]
            Configuration options for text output.

        temperature : typing.Optional[float]
            Sampling temperature to use, between 0 and 2. Higher values make the output more random.

        top_p : typing.Optional[float]
            Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.

        presence_penalty : typing.Optional[float]
            Penalizes new tokens based on whether they appear in the text so far.

        frequency_penalty : typing.Optional[float]
            Penalizes new tokens based on their frequency in the text so far.

        parallel_tool_calls : typing.Optional[bool]
            Whether the model may call multiple tools in parallel.

        stream : typing.Optional[bool]
            Whether to stream response events as server-sent events.

        stream_options : typing.Optional[CreateResponseBodyStreamOptions]
            Options that control streamed response behavior.

        background : typing.Optional[bool]
            Whether to run the request in the background and return immediately.

        max_output_tokens : typing.Optional[int]
            The maximum number of tokens the model may generate for this response.

        max_tool_calls : typing.Optional[int]
            The maximum number of tool calls the model may make while generating the response.

        reasoning : typing.Optional[CreateResponseBodyReasoning]
            Configuration options for reasoning behavior.

        safety_identifier : typing.Optional[str]
            A stable identifier used for safety monitoring and abuse detection.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        truncation : typing.Optional[CreateResponseBodyTruncation]
            Controls how the service truncates the input when it exceeds the model context window.

        instructions : typing.Optional[str]
            Additional instructions to guide the model for this request.

        store : typing.Optional[bool]
            Whether to store the response so it can be retrieved later.

        service_tier : typing.Optional[CreateResponseBodyServiceTier]
            The service tier to use for this request.

        top_logprobs : typing.Optional[int]
            The number of most likely tokens to return at each position, along with their log probabilities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseResource]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "responses",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[CreateResponseBodyInput], direction="write"
                ),
                "previous_response_id": previous_response_id,
                "include": include,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Optional[typing.Sequence[ResponsesToolParam]], direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=typing.Optional[CreateResponseBodyToolChoice], direction="write"
                ),
                "metadata": metadata,
                "text": convert_and_respect_annotation_metadata(
                    object_=text, annotation=typing.Optional[CreateResponseBodyText], direction="write"
                ),
                "temperature": temperature,
                "top_p": top_p,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty,
                "parallel_tool_calls": parallel_tool_calls,
                "stream": stream,
                "stream_options": convert_and_respect_annotation_metadata(
                    object_=stream_options,
                    annotation=typing.Optional[CreateResponseBodyStreamOptions],
                    direction="write",
                ),
                "background": background,
                "max_output_tokens": max_output_tokens,
                "max_tool_calls": max_tool_calls,
                "reasoning": convert_and_respect_annotation_metadata(
                    object_=reasoning, annotation=typing.Optional[CreateResponseBodyReasoning], direction="write"
                ),
                "safety_identifier": safety_identifier,
                "prompt_cache_key": prompt_cache_key,
                "truncation": truncation,
                "instructions": instructions,
                "store": store,
                "service_tier": service_tier,
                "top_logprobs": top_logprobs,
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
                    ResponseResource,
                    parse_obj_as(
                        type_=ResponseResource,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def createresponse(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        input: typing.Optional[CreateResponseBodyInput] = OMIT,
        previous_response_id: typing.Optional[str] = OMIT,
        include: typing.Optional[typing.Sequence[IncludeEnum]] = OMIT,
        tools: typing.Optional[typing.Sequence[ResponsesToolParam]] = OMIT,
        tool_choice: typing.Optional[CreateResponseBodyToolChoice] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        text: typing.Optional[CreateResponseBodyText] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        presence_penalty: typing.Optional[float] = OMIT,
        frequency_penalty: typing.Optional[float] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        stream_options: typing.Optional[CreateResponseBodyStreamOptions] = OMIT,
        background: typing.Optional[bool] = OMIT,
        max_output_tokens: typing.Optional[int] = OMIT,
        max_tool_calls: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[CreateResponseBodyReasoning] = OMIT,
        safety_identifier: typing.Optional[str] = OMIT,
        prompt_cache_key: typing.Optional[str] = OMIT,
        truncation: typing.Optional[CreateResponseBodyTruncation] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        store: typing.Optional[bool] = OMIT,
        service_tier: typing.Optional[CreateResponseBodyServiceTier] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseResource]:
        """
        Creates a response.

        Parameters
        ----------
        model : typing.Optional[str]
            The model to use for this request, e.g. 'gpt-5.2'.

        input : typing.Optional[CreateResponseBodyInput]
            Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.

        previous_response_id : typing.Optional[str]
            The ID of the response to use as the prior turn for this request.

        include : typing.Optional[typing.Sequence[IncludeEnum]]

        tools : typing.Optional[typing.Sequence[ResponsesToolParam]]
            A list of tools that the model may call while generating the response.

        tool_choice : typing.Optional[CreateResponseBodyToolChoice]
            Controls which tool the model should use, if any.

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
                    Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.

        text : typing.Optional[CreateResponseBodyText]
            Configuration options for text output.

        temperature : typing.Optional[float]
            Sampling temperature to use, between 0 and 2. Higher values make the output more random.

        top_p : typing.Optional[float]
            Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.

        presence_penalty : typing.Optional[float]
            Penalizes new tokens based on whether they appear in the text so far.

        frequency_penalty : typing.Optional[float]
            Penalizes new tokens based on their frequency in the text so far.

        parallel_tool_calls : typing.Optional[bool]
            Whether the model may call multiple tools in parallel.

        stream : typing.Optional[bool]
            Whether to stream response events as server-sent events.

        stream_options : typing.Optional[CreateResponseBodyStreamOptions]
            Options that control streamed response behavior.

        background : typing.Optional[bool]
            Whether to run the request in the background and return immediately.

        max_output_tokens : typing.Optional[int]
            The maximum number of tokens the model may generate for this response.

        max_tool_calls : typing.Optional[int]
            The maximum number of tool calls the model may make while generating the response.

        reasoning : typing.Optional[CreateResponseBodyReasoning]
            Configuration options for reasoning behavior.

        safety_identifier : typing.Optional[str]
            A stable identifier used for safety monitoring and abuse detection.

        prompt_cache_key : typing.Optional[str]
            A key to use when reading from or writing to the prompt cache.

        truncation : typing.Optional[CreateResponseBodyTruncation]
            Controls how the service truncates the input when it exceeds the model context window.

        instructions : typing.Optional[str]
            Additional instructions to guide the model for this request.

        store : typing.Optional[bool]
            Whether to store the response so it can be retrieved later.

        service_tier : typing.Optional[CreateResponseBodyServiceTier]
            The service tier to use for this request.

        top_logprobs : typing.Optional[int]
            The number of most likely tokens to return at each position, along with their log probabilities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseResource]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "responses",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[CreateResponseBodyInput], direction="write"
                ),
                "previous_response_id": previous_response_id,
                "include": include,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Optional[typing.Sequence[ResponsesToolParam]], direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=typing.Optional[CreateResponseBodyToolChoice], direction="write"
                ),
                "metadata": metadata,
                "text": convert_and_respect_annotation_metadata(
                    object_=text, annotation=typing.Optional[CreateResponseBodyText], direction="write"
                ),
                "temperature": temperature,
                "top_p": top_p,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty,
                "parallel_tool_calls": parallel_tool_calls,
                "stream": stream,
                "stream_options": convert_and_respect_annotation_metadata(
                    object_=stream_options,
                    annotation=typing.Optional[CreateResponseBodyStreamOptions],
                    direction="write",
                ),
                "background": background,
                "max_output_tokens": max_output_tokens,
                "max_tool_calls": max_tool_calls,
                "reasoning": convert_and_respect_annotation_metadata(
                    object_=reasoning, annotation=typing.Optional[CreateResponseBodyReasoning], direction="write"
                ),
                "safety_identifier": safety_identifier,
                "prompt_cache_key": prompt_cache_key,
                "truncation": truncation,
                "instructions": instructions,
                "store": store,
                "service_tier": service_tier,
                "top_logprobs": top_logprobs,
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
                    ResponseResource,
                    parse_obj_as(
                        type_=ResponseResource,
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
