

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
from ..types.items_result_of_project import ItemsResultOfProject
from ..types.items_result_of_project_membership import ItemsResultOfProjectMembership
from ..types.project import Project
from ..types.project_membership import ProjectMembership
from ..types.sort_direction import SortDirection
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getprojects(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemsResultOfProject]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        user_id : typing.Optional[str]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemsResultOfProject]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Projects",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "userId": user_id,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfProject,
                    parse_obj_as(
                        type_=ItemsResultOfProject,
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

    def createproject(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Project]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Projects",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
                "organizationId": create_project_organization_id,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def getproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Project]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        update_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Project]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        update_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
                "organizationId": update_project_organization_id,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def deleteproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
            },
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

    def getprojectmemberships(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemsResultOfProjectMembership]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemsResultOfProjectMembership]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfProjectMembership,
                    parse_obj_as(
                        type_=ItemsResultOfProjectMembership,
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

    def createprojectmembership(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectMembership]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "userId": user_id,
                "from": from_,
                "thru": thru,
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
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    def getprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectMembership]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    def updateprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectMembership]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "from": from_,
                "thru": thru,
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
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    def deleteprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
            },
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


class AsyncRawProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getprojects(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemsResultOfProject]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        user_id : typing.Optional[str]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemsResultOfProject]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Projects",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "userId": user_id,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfProject,
                    parse_obj_as(
                        type_=ItemsResultOfProject,
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

    async def createproject(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Project]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Projects",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
                "organizationId": create_project_organization_id,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def getproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Project]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        update_project_organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Project]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        update_project_organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
                "organizationId": update_project_organization_id,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def deleteproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
            },
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

    async def getprojectmemberships(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemsResultOfProjectMembership]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemsResultOfProjectMembership]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfProjectMembership,
                    parse_obj_as(
                        type_=ItemsResultOfProjectMembership,
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

    async def createprojectmembership(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectMembership]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "userId": user_id,
                "from": from_,
                "thru": thru,
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
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    async def getprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectMembership]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    async def updateprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        from_: typing.Optional[dt.datetime] = OMIT,
        thru: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectMembership]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        from_ : typing.Optional[dt.datetime]

        thru : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectMembership]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "from": from_,
                "thru": thru,
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
                    ProjectMembership,
                    parse_obj_as(
                        type_=ProjectMembership,
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

    async def deleteprojectmembership(
        self,
        id: int,
        membership_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        membership_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Projects/{encode_path_param(id)}/Memberships/{encode_path_param(membership_id)}",
            method="DELETE",
            params={
                "organizationId": organization_id,
            },
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
