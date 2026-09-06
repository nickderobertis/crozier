

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.image_rendering_mode import ImageRenderingMode
from ..types.org_name import OrgName
from ..types.organization import Organization
from ..types.organization_id_param import OrganizationIdParam
from ..types.patch_organization_members_output import PatchOrganizationMembersOutput
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawOrganizationsClient, RawOrganizationsClient
from .types.get_organization_response import GetOrganizationResponse
from .types.patch_organization_members_invite_users import PatchOrganizationMembersInviteUsers
from .types.patch_organization_members_remove_users import PatchOrganizationMembersRemoveUsers


OMIT = typing.cast(typing.Any, ...)


class OrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsClient
        """
        return self._raw_client

    def get_organization(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetOrganizationResponse:
        """
        List out all organizations. The organizations are sorted by creation date, with the most recently-created organizations coming first

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

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationResponse
            Returns a list of organization objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.get_organization()
        """
        _response = self._raw_client.get_organization(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def get_organization_id(
        self, organization_id: OrganizationIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Get an organization object by its id

        Parameters
        ----------
        organization_id : OrganizationIdParam
            Organization id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            Returns the organization object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.get_organization_id(
            organization_id="organization_id",
        )
        """
        _response = self._raw_client.get_organization_id(organization_id, request_options=request_options)
        return _response.data

    def patch_organization_id(
        self,
        organization_id: OrganizationIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        api_url: typing.Optional[str] = OMIT,
        is_universal_api: typing.Optional[bool] = OMIT,
        is_dataplane_private: typing.Optional[bool] = OMIT,
        proxy_url: typing.Optional[str] = OMIT,
        realtime_url: typing.Optional[str] = OMIT,
        image_rendering_mode: typing.Optional[ImageRenderingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Partially update an organization object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        organization_id : OrganizationIdParam
            Organization id

        name : typing.Optional[str]
            Name of the organization

        api_url : typing.Optional[str]

        is_universal_api : typing.Optional[bool]

        is_dataplane_private : typing.Optional[bool]

        proxy_url : typing.Optional[str]

        realtime_url : typing.Optional[str]

        image_rendering_mode : typing.Optional[ImageRenderingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            Returns the organization object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.patch_organization_id(
            organization_id="organization_id",
        )
        """
        _response = self._raw_client.patch_organization_id(
            organization_id,
            name=name,
            api_url=api_url,
            is_universal_api=is_universal_api,
            is_dataplane_private=is_dataplane_private,
            proxy_url=proxy_url,
            realtime_url=realtime_url,
            image_rendering_mode=image_rendering_mode,
            request_options=request_options,
        )
        return _response.data

    def patch_organization_members(
        self,
        *,
        invite_users: typing.Optional[PatchOrganizationMembersInviteUsers] = OMIT,
        remove_users: typing.Optional[PatchOrganizationMembersRemoveUsers] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchOrganizationMembersOutput:
        """
        Modify organization membership

        Parameters
        ----------
        invite_users : typing.Optional[PatchOrganizationMembersInviteUsers]
            Users to invite to the organization

        remove_users : typing.Optional[PatchOrganizationMembersRemoveUsers]
            Users to remove from the organization

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the name of the organization.

        org_id : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the id of the organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchOrganizationMembersOutput
            A success status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.patch_organization_members()
        """
        _response = self._raw_client.patch_organization_members(
            invite_users=invite_users,
            remove_users=remove_users,
            org_name=org_name,
            org_id=org_id,
            request_options=request_options,
        )
        return _response.data


class AsyncOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsClient
        """
        return self._raw_client

    async def get_organization(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetOrganizationResponse:
        """
        List out all organizations. The organizations are sorted by creation date, with the most recently-created organizations coming first

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

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationResponse
            Returns a list of organization objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.get_organization()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organization(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def get_organization_id(
        self, organization_id: OrganizationIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Get an organization object by its id

        Parameters
        ----------
        organization_id : OrganizationIdParam
            Organization id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            Returns the organization object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.get_organization_id(
                organization_id="organization_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organization_id(organization_id, request_options=request_options)
        return _response.data

    async def patch_organization_id(
        self,
        organization_id: OrganizationIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        api_url: typing.Optional[str] = OMIT,
        is_universal_api: typing.Optional[bool] = OMIT,
        is_dataplane_private: typing.Optional[bool] = OMIT,
        proxy_url: typing.Optional[str] = OMIT,
        realtime_url: typing.Optional[str] = OMIT,
        image_rendering_mode: typing.Optional[ImageRenderingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Partially update an organization object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        organization_id : OrganizationIdParam
            Organization id

        name : typing.Optional[str]
            Name of the organization

        api_url : typing.Optional[str]

        is_universal_api : typing.Optional[bool]

        is_dataplane_private : typing.Optional[bool]

        proxy_url : typing.Optional[str]

        realtime_url : typing.Optional[str]

        image_rendering_mode : typing.Optional[ImageRenderingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            Returns the organization object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.patch_organization_id(
                organization_id="organization_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_organization_id(
            organization_id,
            name=name,
            api_url=api_url,
            is_universal_api=is_universal_api,
            is_dataplane_private=is_dataplane_private,
            proxy_url=proxy_url,
            realtime_url=realtime_url,
            image_rendering_mode=image_rendering_mode,
            request_options=request_options,
        )
        return _response.data

    async def patch_organization_members(
        self,
        *,
        invite_users: typing.Optional[PatchOrganizationMembersInviteUsers] = OMIT,
        remove_users: typing.Optional[PatchOrganizationMembersRemoveUsers] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchOrganizationMembersOutput:
        """
        Modify organization membership

        Parameters
        ----------
        invite_users : typing.Optional[PatchOrganizationMembersInviteUsers]
            Users to invite to the organization

        remove_users : typing.Optional[PatchOrganizationMembersRemoveUsers]
            Users to remove from the organization

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the name of the organization.

        org_id : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the id of the organization.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchOrganizationMembersOutput
            A success status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.patch_organization_members()


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_organization_members(
            invite_users=invite_users,
            remove_users=remove_users,
            org_name=org_name,
            org_id=org_id,
            request_options=request_options,
        )
        return _response.data
