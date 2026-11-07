

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_user_invitation import OrganizationUserInvitation
from ..types.paginated_response_of_organization import PaginatedResponseOfOrganization
from ..types.paginated_response_of_role import PaginatedResponseOfRole
from ..types.paginated_response_of_user_presentation import PaginatedResponseOfUserPresentation
from ..types.paginated_response_of_user_roles import PaginatedResponseOfUserRoles
from ..types.paginated_response_ofstring import PaginatedResponseOfstring
from ..types.simple_message_response import SimpleMessageResponse
from ..types.user_presentation import UserPresentation
from ..types.user_registration_response import UserRegistrationResponse
from .raw_client import AsyncRawAccountsClient, RawAccountsClient


OMIT = typing.cast(typing.Any, ...)


class AccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountsClient
        """
        return self._raw_client

    def request_password_reset(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleMessageResponse:
        """
        Requesting a reset for a new password.

        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleMessageResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.request_password_reset(
            username="username",
        )
        """
        _response = self._raw_client.request_password_reset(username=username, request_options=request_options)
        return _response.data

    def verify_password_reset(
        self, *, password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleMessageResponse:
        """
        Setting a new password and verifying the request to set the password.

        Parameters
        ----------
        password : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleMessageResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.verify_password_reset(
            password="password",
            token="token",
        )
        """
        _response = self._raw_client.verify_password_reset(
            password=password, token=token, request_options=request_options
        )
        return _response.data

    def register_user(
        self, *, email: str, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserRegistrationResponse:
        """
        Registering a new user.

        Parameters
        ----------
        email : str

        password : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRegistrationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.register_user(
            email="email",
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.register_user(
            email=email, password=password, username=username, request_options=request_options
        )
        return _response.data

    def complete_registration(
        self,
        *,
        password: str,
        username: str,
        verification_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completing a registration e.g. for invited users. Finish registration with a username and a password.

        Parameters
        ----------
        password : str

        username : str

        verification_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.complete_registration(
            password="password",
            username="username",
            verification_token="verificationToken",
        )
        """
        _response = self._raw_client.complete_registration(
            password=password, username=username, verification_token=verification_token, request_options=request_options
        )
        return _response.data

    def verify_user_registration(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Verifies a new user registration.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.verify_user_registration(
            token="token",
        )
        """
        _response = self._raw_client.verify_user_registration(token=token, request_options=request_options)
        return _response.data

    def get_all_organization_roles(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserRoles:
        """
        Listing users and their roles in a paginated manner.

        Parameters
        ----------
        organization_id : str
            organizationId

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserRoles
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.get_all_organization_roles(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_all_organization_roles(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_users_of_organization(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserPresentation:
        """
        Finding users in the specified organization in a paginated manner.

        Parameters
        ----------
        organization_id : str
            organizationId

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.get_users_of_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_users_of_organization(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def invite_users(
        self,
        organization_id: str,
        *,
        invitations: typing.Sequence[OrganizationUserInvitation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization where users should be invited

        invitations : typing.Sequence[OrganizationUserInvitation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, OrganizationUserInvitation

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.invite_users(
            organization_id="organizationId",
            invitations=[
                OrganizationUserInvitation(
                    roles=["roles"],
                )
            ],
        )
        """
        _response = self._raw_client.invite_users(
            organization_id, invitations=invitations, request_options=request_options
        )
        return _response.data

    def get_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfstring:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfstring
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.get_user_roles(
            organization_id="organizationId",
            username="username",
        )
        """
        _response = self._raw_client.get_user_roles(
            organization_id, username, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def add_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        roles : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.add_user_roles(
            organization_id="organizationId",
            username="username",
        )
        """
        _response = self._raw_client.add_user_roles(
            organization_id, username, roles=roles, request_options=request_options
        )
        return _response.data

    def remove_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        roles : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.remove_user_roles(
            organization_id="organizationId",
            username="username",
        )
        """
        _response = self._raw_client.remove_user_roles(
            organization_id, username, roles=roles, request_options=request_options
        )
        return _response.data

    def list_all_roles(
        self,
        *,
        privilege: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfRole:
        """
        Listing of roles.

        Parameters
        ----------
        privilege : typing.Optional[str]
            If specified the roles will be filtered containing that privilege.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfRole
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.list_all_roles()
        """
        _response = self._raw_client.list_all_roles(
            privilege=privilege, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_organizations_of_user(
        self,
        *,
        role: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfOrganization:
        """
        Parameters
        ----------
        role : typing.Optional[str]
            role

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfOrganization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.get_organizations_of_user()
        """
        _response = self._raw_client.get_organizations_of_user(
            role=role, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def find_users(
        self,
        *,
        username_prefix: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserPresentation:
        """
        Parameters
        ----------
        username_prefix : typing.Optional[str]

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.find_users()
        """
        _response = self._raw_client.find_users(
            username_prefix=username_prefix, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def find_user_by_username(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserPresentation:
        """
        Parameters
        ----------
        username : str
            username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.find_user_by_username(
            username="username",
        )
        """
        _response = self._raw_client.find_user_by_username(username, request_options=request_options)
        return _response.data

    def login(
        self,
        *,
        login: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ID4i API Login

        Parameters
        ----------
        login : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.accounts.login()
        """
        _response = self._raw_client.login(login=login, password=password, request_options=request_options)
        return _response.data


class AsyncAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountsClient
        """
        return self._raw_client

    async def request_password_reset(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleMessageResponse:
        """
        Requesting a reset for a new password.

        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleMessageResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.request_password_reset(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_password_reset(username=username, request_options=request_options)
        return _response.data

    async def verify_password_reset(
        self, *, password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimpleMessageResponse:
        """
        Setting a new password and verifying the request to set the password.

        Parameters
        ----------
        password : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimpleMessageResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.verify_password_reset(
                password="password",
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_password_reset(
            password=password, token=token, request_options=request_options
        )
        return _response.data

    async def register_user(
        self, *, email: str, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserRegistrationResponse:
        """
        Registering a new user.

        Parameters
        ----------
        email : str

        password : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRegistrationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.register_user(
                email="email",
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_user(
            email=email, password=password, username=username, request_options=request_options
        )
        return _response.data

    async def complete_registration(
        self,
        *,
        password: str,
        username: str,
        verification_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Completing a registration e.g. for invited users. Finish registration with a username and a password.

        Parameters
        ----------
        password : str

        username : str

        verification_token : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.complete_registration(
                password="password",
                username="username",
                verification_token="verificationToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_registration(
            password=password, username=username, verification_token=verification_token, request_options=request_options
        )
        return _response.data

    async def verify_user_registration(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Verifies a new user registration.

        Parameters
        ----------
        token : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.verify_user_registration(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_user_registration(token=token, request_options=request_options)
        return _response.data

    async def get_all_organization_roles(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserRoles:
        """
        Listing users and their roles in a paginated manner.

        Parameters
        ----------
        organization_id : str
            organizationId

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserRoles
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.get_all_organization_roles(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_organization_roles(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_users_of_organization(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserPresentation:
        """
        Finding users in the specified organization in a paginated manner.

        Parameters
        ----------
        organization_id : str
            organizationId

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.get_users_of_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_of_organization(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def invite_users(
        self,
        organization_id: str,
        *,
        invitations: typing.Sequence[OrganizationUserInvitation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization where users should be invited

        invitations : typing.Sequence[OrganizationUserInvitation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OrganizationUserInvitation

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.invite_users(
                organization_id="organizationId",
                invitations=[
                    OrganizationUserInvitation(
                        roles=["roles"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite_users(
            organization_id, invitations=invitations, request_options=request_options
        )
        return _response.data

    async def get_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfstring:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfstring
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.get_user_roles(
                organization_id="organizationId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_roles(
            organization_id, username, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def add_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        roles : typing.Optional[typing.Sequence[str]]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.add_user_roles(
                organization_id="organizationId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_roles(
            organization_id, username, roles=roles, request_options=request_options
        )
        return _response.data

    async def remove_user_roles(
        self,
        organization_id: str,
        username: str,
        *,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        username : str
            username

        roles : typing.Optional[typing.Sequence[str]]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.remove_user_roles(
                organization_id="organizationId",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_user_roles(
            organization_id, username, roles=roles, request_options=request_options
        )
        return _response.data

    async def list_all_roles(
        self,
        *,
        privilege: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfRole:
        """
        Listing of roles.

        Parameters
        ----------
        privilege : typing.Optional[str]
            If specified the roles will be filtered containing that privilege.

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfRole
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.list_all_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_roles(
            privilege=privilege, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_organizations_of_user(
        self,
        *,
        role: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfOrganization:
        """
        Parameters
        ----------
        role : typing.Optional[str]
            role

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfOrganization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.get_organizations_of_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organizations_of_user(
            role=role, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def find_users(
        self,
        *,
        username_prefix: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfUserPresentation:
        """
        Parameters
        ----------
        username_prefix : typing.Optional[str]

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfUserPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.find_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_users(
            username_prefix=username_prefix, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def find_user_by_username(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserPresentation:
        """
        Parameters
        ----------
        username : str
            username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.find_user_by_username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_user_by_username(username, request_options=request_options)
        return _response.data

    async def login(
        self,
        *,
        login: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ID4i API Login

        Parameters
        ----------
        login : typing.Optional[str]

        password : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounts.login()


        asyncio.run(main())
        """
        _response = await self._raw_client.login(login=login, password=password, request_options=request_options)
        return _response.data
