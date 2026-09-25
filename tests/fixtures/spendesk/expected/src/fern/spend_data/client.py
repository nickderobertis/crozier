

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payable import Payable
from ..types.settlements_response import SettlementsResponse
from ..types.snapshot_response import SnapshotResponse
from .raw_client import AsyncRawSpendDataClient, RawSpendDataClient


OMIT = typing.cast(typing.Any, ...)


class SpendDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpendDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpendDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpendDataClient
        """
        return self._raw_client

    def listsettlements(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SettlementsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettlementsResponse
            Settlements retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.listsettlements()
        """
        _response = self._raw_client.listsettlements(page=page, per_page=per_page, request_options=request_options)
        return _response.data

    def updatesettlementstate(
        self, *, ids: typing.Sequence[str], state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        state : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.updatesettlementstate(
            ids=["ids"],
            state="state",
        )
        """
        _response = self._raw_client.updatesettlementstate(ids=ids, state=state, request_options=request_options)
        return _response.data

    def listbankfees(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.listbankfees()
        """
        _response = self._raw_client.listbankfees(request_options=request_options)
        return _response.data

    def getpayablessnapshot(
        self, *, snapshot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SnapshotResponse:
        """
        Parameters
        ----------
        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnapshotResponse
            Snapshot retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.getpayablessnapshot(
            snapshot_id="snapshot_id",
        )
        """
        _response = self._raw_client.getpayablessnapshot(snapshot_id=snapshot_id, request_options=request_options)
        return _response.data

    def createpayablessnapshot(
        self,
        *,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnapshotResponse:
        """
        Parameters
        ----------
        filters : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnapshotResponse
            Snapshot created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.createpayablessnapshot()
        """
        _response = self._raw_client.createpayablessnapshot(filters=filters, request_options=request_options)
        return _response.data

    def getpayable(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payable:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payable
            Payable retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.getpayable(
            id="id",
        )
        """
        _response = self._raw_client.getpayable(id, request_options=request_options)
        return _response.data

    def getpayableattachments(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.getpayableattachments(
            id="id",
        )
        """
        _response = self._raw_client.getpayableattachments(id, request_options=request_options)
        return _response.data

    def updatebookkeepingstatus(
        self, *, ids: typing.Sequence[str], status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        status : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.updatebookkeepingstatus(
            ids=["ids"],
            status="status",
        )
        """
        _response = self._raw_client.updatebookkeepingstatus(ids=ids, status=status, request_options=request_options)
        return _response.data

    def listwalletloads(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.listwalletloads()
        """
        _response = self._raw_client.listwalletloads(request_options=request_options)
        return _response.data

    def getwalletsummary(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.spend_data.getwalletsummary()
        """
        _response = self._raw_client.getwalletsummary(request_options=request_options)
        return _response.data


class AsyncSpendDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpendDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpendDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpendDataClient
        """
        return self._raw_client

    async def listsettlements(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SettlementsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettlementsResponse
            Settlements retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.listsettlements()


        asyncio.run(main())
        """
        _response = await self._raw_client.listsettlements(
            page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def updatesettlementstate(
        self, *, ids: typing.Sequence[str], state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        state : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.updatesettlementstate(
                ids=["ids"],
                state="state",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesettlementstate(ids=ids, state=state, request_options=request_options)
        return _response.data

    async def listbankfees(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.listbankfees()


        asyncio.run(main())
        """
        _response = await self._raw_client.listbankfees(request_options=request_options)
        return _response.data

    async def getpayablessnapshot(
        self, *, snapshot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SnapshotResponse:
        """
        Parameters
        ----------
        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnapshotResponse
            Snapshot retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.getpayablessnapshot(
                snapshot_id="snapshot_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpayablessnapshot(snapshot_id=snapshot_id, request_options=request_options)
        return _response.data

    async def createpayablessnapshot(
        self,
        *,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnapshotResponse:
        """
        Parameters
        ----------
        filters : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnapshotResponse
            Snapshot created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.createpayablessnapshot()


        asyncio.run(main())
        """
        _response = await self._raw_client.createpayablessnapshot(filters=filters, request_options=request_options)
        return _response.data

    async def getpayable(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payable:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payable
            Payable retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.getpayable(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpayable(id, request_options=request_options)
        return _response.data

    async def getpayableattachments(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.getpayableattachments(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpayableattachments(id, request_options=request_options)
        return _response.data

    async def updatebookkeepingstatus(
        self, *, ids: typing.Sequence[str], status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        status : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.updatebookkeepingstatus(
                ids=["ids"],
                status="status",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatebookkeepingstatus(
            ids=ids, status=status, request_options=request_options
        )
        return _response.data

    async def listwalletloads(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.listwalletloads()


        asyncio.run(main())
        """
        _response = await self._raw_client.listwalletloads(request_options=request_options)
        return _response.data

    async def getwalletsummary(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.spend_data.getwalletsummary()


        asyncio.run(main())
        """
        _response = await self._raw_client.getwalletsummary(request_options=request_options)
        return _response.data
