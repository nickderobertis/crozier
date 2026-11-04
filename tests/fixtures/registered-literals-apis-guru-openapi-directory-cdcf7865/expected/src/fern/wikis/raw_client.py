

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.wiki_read_response import WikiReadResponse
from pydantic import ValidationError


class RawWikisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def wiki_read(
        self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WikiReadResponse]:
        """
        Retrieves the details about a specific wiki.
        A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WikiReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wikis/{encode_path_param(wiki_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WikiReadResponse,
                    parse_obj_as(
                        type_=WikiReadResponse,
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

    def wiki_content(
        self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Retrieves the plaintext content of a wiki in markdown format.
        #### Returns
        Returns `text/markdown` of the wiki content itself.
        If the request is unsuccessful, plaintext with the error message will be displayed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wikis/{encode_path_param(wiki_id)}/content/",
            method="GET",
            request_options=request_options,
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


class AsyncRawWikisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def wiki_read(
        self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WikiReadResponse]:
        """
        Retrieves the details about a specific wiki.
        A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WikiReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wikis/{encode_path_param(wiki_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WikiReadResponse,
                    parse_obj_as(
                        type_=WikiReadResponse,
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

    async def wiki_content(
        self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Retrieves the plaintext content of a wiki in markdown format.
        #### Returns
        Returns `text/markdown` of the wiki content itself.
        If the request is unsuccessful, plaintext with the error message will be displayed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wikis/{encode_path_param(wiki_id)}/content/",
            method="GET",
            request_options=request_options,
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
