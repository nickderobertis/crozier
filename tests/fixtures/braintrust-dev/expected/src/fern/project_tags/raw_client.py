

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
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.project_tag import ProjectTag
from ..types.project_tag_id_param import ProjectTagIdParam
from ..types.project_tag_name import ProjectTagName
from ..types.starting_after import StartingAfter
from .types.get_project_tag_response import GetProjectTagResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectTagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_tag(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_tag_name: typing.Optional[ProjectTagName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetProjectTagResponse]:
        """
        List out all project_tags. The project_tags are sorted by creation date, with the most recently-created project_tags coming first

        Parameters
        ----------
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

        project_tag_name : typing.Optional[ProjectTagName]
            Name of the project_tag to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectTagResponse]
            Returns a list of project_tag objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "project_tag_name": project_tag_name,
                "project_name": project_name,
                "project_id": project_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectTagResponse,
                    parse_obj_as(
                        type_=GetProjectTagResponse,
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

    def post_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectTag]:
        """
        Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectTag]
            Returns the new project_tag object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "color": color,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    def put_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectTag]:
        """
        Create or replace project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will replace the existing project_tag with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectTag]
            Returns the new project_tag object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="PUT",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "color": color,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    def get_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectTag]:
        """
        Get a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectTag]
            Returns the project_tag object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    def delete_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectTag]:
        """
        Delete a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectTag]
            Returns the deleted project_tag object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    def patch_project_tag_id(
        self,
        project_tag_id: ProjectTagIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectTag]:
        """
        Partially update a project_tag object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        name : typing.Optional[str]
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectTag]
            Returns the project_tag object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "color": color,
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
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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


class AsyncRawProjectTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_tag(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        project_tag_name: typing.Optional[ProjectTagName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetProjectTagResponse]:
        """
        List out all project_tags. The project_tags are sorted by creation date, with the most recently-created project_tags coming first

        Parameters
        ----------
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

        project_tag_name : typing.Optional[ProjectTagName]
            Name of the project_tag to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectTagResponse]
            Returns a list of project_tag objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "project_tag_name": project_tag_name,
                "project_name": project_name,
                "project_id": project_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectTagResponse,
                    parse_obj_as(
                        type_=GetProjectTagResponse,
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

    async def post_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectTag]:
        """
        Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectTag]
            Returns the new project_tag object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "color": color,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    async def put_project_tag(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectTag]:
        """
        Create or replace project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will replace the existing project_tag with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the project tag belongs under

        name : str
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectTag]
            Returns the new project_tag object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/project_tag",
            method="PUT",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "color": color,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    async def get_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectTag]:
        """
        Get a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectTag]
            Returns the project_tag object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    async def delete_project_tag_id(
        self, project_tag_id: ProjectTagIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectTag]:
        """
        Delete a project_tag object by its id

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectTag]
            Returns the deleted project_tag object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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

    async def patch_project_tag_id(
        self,
        project_tag_id: ProjectTagIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectTag]:
        """
        Partially update a project_tag object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        project_tag_id : ProjectTagIdParam
            ProjectTag id

        name : typing.Optional[str]
            Name of the project tag

        description : typing.Optional[str]
            Textual description of the project tag

        color : typing.Optional[str]
            Color of the tag for the UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectTag]
            Returns the project_tag object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_tag/{encode_path_param(project_tag_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "color": color,
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
                    ProjectTag,
                    parse_obj_as(
                        type_=ProjectTag,
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
