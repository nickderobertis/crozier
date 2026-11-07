

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.user_status_user_status_get_status200response import UserStatusUserStatusGetStatus200Response
from .raw_client import AsyncRawUserStatusUserStatusClient, RawUserStatusUserStatusClient


class UserStatusUserStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserStatusUserStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserStatusUserStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserStatusUserStatusClient
        """
        return self._raw_client

    def get_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The status was found successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data

    def set_status(
        self, *, status_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status_type : str
            The new status type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The status was updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.set_status(
            status_type="statusType",
        )
        """
        _response = self._raw_client.set_status(status_type=status_type, request_options=request_options)
        return _response.data

    def set_predefined_message(
        self,
        *,
        message_id: str,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        message_id : str
            ID of the predefined message

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The message was updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.set_predefined_message(
            message_id="messageId",
        )
        """
        _response = self._raw_client.set_predefined_message(
            message_id=message_id, clear_at=clear_at, request_options=request_options
        )
        return _response.data

    def set_custom_message(
        self,
        *,
        status_icon: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status_icon : typing.Optional[str]
            Icon of the status

        message : typing.Optional[str]
            Message of the status

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The message was updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.set_custom_message()
        """
        _response = self._raw_client.set_custom_message(
            status_icon=status_icon, message=message, clear_at=clear_at, request_options=request_options
        )
        return _response.data

    def clear_message(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.clear_message()
        """
        _response = self._raw_client.clear_message(request_options=request_options)
        return _response.data

    def revert_status(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        message_id : str
            ID of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            Status reverted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_status_user_status.revert_status(
            message_id="messageId",
        )
        """
        _response = self._raw_client.revert_status(message_id, request_options=request_options)
        return _response.data


class AsyncUserStatusUserStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserStatusUserStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserStatusUserStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserStatusUserStatusClient
        """
        return self._raw_client

    async def get_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The status was found successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data

    async def set_status(
        self, *, status_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status_type : str
            The new status type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The status was updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.set_status(
                status_type="statusType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_status(status_type=status_type, request_options=request_options)
        return _response.data

    async def set_predefined_message(
        self,
        *,
        message_id: str,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        message_id : str
            ID of the predefined message

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The message was updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.set_predefined_message(
                message_id="messageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_predefined_message(
            message_id=message_id, clear_at=clear_at, request_options=request_options
        )
        return _response.data

    async def set_custom_message(
        self,
        *,
        status_icon: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        status_icon : typing.Optional[str]
            Icon of the status

        message : typing.Optional[str]
            Message of the status

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            The message was updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.set_custom_message()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_custom_message(
            status_icon=status_icon, message=message, clear_at=clear_at, request_options=request_options
        )
        return _response.data

    async def clear_message(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.clear_message()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_message(request_options=request_options)
        return _response.data

    async def revert_status(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserStatusUserStatusGetStatus200Response:
        """
        Parameters
        ----------
        message_id : str
            ID of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserStatusUserStatusGetStatus200Response
            Status reverted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user_status_user_status.revert_status(
                message_id="messageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revert_status(message_id, request_options=request_options)
        return _response.data
