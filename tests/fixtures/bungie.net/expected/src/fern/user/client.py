

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.user_get_available_themes_response import UserGetAvailableThemesResponse
from .types.user_get_bungie_net_user_by_id_response import UserGetBungieNetUserByIdResponse
from .types.user_get_credential_types_for_target_account_response import UserGetCredentialTypesForTargetAccountResponse
from .types.user_get_membership_data_by_id_response import UserGetMembershipDataByIdResponse
from .types.user_get_membership_data_for_current_user_response import UserGetMembershipDataForCurrentUserResponse
from .types.user_get_membership_from_hard_linked_credential_response import (
    UserGetMembershipFromHardLinkedCredentialResponse,
)
from .types.user_get_sanitized_platform_display_names_response import UserGetSanitizedPlatformDisplayNamesResponse
from .types.user_search_by_global_name_post_response import UserSearchByGlobalNamePostResponse
from .types.user_search_by_global_name_prefix_response import UserSearchByGlobalNamePrefixResponse


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

    def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetAvailableThemesResponse:
        """
        Returns a list of all available user themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetAvailableThemesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getavailablethemes()
        """
        _response = self._raw_client.getavailablethemes(request_options=request_options)
        return _response.data

    def getbungienetuserbyid(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetBungieNetUserByIdResponse:
        """
        Loads a bungienet user by membership id.

        Parameters
        ----------
        id : int
            The requested Bungie.net membership id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetBungieNetUserByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getbungienetuserbyid(
            id=1000000,
        )
        """
        _response = self._raw_client.getbungienetuserbyid(id, request_options=request_options)
        return _response.data

    def getcredentialtypesfortargetaccount(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetCredentialTypesForTargetAccountResponse:
        """
        Returns a list of credential types attached to the requested account

        Parameters
        ----------
        membership_id : int
            The user's membership id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetCredentialTypesForTargetAccountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getcredentialtypesfortargetaccount(
            membership_id=1000000,
        )
        """
        _response = self._raw_client.getcredentialtypesfortargetaccount(membership_id, request_options=request_options)
        return _response.data

    def getmembershipfromhardlinkedcredential(
        self, cr_type: int, credential: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipFromHardLinkedCredentialResponse:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Parameters
        ----------
        cr_type : int
            The credential type. 'SteamId' is the only valid value at present.

        credential : str
            The credential to look up. Must be a valid SteamID64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipFromHardLinkedCredentialResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getmembershipfromhardlinkedcredential(
            cr_type=1,
            credential="credential",
        )
        """
        _response = self._raw_client.getmembershipfromhardlinkedcredential(
            cr_type, credential, request_options=request_options
        )
        return _response.data

    def getmembershipdatabyid(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipDataByIdResponse:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Parameters
        ----------
        membership_id : int
            The membership ID of the target user.

        membership_type : int
            Type of the supplied membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipDataByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getmembershipdatabyid(
            membership_id=1000000,
            membership_type=1,
        )
        """
        _response = self._raw_client.getmembershipdatabyid(
            membership_id, membership_type, request_options=request_options
        )
        return _response.data

    def getmembershipdataforcurrentuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipDataForCurrentUserResponse:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipDataForCurrentUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getmembershipdataforcurrentuser()
        """
        _response = self._raw_client.getmembershipdataforcurrentuser(request_options=request_options)
        return _response.data

    def getsanitizedplatformdisplaynames(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetSanitizedPlatformDisplayNamesResponse:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Parameters
        ----------
        membership_id : int
            The requested membership id to load.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetSanitizedPlatformDisplayNamesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.getsanitizedplatformdisplaynames(
            membership_id=1000000,
        )
        """
        _response = self._raw_client.getsanitizedplatformdisplaynames(membership_id, request_options=request_options)
        return _response.data

    def searchbyglobalnamepost(
        self, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserSearchByGlobalNamePostResponse:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Parameters
        ----------
        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSearchByGlobalNamePostResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.searchbyglobalnamepost(
            page=1,
        )
        """
        _response = self._raw_client.searchbyglobalnamepost(page, request_options=request_options)
        return _response.data

    def searchbyglobalnameprefix(
        self, display_name_prefix: str, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserSearchByGlobalNamePrefixResponse:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Parameters
        ----------
        display_name_prefix : str
            The display name prefix you're looking for.

        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSearchByGlobalNamePrefixResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.user.searchbyglobalnameprefix(
            display_name_prefix="displayNamePrefix",
            page=1,
        )
        """
        _response = self._raw_client.searchbyglobalnameprefix(
            display_name_prefix, page, request_options=request_options
        )
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

    async def getavailablethemes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetAvailableThemesResponse:
        """
        Returns a list of all available user themes.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetAvailableThemesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getavailablethemes()


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailablethemes(request_options=request_options)
        return _response.data

    async def getbungienetuserbyid(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetBungieNetUserByIdResponse:
        """
        Loads a bungienet user by membership id.

        Parameters
        ----------
        id : int
            The requested Bungie.net membership id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetBungieNetUserByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getbungienetuserbyid(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbungienetuserbyid(id, request_options=request_options)
        return _response.data

    async def getcredentialtypesfortargetaccount(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetCredentialTypesForTargetAccountResponse:
        """
        Returns a list of credential types attached to the requested account

        Parameters
        ----------
        membership_id : int
            The user's membership id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetCredentialTypesForTargetAccountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getcredentialtypesfortargetaccount(
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcredentialtypesfortargetaccount(
            membership_id, request_options=request_options
        )
        return _response.data

    async def getmembershipfromhardlinkedcredential(
        self, cr_type: int, credential: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipFromHardLinkedCredentialResponse:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Parameters
        ----------
        cr_type : int
            The credential type. 'SteamId' is the only valid value at present.

        credential : str
            The credential to look up. Must be a valid SteamID64.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipFromHardLinkedCredentialResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getmembershipfromhardlinkedcredential(
                cr_type=1,
                credential="credential",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmembershipfromhardlinkedcredential(
            cr_type, credential, request_options=request_options
        )
        return _response.data

    async def getmembershipdatabyid(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipDataByIdResponse:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Parameters
        ----------
        membership_id : int
            The membership ID of the target user.

        membership_type : int
            Type of the supplied membership ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipDataByIdResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getmembershipdatabyid(
                membership_id=1000000,
                membership_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmembershipdatabyid(
            membership_id, membership_type, request_options=request_options
        )
        return _response.data

    async def getmembershipdataforcurrentuser(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetMembershipDataForCurrentUserResponse:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetMembershipDataForCurrentUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getmembershipdataforcurrentuser()


        asyncio.run(main())
        """
        _response = await self._raw_client.getmembershipdataforcurrentuser(request_options=request_options)
        return _response.data

    async def getsanitizedplatformdisplaynames(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGetSanitizedPlatformDisplayNamesResponse:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Parameters
        ----------
        membership_id : int
            The requested membership id to load.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGetSanitizedPlatformDisplayNamesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.getsanitizedplatformdisplaynames(
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsanitizedplatformdisplaynames(
            membership_id, request_options=request_options
        )
        return _response.data

    async def searchbyglobalnamepost(
        self, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserSearchByGlobalNamePostResponse:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Parameters
        ----------
        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSearchByGlobalNamePostResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.searchbyglobalnamepost(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchbyglobalnamepost(page, request_options=request_options)
        return _response.data

    async def searchbyglobalnameprefix(
        self, display_name_prefix: str, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserSearchByGlobalNamePrefixResponse:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Parameters
        ----------
        display_name_prefix : str
            The display name prefix you're looking for.

        page : int
            The zero-based page of results you desire.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSearchByGlobalNamePrefixResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.user.searchbyglobalnameprefix(
                display_name_prefix="displayNamePrefix",
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchbyglobalnameprefix(
            display_name_prefix, page, request_options=request_options
        )
        return _response.data
