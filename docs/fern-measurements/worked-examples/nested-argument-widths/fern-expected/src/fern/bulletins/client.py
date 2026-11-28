

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulletin import Bulletin
from .raw_client import AsyncRawBulletinsClient, RawBulletinsClient


OMIT = typing.cast(typing.Any, ...)


class BulletinsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBulletinsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBulletinsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBulletinsClient
        """
        return self._raw_client

    def notify_bulletin(
        self,
        bulletin_id: str,
        *,
        cc_addresses: typing.Sequence[str],
        bcc_addresses: typing.Sequence[str],
        routing: typing.Dict[str, str],
        handling: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bulletin:
        """
        Parameters
        ----------
        bulletin_id : str

        cc_addresses : typing.Sequence[str]

        bcc_addresses : typing.Sequence[str]

        routing : typing.Dict[str, str]

        handling : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bulletin
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bulletins.notify_bulletin(
            bulletin_id="bulletin_id",
            cc_addresses=["alpha-one@example.com", "second-beta-twoooo@example.com"],
            bcc_addresses=["alpha-on@example.com", "second-beta-twooo@example.com"],
            routing={"priority": "high", "channel": "postal-mail-express-one-twooo"},
            handling={"priority": "high", "channel": "postal-mail-express-one-tww"},
        )
        """
        _response = self._raw_client.notify_bulletin(
            bulletin_id,
            cc_addresses=cc_addresses,
            bcc_addresses=bcc_addresses,
            routing=routing,
            handling=handling,
            request_options=request_options,
        )
        return _response.data


class AsyncBulletinsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBulletinsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBulletinsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBulletinsClient
        """
        return self._raw_client

    async def notify_bulletin(
        self,
        bulletin_id: str,
        *,
        cc_addresses: typing.Sequence[str],
        bcc_addresses: typing.Sequence[str],
        routing: typing.Dict[str, str],
        handling: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Bulletin:
        """
        Parameters
        ----------
        bulletin_id : str

        cc_addresses : typing.Sequence[str]

        bcc_addresses : typing.Sequence[str]

        routing : typing.Dict[str, str]

        handling : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Bulletin
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bulletins.notify_bulletin(
                bulletin_id="bulletin_id",
                cc_addresses=[
                    "alpha-one@example.com",
                    "second-beta-twoooo@example.com",
                ],
                bcc_addresses=["alpha-on@example.com", "second-beta-twooo@example.com"],
                routing={
                    "priority": "high",
                    "channel": "postal-mail-express-one-twooo",
                },
                handling={"priority": "high", "channel": "postal-mail-express-one-tww"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.notify_bulletin(
            bulletin_id,
            cc_addresses=cc_addresses,
            bcc_addresses=bcc_addresses,
            routing=routing,
            handling=handling,
            request_options=request_options,
        )
        return _response.data
