

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
from ..errors.bad_request_error import BadRequestError
from ..types.page_id_parent_request import PageIdParentRequest
from ..types.rich_text_request import RichTextRequest
from ..types.sort_object import SortObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDataSourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def query_data_source(
        self,
        data_source_id: str,
        *,
        filter_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.Sequence[SortObject]] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Query a data source (database) using filters and sorts

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source (database)

        filter_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of page property value IDs to limit the response

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter conditions for querying the data source

        sorts : typing.Optional[typing.Sequence[SortObject]]

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        archived : typing.Optional[bool]

        in_trash : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}/query",
            method="POST",
            params={
                "filter_properties": filter_properties,
            },
            json={
                "filter": filter,
                "sorts": convert_and_respect_annotation_metadata(
                    object_=sorts, annotation=typing.Sequence[SortObject], direction="write"
                ),
                "start_cursor": start_cursor,
                "page_size": page_size,
                "archived": archived,
                "in_trash": in_trash,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def retrieve_a_data_source(
        self, data_source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Retrieve metadata and schema for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_a_data_source(
        self,
        data_source_id: str,
        *,
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        description: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update properties of a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        description : typing.Optional[typing.Sequence[RichTextRequest]]

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            Property schema updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}",
            method="PATCH",
            json={
                "title": convert_and_respect_annotation_metadata(
                    object_=title, annotation=typing.Sequence[RichTextRequest], direction="write"
                ),
                "description": convert_and_respect_annotation_metadata(
                    object_=description, annotation=typing.Sequence[RichTextRequest], direction="write"
                ),
                "properties": properties,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def create_a_data_source(
        self,
        *,
        parent: PageIdParentRequest,
        properties: typing.Dict[str, typing.Any],
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Create a new data source (database)

        Parameters
        ----------
        parent : PageIdParentRequest

        properties : typing.Dict[str, typing.Any]
            Property schema of data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/data_sources",
            method="POST",
            json={
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=PageIdParentRequest, direction="write"
                ),
                "properties": properties,
                "title": convert_and_respect_annotation_metadata(
                    object_=title, annotation=typing.Sequence[RichTextRequest], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def list_data_source_templates(
        self,
        data_source_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        List available templates for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}/templates",
            method="GET",
            params={
                "start_cursor": start_cursor,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawDataSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def query_data_source(
        self,
        data_source_id: str,
        *,
        filter_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sorts: typing.Optional[typing.Sequence[SortObject]] = OMIT,
        start_cursor: typing.Optional[str] = OMIT,
        page_size: typing.Optional[int] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        in_trash: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Query a data source (database) using filters and sorts

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source (database)

        filter_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of page property value IDs to limit the response

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter conditions for querying the data source

        sorts : typing.Optional[typing.Sequence[SortObject]]

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        archived : typing.Optional[bool]

        in_trash : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}/query",
            method="POST",
            params={
                "filter_properties": filter_properties,
            },
            json={
                "filter": filter,
                "sorts": convert_and_respect_annotation_metadata(
                    object_=sorts, annotation=typing.Sequence[SortObject], direction="write"
                ),
                "start_cursor": start_cursor,
                "page_size": page_size,
                "archived": archived,
                "in_trash": in_trash,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def retrieve_a_data_source(
        self, data_source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Retrieve metadata and schema for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_a_data_source(
        self,
        data_source_id: str,
        *,
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        description: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        properties: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Update properties of a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        description : typing.Optional[typing.Sequence[RichTextRequest]]

        properties : typing.Optional[typing.Dict[str, typing.Any]]
            Property schema updates

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}",
            method="PATCH",
            json={
                "title": convert_and_respect_annotation_metadata(
                    object_=title, annotation=typing.Sequence[RichTextRequest], direction="write"
                ),
                "description": convert_and_respect_annotation_metadata(
                    object_=description, annotation=typing.Sequence[RichTextRequest], direction="write"
                ),
                "properties": properties,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def create_a_data_source(
        self,
        *,
        parent: PageIdParentRequest,
        properties: typing.Dict[str, typing.Any],
        title: typing.Optional[typing.Sequence[RichTextRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Create a new data source (database)

        Parameters
        ----------
        parent : PageIdParentRequest

        properties : typing.Dict[str, typing.Any]
            Property schema of data source

        title : typing.Optional[typing.Sequence[RichTextRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/data_sources",
            method="POST",
            json={
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=PageIdParentRequest, direction="write"
                ),
                "properties": properties,
                "title": convert_and_respect_annotation_metadata(
                    object_=title, annotation=typing.Sequence[RichTextRequest], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def list_data_source_templates(
        self,
        data_source_id: str,
        *,
        start_cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        List available templates for a data source

        Parameters
        ----------
        data_source_id : str
            Identifier for a Notion data source

        start_cursor : typing.Optional[str]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/data_sources/{encode_path_param(data_source_id)}/templates",
            method="GET",
            params={
                "start_cursor": start_cursor,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
