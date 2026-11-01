

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.axis_section_treeless import AxisSectionTreeless
from .types.get_api_v3axes_response import GetApiV3AxesResponse
from .types.get_api_v3axis_sections_axis_section_id_response import GetApiV3AxisSectionsAxisSectionIdResponse
from .types.get_api_v3axissections_response import GetApiV3AxissectionsResponse
from .types.post_api_v3axis_sections_response import PostApiV3AxisSectionsResponse
from .types.put_api_v3axis_sections_axis_section_id_response import PutApiV3AxisSectionsAxisSectionIdResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAxisSectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_v3axes(
        self,
        *,
        paging: str,
        id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        is_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetApiV3AxesResponse]:
        """
        List all Axes satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on axes unique identifiers.

        is_active : typing.Optional[bool]
            Filter on axes active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiV3AxesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/axes",
            method="GET",
            params={
                "id": id,
                "isActive": is_active,
                "paging": paging,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxesResponse,
                    parse_obj_as(
                        type_=GetApiV3AxesResponse,
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

    def get_api_v3axissections(
        self,
        *,
        paging: str,
        axis_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        owner_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetApiV3AxissectionsResponse]:
        """
        List all AxisSections satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        axis_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the axis it belongs to.

        owner_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the owner managing it.

        active : typing.Optional[bool]
            Filter on active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiV3AxissectionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/axisSections",
            method="GET",
            params={
                "paging": paging,
                "axisId": axis_id,
                "ownerId": owner_id,
                "active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxissectionsResponse,
                    parse_obj_as(
                        type_=GetApiV3AxissectionsResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def post_api_v3axis_sections(
        self,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiV3AxisSectionsResponse]:
        """
        Create a new AxisSection.

        Parameters
        ----------
        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiV3AxisSectionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/axisSections",
            method="POST",
            json={
                "parentAxisSections": convert_and_respect_annotation_metadata(
                    object_=parent_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "childrenAxisSections": convert_and_respect_annotation_metadata(
                    object_=children_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "id": id,
                "name": name,
                "url": url,
                "code": code,
                "multilingualName": multilingual_name,
                "description": description,
                "ownerId": owner_id,
                "startOn": start_on,
                "endOn": end_on,
                "active": active,
                "axisId": axis_id,
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
                    PostApiV3AxisSectionsResponse,
                    parse_obj_as(
                        type_=PostApiV3AxisSectionsResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetApiV3AxisSectionsAxisSectionIdResponse]:
        """
        Retrieve a single AxisSection by its unique identifier.

        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiV3AxisSectionsAxisSectionIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxisSectionsAxisSectionIdResponse,
                    parse_obj_as(
                        type_=GetApiV3AxisSectionsAxisSectionIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def put_api_v3axis_sections_axis_section_id(
        self,
        axis_section_id: int,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutApiV3AxisSectionsAxisSectionIdResponse]:
        """
        Partial or complete update to an existing AxisSection.

        Parameters
        ----------
        axis_section_id : int

        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutApiV3AxisSectionsAxisSectionIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="PUT",
            json={
                "parentAxisSections": convert_and_respect_annotation_metadata(
                    object_=parent_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "childrenAxisSections": convert_and_respect_annotation_metadata(
                    object_=children_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "id": id,
                "name": name,
                "url": url,
                "code": code,
                "multilingualName": multilingual_name,
                "description": description,
                "ownerId": owner_id,
                "startOn": start_on,
                "endOn": end_on,
                "active": active,
                "axisId": axis_id,
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
                    PutApiV3AxisSectionsAxisSectionIdResponse,
                    parse_obj_as(
                        type_=PutApiV3AxisSectionsAxisSectionIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawAxisSectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_v3axes(
        self,
        *,
        paging: str,
        id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        is_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetApiV3AxesResponse]:
        """
        List all Axes satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on axes unique identifiers.

        is_active : typing.Optional[bool]
            Filter on axes active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiV3AxesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/axes",
            method="GET",
            params={
                "id": id,
                "isActive": is_active,
                "paging": paging,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxesResponse,
                    parse_obj_as(
                        type_=GetApiV3AxesResponse,
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

    async def get_api_v3axissections(
        self,
        *,
        paging: str,
        axis_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        owner_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetApiV3AxissectionsResponse]:
        """
        List all AxisSections satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        axis_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the axis it belongs to.

        owner_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            Filter on the owner managing it.

        active : typing.Optional[bool]
            Filter on active status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiV3AxissectionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/axisSections",
            method="GET",
            params={
                "paging": paging,
                "axisId": axis_id,
                "ownerId": owner_id,
                "active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxissectionsResponse,
                    parse_obj_as(
                        type_=GetApiV3AxissectionsResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def post_api_v3axis_sections(
        self,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiV3AxisSectionsResponse]:
        """
        Create a new AxisSection.

        Parameters
        ----------
        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiV3AxisSectionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/axisSections",
            method="POST",
            json={
                "parentAxisSections": convert_and_respect_annotation_metadata(
                    object_=parent_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "childrenAxisSections": convert_and_respect_annotation_metadata(
                    object_=children_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "id": id,
                "name": name,
                "url": url,
                "code": code,
                "multilingualName": multilingual_name,
                "description": description,
                "ownerId": owner_id,
                "startOn": start_on,
                "endOn": end_on,
                "active": active,
                "axisId": axis_id,
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
                    PostApiV3AxisSectionsResponse,
                    parse_obj_as(
                        type_=PostApiV3AxisSectionsResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetApiV3AxisSectionsAxisSectionIdResponse]:
        """
        Retrieve a single AxisSection by its unique identifier.

        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiV3AxisSectionsAxisSectionIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiV3AxisSectionsAxisSectionIdResponse,
                    parse_obj_as(
                        type_=GetApiV3AxisSectionsAxisSectionIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def put_api_v3axis_sections_axis_section_id(
        self,
        axis_section_id: int,
        *,
        code: str,
        multilingual_name: str,
        axis_id: int,
        parent_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        children_axis_sections: typing.Optional[typing.Sequence[AxisSectionTreeless]] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[int] = OMIT,
        start_on: typing.Optional[dt.datetime] = OMIT,
        end_on: typing.Optional[dt.datetime] = OMIT,
        active: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutApiV3AxisSectionsAxisSectionIdResponse]:
        """
        Partial or complete update to an existing AxisSection.

        Parameters
        ----------
        axis_section_id : int

        code : str

        multilingual_name : str

        axis_id : int

        parent_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        children_axis_sections : typing.Optional[typing.Sequence[AxisSectionTreeless]]

        id : typing.Optional[int]

        name : typing.Optional[str]

        url : typing.Optional[str]

        description : typing.Optional[str]

        owner_id : typing.Optional[int]

        start_on : typing.Optional[dt.datetime]

        end_on : typing.Optional[dt.datetime]

        active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutApiV3AxisSectionsAxisSectionIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="PUT",
            json={
                "parentAxisSections": convert_and_respect_annotation_metadata(
                    object_=parent_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "childrenAxisSections": convert_and_respect_annotation_metadata(
                    object_=children_axis_sections, annotation=typing.Sequence[AxisSectionTreeless], direction="write"
                ),
                "id": id,
                "name": name,
                "url": url,
                "code": code,
                "multilingualName": multilingual_name,
                "description": description,
                "ownerId": owner_id,
                "startOn": start_on,
                "endOn": end_on,
                "active": active,
                "axisId": axis_id,
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
                    PutApiV3AxisSectionsAxisSectionIdResponse,
                    parse_obj_as(
                        type_=PutApiV3AxisSectionsAxisSectionIdResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_api_v3axis_sections_axis_section_id(
        self, axis_section_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        axis_section_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/axisSections/{encode_path_param(axis_section_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
