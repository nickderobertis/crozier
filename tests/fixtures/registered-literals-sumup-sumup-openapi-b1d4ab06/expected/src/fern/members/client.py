

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attributes import Attributes
from ..types.member import Member
from ..types.membership_status import MembershipStatus
from ..types.metadata import Metadata
from .raw_client import AsyncRawMembersClient, RawMembersClient
from .types.list_merchant_members_response import ListMerchantMembersResponse
from .types.update_merchant_member_request_user import UpdateMerchantMemberRequestUser


OMIT = typing.cast(typing.Any, ...)


class MembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMembersClient
        """
        return self._raw_client

    def list_merchant_members(
        self,
        merchant_code: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        scroll: typing.Optional[bool] = None,
        email: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        status: typing.Optional[MembershipStatus] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMerchantMembersResponse:
        """
        Lists merchant members.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        scroll : typing.Optional[bool]
            Indicates to skip count query.

        email : typing.Optional[str]
            Filter the returned members by email address prefix.

        user_id : typing.Optional[str]
            Search for a member by user id.

        status : typing.Optional[MembershipStatus]
            Filter the returned members by the membership status.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned members by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMerchantMembersResponse
            Returns a list of Member objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.members.list_merchant_members(
            merchant_code="MK10CL2A",
            offset=0,
            limit=10,
            scroll=True,
            email="user",
            user_id="245b2ead-85bf-45ff-856f-311a88a5d454",
        )
        """
        _response = self._raw_client.list_merchant_members(
            merchant_code,
            offset=offset,
            limit=limit,
            scroll=scroll,
            email=email,
            user_id=user_id,
            status=status,
            roles=roles,
            request_options=request_options,
        )
        return _response.data

    def create_merchant_member(
        self,
        merchant_code: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        is_managed_user: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Adds a member to the merchant account with the specified roles.

        By default, sends an invitation email to the provided address. The recipient must accept the invitation to join the account.
        When `is_managed_user` is `true`, creates a managed user with the provided password and optional nickname and assigns the roles directly, without sending an invitation.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        email : str
            Email address of the member to add.

        roles : typing.Sequence[str]
            List of roles to assign to the new member.

        is_managed_user : typing.Optional[bool]
            True if the user is managed by the merchant. In this case, we'll created a virtual user with the provided password and nickname.

        password : typing.Optional[str]
            Password of the member to add. Only used if `is_managed_user` is true. In the case of service accounts, the password is not used and can not be defined by the caller.

        nickname : typing.Optional[str]
            Nickname of the member to add. Only used if `is_managed_user` is true. Used for display purposes only.

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the Member object if the creation succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.members.create_merchant_member(
            merchant_code="MK10CL2A",
            email="karl.berg@example.com",
            roles=["role_employee"],
        )
        """
        _response = self._raw_client.create_merchant_member(
            merchant_code,
            email=email,
            roles=roles,
            is_managed_user=is_managed_user,
            password=password,
            nickname=nickname,
            metadata=metadata,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    def get_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Member:
        """
        Retrieve a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the Member object for a valid identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.members.get_merchant_member(
            merchant_code="MK10CL2A",
            member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
        )
        """
        _response = self._raw_client.get_merchant_member(merchant_code, member_id, request_options=request_options)
        return _response.data

    def update_merchant_member(
        self,
        merchant_code: str,
        member_id: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        user: typing.Optional[UpdateMerchantMemberRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Updates a merchant member and returns the updated member.

        Providing `roles` replaces the member's assigned roles and can grant or revoke access. Providing `metadata` replaces the entire metadata object.
        For managed users, `user.nickname` changes the display name and `user.password` replaces the password. Updating the password also enables the managed user account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        roles : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        user : typing.Optional[UpdateMerchantMemberRequestUser]
            Allows you to update user data of managed users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the updated Member object if the update succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.members.update_merchant_member(
            merchant_code="MK10CL2A",
            member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
        )
        """
        _response = self._raw_client.update_merchant_member(
            merchant_code,
            member_id,
            roles=roles,
            metadata=metadata,
            attributes=attributes,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def delete_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

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
        client.members.delete_merchant_member(
            merchant_code="MK10CL2A",
            member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
        )
        """
        _response = self._raw_client.delete_merchant_member(merchant_code, member_id, request_options=request_options)
        return _response.data


class AsyncMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMembersClient
        """
        return self._raw_client

    async def list_merchant_members(
        self,
        merchant_code: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        scroll: typing.Optional[bool] = None,
        email: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        status: typing.Optional[MembershipStatus] = None,
        roles: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMerchantMembersResponse:
        """
        Lists merchant members.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        offset : typing.Optional[int]
            Offset of the first member to return.

        limit : typing.Optional[int]
            Maximum number of members to return.

        scroll : typing.Optional[bool]
            Indicates to skip count query.

        email : typing.Optional[str]
            Filter the returned members by email address prefix.

        user_id : typing.Optional[str]
            Search for a member by user id.

        status : typing.Optional[MembershipStatus]
            Filter the returned members by the membership status.

        roles : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter the returned members by role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMerchantMembersResponse
            Returns a list of Member objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.members.list_merchant_members(
                merchant_code="MK10CL2A",
                offset=0,
                limit=10,
                scroll=True,
                email="user",
                user_id="245b2ead-85bf-45ff-856f-311a88a5d454",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_merchant_members(
            merchant_code,
            offset=offset,
            limit=limit,
            scroll=scroll,
            email=email,
            user_id=user_id,
            status=status,
            roles=roles,
            request_options=request_options,
        )
        return _response.data

    async def create_merchant_member(
        self,
        merchant_code: str,
        *,
        email: str,
        roles: typing.Sequence[str],
        is_managed_user: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Adds a member to the merchant account with the specified roles.

        By default, sends an invitation email to the provided address. The recipient must accept the invitation to join the account.
        When `is_managed_user` is `true`, creates a managed user with the provided password and optional nickname and assigns the roles directly, without sending an invitation.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        email : str
            Email address of the member to add.

        roles : typing.Sequence[str]
            List of roles to assign to the new member.

        is_managed_user : typing.Optional[bool]
            True if the user is managed by the merchant. In this case, we'll created a virtual user with the provided password and nickname.

        password : typing.Optional[str]
            Password of the member to add. Only used if `is_managed_user` is true. In the case of service accounts, the password is not used and can not be defined by the caller.

        nickname : typing.Optional[str]
            Nickname of the member to add. Only used if `is_managed_user` is true. Used for display purposes only.

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the Member object if the creation succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.members.create_merchant_member(
                merchant_code="MK10CL2A",
                email="karl.berg@example.com",
                roles=["role_employee"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_merchant_member(
            merchant_code,
            email=email,
            roles=roles,
            is_managed_user=is_managed_user,
            password=password,
            nickname=nickname,
            metadata=metadata,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    async def get_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Member:
        """
        Retrieve a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the Member object for a valid identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.members.get_merchant_member(
                merchant_code="MK10CL2A",
                member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_merchant_member(
            merchant_code, member_id, request_options=request_options
        )
        return _response.data

    async def update_merchant_member(
        self,
        merchant_code: str,
        member_id: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        attributes: typing.Optional[Attributes] = OMIT,
        user: typing.Optional[UpdateMerchantMemberRequestUser] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Member:
        """
        Updates a merchant member and returns the updated member.

        Providing `roles` replaces the member's assigned roles and can grant or revoke access. Providing `metadata` replaces the entire metadata object.
        For managed users, `user.nickname` changes the display name and `user.password` replaces the password. Updating the password also enables the managed user account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

        roles : typing.Optional[typing.Sequence[str]]

        metadata : typing.Optional[Metadata]

        attributes : typing.Optional[Attributes]

        user : typing.Optional[UpdateMerchantMemberRequestUser]
            Allows you to update user data of managed users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Member
            Returns the updated Member object if the update succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.members.update_merchant_member(
                merchant_code="MK10CL2A",
                member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_merchant_member(
            merchant_code,
            member_id,
            roles=roles,
            metadata=metadata,
            attributes=attributes,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def delete_merchant_member(
        self, merchant_code: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a merchant member.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        member_id : str
            The ID of the member to retrieve.

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
            await client.members.delete_merchant_member(
                merchant_code="MK10CL2A",
                member_id="mem_WZsm7QTPhVrompscmPhoGTXXcrd58fr9MOhP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_merchant_member(
            merchant_code, member_id, request_options=request_options
        )
        return _response.data
