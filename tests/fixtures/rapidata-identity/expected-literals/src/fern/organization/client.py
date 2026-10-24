

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accept_org_invitation_by_id_endpoint_output import AcceptOrgInvitationByIdEndpointOutput
from ..types.accept_org_invitation_endpoint_output import AcceptOrgInvitationEndpointOutput
from ..types.create_organization_endpoint_output import CreateOrganizationEndpointOutput
from ..types.get_organization_endpoint_output import GetOrganizationEndpointOutput
from ..types.get_organizations_all_request_id import GetOrganizationsAllRequestId
from ..types.get_organizations_all_request_name import GetOrganizationsAllRequestName
from ..types.get_organizations_all_request_owner_email import GetOrganizationsAllRequestOwnerEmail
from ..types.get_organizations_request_id import GetOrganizationsRequestId
from ..types.get_organizations_request_name import GetOrganizationsRequestName
from ..types.invite_org_member_endpoint_output import InviteOrgMemberEndpointOutput
from ..types.list_my_org_invitations_endpoint_output import ListMyOrgInvitationsEndpointOutput
from ..types.list_org_invitations_endpoint_output import ListOrgInvitationsEndpointOutput
from ..types.list_org_members_endpoint_output import ListOrgMembersEndpointOutput
from ..types.org_role import OrgRole
from ..types.query_all_organizations_endpoint_paged_result_of_output import (
    QueryAllOrganizationsEndpointPagedResultOfOutput,
)
from ..types.query_organizations_endpoint_paged_result_of_output import QueryOrganizationsEndpointPagedResultOfOutput
from .raw_client import AsyncRawOrganizationClient, RawOrganizationClient
from .types.get_organizations_all_request_logic import GetOrganizationsAllRequestLogic
from .types.get_organizations_all_request_sort_item import GetOrganizationsAllRequestSortItem
from .types.get_organizations_request_logic import GetOrganizationsRequestLogic
from .types.get_organizations_request_sort_item import GetOrganizationsRequestSortItem


