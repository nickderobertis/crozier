

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
from ..types.delete_snippet_response import DeleteSnippetResponse
from ..types.retrieve_snippet_response import RetrieveSnippetResponse
from ..types.snippet import Snippet
from ..types.upsert_snippet_response import UpsertSnippetResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSnippetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveSnippetResponse]:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveSnippetResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveSnippetResponse,
                    parse_obj_as(
                        type_=RetrieveSnippetResponse,
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

    def upsert_snippet(
        self, site_id: str, *, snippet: Snippet, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpsertSnippetResponse]:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : Snippet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpsertSnippetResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="POST",
            json={
                "snippet": convert_and_respect_annotation_metadata(
                    object_=snippet, annotation=Snippet, direction="write"
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
                    UpsertSnippetResponse,
                    parse_obj_as(
                        type_=UpsertSnippetResponse,
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

    def delete_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteSnippetResponse]:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteSnippetResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSnippetResponse,
                    parse_obj_as(
                        type_=DeleteSnippetResponse,
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


class AsyncRawSnippetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveSnippetResponse]:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveSnippetResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveSnippetResponse,
                    parse_obj_as(
                        type_=RetrieveSnippetResponse,
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

    async def upsert_snippet(
        self, site_id: str, *, snippet: Snippet, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpsertSnippetResponse]:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : Snippet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpsertSnippetResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="POST",
            json={
                "snippet": convert_and_respect_annotation_metadata(
                    object_=snippet, annotation=Snippet, direction="write"
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
                    UpsertSnippetResponse,
                    parse_obj_as(
                        type_=UpsertSnippetResponse,
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

    async def delete_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteSnippetResponse]:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteSnippetResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/sites/{encode_path_param(site_id)}/snippet",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSnippetResponse,
                    parse_obj_as(
                        type_=DeleteSnippetResponse,
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
