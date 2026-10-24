

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.item import Item
from ..types.section import Section
from ..types.section_result import SectionResult
from ..types.write_result import WriteResult
from .types.update_section_response import UpdateSectionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_section(
        self,
        filename: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SectionResult]:
        """
        Appends a new section. A `name` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        name : str
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SectionResult]
            Section added
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections",
            method="POST",
            json={
                "name": name,
                "icon": icon,
                "displayData": display_data,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "widgets": widgets,
                "filteredItems": filtered_items,
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
                    SectionResult,
                    parse_obj_as(
                        type_=SectionResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Section]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Section]
            Section
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Section,
                    parse_obj_as(
                        type_=Section,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def delete_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WriteResult]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WriteResult]
            Saved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WriteResult,
                    parse_obj_as(
                        type_=WriteResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def update_section(
        self,
        filename: str,
        sid: str,
        *,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSectionResponse]:
        """
        Shallow-merges the supplied fields. Sending `items` replaces the whole array.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        name : typing.Optional[str]
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSectionResponse]
            Updated section
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="PATCH",
            json={
                "name": name,
                "icon": icon,
                "displayData": display_data,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "widgets": widgets,
                "filteredItems": filtered_items,
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
                    UpdateSectionResponse,
                    parse_obj_as(
                        type_=UpdateSectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawSectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_section(
        self,
        filename: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SectionResult]:
        """
        Appends a new section. A `name` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        name : str
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SectionResult]
            Section added
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections",
            method="POST",
            json={
                "name": name,
                "icon": icon,
                "displayData": display_data,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "widgets": widgets,
                "filteredItems": filtered_items,
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
                    SectionResult,
                    parse_obj_as(
                        type_=SectionResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Section]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Section]
            Section
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Section,
                    parse_obj_as(
                        type_=Section,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def delete_section(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WriteResult]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WriteResult]
            Saved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WriteResult,
                    parse_obj_as(
                        type_=WriteResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def update_section(
        self,
        filename: str,
        sid: str,
        *,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        widgets: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        filtered_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSectionResponse]:
        """
        Shallow-merges the supplied fields. Sending `items` replaces the whole array.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        name : typing.Optional[str]
            Section heading (unique)

        icon : typing.Optional[str]
            Section icon

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-section display options

        items : typing.Optional[typing.Sequence[Item]]
            The links/apps in this section

        widgets : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Widgets shown in this section

        filtered_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Items pulled from another source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSectionResponse]
            Updated section
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}",
            method="PATCH",
            json={
                "name": name,
                "icon": icon,
                "displayData": display_data,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "widgets": widgets,
                "filteredItems": filtered_items,
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
                    UpdateSectionResponse,
                    parse_obj_as(
                        type_=UpdateSectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
