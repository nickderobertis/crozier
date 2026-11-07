

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_completion_audio_param import ChatCompletionAudioParam
from ..types.chat_completion_function_tool_param import ChatCompletionFunctionToolParam
from ..types.chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from ..types.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from ..types.open_ai_page_model import OpenAiPageModel
from ..types.openai_types_chat_completion_create_params_function import OpenaiTypesChatCompletionCreateParamsFunction
from ..types.web_search_options import WebSearchOptions
from .raw_client import AsyncRawOpenaiClient, RawOpenaiClient
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


OMIT = typing.cast(typing.Any, ...)


class OpenaiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenaiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenaiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenaiClient
        """
        return self._raw_client

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern.openai import ChatCompletionRequestMessagesItem_Developer

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.openai.create_chat_completion(
            messages=[
                ChatCompletionRequestMessagesItem_Developer(
                    content="content",
                )
            ],
            model="gpt-5.2",
        )
        """
        _response = self._raw_client.create_chat_completion(
            messages=messages,
            model=model,
            audio=audio,
            frequency_penalty=frequency_penalty,
            function_call=function_call,
            functions=functions,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_completion_tokens=max_completion_tokens,
            max_tokens=max_tokens,
            metadata=metadata,
            modalities=modalities,
            n=n,
            parallel_tool_calls=parallel_tool_calls,
            prediction=prediction,
            presence_penalty=presence_penalty,
            reasoning_effort=reasoning_effort,
            response_format=response_format,
            seed=seed,
            service_tier=service_tier,
            stop=stop,
            store=store,
            stream=stream,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_logprobs=top_logprobs,
            top_p=top_p,
            user=user,
            web_search_options=web_search_options,
            request_options=request_options,
        )
        return _response.data

    def create_embedding(
        self,
        *,
        model: str,
        input: EmbeddingsRequestInput,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.openai.create_embedding(
            model="model",
            input=["input"],
        )
        """
        _response = self._raw_client.create_embedding(
            model=model, input=input, encoding_format=encoding_format, request_options=request_options
        )
        return _response.data

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAiPageModel:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiPageModel
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.openai.list_models()
        """
        _response = self._raw_client.list_models(request_options=request_options)
        return _response.data


class AsyncOpenaiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenaiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenaiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenaiClient
        """
        return self._raw_client

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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern.openai import ChatCompletionRequestMessagesItem_Developer

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.openai.create_chat_completion(
                messages=[
                    ChatCompletionRequestMessagesItem_Developer(
                        content="content",
                    )
                ],
                model="gpt-5.2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_chat_completion(
            messages=messages,
            model=model,
            audio=audio,
            frequency_penalty=frequency_penalty,
            function_call=function_call,
            functions=functions,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_completion_tokens=max_completion_tokens,
            max_tokens=max_tokens,
            metadata=metadata,
            modalities=modalities,
            n=n,
            parallel_tool_calls=parallel_tool_calls,
            prediction=prediction,
            presence_penalty=presence_penalty,
            reasoning_effort=reasoning_effort,
            response_format=response_format,
            seed=seed,
            service_tier=service_tier,
            stop=stop,
            store=store,
            stream=stream,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_logprobs=top_logprobs,
            top_p=top_p,
            user=user,
            web_search_options=web_search_options,
            request_options=request_options,
        )
        return _response.data

    async def create_embedding(
        self,
        *,
        model: str,
        input: EmbeddingsRequestInput,
        encoding_format: typing.Optional[EmbeddingsRequestEncodingFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.openai.create_embedding(
                model="model",
                input=["input"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_embedding(
            model=model, input=input, encoding_format=encoding_format, request_options=request_options
        )
        return _response.data

    async def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAiPageModel:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAiPageModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.openai.list_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(request_options=request_options)
        return _response.data
