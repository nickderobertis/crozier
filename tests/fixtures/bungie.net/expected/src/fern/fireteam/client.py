

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFireteamClient, RawFireteamClient
from .types.fireteam_get_active_private_clan_fireteam_count_response import (
    FireteamGetActivePrivateClanFireteamCountResponse,
)
from .types.fireteam_get_available_clan_fireteams_response import FireteamGetAvailableClanFireteamsResponse
from .types.fireteam_get_clan_fireteam_response import FireteamGetClanFireteamResponse
from .types.fireteam_get_my_clan_fireteams_response import FireteamGetMyClanFireteamsResponse
from .types.fireteam_search_public_available_clan_fireteams_response import (
    FireteamSearchPublicAvailableClanFireteamsResponse,
)


class FireteamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFireteamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFireteamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFireteamClient
        """
        return self._raw_client

    def getactiveprivateclanfireteamcount(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FireteamGetActivePrivateClanFireteamCountResponse:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetActivePrivateClanFireteamCountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fireteam.getactiveprivateclanfireteamcount(
            group_id=1000000,
        )
        """
        _response = self._raw_client.getactiveprivateclanfireteamcount(group_id, request_options=request_options)
        return _response.data

    def getavailableclanfireteams(
        self,
        group_id: int,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        public_only: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamGetAvailableClanFireteamsResponse:
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        public_only : int
            Determines public/private filtering.

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetAvailableClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fireteam.getavailableclanfireteams(
            group_id=1000000,
            platform=1,
            activity_type=1,
            date_range=1,
            slot_filter=1,
            public_only=1,
            page=1,
        )
        """
        _response = self._raw_client.getavailableclanfireteams(
            group_id,
            platform,
            activity_type,
            date_range,
            slot_filter,
            public_only,
            page,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data

    def getmyclanfireteams(
        self,
        group_id: int,
        platform: int,
        include_closed: bool,
        page: int,
        *,
        group_filter: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamGetMyClanFireteamsResponse:
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Parameters
        ----------
        group_id : int
            The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).

        platform : int
            The platform filter.

        include_closed : bool
            If true, return fireteams that have been closed.

        page : int
            Deprecated parameter, ignored.

        group_filter : typing.Optional[bool]
            If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetMyClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fireteam.getmyclanfireteams(
            group_id=1000000,
            platform=1,
            include_closed=True,
            page=1,
        )
        """
        _response = self._raw_client.getmyclanfireteams(
            group_id,
            platform,
            include_closed,
            page,
            group_filter=group_filter,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data

    def getclanfireteam(
        self, group_id: int, fireteam_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FireteamGetClanFireteamResponse:
        """
        Gets a specific fireteam.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        fireteam_id : int
            The unique id of the fireteam.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetClanFireteamResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fireteam.getclanfireteam(
            group_id=1000000,
            fireteam_id=1000000,
        )
        """
        _response = self._raw_client.getclanfireteam(group_id, fireteam_id, request_options=request_options)
        return _response.data

    def searchpublicavailableclanfireteams(
        self,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamSearchPublicAvailableClanFireteamsResponse:
        """
        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamSearchPublicAvailableClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fireteam.searchpublicavailableclanfireteams(
            platform=1,
            activity_type=1,
            date_range=1,
            slot_filter=1,
            page=1,
        )
        """
        _response = self._raw_client.searchpublicavailableclanfireteams(
            platform,
            activity_type,
            date_range,
            slot_filter,
            page,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data


class AsyncFireteamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFireteamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFireteamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFireteamClient
        """
        return self._raw_client

    async def getactiveprivateclanfireteamcount(
        self, group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FireteamGetActivePrivateClanFireteamCountResponse:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetActivePrivateClanFireteamCountResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fireteam.getactiveprivateclanfireteamcount(
                group_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getactiveprivateclanfireteamcount(group_id, request_options=request_options)
        return _response.data

    async def getavailableclanfireteams(
        self,
        group_id: int,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        public_only: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamGetAvailableClanFireteamsResponse:
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        public_only : int
            Determines public/private filtering.

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetAvailableClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fireteam.getavailableclanfireteams(
                group_id=1000000,
                platform=1,
                activity_type=1,
                date_range=1,
                slot_filter=1,
                public_only=1,
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailableclanfireteams(
            group_id,
            platform,
            activity_type,
            date_range,
            slot_filter,
            public_only,
            page,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data

    async def getmyclanfireteams(
        self,
        group_id: int,
        platform: int,
        include_closed: bool,
        page: int,
        *,
        group_filter: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamGetMyClanFireteamsResponse:
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Parameters
        ----------
        group_id : int
            The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).

        platform : int
            The platform filter.

        include_closed : bool
            If true, return fireteams that have been closed.

        page : int
            Deprecated parameter, ignored.

        group_filter : typing.Optional[bool]
            If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetMyClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fireteam.getmyclanfireteams(
                group_id=1000000,
                platform=1,
                include_closed=True,
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmyclanfireteams(
            group_id,
            platform,
            include_closed,
            page,
            group_filter=group_filter,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data

    async def getclanfireteam(
        self, group_id: int, fireteam_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FireteamGetClanFireteamResponse:
        """
        Gets a specific fireteam.

        Parameters
        ----------
        group_id : int
            The group id of the clan.

        fireteam_id : int
            The unique id of the fireteam.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamGetClanFireteamResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fireteam.getclanfireteam(
                group_id=1000000,
                fireteam_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getclanfireteam(group_id, fireteam_id, request_options=request_options)
        return _response.data

    async def searchpublicavailableclanfireteams(
        self,
        platform: int,
        activity_type: int,
        date_range: int,
        slot_filter: int,
        page: int,
        *,
        exclude_immediate: typing.Optional[bool] = None,
        lang_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FireteamSearchPublicAvailableClanFireteamsResponse:
        """
        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

        Parameters
        ----------
        platform : int
            The platform filter.

        activity_type : int
            The activity type to filter by.

        date_range : int
            The date range to grab available fireteams.

        slot_filter : int
            Filters based on available slots

        page : int
            Zero based page

        exclude_immediate : typing.Optional[bool]
            If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.

        lang_filter : typing.Optional[str]
            An optional language filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FireteamSearchPublicAvailableClanFireteamsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fireteam.searchpublicavailableclanfireteams(
                platform=1,
                activity_type=1,
                date_range=1,
                slot_filter=1,
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.searchpublicavailableclanfireteams(
            platform,
            activity_type,
            date_range,
            slot_filter,
            page,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
            request_options=request_options,
        )
        return _response.data
