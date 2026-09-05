

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.endpoint_get_markdown_emoticons import EndpointGetMarkdownEmoticons
from ..types.endpoint_post_markdown import EndpointPostMarkdown
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMarkdownClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_markdown(
        self,
        *,
        text_raw: str,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostMarkdown]:
        """
        Parameters
        ----------
        text_raw : str

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostMarkdown]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "markdown",
            method="POST",
            data={
                "text_emoticons": text_emoticons,
                "text_raw": text_raw,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMarkdown,
                    parse_obj_as(
                        type_=EndpointPostMarkdown,
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

    def get_markdown_emoticons(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetMarkdownEmoticons]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetMarkdownEmoticons]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "markdown/emoticons",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMarkdownEmoticons,
                    parse_obj_as(
                        type_=EndpointGetMarkdownEmoticons,
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


class AsyncRawMarkdownClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_markdown(
        self,
        *,
        text_raw: str,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostMarkdown]:
        """
        Parameters
        ----------
        text_raw : str

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostMarkdown]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "markdown",
            method="POST",
            data={
                "text_emoticons": text_emoticons,
                "text_raw": text_raw,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMarkdown,
                    parse_obj_as(
                        type_=EndpointPostMarkdown,
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

    async def get_markdown_emoticons(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetMarkdownEmoticons]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetMarkdownEmoticons]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "markdown/emoticons",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMarkdownEmoticons,
                    parse_obj_as(
                        type_=EndpointGetMarkdownEmoticons,
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
