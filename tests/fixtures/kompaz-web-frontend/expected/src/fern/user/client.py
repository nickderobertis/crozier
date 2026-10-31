

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_role import UserRole
from ..types.user_status import UserStatus
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.user_index_response import UserIndexResponse
from .types.user_invite_response import UserInviteResponse
from .types.user_restore_response import UserRestoreResponse
from .types.user_show_response import UserShowResponse
from .types.user_update_own_profile_response import UserUpdateOwnProfileResponse
from .types.user_update_response import UserUpdateResponse


OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def index(
        self,
        *,
        status: typing.Optional[UserStatus] = None,
        search: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserIndexResponse:
        """
        Parameters
        ----------
        status : typing.Optional[UserStatus]

        search : typing.Optional[str]

        organization_id : typing.Optional[str]

        include_deleted : typing.Optional[bool]

        page_number : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserIndexResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.index()
        """
        _response = self._raw_client.index(
            status=status,
            search=search,
            organization_id=organization_id,
            include_deleted=include_deleted,
            page_number=page_number,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def updateownprofile(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserUpdateOwnProfileResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserUpdateOwnProfileResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.updateownprofile(
            name="name",
        )
        """
        _response = self._raw_client.updateownprofile(name=name, request_options=request_options)
        return _response.data

    def show(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserShowResponse:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserShowResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.show(
            user="user",
        )
        """
        _response = self._raw_client.show(user, request_options=request_options)
        return _response.data

    def update(
        self,
        user: str,
        *,
        name: str,
        email: str,
        role: typing.Optional[UserRole] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserUpdateResponse:
        """
        Parameters
        ----------
        user : str
            The user ID

        name : str

        email : str

        role : typing.Optional[UserRole]

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserUpdateResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.update(
            user="user",
            name="name",
            email="email",
        )
        """
        _response = self._raw_client.update(
            user, name=name, email=email, role=role, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def destroy(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.destroy(
            user="user",
        )
        """
        _response = self._raw_client.destroy(user, request_options=request_options)
        return _response.data

    def invite(
        self,
        *,
        email: str,
        name: str,
        role: UserRole,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserInviteResponse:
        """
        Parameters
        ----------
        email : str

        name : str

        role : UserRole

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInviteResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi, UserRole

        client = FernApi()
        client.user.invite(
            email="email",
            name="name",
            role=UserRole.MEMBER,
        )
        """
        _response = self._raw_client.invite(
            email=email, name=name, role=role, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def resendinvitation(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.resendinvitation(
            user="user",
        )
        """
        _response = self._raw_client.resendinvitation(user, request_options=request_options)
        return _response.data

    def restore(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserRestoreResponse:
        """
        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRestoreResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user.restore(
            user="user",
        )
        """
        _response = self._raw_client.restore(user, request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def index(
        self,
        *,
        status: typing.Optional[UserStatus] = None,
        search: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserIndexResponse:
        """
        Parameters
        ----------
        status : typing.Optional[UserStatus]

        search : typing.Optional[str]

        organization_id : typing.Optional[str]

        include_deleted : typing.Optional[bool]

        page_number : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserIndexResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.index()


        asyncio.run(main())
        """
        _response = await self._raw_client.index(
            status=status,
            search=search,
            organization_id=organization_id,
            include_deleted=include_deleted,
            page_number=page_number,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def updateownprofile(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserUpdateOwnProfileResponse:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserUpdateOwnProfileResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.updateownprofile(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateownprofile(name=name, request_options=request_options)
        return _response.data

    async def show(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> UserShowResponse:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserShowResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.show(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show(user, request_options=request_options)
        return _response.data

    async def update(
        self,
        user: str,
        *,
        name: str,
        email: str,
        role: typing.Optional[UserRole] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserUpdateResponse:
        """
        Parameters
        ----------
        user : str
            The user ID

        name : str

        email : str

        role : typing.Optional[UserRole]

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserUpdateResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.update(
                user="user",
                name="name",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            user, name=name, email=email, role=role, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def destroy(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.destroy(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy(user, request_options=request_options)
        return _response.data

    async def invite(
        self,
        *,
        email: str,
        name: str,
        role: UserRole,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserInviteResponse:
        """
        Parameters
        ----------
        email : str

        name : str

        role : UserRole

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInviteResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UserRole

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.invite(
                email="email",
                name="name",
                role=UserRole.MEMBER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite(
            email=email, name=name, role=role, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def resendinvitation(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        user : str
            The user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.resendinvitation(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resendinvitation(user, request_options=request_options)
        return _response.data

    async def restore(
        self, user: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserRestoreResponse:
        """
        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRestoreResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user.restore(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore(user, request_options=request_options)
        return _response.data
