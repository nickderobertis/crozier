

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .types.chat_message import ChatMessage
from .types.chat_request_format import ChatRequestFormat
from .types.chat_request_keep_alive import ChatRequestKeepAlive
from .types.chat_response import ChatResponse
from .types.create_request_license import CreateRequestLicense
from .types.embed_request_input import EmbedRequestInput
from .types.embed_response import EmbedResponse
from .types.error_response import ErrorResponse
from .types.generate_request_format import GenerateRequestFormat
from .types.generate_request_keep_alive import GenerateRequestKeepAlive
from .types.generate_response import GenerateResponse
from .types.list_response import ListResponse
from .types.model_options import ModelOptions
from .types.ps_response import PsResponse
from .types.show_response import ShowResponse
from .types.status_response import StatusResponse
from .types.think_value import ThinkValue
from .types.tool_definition import ToolDefinition
from .types.version_response import VersionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate(
        self,
        *,
        model: str,
        prompt: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[str]] = OMIT,
        format: typing.Optional[GenerateRequestFormat] = OMIT,
        system: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[GenerateRequestKeepAlive] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GenerateResponse]:
        """
        Generates a response for the provided prompt

        Parameters
        ----------
        model : str
            Model name

        prompt : typing.Optional[str]
            Text for the model to generate a response from

        suffix : typing.Optional[str]
            Used for fill-in-the-middle models, text that appears after the user prompt and before the model response

        images : typing.Optional[typing.Sequence[str]]

        format : typing.Optional[GenerateRequestFormat]
            Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.

        system : typing.Optional[str]
            System prompt for the model to generate a response from

        stream : typing.Optional[bool]
            When true, returns a stream of partial responses

        think : typing.Optional[ThinkValue]

        raw : typing.Optional[bool]
            When true, returns the raw response from the model without any prompt templating

        keep_alive : typing.Optional[GenerateRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        options : typing.Optional[ModelOptions]

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GenerateResponse]
            Generation responses
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/generate",
            method="POST",
            json={
                "model": model,
                "prompt": prompt,
                "suffix": suffix,
                "images": images,
                "format": convert_and_respect_annotation_metadata(
                    object_=format, annotation=GenerateRequestFormat, direction="write"
                ),
                "system": system,
                "stream": stream,
                "think": convert_and_respect_annotation_metadata(
                    object_=think, annotation=typing.Optional[ThinkValue], direction="write"
                ),
                "raw": raw,
                "keep_alive": convert_and_respect_annotation_metadata(
                    object_=keep_alive, annotation=GenerateRequestKeepAlive, direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
                ),
                "logprobs": logprobs,
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
                    GenerateResponse,
                    parse_obj_as(
                        type_=GenerateResponse,
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

    def chat(
        self,
        *,
        model: str,
        messages: typing.Sequence[ChatMessage],
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        format: typing.Optional[ChatRequestFormat] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        keep_alive: typing.Optional[ChatRequestKeepAlive] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatResponse]:
        """
        Generate the next chat message in a conversation between a user and an assistant.

        Parameters
        ----------
        model : str
            Model name

        messages : typing.Sequence[ChatMessage]
            Chat history as an array of message objects (each with a role and content)

        tools : typing.Optional[typing.Sequence[ToolDefinition]]
            Optional list of function tools the model may call during the chat

        format : typing.Optional[ChatRequestFormat]
            Format to return a response in. Can be `json` or a JSON schema

        options : typing.Optional[ModelOptions]

        stream : typing.Optional[bool]

        think : typing.Optional[ThinkValue]

        keep_alive : typing.Optional[ChatRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatResponse]
            Chat response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/chat",
            method="POST",
            json={
                "model": model,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[ToolDefinition], direction="write"
                ),
                "format": convert_and_respect_annotation_metadata(
                    object_=format, annotation=ChatRequestFormat, direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
                ),
                "stream": stream,
                "think": convert_and_respect_annotation_metadata(
                    object_=think, annotation=typing.Optional[ThinkValue], direction="write"
                ),
                "keep_alive": convert_and_respect_annotation_metadata(
                    object_=keep_alive, annotation=ChatRequestKeepAlive, direction="write"
                ),
                "logprobs": logprobs,
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
                    ChatResponse,
                    parse_obj_as(
                        type_=ChatResponse,
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

    def embed(
        self,
        *,
        model: str,
        input: EmbedRequestInput,
        truncate: typing.Optional[bool] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        keep_alive: typing.Optional[str] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmbedResponse]:
        """
        Creates vector embeddings representing the input text

        Parameters
        ----------
        model : str
            Model name

        input : EmbedRequestInput
            Text or array of texts to generate embeddings for

        truncate : typing.Optional[bool]
            If true, truncate inputs that exceed the context window. If false, returns an error.

        dimensions : typing.Optional[int]
            Number of dimensions to generate embeddings for

        keep_alive : typing.Optional[str]
            Model keep-alive duration

        options : typing.Optional[ModelOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmbedResponse]
            Vector embeddings for the input text
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/embed",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbedRequestInput, direction="write"
                ),
                "truncate": truncate,
                "dimensions": dimensions,
                "keep_alive": keep_alive,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
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
                    EmbedResponse,
                    parse_obj_as(
                        type_=EmbedResponse,
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ListResponse]:
        """
        Fetch a list of models and their details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponse]
            List available models
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/tags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponse,
                    parse_obj_as(
                        type_=ListResponse,
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

    def ps(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[PsResponse]:
        """
        Retrieve a list of models that are currently running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PsResponse]
            Models currently loaded into memory
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PsResponse,
                    parse_obj_as(
                        type_=PsResponse,
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

    def show(
        self,
        *,
        model: str,
        verbose: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShowResponse]:
        """
        Parameters
        ----------
        model : str
            Model name to show

        verbose : typing.Optional[bool]
            If true, includes large verbose fields in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShowResponse]
            Model information
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/show",
            method="POST",
            json={
                "model": model,
                "verbose": verbose,
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
                    ShowResponse,
                    parse_obj_as(
                        type_=ShowResponse,
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

    def create(
        self,
        *,
        model: str,
        from_: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        renderer: typing.Optional[str] = OMIT,
        parser: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        draft_files: typing.Optional[typing.Dict[str, str]] = OMIT,
        license: typing.Optional[CreateRequestLicense] = OMIT,
        system: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatMessage]] = OMIT,
        quantize: typing.Optional[str] = OMIT,
        draft_quantize: typing.Optional[str] = OMIT,
        requires: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name for the model to create

        from_ : typing.Optional[str]
            Existing model to create from

        template : typing.Optional[str]
            Prompt template to use for the model

        renderer : typing.Optional[str]
            Name of the renderer for the model

        parser : typing.Optional[str]
            Name of the parser for the model

        files : typing.Optional[typing.Dict[str, str]]
            Source file names mapped to their SHA-256 digests. Split GGUF models must include each shard under its original split filename.

        draft_files : typing.Optional[typing.Dict[str, str]]
            Draft source file names mapped to their SHA-256 digests

        license : typing.Optional[CreateRequestLicense]
            License string or list of licenses for the model

        system : typing.Optional[str]
            System prompt to embed in the model

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value parameters for the model

        messages : typing.Optional[typing.Sequence[ChatMessage]]
            Message history to use for the model

        quantize : typing.Optional[str]
            Quantization level to apply during import (e.g. `nvfp4`)

        draft_quantize : typing.Optional[str]
            Quantization level to apply to draft weights during import

        requires : typing.Optional[str]
            Minimum Ollama version required by the model

        stream : typing.Optional[bool]
            Stream status updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatusResponse]
            Stream of create status updates
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/create",
            method="POST",
            json={
                "model": model,
                "from": from_,
                "template": template,
                "renderer": renderer,
                "parser": parser,
                "files": files,
                "draft_files": draft_files,
                "license": convert_and_respect_annotation_metadata(
                    object_=license, annotation=CreateRequestLicense, direction="write"
                ),
                "system": system,
                "parameters": parameters,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "quantize": quantize,
                "draft_quantize": draft_quantize,
                "requires": requires,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    def create_blob(
        self,
        digest: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/blobs/{encode_path_param(digest)}",
            method="POST",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def head_blob(self, digest: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/blobs/{encode_path_param(digest)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def copy(
        self, *, source: str, destination: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        source : str
            Existing model name to copy from

        destination : str
            New model name to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/copy",
            method="POST",
            json={
                "source": source,
                "destination": destination,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pull(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name of the model to download

        insecure : typing.Optional[bool]
            Allow downloading over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatusResponse]
            Pull status updates.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/pull",
            method="POST",
            json={
                "model": model,
                "insecure": insecure,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    def push(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name of the model to publish

        insecure : typing.Optional[bool]
            Allow publishing over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatusResponse]
            Push status updates.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/push",
            method="POST",
            json={
                "model": model,
                "insecure": insecure,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    def delete(self, *, model: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        model : str
            Model name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/delete",
            method="DELETE",
            json={
                "model": model,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[VersionResponse]:
        """
        Retrieve the version of the Ollama

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VersionResponse]
            Version information
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionResponse,
                    parse_obj_as(
                        type_=VersionResponse,
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

    async def generate(
        self,
        *,
        model: str,
        prompt: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[str]] = OMIT,
        format: typing.Optional[GenerateRequestFormat] = OMIT,
        system: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        keep_alive: typing.Optional[GenerateRequestKeepAlive] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GenerateResponse]:
        """
        Generates a response for the provided prompt

        Parameters
        ----------
        model : str
            Model name

        prompt : typing.Optional[str]
            Text for the model to generate a response from

        suffix : typing.Optional[str]
            Used for fill-in-the-middle models, text that appears after the user prompt and before the model response

        images : typing.Optional[typing.Sequence[str]]

        format : typing.Optional[GenerateRequestFormat]
            Structured output format for the model to generate a response from. Supports either the string `"json"` or a JSON schema object.

        system : typing.Optional[str]
            System prompt for the model to generate a response from

        stream : typing.Optional[bool]
            When true, returns a stream of partial responses

        think : typing.Optional[ThinkValue]

        raw : typing.Optional[bool]
            When true, returns the raw response from the model without any prompt templating

        keep_alive : typing.Optional[GenerateRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        options : typing.Optional[ModelOptions]

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GenerateResponse]
            Generation responses
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/generate",
            method="POST",
            json={
                "model": model,
                "prompt": prompt,
                "suffix": suffix,
                "images": images,
                "format": convert_and_respect_annotation_metadata(
                    object_=format, annotation=GenerateRequestFormat, direction="write"
                ),
                "system": system,
                "stream": stream,
                "think": convert_and_respect_annotation_metadata(
                    object_=think, annotation=typing.Optional[ThinkValue], direction="write"
                ),
                "raw": raw,
                "keep_alive": convert_and_respect_annotation_metadata(
                    object_=keep_alive, annotation=GenerateRequestKeepAlive, direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
                ),
                "logprobs": logprobs,
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
                    GenerateResponse,
                    parse_obj_as(
                        type_=GenerateResponse,
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

    async def chat(
        self,
        *,
        model: str,
        messages: typing.Sequence[ChatMessage],
        tools: typing.Optional[typing.Sequence[ToolDefinition]] = OMIT,
        format: typing.Optional[ChatRequestFormat] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        think: typing.Optional[ThinkValue] = OMIT,
        keep_alive: typing.Optional[ChatRequestKeepAlive] = OMIT,
        logprobs: typing.Optional[bool] = OMIT,
        top_logprobs: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatResponse]:
        """
        Generate the next chat message in a conversation between a user and an assistant.

        Parameters
        ----------
        model : str
            Model name

        messages : typing.Sequence[ChatMessage]
            Chat history as an array of message objects (each with a role and content)

        tools : typing.Optional[typing.Sequence[ToolDefinition]]
            Optional list of function tools the model may call during the chat

        format : typing.Optional[ChatRequestFormat]
            Format to return a response in. Can be `json` or a JSON schema

        options : typing.Optional[ModelOptions]

        stream : typing.Optional[bool]

        think : typing.Optional[ThinkValue]

        keep_alive : typing.Optional[ChatRequestKeepAlive]
            Model keep-alive duration (for example `5m` or `0` to unload immediately)

        logprobs : typing.Optional[bool]
            Whether to return log probabilities of the output tokens

        top_logprobs : typing.Optional[int]
            Number of most likely tokens to return at each token position when logprobs are enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatResponse]
            Chat response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/chat",
            method="POST",
            json={
                "model": model,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[ToolDefinition], direction="write"
                ),
                "format": convert_and_respect_annotation_metadata(
                    object_=format, annotation=ChatRequestFormat, direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
                ),
                "stream": stream,
                "think": convert_and_respect_annotation_metadata(
                    object_=think, annotation=typing.Optional[ThinkValue], direction="write"
                ),
                "keep_alive": convert_and_respect_annotation_metadata(
                    object_=keep_alive, annotation=ChatRequestKeepAlive, direction="write"
                ),
                "logprobs": logprobs,
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
                    ChatResponse,
                    parse_obj_as(
                        type_=ChatResponse,
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

    async def embed(
        self,
        *,
        model: str,
        input: EmbedRequestInput,
        truncate: typing.Optional[bool] = OMIT,
        dimensions: typing.Optional[int] = OMIT,
        keep_alive: typing.Optional[str] = OMIT,
        options: typing.Optional[ModelOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmbedResponse]:
        """
        Creates vector embeddings representing the input text

        Parameters
        ----------
        model : str
            Model name

        input : EmbedRequestInput
            Text or array of texts to generate embeddings for

        truncate : typing.Optional[bool]
            If true, truncate inputs that exceed the context window. If false, returns an error.

        dimensions : typing.Optional[int]
            Number of dimensions to generate embeddings for

        keep_alive : typing.Optional[str]
            Model keep-alive duration

        options : typing.Optional[ModelOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmbedResponse]
            Vector embeddings for the input text
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/embed",
            method="POST",
            json={
                "model": model,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=EmbedRequestInput, direction="write"
                ),
                "truncate": truncate,
                "dimensions": dimensions,
                "keep_alive": keep_alive,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=ModelOptions, direction="write"
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
                    EmbedResponse,
                    parse_obj_as(
                        type_=EmbedResponse,
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[ListResponse]:
        """
        Fetch a list of models and their details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponse]
            List available models
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/tags",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponse,
                    parse_obj_as(
                        type_=ListResponse,
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

    async def ps(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[PsResponse]:
        """
        Retrieve a list of models that are currently running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PsResponse]
            Models currently loaded into memory
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PsResponse,
                    parse_obj_as(
                        type_=PsResponse,
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

    async def show(
        self,
        *,
        model: str,
        verbose: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShowResponse]:
        """
        Parameters
        ----------
        model : str
            Model name to show

        verbose : typing.Optional[bool]
            If true, includes large verbose fields in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShowResponse]
            Model information
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/show",
            method="POST",
            json={
                "model": model,
                "verbose": verbose,
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
                    ShowResponse,
                    parse_obj_as(
                        type_=ShowResponse,
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

    async def create(
        self,
        *,
        model: str,
        from_: typing.Optional[str] = OMIT,
        template: typing.Optional[str] = OMIT,
        renderer: typing.Optional[str] = OMIT,
        parser: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        draft_files: typing.Optional[typing.Dict[str, str]] = OMIT,
        license: typing.Optional[CreateRequestLicense] = OMIT,
        system: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[ChatMessage]] = OMIT,
        quantize: typing.Optional[str] = OMIT,
        draft_quantize: typing.Optional[str] = OMIT,
        requires: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name for the model to create

        from_ : typing.Optional[str]
            Existing model to create from

        template : typing.Optional[str]
            Prompt template to use for the model

        renderer : typing.Optional[str]
            Name of the renderer for the model

        parser : typing.Optional[str]
            Name of the parser for the model

        files : typing.Optional[typing.Dict[str, str]]
            Source file names mapped to their SHA-256 digests. Split GGUF models must include each shard under its original split filename.

        draft_files : typing.Optional[typing.Dict[str, str]]
            Draft source file names mapped to their SHA-256 digests

        license : typing.Optional[CreateRequestLicense]
            License string or list of licenses for the model

        system : typing.Optional[str]
            System prompt to embed in the model

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value parameters for the model

        messages : typing.Optional[typing.Sequence[ChatMessage]]
            Message history to use for the model

        quantize : typing.Optional[str]
            Quantization level to apply during import (e.g. `nvfp4`)

        draft_quantize : typing.Optional[str]
            Quantization level to apply to draft weights during import

        requires : typing.Optional[str]
            Minimum Ollama version required by the model

        stream : typing.Optional[bool]
            Stream status updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatusResponse]
            Stream of create status updates
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/create",
            method="POST",
            json={
                "model": model,
                "from": from_,
                "template": template,
                "renderer": renderer,
                "parser": parser,
                "files": files,
                "draft_files": draft_files,
                "license": convert_and_respect_annotation_metadata(
                    object_=license, annotation=CreateRequestLicense, direction="write"
                ),
                "system": system,
                "parameters": parameters,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "quantize": quantize,
                "draft_quantize": draft_quantize,
                "requires": requires,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    async def create_blob(
        self,
        digest: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/blobs/{encode_path_param(digest)}",
            method="POST",
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def head_blob(
        self, digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        digest : str
            SHA256 digest identifier, prefixed with `sha256:`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/blobs/{encode_path_param(digest)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def copy(
        self, *, source: str, destination: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        source : str
            Existing model name to copy from

        destination : str
            New model name to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/copy",
            method="POST",
            json={
                "source": source,
                "destination": destination,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pull(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name of the model to download

        insecure : typing.Optional[bool]
            Allow downloading over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatusResponse]
            Pull status updates.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/pull",
            method="POST",
            json={
                "model": model,
                "insecure": insecure,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    async def push(
        self,
        *,
        model: str,
        insecure: typing.Optional[bool] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StatusResponse]:
        """
        Parameters
        ----------
        model : str
            Name of the model to publish

        insecure : typing.Optional[bool]
            Allow publishing over insecure connections

        stream : typing.Optional[bool]
            Stream progress updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatusResponse]
            Push status updates.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/push",
            method="POST",
            json={
                "model": model,
                "insecure": insecure,
                "stream": stream,
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
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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

    async def delete(
        self, *, model: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        model : str
            Model name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/delete",
            method="DELETE",
            json={
                "model": model,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def version(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VersionResponse]:
        """
        Retrieve the version of the Ollama

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VersionResponse]
            Version information
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionResponse,
                    parse_obj_as(
                        type_=VersionResponse,
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
