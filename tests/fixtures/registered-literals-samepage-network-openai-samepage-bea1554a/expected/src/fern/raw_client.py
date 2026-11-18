

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.notebooks_get_response import NotebooksGetResponse
from .types.page_post_response import PagePostResponse
from .types.query_post_response import QueryPostResponse
from .types.query_request_conditions_item import QueryRequestConditionsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotebooksGetResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotebooksGetResponse]
            A list of notebooks this account has access to
        """
        _response = self._client_wrapper.httpx_client.request(
            "extensions/openai/notebooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotebooksGetResponse,
                    parse_obj_as(
                        type_=NotebooksGetResponse,
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

    def page(
        self, *, notebook_uuid: str, notebook_page_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PagePostResponse]:
        """
        Parameters
        ----------
        notebook_uuid : str
            The application to request. Must be in UUID format.

        notebook_page_id : str
            The page from the application to request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagePostResponse]
            Page data in the SamePage AtJson format
        """
        _response = self._client_wrapper.httpx_client.request(
            "extensions/openai/page",
            method="POST",
            json={
                "notebookUuid": notebook_uuid,
                "notebookPageId": notebook_page_id,
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
                    PagePostResponse,
                    parse_obj_as(
                        type_=PagePostResponse,
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

    def query(
        self,
        *,
        targets: typing.Sequence[str],
        conditions: typing.Sequence[QueryRequestConditionsItem],
        return_node: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryPostResponse]:
        """
        Parameters
        ----------
        targets : typing.Sequence[str]
            The notebook ids this query should target.

        conditions : typing.Sequence[QueryRequestConditionsItem]
            The conditions that muse be met to satisfy the query

        return_node : str
            The node acting as the source of the entire query

        label : str
            The human-readable label to assign to this query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryPostResponse]
            The data shared to the SamePage Network
        """
        _response = self._client_wrapper.httpx_client.request(
            "extensions/openai/query",
            method="POST",
            json={
                "targets": targets,
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[QueryRequestConditionsItem], direction="write"
                ),
                "returnNode": return_node,
                "label": label,
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
                    QueryPostResponse,
                    parse_obj_as(
                        type_=QueryPostResponse,
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

    async def notebooks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotebooksGetResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotebooksGetResponse]
            A list of notebooks this account has access to
        """
        _response = await self._client_wrapper.httpx_client.request(
            "extensions/openai/notebooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotebooksGetResponse,
                    parse_obj_as(
                        type_=NotebooksGetResponse,
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

    async def page(
        self, *, notebook_uuid: str, notebook_page_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PagePostResponse]:
        """
        Parameters
        ----------
        notebook_uuid : str
            The application to request. Must be in UUID format.

        notebook_page_id : str
            The page from the application to request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagePostResponse]
            Page data in the SamePage AtJson format
        """
        _response = await self._client_wrapper.httpx_client.request(
            "extensions/openai/page",
            method="POST",
            json={
                "notebookUuid": notebook_uuid,
                "notebookPageId": notebook_page_id,
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
                    PagePostResponse,
                    parse_obj_as(
                        type_=PagePostResponse,
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

    async def query(
        self,
        *,
        targets: typing.Sequence[str],
        conditions: typing.Sequence[QueryRequestConditionsItem],
        return_node: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryPostResponse]:
        """
        Parameters
        ----------
        targets : typing.Sequence[str]
            The notebook ids this query should target.

        conditions : typing.Sequence[QueryRequestConditionsItem]
            The conditions that muse be met to satisfy the query

        return_node : str
            The node acting as the source of the entire query

        label : str
            The human-readable label to assign to this query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryPostResponse]
            The data shared to the SamePage Network
        """
        _response = await self._client_wrapper.httpx_client.request(
            "extensions/openai/query",
            method="POST",
            json={
                "targets": targets,
                "conditions": convert_and_respect_annotation_metadata(
                    object_=conditions, annotation=typing.Sequence[QueryRequestConditionsItem], direction="write"
                ),
                "returnNode": return_node,
                "label": label,
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
                    QueryPostResponse,
                    parse_obj_as(
                        type_=QueryPostResponse,
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
