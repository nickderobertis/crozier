

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.items_result_of_team import ItemsResultOfTeam
from ..types.items_result_of_team_membership import ItemsResultOfTeamMembership
from ..types.sort_direction import SortDirection
from ..types.team import Team
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getteams(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemsResultOfTeam]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemsResultOfTeam]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Teams",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfTeam,
                    parse_obj_as(
                        type_=ItemsResultOfTeam,
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

    def createteam(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Team]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/Teams",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    def getteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Team]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    def updateteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Team]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Team]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    def deleteteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
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

    def addmember(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Members",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def removemember(
        self,
        id: str,
        user_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        user_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Members/{encode_path_param(user_id)}",
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

    def getmemberships(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemsResultOfTeamMembership]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemsResultOfTeamMembership]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Memberships",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfTeamMembership,
                    parse_obj_as(
                        type_=ItemsResultOfTeamMembership,
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


class AsyncRawTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getteams(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemsResultOfTeam]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemsResultOfTeam]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Teams",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfTeam,
                    parse_obj_as(
                        type_=ItemsResultOfTeam,
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

    async def createteam(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Team]:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/Teams",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    async def getteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Team]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
            method="GET",
            params={
                "organizationId": organization_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    async def updateteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Team]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Team]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
            method="PUT",
            params={
                "organizationId": organization_id,
            },
            json={
                "name": name,
                "description": description,
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
                    Team,
                    parse_obj_as(
                        type_=Team,
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

    async def deleteteam(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}",
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

    async def addmember(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        user_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Members",
            method="POST",
            params={
                "organizationId": organization_id,
            },
            json={
                "userId": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def removemember(
        self,
        id: str,
        user_id: str,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        user_id : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Members/{encode_path_param(user_id)}",
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

    async def getmemberships(
        self,
        id: str,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemsResultOfTeamMembership]:
        """
        Parameters
        ----------
        id : str

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_string : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemsResultOfTeamMembership]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/Teams/{encode_path_param(id)}/Memberships",
            method="GET",
            params={
                "organizationId": organization_id,
                "page": page,
                "pageSize": page_size,
                "searchString": search_string,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemsResultOfTeamMembership,
                    parse_obj_as(
                        type_=ItemsResultOfTeamMembership,
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
