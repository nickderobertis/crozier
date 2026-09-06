

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
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.acl_object_id import AclObjectId
from ..types.acl_object_type import AclObjectType
from ..types.app_limit_param import AppLimitParam
from ..types.create_view_view_type import CreateViewViewType
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.starting_after import StartingAfter
from ..types.view import View
from ..types.view_data import ViewData
from ..types.view_id_param import ViewIdParam
from ..types.view_name import ViewName
from ..types.view_options import ViewOptions
from ..types.view_type import ViewType
from .types.get_view_response import GetViewResponse
from .types.patch_view_view_type import PatchViewViewType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawViewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        view_name: typing.Optional[ViewName] = None,
        view_type: typing.Optional[ViewType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetViewResponse]:
        """
        List out all views. The views are sorted by creation date, with the most recently-created views coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        view_name : typing.Optional[ViewName]
            Name of the view to search for

        view_type : typing.Optional[ViewType]
            Type of object that the view corresponds to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetViewResponse]
            Returns a list of view objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/view",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "view_name": view_name,
                "view_type": view_type,
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetViewResponse,
                    parse_obj_as(
                        type_=GetViewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[View]:
        """
        Create a new view. If there is an existing view with the same name as the one specified in the request, will return the existing view unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[View]
            Returns the new view object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/view",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
                "deleted_at": deleted_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def put_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[View]:
        """
        Create or replace view. If there is an existing view with the same name as the one specified in the request, will replace the existing view with the provided fields

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[View]
            Returns the new view object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/view",
            method="PUT",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
                "deleted_at": deleted_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def get_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[View]:
        """
        Get a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[View]
            Returns the view object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="GET",
            params={
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def delete_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[View]:
        """
        Delete a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[View]
            Returns the deleted view object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="DELETE",
            json={
                "object_type": object_type,
                "object_id": object_id,
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
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def patch_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: typing.Optional[PatchViewViewType] = OMIT,
        name: typing.Optional[str] = OMIT,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[View]:
        """
        Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : typing.Optional[PatchViewViewType]
            Type of object that the view corresponds to.

        name : typing.Optional[str]
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[View]
            Returns the view object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="PATCH",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
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
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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


class AsyncRawViewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        view_name: typing.Optional[ViewName] = None,
        view_type: typing.Optional[ViewType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetViewResponse]:
        """
        List out all views. The views are sorted by creation date, with the most recently-created views coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        view_name : typing.Optional[ViewName]
            Name of the view to search for

        view_type : typing.Optional[ViewType]
            Type of object that the view corresponds to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetViewResponse]
            Returns a list of view objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/view",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "view_name": view_name,
                "view_type": view_type,
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetViewResponse,
                    parse_obj_as(
                        type_=GetViewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[View]:
        """
        Create a new view. If there is an existing view with the same name as the one specified in the request, will return the existing view unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[View]
            Returns the new view object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/view",
            method="POST",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
                "deleted_at": deleted_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def put_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[View]:
        """
        Create or replace view. If there is an existing view with the same name as the one specified in the request, will replace the existing view with the provided fields

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[View]
            Returns the new view object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/view",
            method="PUT",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
                "deleted_at": deleted_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[View]:
        """
        Get a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[View]
            Returns the view object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="GET",
            params={
                "object_type": object_type,
                "object_id": object_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def delete_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[View]:
        """
        Delete a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[View]
            Returns the deleted view object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="DELETE",
            json={
                "object_type": object_type,
                "object_id": object_id,
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
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def patch_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: typing.Optional[PatchViewViewType] = OMIT,
        name: typing.Optional[str] = OMIT,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[View]:
        """
        Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : typing.Optional[PatchViewViewType]
            Type of object that the view corresponds to.

        name : typing.Optional[str]
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[View]
            Returns the view object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/view/{encode_path_param(view_id)}",
            method="PATCH",
            json={
                "object_type": object_type,
                "object_id": object_id,
                "view_type": view_type,
                "name": name,
                "view_data": convert_and_respect_annotation_metadata(
                    object_=view_data, annotation=typing.Optional[ViewData], direction="write"
                ),
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[ViewOptions], direction="write"
                ),
                "user_id": user_id,
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
                    View,
                    parse_obj_as(
                        type_=View,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
