

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_info_item import AppInfoItem
from ..types.login_response import LoginResponse
from ..types.user_info_response import UserInfoResponse
from .raw_client import AsyncRawSteamClient, RawSteamClient
from .types.get_v1steam_filedetails_response import GetV1SteamFiledetailsResponse
from .types.open_id_body_mode import OpenIdBodyMode
from .types.post_v1steam_login_request_openid_mode import PostV1SteamLoginRequestOpenidMode


OMIT = typing.cast(typing.Any, ...)


class SteamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSteamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSteamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSteamClient
        """
        return self._raw_client

    def get_steam_app_info(
        self,
        *,
        app_id: int,
        raw: typing.Optional[bool] = None,
        controller_support: typing.Optional[bool] = None,
        official_configs: typing.Optional[bool] = None,
        force_refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppInfoItem:
        """
        Retrieve app information from Steam Store for a given app ID

        Parameters
        ----------
        app_id : int

        raw : typing.Optional[bool]

        controller_support : typing.Optional[bool]

        official_configs : typing.Optional[bool]

        force_refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppInfoItem
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steam.get_steam_app_info(
            app_id=1,
        )
        """
        _response = self._raw_client.get_steam_app_info(
            app_id=app_id,
            raw=raw,
            controller_support=controller_support,
            official_configs=official_configs,
            force_refresh=force_refresh,
            request_options=request_options,
        )
        return _response.data

    def get_controller_config_details(
        self,
        *,
        file_id: int,
        playtime_stats: typing.Optional[int] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1SteamFiledetailsResponse:
        """

        Retrieve details for a given controller config file ID.
        If a non-controller config file ID is provided, this will respond with a 404

        Parameters
        ----------
        file_id : int

        playtime_stats : typing.Optional[int]
            Number of days for playtime statistics

        raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1SteamFiledetailsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steam.get_controller_config_details(
            file_id=1,
        )
        """
        _response = self._raw_client.get_controller_config_details(
            file_id=file_id, playtime_stats=playtime_stats, raw=raw, request_options=request_options
        )
        return _response.data

    def log_in_with_steam(
        self,
        *,
        assoc_handle: str,
        claimed_id: str,
        identity: str,
        mode: OpenIdBodyMode,
        ns: str,
        op_endpoint: str,
        response_nonce: str,
        return_to: str,
        sig: str,
        signed: str,
        openid_ns: typing.Optional[str] = None,
        openid_mode: typing.Optional[PostV1SteamLoginRequestOpenidMode] = None,
        openid_op_endpoint: typing.Optional[str] = None,
        openid_claimed_id: typing.Optional[str] = None,
        openid_identity: typing.Optional[str] = None,
        openid_return_to: typing.Optional[str] = None,
        openid_response_nonce: typing.Optional[str] = None,
        openid_assoc_handle: typing.Optional[str] = None,
        openid_signed: typing.Optional[str] = None,
        openid_sig: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginResponse:
        """
        Authenticate user via Steam OpenID and return JWT token
                    Wrapper endpoint for SSR frontend

        Parameters
        ----------
        assoc_handle : str

        claimed_id : str

        identity : str

        mode : OpenIdBodyMode

        ns : str

        op_endpoint : str

        response_nonce : str

        return_to : str

        sig : str

        signed : str

        openid_ns : typing.Optional[str]

        openid_mode : typing.Optional[PostV1SteamLoginRequestOpenidMode]

        openid_op_endpoint : typing.Optional[str]

        openid_claimed_id : typing.Optional[str]

        openid_identity : typing.Optional[str]

        openid_return_to : typing.Optional[str]

        openid_response_nonce : typing.Optional[str]

        openid_assoc_handle : typing.Optional[str]

        openid_signed : typing.Optional[str]

        openid_sig : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            OK

        Examples
        --------
        from fern.steam import OpenIdBodyMode

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steam.log_in_with_steam(
            assoc_handle="assoc_handle",
            claimed_id="claimed_id",
            identity="identity",
            mode=OpenIdBodyMode.ID_RES,
            ns="ns",
            op_endpoint="op_endpoint",
            response_nonce="response_nonce",
            return_to="return_to",
            sig="sig",
            signed="signed",
        )
        """
        _response = self._raw_client.log_in_with_steam(
            assoc_handle=assoc_handle,
            claimed_id=claimed_id,
            identity=identity,
            mode=mode,
            ns=ns,
            op_endpoint=op_endpoint,
            response_nonce=response_nonce,
            return_to=return_to,
            sig=sig,
            signed=signed,
            openid_ns=openid_ns,
            openid_mode=openid_mode,
            openid_op_endpoint=openid_op_endpoint,
            openid_claimed_id=openid_claimed_id,
            openid_identity=openid_identity,
            openid_return_to=openid_return_to,
            openid_response_nonce=openid_response_nonce,
            openid_assoc_handle=openid_assoc_handle,
            openid_signed=openid_signed,
            openid_sig=openid_sig,
            request_options=request_options,
        )
        return _response.data

    def get_steam_user_info(
        self,
        *,
        user_id: typing.Optional[str] = None,
        include_avatar_frame: typing.Optional[bool] = None,
        include_profile_background: typing.Optional[bool] = None,
        include_mini_profile_background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserInfoResponse:
        """
        Retrieve user information from Steam for the provided userId,
        or for attempt authenticated user if no userId is provided
        Returns 401 if no id provided and token is invalid and 400 if everything is missing

        Parameters
        ----------
        user_id : typing.Optional[str]

        include_avatar_frame : typing.Optional[bool]

        include_profile_background : typing.Optional[bool]

        include_mini_profile_background : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfoResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steam.get_steam_user_info()
        """
        _response = self._raw_client.get_steam_user_info(
            user_id=user_id,
            include_avatar_frame=include_avatar_frame,
            include_profile_background=include_profile_background,
            include_mini_profile_background=include_mini_profile_background,
            request_options=request_options,
        )
        return _response.data


class AsyncSteamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSteamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSteamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSteamClient
        """
        return self._raw_client

    async def get_steam_app_info(
        self,
        *,
        app_id: int,
        raw: typing.Optional[bool] = None,
        controller_support: typing.Optional[bool] = None,
        official_configs: typing.Optional[bool] = None,
        force_refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppInfoItem:
        """
        Retrieve app information from Steam Store for a given app ID

        Parameters
        ----------
        app_id : int

        raw : typing.Optional[bool]

        controller_support : typing.Optional[bool]

        official_configs : typing.Optional[bool]

        force_refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppInfoItem
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steam.get_steam_app_info(
                app_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_steam_app_info(
            app_id=app_id,
            raw=raw,
            controller_support=controller_support,
            official_configs=official_configs,
            force_refresh=force_refresh,
            request_options=request_options,
        )
        return _response.data

    async def get_controller_config_details(
        self,
        *,
        file_id: int,
        playtime_stats: typing.Optional[int] = None,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1SteamFiledetailsResponse:
        """

        Retrieve details for a given controller config file ID.
        If a non-controller config file ID is provided, this will respond with a 404

        Parameters
        ----------
        file_id : int

        playtime_stats : typing.Optional[int]
            Number of days for playtime statistics

        raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1SteamFiledetailsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steam.get_controller_config_details(
                file_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_controller_config_details(
            file_id=file_id, playtime_stats=playtime_stats, raw=raw, request_options=request_options
        )
        return _response.data

    async def log_in_with_steam(
        self,
        *,
        assoc_handle: str,
        claimed_id: str,
        identity: str,
        mode: OpenIdBodyMode,
        ns: str,
        op_endpoint: str,
        response_nonce: str,
        return_to: str,
        sig: str,
        signed: str,
        openid_ns: typing.Optional[str] = None,
        openid_mode: typing.Optional[PostV1SteamLoginRequestOpenidMode] = None,
        openid_op_endpoint: typing.Optional[str] = None,
        openid_claimed_id: typing.Optional[str] = None,
        openid_identity: typing.Optional[str] = None,
        openid_return_to: typing.Optional[str] = None,
        openid_response_nonce: typing.Optional[str] = None,
        openid_assoc_handle: typing.Optional[str] = None,
        openid_signed: typing.Optional[str] = None,
        openid_sig: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginResponse:
        """
        Authenticate user via Steam OpenID and return JWT token
                    Wrapper endpoint for SSR frontend

        Parameters
        ----------
        assoc_handle : str

        claimed_id : str

        identity : str

        mode : OpenIdBodyMode

        ns : str

        op_endpoint : str

        response_nonce : str

        return_to : str

        sig : str

        signed : str

        openid_ns : typing.Optional[str]

        openid_mode : typing.Optional[PostV1SteamLoginRequestOpenidMode]

        openid_op_endpoint : typing.Optional[str]

        openid_claimed_id : typing.Optional[str]

        openid_identity : typing.Optional[str]

        openid_return_to : typing.Optional[str]

        openid_response_nonce : typing.Optional[str]

        openid_assoc_handle : typing.Optional[str]

        openid_signed : typing.Optional[str]

        openid_sig : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            OK

        Examples
        --------
        import asyncio

        from fern.steam import OpenIdBodyMode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steam.log_in_with_steam(
                assoc_handle="assoc_handle",
                claimed_id="claimed_id",
                identity="identity",
                mode=OpenIdBodyMode.ID_RES,
                ns="ns",
                op_endpoint="op_endpoint",
                response_nonce="response_nonce",
                return_to="return_to",
                sig="sig",
                signed="signed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_in_with_steam(
            assoc_handle=assoc_handle,
            claimed_id=claimed_id,
            identity=identity,
            mode=mode,
            ns=ns,
            op_endpoint=op_endpoint,
            response_nonce=response_nonce,
            return_to=return_to,
            sig=sig,
            signed=signed,
            openid_ns=openid_ns,
            openid_mode=openid_mode,
            openid_op_endpoint=openid_op_endpoint,
            openid_claimed_id=openid_claimed_id,
            openid_identity=openid_identity,
            openid_return_to=openid_return_to,
            openid_response_nonce=openid_response_nonce,
            openid_assoc_handle=openid_assoc_handle,
            openid_signed=openid_signed,
            openid_sig=openid_sig,
            request_options=request_options,
        )
        return _response.data

    async def get_steam_user_info(
        self,
        *,
        user_id: typing.Optional[str] = None,
        include_avatar_frame: typing.Optional[bool] = None,
        include_profile_background: typing.Optional[bool] = None,
        include_mini_profile_background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserInfoResponse:
        """
        Retrieve user information from Steam for the provided userId,
        or for attempt authenticated user if no userId is provided
        Returns 401 if no id provided and token is invalid and 400 if everything is missing

        Parameters
        ----------
        user_id : typing.Optional[str]

        include_avatar_frame : typing.Optional[bool]

        include_profile_background : typing.Optional[bool]

        include_mini_profile_background : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfoResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steam.get_steam_user_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_steam_user_info(
            user_id=user_id,
            include_avatar_frame=include_avatar_frame,
            include_profile_background=include_profile_background,
            include_mini_profile_background=include_mini_profile_background,
            request_options=request_options,
        )
        return _response.data
