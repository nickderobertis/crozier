

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.chat_message import ChatMessage
from ..types.http_validation_error import HttpValidationError
from ..types.language_model import LanguageModel
from ..types.post_chat_completion_response import PostChatCompletionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_chat_completion(
        self,
        domain: str,
        *,
        messages: typing.Sequence[ChatMessage],
        model: typing.Optional[LanguageModel] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        system_prompt: typing.Optional[str] = OMIT,
        rewrite_query: typing.Optional[bool] = OMIT,
        user_is_authed: typing.Optional[bool] = OMIT,
        allowed_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        source: typing.Optional[str] = OMIT,
        basepaths: typing.Optional[typing.Sequence[str]] = OMIT,
        skip_save_query: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostChatCompletionResponse]:
        """
        Parameters
        ----------
        domain : str

        messages : typing.Sequence[ChatMessage]
            The messages to use for the chat completion

        model : typing.Optional[LanguageModel]
            The model to use for the chat completion

        max_tokens : typing.Optional[int]
            The maximum number of tokens to generate. Note: setting a token count lower than 2000 may result in incomplete responses. You can add a custom system prompt to control the verbosity of the response.

        system_prompt : typing.Optional[str]
            The system prompt to use for the chat completion

        rewrite_query : typing.Optional[bool]
            Whether to rewrite the query using query decomposition

        user_is_authed : typing.Optional[bool]
            Whether the requesting user is authenticated. When true, authed chunks are included in results.

        allowed_roles : typing.Optional[typing.Sequence[str]]
            Roles the authenticated user has. Used to filter chunks by role-based access control.

        source : typing.Optional[str]
            The origin of the request (e.g. 'web', 'slack', 'api').

        basepaths : typing.Optional[typing.Sequence[str]]
            Restrict retrieval to pages under these URL path prefixes (e.g. ['/my-product']). Matches the scoping the Ask AI widget applies when embedded under a product path. Omit to search the whole site.

        skip_save_query : typing.Optional[bool]
            Set to true for test or eval traffic. The request is answered (and billed) normally but is excluded from usage analytics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostChatCompletionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chat/{encode_path_param(domain)}",
            method="POST",
            json={
                "model": model,
                "max_tokens": max_tokens,
                "system_prompt": system_prompt,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "rewrite_query": rewrite_query,
                "user_is_authed": user_is_authed,
                "allowed_roles": allowed_roles,
                "source": source,
                "basepaths": basepaths,
                "skip_save_query": skip_save_query,
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
                    PostChatCompletionResponse,
                    parse_obj_as(
                        type_=PostChatCompletionResponse,
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


class AsyncRawChatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_chat_completion(
        self,
        domain: str,
        *,
        messages: typing.Sequence[ChatMessage],
        model: typing.Optional[LanguageModel] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        system_prompt: typing.Optional[str] = OMIT,
        rewrite_query: typing.Optional[bool] = OMIT,
        user_is_authed: typing.Optional[bool] = OMIT,
        allowed_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        source: typing.Optional[str] = OMIT,
        basepaths: typing.Optional[typing.Sequence[str]] = OMIT,
        skip_save_query: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostChatCompletionResponse]:
        """
        Parameters
        ----------
        domain : str

        messages : typing.Sequence[ChatMessage]
            The messages to use for the chat completion

        model : typing.Optional[LanguageModel]
            The model to use for the chat completion

        max_tokens : typing.Optional[int]
            The maximum number of tokens to generate. Note: setting a token count lower than 2000 may result in incomplete responses. You can add a custom system prompt to control the verbosity of the response.

        system_prompt : typing.Optional[str]
            The system prompt to use for the chat completion

        rewrite_query : typing.Optional[bool]
            Whether to rewrite the query using query decomposition

        user_is_authed : typing.Optional[bool]
            Whether the requesting user is authenticated. When true, authed chunks are included in results.

        allowed_roles : typing.Optional[typing.Sequence[str]]
            Roles the authenticated user has. Used to filter chunks by role-based access control.

        source : typing.Optional[str]
            The origin of the request (e.g. 'web', 'slack', 'api').

        basepaths : typing.Optional[typing.Sequence[str]]
            Restrict retrieval to pages under these URL path prefixes (e.g. ['/my-product']). Matches the scoping the Ask AI widget applies when embedded under a product path. Omit to search the whole site.

        skip_save_query : typing.Optional[bool]
            Set to true for test or eval traffic. The request is answered (and billed) normally but is excluded from usage analytics.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostChatCompletionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chat/{encode_path_param(domain)}",
            method="POST",
            json={
                "model": model,
                "max_tokens": max_tokens,
                "system_prompt": system_prompt,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[ChatMessage], direction="write"
                ),
                "rewrite_query": rewrite_query,
                "user_is_authed": user_is_authed,
                "allowed_roles": allowed_roles,
                "source": source,
                "basepaths": basepaths,
                "skip_save_query": skip_save_query,
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
                    PostChatCompletionResponse,
                    parse_obj_as(
                        type_=PostChatCompletionResponse,
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
