

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient


OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationsClient
        """
        return self._raw_client

    def postmail(
        self,
        *,
        is_body_html: bool,
        message_body: str,
        subject: str,
        to_addresses: typing.Sequence[str],
        cc_addresses: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        is_body_html : bool

        message_body : str

        subject : str

        to_addresses : typing.Sequence[str]

        cc_addresses : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.postmail(
            is_body_html=True,
            message_body="MessageBody",
            subject="Subject",
            to_addresses=["To_Addresses"],
        )
        """
        _response = self._raw_client.postmail(
            is_body_html=is_body_html,
            message_body=message_body,
            subject=subject,
            to_addresses=to_addresses,
            cc_addresses=cc_addresses,
            request_options=request_options,
        )
        return _response.data


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationsClient
        """
        return self._raw_client

    async def postmail(
        self,
        *,
        is_body_html: bool,
        message_body: str,
        subject: str,
        to_addresses: typing.Sequence[str],
        cc_addresses: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        is_body_html : bool

        message_body : str

        subject : str

        to_addresses : typing.Sequence[str]

        cc_addresses : typing.Optional[typing.Sequence[str]]

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
            await client.notifications.postmail(
                is_body_html=True,
                message_body="MessageBody",
                subject="Subject",
                to_addresses=["To_Addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postmail(
            is_body_html=is_body_html,
            message_body=message_body,
            subject=subject,
            to_addresses=to_addresses,
            cc_addresses=cc_addresses,
            request_options=request_options,
        )
        return _response.data
