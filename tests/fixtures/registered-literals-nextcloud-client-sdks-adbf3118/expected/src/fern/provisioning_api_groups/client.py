

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
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
from .raw_client import AsyncRawProvisioningApiGroupsClient, RawProvisioningApiGroupsClient


class ProvisioningApiGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvisioningApiGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvisioningApiGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvisioningApiGroupsClient
        """
        return self._raw_client

    def get_groups(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroups200Response:
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
        ProvisioningApiGroupsGetGroups200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.get_groups()
        """
        _response = self._raw_client.get_groups(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def add_group(
        self,
        *,
        groupid: str,
        displayname: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.add_group(
            groupid="groupid",
        )
        """
        _response = self._raw_client.add_group(
            groupid=groupid, displayname=displayname, request_options=request_options
        )
        return _response.data

    def get_groups_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupsDetails200Response:
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
        ProvisioningApiGroupsGetGroupsDetails200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.get_groups_details()
        """
        _response = self._raw_client.get_groups_details(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_group_users(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetGroupUsers200Response
            User IDs returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.get_group_users(
            group_id="groupId",
        )
        """
        _response = self._raw_client.get_group_users(group_id, request_options=request_options)
        return _response.data

    def get_group_users_details(
        self,
        group_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsersDetails200Response:
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
        ProvisioningApiGroupsGetGroupUsersDetails200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.get_group_users_details(
            group_id="groupId",
        )
        """
        _response = self._raw_client.get_group_users_details(
            group_id, search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_sub_admins_of_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
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
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.get_sub_admins_of_group(
            group_id="groupId",
        )
        """
        _response = self._raw_client.get_sub_admins_of_group(group_id, request_options=request_options)
        return _response.data

    def get_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

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
        client.provisioning_api_groups.get_group(
            group_id="groupId",
        )
        """
        _response = self._raw_client.get_group(group_id, request_options=request_options)
        return _response.data

    def update_group(
        self, group_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.update_group(
            group_id="groupId",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.update_group(group_id, key=key, value=value, request_options=request_options)
        return _response.data

    def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provisioning_api_groups.delete_group(
            group_id="groupId",
        )
        """
        _response = self._raw_client.delete_group(group_id, request_options=request_options)
        return _response.data


class AsyncProvisioningApiGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvisioningApiGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvisioningApiGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvisioningApiGroupsClient
        """
        return self._raw_client

    async def get_groups(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroups200Response:
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
            await client.provisioning_api_groups.get_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_groups(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def add_group(
        self,
        *,
        groupid: str,
        displayname: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
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
            await client.provisioning_api_groups.add_group(
                groupid="groupid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group(
            groupid=groupid, displayname=displayname, request_options=request_options
        )
        return _response.data

    async def get_groups_details(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupsDetails200Response:
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
        ProvisioningApiGroupsGetGroupsDetails200Response


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
            await client.provisioning_api_groups.get_groups_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_groups_details(
            search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_group_users(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetGroupUsers200Response
            User IDs returned

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
            await client.provisioning_api_groups.get_group_users(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_users(group_id, request_options=request_options)
        return _response.data

    async def get_group_users_details(
        self,
        group_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisioningApiGroupsGetGroupUsersDetails200Response:
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
            await client.provisioning_api_groups.get_group_users_details(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_users_details(
            group_id, search=search, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_sub_admins_of_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
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
            await client.provisioning_api_groups.get_sub_admins_of_group(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sub_admins_of_group(group_id, request_options=request_options)
        return _response.data

    async def get_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetGroupUsers200Response:
        """
        Parameters
        ----------
        group_id : str
            ID of the group

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
            await client.provisioning_api_groups.get_group(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group(group_id, request_options=request_options)
        return _response.data

    async def update_group(
        self, group_id: str, *, key: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
            await client.provisioning_api_groups.update_group(
                group_id="groupId",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group(group_id, key=key, value=value, request_options=request_options)
        return _response.data

    async def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
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
            await client.provisioning_api_groups.delete_group(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(group_id, request_options=request_options)
        return _response.data
