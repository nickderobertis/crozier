

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSocialClient, RawSocialClient
from .types.social_accept_friend_request_response import SocialAcceptFriendRequestResponse
from .types.social_decline_friend_request_response import SocialDeclineFriendRequestResponse
from .types.social_get_friend_list_response import SocialGetFriendListResponse
from .types.social_get_friend_request_list_response import SocialGetFriendRequestListResponse
from .types.social_get_platform_friend_list_response import SocialGetPlatformFriendListResponse
from .types.social_issue_friend_request_response import SocialIssueFriendRequestResponse
from .types.social_remove_friend_request_response import SocialRemoveFriendRequestResponse
from .types.social_remove_friend_response import SocialRemoveFriendResponse


class SocialClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSocialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSocialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSocialClient
        """
        return self._raw_client

    def getfriendlist(self, *, request_options: typing.Optional[RequestOptions] = None) -> SocialGetFriendListResponse:
        """
        Returns your Bungie Friend list

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetFriendListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.getfriendlist()
        """
        _response = self._raw_client.getfriendlist(request_options=request_options)
        return _response.data

    def issuefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialIssueFriendRequestResponse:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialIssueFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.issuefriendrequest(
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.issuefriendrequest(membership_id, request_options=request_options)
        return _response.data

    def removefriend(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialRemoveFriendResponse:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialRemoveFriendResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.removefriend(
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.removefriend(membership_id, request_options=request_options)
        return _response.data

    def getfriendrequestlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialGetFriendRequestListResponse:
        """
        Returns your friend request queue.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetFriendRequestListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.getfriendrequestlist()
        """
        _response = self._raw_client.getfriendrequestlist(request_options=request_options)
        return _response.data

    def acceptfriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialAcceptFriendRequestResponse:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialAcceptFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.acceptfriendrequest(
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.acceptfriendrequest(membership_id, request_options=request_options)
        return _response.data

    def declinefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialDeclineFriendRequestResponse:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to decline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialDeclineFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.declinefriendrequest(
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.declinefriendrequest(membership_id, request_options=request_options)
        return _response.data

    def removefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialRemoveFriendRequestResponse:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialRemoveFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.removefriendrequest(
            membership_id="membershipId",
        )
        """
        _response = self._raw_client.removefriendrequest(membership_id, request_options=request_options)
        return _response.data

    def getplatformfriendlist(
        self, friend_platform: int, page: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialGetPlatformFriendListResponse:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Parameters
        ----------
        friend_platform : int
            The platform friend type.

        page : str
            The zero based page to return. Page size is 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetPlatformFriendListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.social.getplatformfriendlist(
            friend_platform=1,
            page="page",
        )
        """
        _response = self._raw_client.getplatformfriendlist(friend_platform, page, request_options=request_options)
        return _response.data


class AsyncSocialClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSocialClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSocialClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSocialClient
        """
        return self._raw_client

    async def getfriendlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialGetFriendListResponse:
        """
        Returns your Bungie Friend list

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetFriendListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.getfriendlist()


        asyncio.run(main())
        """
        _response = await self._raw_client.getfriendlist(request_options=request_options)
        return _response.data

    async def issuefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialIssueFriendRequestResponse:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to add.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialIssueFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.issuefriendrequest(
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issuefriendrequest(membership_id, request_options=request_options)
        return _response.data

    async def removefriend(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialRemoveFriendResponse:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialRemoveFriendResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.removefriend(
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removefriend(membership_id, request_options=request_options)
        return _response.data

    async def getfriendrequestlist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialGetFriendRequestListResponse:
        """
        Returns your friend request queue.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetFriendRequestListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.getfriendrequestlist()


        asyncio.run(main())
        """
        _response = await self._raw_client.getfriendrequestlist(request_options=request_options)
        return _response.data

    async def acceptfriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialAcceptFriendRequestResponse:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialAcceptFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.acceptfriendrequest(
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.acceptfriendrequest(membership_id, request_options=request_options)
        return _response.data

    async def declinefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialDeclineFriendRequestResponse:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to decline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialDeclineFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.declinefriendrequest(
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.declinefriendrequest(membership_id, request_options=request_options)
        return _response.data

    async def removefriendrequest(
        self, membership_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialRemoveFriendRequestResponse:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Parameters
        ----------
        membership_id : str
            The membership id of the user you wish to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialRemoveFriendRequestResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.removefriendrequest(
                membership_id="membershipId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removefriendrequest(membership_id, request_options=request_options)
        return _response.data

    async def getplatformfriendlist(
        self, friend_platform: int, page: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SocialGetPlatformFriendListResponse:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Parameters
        ----------
        friend_platform : int
            The platform friend type.

        page : str
            The zero based page to return. Page size is 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SocialGetPlatformFriendListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.social.getplatformfriendlist(
                friend_platform=1,
                page="page",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getplatformfriendlist(friend_platform, page, request_options=request_options)
        return _response.data
