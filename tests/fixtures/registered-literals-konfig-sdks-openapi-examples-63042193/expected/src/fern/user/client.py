

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_get_information_response import UserGetInformationResponse
from ..types.user_get_user_information_response import UserGetUserInformationResponse
from ..types.user_list_collaborations_response import UserListCollaborationsResponse
from .raw_client import AsyncRawUserClient, RawUserClient


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

    def getinformation(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserGetInformationResponse:
        """
        Provides information about the user that is currently signed in.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetInformationResponse
            User login information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getinformation()
        """
        _response = self._raw_client.getinformation(request_options=request_options)
        return _response.data

    def listcollaborations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserListCollaborationsResponse:
        """
        Provides the set of organizations of which a user is a member or a collaborator.

        The set of organizations that a user can collaborate on is composed of:

        * Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
        * The parent organization of repository that the user can collaborate on, but is not necessarily a member of
        * The organization of the current user's account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserListCollaborationsResponse
            Collaborations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.listcollaborations()
        """
        _response = self._raw_client.listcollaborations(request_options=request_options)
        return _response.data

    def getuserinformation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetUserInformationResponse:
        """
        Provides information about the user with the given ID.

        Parameters
        ----------
        id : str
            The unique ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetUserInformationResponse
            User login information.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getuserinformation(
            id="id",
        )
        """
        _response = self._raw_client.getuserinformation(id, request_options=request_options)
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

    async def getinformation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetInformationResponse:
        """
        Provides information about the user that is currently signed in.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetInformationResponse
            User login information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getinformation()


        asyncio.run(main())
        """
        _response = await self._raw_client.getinformation(request_options=request_options)
        return _response.data

    async def listcollaborations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserListCollaborationsResponse:
        """
        Provides the set of organizations of which a user is a member or a collaborator.

        The set of organizations that a user can collaborate on is composed of:

        * Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
        * The parent organization of repository that the user can collaborate on, but is not necessarily a member of
        * The organization of the current user's account

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserListCollaborationsResponse
            Collaborations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.listcollaborations()


        asyncio.run(main())
        """
        _response = await self._raw_client.listcollaborations(request_options=request_options)
        return _response.data

    async def getuserinformation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetUserInformationResponse:
        """
        Provides information about the user with the given ID.

        Parameters
        ----------
        id : str
            The unique ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetUserInformationResponse
            User login information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getuserinformation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getuserinformation(id, request_options=request_options)
        return _response.data
