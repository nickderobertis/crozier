

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
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
from .raw_client import AsyncRawProvisioningApiUsersClient, RawProvisioningApiUsersClient


class ProvisioningApiUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvisioningApiUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvisioningApiUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvisioningApiUsersClient
        """
        return self._raw_client

    def get_users(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
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
        ProvisioningApiGroupsGetGroupUsers200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_users()
        """
        _response = self._raw_client.get_users(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

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
    ) -> ProvisioningApiUsersAddUser200Response:
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
        ProvisioningApiUsersAddUser200Response
            User added successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.add_user(
            userid="userid",
        )
        """
        _response = self._raw_client.add_user(
            userid=userid,
            password=password,
            display_name=display_name,
            email=email,
            groups=groups,
            subadmin=subadmin,
            quota=quota,
            language=language,
            manager=manager,
            request_options=request_options,
        )
        return _response.data

    def get_users_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsersDetails200Response:
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
        ProvisioningApiGroupsGetGroupUsersDetails200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_users_details()
        """
        _response = self._raw_client.get_users_details(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def search_by_phone_numbers(
        self, *, location: str, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersSearchByPhoneNumbers200Response:
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
        ProvisioningApiUsersSearchByPhoneNumbers200Response
            Users returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.search_by_phone_numbers(
            location="location",
            search="search",
        )
        """
        _response = self._raw_client.search_by_phone_numbers(
            location=location, search=search, request_options=request_options
        )
        return _response.data

    def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersGetUser200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiUsersGetUser200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    def edit_user(
        self, user_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.edit_user(
            user_id="userId",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.edit_user(user_id, key=key, value=value, request_options=request_options)
        return _response.data

    def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.delete_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersGetUser200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiUsersGetUser200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_current_user()
        """
        _response = self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    def get_editable_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_editable_fields()
        """
        _response = self._raw_client.get_editable_fields(request_options=request_options)
        return _response.data

    def get_editable_fields_for_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_editable_fields_for_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_editable_fields_for_user(user_id, request_options=request_options)
        return _response.data

    def edit_user_multi_value(
        self,
        user_id: str,
        collection_name: str,
        *,
        key: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.edit_user_multi_value(
            user_id="userId",
            collection_name="collectionName",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.edit_user_multi_value(
            user_id, collection_name, key=key, value=value, request_options=request_options
        )
        return _response.data

    def wipe_user_devices(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.wipe_user_devices(
            user_id="userId",
        )
        """
        _response = self._raw_client.wipe_user_devices(user_id, request_options=request_options)
        return _response.data

    def enable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.enable_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.enable_user(user_id, request_options=request_options)
        return _response.data

    def disable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.disable_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.disable_user(user_id, request_options=request_options)
        return _response.data

    def get_users_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroups200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetGroups200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_users_groups(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_users_groups(user_id, request_options=request_options)
        return _response.data

    def add_to_group(
        self,
        user_id: str,
        *,
        groupid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.add_to_group(
            user_id="userId",
        )
        """
        _response = self._raw_client.add_to_group(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    def remove_from_group(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.remove_from_group(
            user_id="userId",
            groupid="groupid",
        )
        """
        _response = self._raw_client.remove_from_group(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    def get_user_sub_admin_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
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
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.get_user_sub_admin_groups(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_user_sub_admin_groups(user_id, request_options=request_options)
        return _response.data

    def add_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.add_sub_admin(
            user_id="userId",
            groupid="groupid",
        )
        """
        _response = self._raw_client.add_sub_admin(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    def remove_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.remove_sub_admin(
            user_id="userId",
            groupid="groupid",
        )
        """
        _response = self._raw_client.remove_sub_admin(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    def resend_welcome_message(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_users.resend_welcome_message(
            user_id="userId",
        )
        """
        _response = self._raw_client.resend_welcome_message(user_id, request_options=request_options)
        return _response.data


class AsyncProvisioningApiUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvisioningApiUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvisioningApiUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvisioningApiUsersClient
        """
        return self._raw_client

    async def get_users(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
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
        ProvisioningApiGroupsGetGroupUsers200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

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
    ) -> ProvisioningApiUsersAddUser200Response:
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
        ProvisioningApiUsersAddUser200Response
            User added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.add_user(
                userid="userid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user(
            userid=userid,
            password=password,
            display_name=display_name,
            email=email,
            groups=groups,
            subadmin=subadmin,
            quota=quota,
            language=language,
            manager=manager,
            request_options=request_options,
        )
        return _response.data

    async def get_users_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsersDetails200Response:
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
        ProvisioningApiGroupsGetGroupUsersDetails200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_users_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_details(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def search_by_phone_numbers(
        self, *, location: str, search: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersSearchByPhoneNumbers200Response:
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
        ProvisioningApiUsersSearchByPhoneNumbers200Response
            Users returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.search_by_phone_numbers(
                location="location",
                search="search",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_by_phone_numbers(
            location=location, search=search, request_options=request_options
        )
        return _response.data

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersGetUser200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiUsersGetUser200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data

    async def edit_user(
        self, user_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.edit_user(
                user_id="userId",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_user(user_id, key=key, value=value, request_options=request_options)
        return _response.data

    async def delete_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.delete_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(user_id, request_options=request_options)
        return _response.data

    async def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiUsersGetUser200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiUsersGetUser200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    async def get_editable_fields(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_editable_fields()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_editable_fields(request_options=request_options)
        return _response.data

    async def get_editable_fields_for_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_editable_fields_for_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_editable_fields_for_user(user_id, request_options=request_options)
        return _response.data

    async def edit_user_multi_value(
        self,
        user_id: str,
        collection_name: str,
        *,
        key: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.edit_user_multi_value(
                user_id="userId",
                collection_name="collectionName",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_user_multi_value(
            user_id, collection_name, key=key, value=value, request_options=request_options
        )
        return _response.data

    async def wipe_user_devices(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.wipe_user_devices(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wipe_user_devices(user_id, request_options=request_options)
        return _response.data

    async def enable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.enable_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_user(user_id, request_options=request_options)
        return _response.data

    async def disable_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.disable_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_user(user_id, request_options=request_options)
        return _response.data

    async def get_users_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroups200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetGroups200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_users_groups(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_groups(user_id, request_options=request_options)
        return _response.data

    async def add_to_group(
        self,
        user_id: str,
        *,
        groupid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.add_to_group(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_to_group(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    async def remove_from_group(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.remove_from_group(
                user_id="userId",
                groupid="groupid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_from_group(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    async def get_user_sub_admin_groups(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
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
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.get_user_sub_admin_groups(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_sub_admin_groups(user_id, request_options=request_options)
        return _response.data

    async def add_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.add_sub_admin(
                user_id="userId",
                groupid="groupid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_sub_admin(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    async def remove_sub_admin(
        self, user_id: str, *, groupid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.remove_sub_admin(
                user_id="userId",
                groupid="groupid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_sub_admin(user_id, groupid=groupid, request_options=request_options)
        return _response.data

    async def resend_welcome_message(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        user_id : str
            ID if the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provisioning_api_users.resend_welcome_message(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend_welcome_message(user_id, request_options=request_options)
        return _response.data
