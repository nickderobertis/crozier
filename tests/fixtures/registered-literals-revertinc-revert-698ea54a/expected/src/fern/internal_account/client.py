

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_app import CommonApp
from ..types.common_app_config import CommonAppConfig
from ..types.common_tpid import CommonTpid
from ..types.internal_delete_revert_app_response import InternalDeleteRevertAppResponse
from ..types.internal_get_account_details_response import InternalGetAccountDetailsResponse
from ..types.internal_svix_account_response import InternalSvixAccountResponse
from ..types.internal_svix_magic_link_response import InternalSvixMagicLinkResponse
from ..types.internalset_onboarding_response import InternalsetOnboardingResponse
from .raw_client import AsyncRawInternalAccountClient, RawInternalAccountClient


OMIT = typing.cast(typing.Any, ...)


class InternalAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalAccountClient
        """
        return self._raw_client

    def internal_account_get_account_details(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalGetAccountDetailsResponse:
        """
        Get details of a revert user account

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAccountDetailsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_get_account_details(
            user_id="userId",
        )
        """
        _response = self._raw_client.internal_account_get_account_details(
            user_id=user_id, request_options=request_options
        )
        return _response.data

    def internal_account_update_account_credentials(
        self,
        *,
        tp_id: CommonTpid,
        is_revert_app: bool,
        app_id: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        app_config: typing.Optional[CommonAppConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonApp:
        """
        Update account credentials (customer app token, secret, scope)

        Parameters
        ----------
        tp_id : CommonTpid

        is_revert_app : bool

        app_id : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        scopes : typing.Optional[typing.Sequence[str]]

        app_config : typing.Optional[CommonAppConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonApp


        Examples
        --------
        from fern import CommonTpid, FernApi

        client = FernApi()
        client.internal_account.internal_account_update_account_credentials(
            tp_id=CommonTpid.HUBSPOT,
            is_revert_app=True,
            app_id="appId",
        )
        """
        _response = self._raw_client.internal_account_update_account_credentials(
            tp_id=tp_id,
            is_revert_app=is_revert_app,
            app_id=app_id,
            client_id=client_id,
            client_secret=client_secret,
            scopes=scopes,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data

    def internal_account_create_revert_app_for_account(
        self,
        *,
        user_id: str,
        tp_id: CommonTpid,
        environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalGetAccountDetailsResponse:
        """
        create Revert App for Account

        Parameters
        ----------
        user_id : str

        tp_id : CommonTpid

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAccountDetailsResponse


        Examples
        --------
        from fern import CommonTpid, FernApi

        client = FernApi()
        client.internal_account.internal_account_create_revert_app_for_account(
            user_id="userId",
            tp_id=CommonTpid.HUBSPOT,
            environment="environment",
        )
        """
        _response = self._raw_client.internal_account_create_revert_app_for_account(
            user_id=user_id, tp_id=tp_id, environment=environment, request_options=request_options
        )
        return _response.data

    def internal_account_delete_revert_appfor_account(
        self, *, app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalDeleteRevertAppResponse:
        """
        delete Revert App for Account

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalDeleteRevertAppResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_delete_revert_appfor_account(
            app_id="appId",
        )
        """
        _response = self._raw_client.internal_account_delete_revert_appfor_account(
            app_id=app_id, request_options=request_options
        )
        return _response.data

    def internal_account_get_svix_account(
        self, id: str, *, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixAccountResponse:
        """
        Get Svix Account

        Parameters
        ----------
        id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_get_svix_account(
            id="id",
            environment="environment",
        )
        """
        _response = self._raw_client.internal_account_get_svix_account(
            id, environment=environment, request_options=request_options
        )
        return _response.data

    def internal_account_create_svix_account(
        self, *, environment: str, account_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixAccountResponse:
        """
        Create Svix Account

        Parameters
        ----------
        environment : str

        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixAccountResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_create_svix_account(
            environment="environment",
            account_id="accountId",
        )
        """
        _response = self._raw_client.internal_account_create_svix_account(
            environment=environment, account_id=account_id, request_options=request_options
        )
        return _response.data

    def internal_account_create_svix_account_magic_link(
        self, *, app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixMagicLinkResponse:
        """
        Create Svix Account Consumer Panel MagicLink

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixMagicLinkResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_create_svix_account_magic_link(
            app_id="appId",
        )
        """
        _response = self._raw_client.internal_account_create_svix_account_magic_link(
            app_id=app_id, request_options=request_options
        )
        return _response.data

    def internal_account_set_onboarding_completed(
        self, *, user_id: str, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalsetOnboardingResponse:
        """
        Set Onboarding Completed

        Parameters
        ----------
        user_id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalsetOnboardingResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal_account.internal_account_set_onboarding_completed(
            user_id="userId",
            environment="environment",
        )
        """
        _response = self._raw_client.internal_account_set_onboarding_completed(
            user_id=user_id, environment=environment, request_options=request_options
        )
        return _response.data


class AsyncInternalAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalAccountClient
        """
        return self._raw_client

    async def internal_account_get_account_details(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalGetAccountDetailsResponse:
        """
        Get details of a revert user account

        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAccountDetailsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_get_account_details(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_get_account_details(
            user_id=user_id, request_options=request_options
        )
        return _response.data

    async def internal_account_update_account_credentials(
        self,
        *,
        tp_id: CommonTpid,
        is_revert_app: bool,
        app_id: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        app_config: typing.Optional[CommonAppConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonApp:
        """
        Update account credentials (customer app token, secret, scope)

        Parameters
        ----------
        tp_id : CommonTpid

        is_revert_app : bool

        app_id : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        scopes : typing.Optional[typing.Sequence[str]]

        app_config : typing.Optional[CommonAppConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonApp


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommonTpid

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_update_account_credentials(
                tp_id=CommonTpid.HUBSPOT,
                is_revert_app=True,
                app_id="appId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_update_account_credentials(
            tp_id=tp_id,
            is_revert_app=is_revert_app,
            app_id=app_id,
            client_id=client_id,
            client_secret=client_secret,
            scopes=scopes,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data

    async def internal_account_create_revert_app_for_account(
        self,
        *,
        user_id: str,
        tp_id: CommonTpid,
        environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalGetAccountDetailsResponse:
        """
        create Revert App for Account

        Parameters
        ----------
        user_id : str

        tp_id : CommonTpid

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalGetAccountDetailsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommonTpid

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_create_revert_app_for_account(
                user_id="userId",
                tp_id=CommonTpid.HUBSPOT,
                environment="environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_create_revert_app_for_account(
            user_id=user_id, tp_id=tp_id, environment=environment, request_options=request_options
        )
        return _response.data

    async def internal_account_delete_revert_appfor_account(
        self, *, app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalDeleteRevertAppResponse:
        """
        delete Revert App for Account

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalDeleteRevertAppResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_delete_revert_appfor_account(
                app_id="appId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_delete_revert_appfor_account(
            app_id=app_id, request_options=request_options
        )
        return _response.data

    async def internal_account_get_svix_account(
        self, id: str, *, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixAccountResponse:
        """
        Get Svix Account

        Parameters
        ----------
        id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_get_svix_account(
                id="id",
                environment="environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_get_svix_account(
            id, environment=environment, request_options=request_options
        )
        return _response.data

    async def internal_account_create_svix_account(
        self, *, environment: str, account_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixAccountResponse:
        """
        Create Svix Account

        Parameters
        ----------
        environment : str

        account_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixAccountResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_create_svix_account(
                environment="environment",
                account_id="accountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_create_svix_account(
            environment=environment, account_id=account_id, request_options=request_options
        )
        return _response.data

    async def internal_account_create_svix_account_magic_link(
        self, *, app_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalSvixMagicLinkResponse:
        """
        Create Svix Account Consumer Panel MagicLink

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalSvixMagicLinkResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_create_svix_account_magic_link(
                app_id="appId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_create_svix_account_magic_link(
            app_id=app_id, request_options=request_options
        )
        return _response.data

    async def internal_account_set_onboarding_completed(
        self, *, user_id: str, environment: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InternalsetOnboardingResponse:
        """
        Set Onboarding Completed

        Parameters
        ----------
        user_id : str

        environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalsetOnboardingResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal_account.internal_account_set_onboarding_completed(
                user_id="userId",
                environment="environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.internal_account_set_onboarding_completed(
            user_id=user_id, environment=environment, request_options=request_options
        )
        return _response.data