OMIT = typing.cast(typing.Any, ...)


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationClient
        """
        return self._raw_client

    def accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptOrgInvitationByIdEndpointOutput:
        """
        Responds with 409 when the invitation is expired, already used, or was issued to a different
         email than the calling customer's.

        Parameters
        ----------
        invitation_id : str
            The id of the invitation to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptOrgInvitationByIdEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
            invitation_id="invitationId",
        )
        """
        _response = self._raw_client.accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
            invitation_id, request_options=request_options
        )
        return _response.data

    def accepts_the_invitation_identified_by_the_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptOrgInvitationEndpointOutput:
        """
        Responds with 409 when the invitation is expired, already used, or was issued to a different
         email than the calling customer's.

        Parameters
        ----------
        token : str
            The single-use invitation token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptOrgInvitationEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.accepts_the_invitation_identified_by_the_token(
            token="token",
        )
        """
        _response = self._raw_client.accepts_the_invitation_identified_by_the_token(
            token=token, request_options=request_options
        )
        return _response.data

    def sets_the_given_members_org_scoped_role(
        self,
        organization_id: str,
        customer_id: str,
        *,
        role: OrgRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Responds with 404 when the customer is not a member and 409 when changing the role of the
         organization's last owner.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        customer_id : str
            The id of the member whose role changes.

        role : OrgRole
            The org-scoped role to assign to the member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.sets_the_given_members_org_scoped_role(
            organization_id="organizationId",
            customer_id="customerId",
            role="Owner",
        )
        """
        _response = self._raw_client.sets_the_given_members_org_scoped_role(
            organization_id, customer_id, role=role, request_options=request_options
        )
        return _response.data

    def returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetOrganizationsRequestSortItem, typing.Sequence[GetOrganizationsRequestSortItem]]
        ] = None,
        id: typing.Optional[GetOrganizationsRequestId] = None,
        name: typing.Optional[GetOrganizationsRequestName] = None,
        logic: typing.Optional[GetOrganizationsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryOrganizationsEndpointPagedResultOfOutput:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetOrganizationsRequestSortItem, typing.Sequence[GetOrganizationsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetOrganizationsRequestId]
            Filter by id.

        name : typing.Optional[GetOrganizationsRequestName]
            Filter by name.

        logic : typing.Optional[GetOrganizationsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryOrganizationsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role()
        """
        _response = self._raw_client.returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role(
            page=page, page_size=page_size, sort=sort, id=id, name=name, logic=logic, request_options=request_options
        )
        return _response.data

    def creates_an_organization_and_makes_the_calling_customer_its_owner(
        self,
        *,
        name: str,
        primary_domain: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrganizationEndpointOutput:
        """
        The calling customer becomes the organization's owner.

        Parameters
        ----------
        name : str
            The human-readable name of the organization.

        primary_domain : typing.Optional[str]
            The primary email domain associated with the organization, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrganizationEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.creates_an_organization_and_makes_the_calling_customer_its_owner(
            name="name",
        )
        """
        _response = self._raw_client.creates_an_organization_and_makes_the_calling_customer_its_owner(
            name=name, primary_domain=primary_domain, request_options=request_options
        )
        return _response.data

    def returns_the_organization_with_the_given_id(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_the_organization_with_the_given_id(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.returns_the_organization_with_the_given_id(
            organization_id, request_options=request_options
        )
        return _response.data

    def deletes_the_organization_and_everything_it_owns_across_the_platform(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This cannot be undone. Every member loses access immediately and each service removes the
         organization's data; invoices already raised are kept. Responds with 409 when the
         organization still has an open invoice or a billing reconciliation in progress — settle those
         first.

        Parameters
        ----------
        organization_id : str
            The id of the organization to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.deletes_the_organization_and_everything_it_owns_across_the_platform(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.deletes_the_organization_and_everything_it_owns_across_the_platform(
            organization_id, request_options=request_options
        )
        return _response.data

    def updates_the_given_organizations_provided_fields(
        self,
        organization_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        auto_join_domain: typing.Optional[str] = OMIT,
        auto_join_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Only the fields present in the body are changed, and only those the caller may change. An
         auto-join domain is rejected when it is malformed or already claimed by another organization;
         enabling auto-join without a claimed domain is rejected as well.

        Parameters
        ----------
        organization_id : str
            The id of the organization to update.

        name : typing.Optional[str]
            The new human-readable name, if changing it.

        auto_join_domain : typing.Optional[str]
            The email domain to claim for auto-join, or null to release the claim. New customers who
             sign up with a confirmed email on this domain join this organization instead of getting a
             personal one, once auto-join is enabled. Existing customers are never moved.

        auto_join_enabled : typing.Optional[bool]
            Whether to auto-join new customers signing up on the claimed domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.updates_the_given_organizations_provided_fields(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.updates_the_given_organizations_provided_fields(
            organization_id,
            name=name,
            auto_join_domain=auto_join_domain,
            auto_join_enabled=auto_join_enabled,
            request_options=request_options,
        )
        return _response.data

    def returns_the_pending_invitations_of_the_given_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgInvitationsEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization whose invitations to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgInvitationsEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_the_pending_invitations_of_the_given_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.returns_the_pending_invitations_of_the_given_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    def creates_an_invitation_to_join_the_organization(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrgRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteOrgMemberEndpointOutput:
        """
        An invitation mail with the accept link is sent to the invitee. The response still carries
         the single-use token the invitee presents to the accept-invitation endpoint, so the link can
         also be shared manually.

        Parameters
        ----------
        organization_id : str
            The id of the organization to invite into.

        email : str
            The email address to invite.

        role : OrgRole
            The org-scoped role the resulting membership will confer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteOrgMemberEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.creates_an_invitation_to_join_the_organization(
            organization_id="organizationId",
            email="email",
            role="Owner",
        )
        """
        _response = self._raw_client.creates_an_invitation_to_join_the_organization(
            organization_id, email=email, role=role, request_options=request_options
        )
        return _response.data

    def returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMyOrgInvitationsEndpointOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMyOrgInvitationsEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address()
        """
        _response = (
            self._raw_client.returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address(
                request_options=request_options
            )
        )
        return _response.data

    def returns_the_members_of_the_given_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgMembersEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization whose members to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgMembersEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_the_members_of_the_given_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.returns_the_members_of_the_given_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    def returns_a_paged_list_of_every_organization(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetOrganizationsAllRequestSortItem, typing.Sequence[GetOrganizationsAllRequestSortItem]]
        ] = None,
        id: typing.Optional[GetOrganizationsAllRequestId] = None,
        name: typing.Optional[GetOrganizationsAllRequestName] = None,
        owner_email: typing.Optional[GetOrganizationsAllRequestOwnerEmail] = None,
        logic: typing.Optional[GetOrganizationsAllRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryAllOrganizationsEndpointPagedResultOfOutput:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetOrganizationsAllRequestSortItem, typing.Sequence[GetOrganizationsAllRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetOrganizationsAllRequestId]
            Filter by id.

        name : typing.Optional[GetOrganizationsAllRequestName]
            Filter by name.

        owner_email : typing.Optional[GetOrganizationsAllRequestOwnerEmail]
            Filter by owner_email.

        logic : typing.Optional[GetOrganizationsAllRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryAllOrganizationsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.returns_a_paged_list_of_every_organization()
        """
        _response = self._raw_client.returns_a_paged_list_of_every_organization(
            page=page,
            page_size=page_size,
            sort=sort,
            id=id,
            name=name,
            owner_email=owner_email,
            logic=logic,
            request_options=request_options,
        )
        return _response.data

    def declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 409 when the invitation is not pending or was issued to a different email than
         the calling customer's.

        Parameters
        ----------
        invitation_id : str
            The id of the invitation to reject.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
            invitation_id="invitationId",
        )
        """
        _response = self._raw_client.declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
            invitation_id, request_options=request_options
        )
        return _response.data

    def removes_the_given_customers_membership_from_the_organization(
        self, organization_id: str, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 404 when the customer is not a member and 409 when removing the organization's
         last owner.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        customer_id : str
            The id of the customer to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.removes_the_given_customers_membership_from_the_organization(
            organization_id="organizationId",
            customer_id="customerId",
        )
        """
        _response = self._raw_client.removes_the_given_customers_membership_from_the_organization(
            organization_id, customer_id, request_options=request_options
        )
        return _response.data

    def revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
        self, organization_id: str, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 404 when the invitation does not belong to the organization and 409 when it is
         not pending.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        invitation_id : str
            The id of the invitation to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
            organization_id="organizationId",
            invitation_id="invitationId",
        )
        """
        _response = self._raw_client.revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
            organization_id, invitation_id, request_options=request_options
        )
        return _response.data

    def sets_the_support_slack_channel_url_for_the_given_organization(
        self,
        organization_id: str,
        *,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A null or empty URL clears the channel. Responds with 404 when no organization with the given id exists.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        url : typing.Optional[str]
            The support Slack channel URL to set, or null/empty to clear it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.sets_the_support_slack_channel_url_for_the_given_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.sets_the_support_slack_channel_url_for_the_given_organization(
            organization_id, url=url, request_options=request_options
        )
        return _response.data

    def switches_the_calling_customers_active_organization_to_the_given_one(
        self, *, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The active organization determines the token's org claim; the change takes effect the next time
         the client refreshes its token. Responds with 403 when the caller is not a member of the target
         organization.

        Parameters
        ----------
        organization_id : str
            The id of the organization to activate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organization.switches_the_calling_customers_active_organization_to_the_given_one(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.switches_the_calling_customers_active_organization_to_the_given_one(
            organization_id=organization_id, request_options=request_options
        )
        return _response.data


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationClient
        """
        return self._raw_client

    async def accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptOrgInvitationByIdEndpointOutput:
        """
        Responds with 409 when the invitation is expired, already used, or was issued to a different
         email than the calling customer's.

        Parameters
        ----------
        invitation_id : str
            The id of the invitation to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptOrgInvitationByIdEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accepts_the_invitation_identified_by_invitation_id_and_sets_the_joined_organization_as_the_callers_active_one(
            invitation_id, request_options=request_options
        )
        return _response.data

    async def accepts_the_invitation_identified_by_the_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptOrgInvitationEndpointOutput:
        """
        Responds with 409 when the invitation is expired, already used, or was issued to a different
         email than the calling customer's.

        Parameters
        ----------
        token : str
            The single-use invitation token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptOrgInvitationEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.accepts_the_invitation_identified_by_the_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accepts_the_invitation_identified_by_the_token(
            token=token, request_options=request_options
        )
        return _response.data

    async def sets_the_given_members_org_scoped_role(
        self,
        organization_id: str,
        customer_id: str,
        *,
        role: OrgRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Responds with 404 when the customer is not a member and 409 when changing the role of the
         organization's last owner.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        customer_id : str
            The id of the member whose role changes.

        role : OrgRole
            The org-scoped role to assign to the member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.sets_the_given_members_org_scoped_role(
                organization_id="organizationId",
                customer_id="customerId",
                role="Owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sets_the_given_members_org_scoped_role(
            organization_id, customer_id, role=role, request_options=request_options
        )
        return _response.data

    async def returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetOrganizationsRequestSortItem, typing.Sequence[GetOrganizationsRequestSortItem]]
        ] = None,
        id: typing.Optional[GetOrganizationsRequestId] = None,
        name: typing.Optional[GetOrganizationsRequestName] = None,
        logic: typing.Optional[GetOrganizationsRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryOrganizationsEndpointPagedResultOfOutput:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetOrganizationsRequestSortItem, typing.Sequence[GetOrganizationsRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetOrganizationsRequestId]
            Filter by id.

        name : typing.Optional[GetOrganizationsRequestName]
            Filter by name.

        logic : typing.Optional[GetOrganizationsRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryOrganizationsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_paged_list_of_the_callers_organizations_each_with_the_callers_role(
            page=page, page_size=page_size, sort=sort, id=id, name=name, logic=logic, request_options=request_options
        )
        return _response.data

    async def creates_an_organization_and_makes_the_calling_customer_its_owner(
        self,
        *,
        name: str,
        primary_domain: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrganizationEndpointOutput:
        """
        The calling customer becomes the organization's owner.

        Parameters
        ----------
        name : str
            The human-readable name of the organization.

        primary_domain : typing.Optional[str]
            The primary email domain associated with the organization, if any.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrganizationEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.creates_an_organization_and_makes_the_calling_customer_its_owner(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_an_organization_and_makes_the_calling_customer_its_owner(
            name=name, primary_domain=primary_domain, request_options=request_options
        )
        return _response.data

    async def returns_the_organization_with_the_given_id(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_the_organization_with_the_given_id(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_the_organization_with_the_given_id(
            organization_id, request_options=request_options
        )
        return _response.data

    async def deletes_the_organization_and_everything_it_owns_across_the_platform(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This cannot be undone. Every member loses access immediately and each service removes the
         organization's data; invoices already raised are kept. Responds with 409 when the
         organization still has an open invoice or a billing reconciliation in progress — settle those
         first.

        Parameters
        ----------
        organization_id : str
            The id of the organization to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.deletes_the_organization_and_everything_it_owns_across_the_platform(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_organization_and_everything_it_owns_across_the_platform(
            organization_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_organizations_provided_fields(
        self,
        organization_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        auto_join_domain: typing.Optional[str] = OMIT,
        auto_join_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Only the fields present in the body are changed, and only those the caller may change. An
         auto-join domain is rejected when it is malformed or already claimed by another organization;
         enabling auto-join without a claimed domain is rejected as well.

        Parameters
        ----------
        organization_id : str
            The id of the organization to update.

        name : typing.Optional[str]
            The new human-readable name, if changing it.

        auto_join_domain : typing.Optional[str]
            The email domain to claim for auto-join, or null to release the claim. New customers who
             sign up with a confirmed email on this domain join this organization instead of getting a
             personal one, once auto-join is enabled. Existing customers are never moved.

        auto_join_enabled : typing.Optional[bool]
            Whether to auto-join new customers signing up on the claimed domain.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.updates_the_given_organizations_provided_fields(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_organizations_provided_fields(
            organization_id,
            name=name,
            auto_join_domain=auto_join_domain,
            auto_join_enabled=auto_join_enabled,
            request_options=request_options,
        )
        return _response.data

    async def returns_the_pending_invitations_of_the_given_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgInvitationsEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization whose invitations to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgInvitationsEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_the_pending_invitations_of_the_given_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_the_pending_invitations_of_the_given_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    async def creates_an_invitation_to_join_the_organization(
        self,
        organization_id: str,
        *,
        email: str,
        role: OrgRole,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteOrgMemberEndpointOutput:
        """
        An invitation mail with the accept link is sent to the invitee. The response still carries
         the single-use token the invitee presents to the accept-invitation endpoint, so the link can
         also be shared manually.

        Parameters
        ----------
        organization_id : str
            The id of the organization to invite into.

        email : str
            The email address to invite.

        role : OrgRole
            The org-scoped role the resulting membership will confer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteOrgMemberEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.creates_an_invitation_to_join_the_organization(
                organization_id="organizationId",
                email="email",
                role="Owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_an_invitation_to_join_the_organization(
            organization_id, email=email, role=role, request_options=request_options
        )
        return _response.data

    async def returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMyOrgInvitationsEndpointOutput:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMyOrgInvitationsEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.returns_the_pending_not_yet_expired_invitations_issued_to_the_callers_email_address(
                request_options=request_options
            )
        )
        return _response.data

    async def returns_the_members_of_the_given_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListOrgMembersEndpointOutput:
        """
        Parameters
        ----------
        organization_id : str
            The id of the organization whose members to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrgMembersEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_the_members_of_the_given_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_the_members_of_the_given_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    async def returns_a_paged_list_of_every_organization(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetOrganizationsAllRequestSortItem, typing.Sequence[GetOrganizationsAllRequestSortItem]]
        ] = None,
        id: typing.Optional[GetOrganizationsAllRequestId] = None,
        name: typing.Optional[GetOrganizationsAllRequestName] = None,
        owner_email: typing.Optional[GetOrganizationsAllRequestOwnerEmail] = None,
        logic: typing.Optional[GetOrganizationsAllRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryAllOrganizationsEndpointPagedResultOfOutput:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetOrganizationsAllRequestSortItem, typing.Sequence[GetOrganizationsAllRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetOrganizationsAllRequestId]
            Filter by id.

        name : typing.Optional[GetOrganizationsAllRequestName]
            Filter by name.

        owner_email : typing.Optional[GetOrganizationsAllRequestOwnerEmail]
            Filter by owner_email.

        logic : typing.Optional[GetOrganizationsAllRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryAllOrganizationsEndpointPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.returns_a_paged_list_of_every_organization()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_paged_list_of_every_organization(
            page=page,
            page_size=page_size,
            sort=sort,
            id=id,
            name=name,
            owner_email=owner_email,
            logic=logic,
            request_options=request_options,
        )
        return _response.data

    async def declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 409 when the invitation is not pending or was issued to a different email than
         the calling customer's.

        Parameters
        ----------
        invitation_id : str
            The id of the invitation to reject.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.declines_the_invitation_identified_by_invitation_id_no_membership_is_created(
            invitation_id, request_options=request_options
        )
        return _response.data

    async def removes_the_given_customers_membership_from_the_organization(
        self, organization_id: str, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 404 when the customer is not a member and 409 when removing the organization's
         last owner.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        customer_id : str
            The id of the customer to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.removes_the_given_customers_membership_from_the_organization(
                organization_id="organizationId",
                customer_id="customerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removes_the_given_customers_membership_from_the_organization(
            organization_id, customer_id, request_options=request_options
        )
        return _response.data

    async def revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
        self, organization_id: str, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Responds with 404 when the invitation does not belong to the organization and 409 when it is
         not pending.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        invitation_id : str
            The id of the invitation to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
                organization_id="organizationId",
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokes_the_given_invitation_so_its_token_can_no_longer_be_accepted(
            organization_id, invitation_id, request_options=request_options
        )
        return _response.data

    async def sets_the_support_slack_channel_url_for_the_given_organization(
        self,
        organization_id: str,
        *,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A null or empty URL clears the channel. Responds with 404 when no organization with the given id exists.

        Parameters
        ----------
        organization_id : str
            The id of the organization.

        url : typing.Optional[str]
            The support Slack channel URL to set, or null/empty to clear it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.sets_the_support_slack_channel_url_for_the_given_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sets_the_support_slack_channel_url_for_the_given_organization(
            organization_id, url=url, request_options=request_options
        )
        return _response.data

    async def switches_the_calling_customers_active_organization_to_the_given_one(
        self, *, organization_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The active organization determines the token's org claim; the change takes effect the next time
         the client refreshes its token. Responds with 403 when the caller is not a member of the target
         organization.

        Parameters
        ----------
        organization_id : str
            The id of the organization to activate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.switches_the_calling_customers_active_organization_to_the_given_one(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.switches_the_calling_customers_active_organization_to_the_given_one(
            organization_id=organization_id, request_options=request_options
        )
        return _response.data
