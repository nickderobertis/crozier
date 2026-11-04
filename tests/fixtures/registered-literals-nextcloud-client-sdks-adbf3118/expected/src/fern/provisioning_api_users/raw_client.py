

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
from ..types.provisioning_api_groups_get_sub_admins_of_group200response import (
    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
)
from ..types.provisioning_api_users_add_user200response import ProvisioningApiUsersAddUser200Response
from ..types.provisioning_api_users_get_user200response import ProvisioningApiUsersGetUser200Response
from ..types.provisioning_api_users_search_by_phone_numbers200response import (
    ProvisioningApiUsersSearchByPhoneNumbers200Response,
)
from pydantic import ValidationError


class RawProvisioningApiUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
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
        HttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users",
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

    def add_user(
        self,
        *,
        userid: str,
        password: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        groups: typing.Optional[str] = None,
        subadmin: typing.Optional[str] = None,
        quota: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        manager: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiUsersAddUser200Response]:
        """
        Parameters
        ----------
        userid : str
            ID of the user

        password : typing.Optional[str]
            Password of the user

        display_name : typing.Optional[str]
            Display name of the user

        email : typing.Optional[str]
            Email of the user

        groups : typing.Optional[str]
            Groups of the user

        subadmin : typing.Optional[str]
            Groups where the user is subadmin

        quota : typing.Optional[str]
            Quota of the user

        language : typing.Optional[str]
            Language of the user

        manager : typing.Optional[str]
            Manager of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiUsersAddUser200Response]
            User added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users",
            method="POST",
            params={
                "userid": userid,
                "password": password,
                "displayName": display_name,
                "email": email,
                "groups": groups,
                "subadmin": subadmin,
                "quota": quota,
                "language": language,
                "manager": manager,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersAddUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersAddUser200Response,
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

    def get_users_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]:
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
        HttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users/details",
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

    def search_by_phone_numbers(
        self, *, location: str, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiUsersSearchByPhoneNumbers200Response]:
        """
        Parameters
        ----------
        location : str
            Location of the phone number (for country code)

        search : str
            Phone numbers to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiUsersSearchByPhoneNumbers200Response]
            Users returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users/search/by-phone",
            method="POST",
            params={
                "location": location,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersSearchByPhoneNumbers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersSearchByPhoneNumbers200Response,
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

    def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiUsersGetUser200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiUsersGetUser200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersGetUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersGetUser200Response,
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

    def edit_user(
        self, user_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        key : str
            Key that will be updated

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
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

    def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
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

    def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiUsersGetUser200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiUsersGetUser200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/user",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersGetUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersGetUser200Response,
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

    def get_editable_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/user/fields",
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

    def get_editable_fields_for_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/user/fields/{encode_path_param(user_id)}",
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

    def edit_user_multi_value(
        self,
        user_id: str,
        collection_name: str,
        *,
        key: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        collection_name : str
            Collection to update

        key : str
            Key that will be updated

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/{encode_path_param(collection_name)}",
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

    def wipe_user_devices(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/wipe",
            method="POST",
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

    def enable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/enable",
            method="PUT",
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

    def disable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/disable",
            method="PUT",
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

    def get_users_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetGroups200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetGroups200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="GET",
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

    def add_to_group(
        self,
        user_id: str,
        *,
        groupid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : typing.Optional[str]
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="POST",
            params={
                "groupid": groupid,
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

    def remove_from_group(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="DELETE",
            params={
                "groupid": groupid,
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

    def get_user_sub_admin_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
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

    def add_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
            method="POST",
            params={
                "groupid": groupid,
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

    def remove_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
            method="DELETE",
            params={
                "groupid": groupid,
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

    def resend_welcome_message(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/welcome",
            method="POST",
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


class AsyncRawProvisioningApiUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_users(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]:
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
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsers200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users",
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

    async def add_user(
        self,
        *,
        userid: str,
        password: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        groups: typing.Optional[str] = None,
        subadmin: typing.Optional[str] = None,
        quota: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        manager: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiUsersAddUser200Response]:
        """
        Parameters
        ----------
        userid : str
            ID of the user

        password : typing.Optional[str]
            Password of the user

        display_name : typing.Optional[str]
            Display name of the user

        email : typing.Optional[str]
            Email of the user

        groups : typing.Optional[str]
            Groups of the user

        subadmin : typing.Optional[str]
            Groups where the user is subadmin

        quota : typing.Optional[str]
            Quota of the user

        language : typing.Optional[str]
            Language of the user

        manager : typing.Optional[str]
            Manager of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiUsersAddUser200Response]
            User added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users",
            method="POST",
            params={
                "userid": userid,
                "password": password,
                "displayName": display_name,
                "email": email,
                "groups": groups,
                "subadmin": subadmin,
                "quota": quota,
                "language": language,
                "manager": manager,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersAddUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersAddUser200Response,
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

    async def get_users_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]:
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
        AsyncHttpResponse[ProvisioningApiGroupsGetGroupUsersDetails200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users/details",
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

    async def search_by_phone_numbers(
        self, *, location: str, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiUsersSearchByPhoneNumbers200Response]:
        """
        Parameters
        ----------
        location : str
            Location of the phone number (for country code)

        search : str
            Phone numbers to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiUsersSearchByPhoneNumbers200Response]
            Users returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/users/search/by-phone",
            method="POST",
            params={
                "location": location,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersSearchByPhoneNumbers200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersSearchByPhoneNumbers200Response,
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

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiUsersGetUser200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiUsersGetUser200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersGetUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersGetUser200Response,
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

    async def edit_user(
        self, user_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        key : str
            Key that will be updated

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
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

    async def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}",
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

    async def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiUsersGetUser200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiUsersGetUser200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/user",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiUsersGetUser200Response,
                    parse_obj_as(
                        type_=ProvisioningApiUsersGetUser200Response,
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

    async def get_editable_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/cloud/user/fields",
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

    async def get_editable_fields_for_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/user/fields/{encode_path_param(user_id)}",
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

    async def edit_user_multi_value(
        self,
        user_id: str,
        collection_name: str,
        *,
        key: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        collection_name : str
            Collection to update

        key : str
            Key that will be updated

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/{encode_path_param(collection_name)}",
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

    async def wipe_user_devices(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/wipe",
            method="POST",
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

    async def enable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/enable",
            method="PUT",
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

    async def disable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/disable",
            method="PUT",
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

    async def get_users_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetGroups200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetGroups200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="GET",
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

    async def add_to_group(
        self,
        user_id: str,
        *,
        groupid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : typing.Optional[str]
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="POST",
            params={
                "groupid": groupid,
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

    async def remove_from_group(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/groups",
            method="DELETE",
            params={
                "groupid": groupid,
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

    async def get_user_sub_admin_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiGroupsGetSubAdminsOfGroup200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
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

    async def add_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
            method="POST",
            params={
                "groupid": groupid,
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

    async def remove_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        user_id : str
            ID of the user

        groupid : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/subadmins",
            method="DELETE",
            params={
                "groupid": groupid,
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

    async def resend_welcome_message(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/cloud/users/{encode_path_param(user_id)}/welcome",
            method="POST",
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
