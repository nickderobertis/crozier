

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSealsClient, RawSealsClient
from .types.inspect_charm_request_token import InspectCharmRequestToken
from .types.seal_registration_seal import SealRegistrationSeal
from .types.stock_shelf_request_shelf_value import StockShelfRequestShelfValue
from .types.verify_badge_request_badge import VerifyBadgeRequestBadge
from .types.verify_charm_request_token import VerifyCharmRequestToken
from .types.verify_logbook_request_entry import VerifyLogbookRequestEntry
from .types.verify_logbook_response import VerifyLogbookResponse
from .types.verify_seal_request_seal import VerifySealRequestSeal
from .types.verify_seal_response import VerifySealResponse


OMIT = typing.cast(typing.Any, ...)


class SealsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSealsClient
        """
        return self._raw_client

    def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifySealResponse:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySealResponse
            Verified

        Examples
        --------
        from fern.seals import VerifySealRequestSeal_Stamp

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.verify_seal(
            seal=VerifySealRequestSeal_Stamp(
                stamp_id="stamp_id",
            ),
        )
        """
        _response = self._raw_client.verify_seal(seal=seal, request_options=request_options)
        return _response.data

    def verify_logbook(
        self, *, entry: VerifyLogbookRequestEntry, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyLogbookResponse:
        """
        Parameters
        ----------
        entry : VerifyLogbookRequestEntry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyLogbookResponse
            Verified

        Examples
        --------
        from fern import EntryV2, FernApi, PageV2, PageV2Edition

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.verify_logbook(
            entry=EntryV2(
                page=PageV2(
                    edition=PageV2Edition.TWO0,
                    keeper="Morwenna",
                ),
            ),
        )
        """
        _response = self._raw_client.verify_logbook(entry=entry, request_options=request_options)
        return _response.data

    def stock_shelf(
        self,
        *,
        shelf: typing.Dict[str, StockShelfRequestShelfValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        shelf : typing.Dict[str, StockShelfRequestShelfValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.seals import StockShelfRequestShelfValue_Stamp

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.stock_shelf(
            shelf={
                "top": StockShelfRequestShelfValue_Stamp(
                    stamp_id="stamp_id",
                )
            },
        )
        """
        _response = self._raw_client.stock_shelf(shelf=shelf, request_options=request_options)
        return _response.data

    def verify_badge(
        self, *, badge: VerifyBadgeRequestBadge, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        badge : VerifyBadgeRequestBadge

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.seals import VerifyBadgeRequestBadge_Copper

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.verify_badge(
            badge=VerifyBadgeRequestBadge_Copper(
                serial="serial",
            ),
        )
        """
        _response = self._raw_client.verify_badge(badge=badge, request_options=request_options)
        return _response.data

    def register_seal(
        self, *, seal: SealRegistrationSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        seal : SealRegistrationSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.seals import SealRegistrationSeal_Stamp

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.register_seal(
            seal=SealRegistrationSeal_Stamp(
                stamp_id="stamp_id",
            ),
        )
        """
        _response = self._raw_client.register_seal(seal=seal, request_options=request_options)
        return _response.data

    def verify_charm(
        self, *, token: VerifyCharmRequestToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token : VerifyCharmRequestToken

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.seals import VerifyCharmRequestToken_Wax

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.verify_charm(
            token=VerifyCharmRequestToken_Wax(
                colour="colour",
            ),
        )
        """
        _response = self._raw_client.verify_charm(token=token, request_options=request_options)
        return _response.data

    def inspect_charm(
        self, *, token: InspectCharmRequestToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token : InspectCharmRequestToken

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.seals import InspectCharmRequestToken_Wax

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.inspect_charm(
            token=InspectCharmRequestToken_Wax(
                colour="colour",
            ),
        )
        """
        _response = self._raw_client.inspect_charm(token=token, request_options=request_options)
        return _response.data


class AsyncSealsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSealsClient
        """
        return self._raw_client

    async def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifySealResponse:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySealResponse
            Verified

        Examples
        --------
        import asyncio

        from fern.seals import VerifySealRequestSeal_Stamp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.verify_seal(
                seal=VerifySealRequestSeal_Stamp(
                    stamp_id="stamp_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_seal(seal=seal, request_options=request_options)
        return _response.data

    async def verify_logbook(
        self, *, entry: VerifyLogbookRequestEntry, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyLogbookResponse:
        """
        Parameters
        ----------
        entry : VerifyLogbookRequestEntry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyLogbookResponse
            Verified

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EntryV2, PageV2, PageV2Edition

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.verify_logbook(
                entry=EntryV2(
                    page=PageV2(
                        edition=PageV2Edition.TWO0,
                        keeper="Morwenna",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_logbook(entry=entry, request_options=request_options)
        return _response.data

    async def stock_shelf(
        self,
        *,
        shelf: typing.Dict[str, StockShelfRequestShelfValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        shelf : typing.Dict[str, StockShelfRequestShelfValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.seals import StockShelfRequestShelfValue_Stamp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.stock_shelf(
                shelf={
                    "top": StockShelfRequestShelfValue_Stamp(
                        stamp_id="stamp_id",
                    )
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stock_shelf(shelf=shelf, request_options=request_options)
        return _response.data

    async def verify_badge(
        self, *, badge: VerifyBadgeRequestBadge, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        badge : VerifyBadgeRequestBadge

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.seals import VerifyBadgeRequestBadge_Copper

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.verify_badge(
                badge=VerifyBadgeRequestBadge_Copper(
                    serial="serial",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_badge(badge=badge, request_options=request_options)
        return _response.data

    async def register_seal(
        self, *, seal: SealRegistrationSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        seal : SealRegistrationSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.seals import SealRegistrationSeal_Stamp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.register_seal(
                seal=SealRegistrationSeal_Stamp(
                    stamp_id="stamp_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_seal(seal=seal, request_options=request_options)
        return _response.data

    async def verify_charm(
        self, *, token: VerifyCharmRequestToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token : VerifyCharmRequestToken

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.seals import VerifyCharmRequestToken_Wax

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.verify_charm(
                token=VerifyCharmRequestToken_Wax(
                    colour="colour",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_charm(token=token, request_options=request_options)
        return _response.data

    async def inspect_charm(
        self, *, token: InspectCharmRequestToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        token : InspectCharmRequestToken

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.seals import InspectCharmRequestToken_Wax

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.inspect_charm(
                token=InspectCharmRequestToken_Wax(
                    colour="colour",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_charm(token=token, request_options=request_options)
        return _response.data
