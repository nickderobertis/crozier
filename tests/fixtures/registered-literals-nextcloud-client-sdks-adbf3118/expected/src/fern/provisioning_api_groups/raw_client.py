

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.provisioning_api_groups_get_group_users200response import ProvisioningApiGroupsGetGroupUsers200Response
from ..types.provisioning_api_groups_get_group_users_details200response import (
    ProvisioningApiGroupsGetGroupUsersDetails200Response,
)
from ..types.provisioning_api_groups_get_groups200response import ProvisioningApiGroupsGetGroups200Response
from ..types.provisioning_api_groups_get_groups_details200response import (
    ProvisioningApiGroupsGetGroupsDetails200Response,
)
from ..types.provisioning_api_groups_get_sub_admins_of_group200response import (
    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
)
from pydantic import ValidationError


class RawProvisioningApiGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_groups(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiGroupsGetGroups200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroups200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroups200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroups200Response,
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

    def add_group(
        self,
        *,
        groupid: str,
        displayname: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        groupid : str
            ID of the group

        displayname : typing.Optional[str]
            Display name of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups",
            method="POST",
            params={
                "groupid": groupid,
                "displayname": displayname,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    def get_groups_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupsDetails200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroupsDetails200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups/details",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupsDetails200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupsDetails200Response,
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

    def get_group_users(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]
            User IDs returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsers200Response,
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

    def get_group_users_details(
        self,
        group_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/users/details",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsersDetails200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsersDetails200Response,
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

    def get_sub_admins_of_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/subadmins",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
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

    def get_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsers200Response,
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

    def update_group(
        self, group_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        key : str
            Key to update, only 'displayname'

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="PUT",
            params={
                "key": key,
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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


class AsyncRawProvisioningApiGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_groups(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroups200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroups200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroups200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroups200Response,
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

    async def add_group(
        self,
        *,
        groupid: str,
        displayname: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        groupid : str
            ID of the group

        displayname : typing.Optional[str]
            Display name of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups",
            method="POST",
            params={
                "groupid": groupid,
                "displayname": displayname,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    async def get_groups_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupsDetails200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupsDetails200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/groups/details",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupsDetails200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupsDetails200Response,
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

    async def get_group_users(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]
            User IDs returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsers200Response,
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

    async def get_group_users_details(
        self,
        group_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        search : typing.Optional[str]
            Text to search for

        limit : typing.Optional[int]
            Limit the amount of groups returned

        offset : typing.Optional[int]
            Offset for searching for groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/users/details",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsersDetails200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsersDetails200Response,
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

    async def get_sub_admins_of_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}/subadmins",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
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

    async def get_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiGroupsGetGroupUsers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiGroupsGetGroupUsers200Response,
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

    async def update_group(
        self, group_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        key : str
            Key to update, only 'displayname'

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="PUT",
            params={
                "key": key,
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    async def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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
