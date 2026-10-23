

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawItemsClient, RawItemsClient
from .types.items_create_request_data import ItemsCreateRequestData
from .types.items_create_request_info import ItemsCreateRequestInfo
from .types.items_create_request_meta_item import ItemsCreateRequestMetaItem


OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawItemsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        info: ItemsCreateRequestInfo,
        created: typing.Optional[dt.datetime] = OMIT,
        meta: typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]] = OMIT,
        data: typing.Optional[ItemsCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        info : ItemsCreateRequestInfo

        created : typing.Optional[dt.datetime]

        meta : typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]]

        data : typing.Optional[ItemsCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern.items import (
            ItemsCreateRequestData,
            ItemsCreateRequestDataProps,
            ItemsCreateRequestInfo,
            ItemsCreateRequestMetaItemUnitId,
            ItemsCreateRequestMetaItemUnitIdKind,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.items.create(
            info=ItemsCreateRequestInfo(
                label="first",
            ),
            created=datetime.datetime.fromisoformat(
                "2024-01-02 03:04:05+00:00",
            ),
            meta=[
                ItemsCreateRequestMetaItemUnitId(
                    kind=ItemsCreateRequestMetaItemUnitIdKind.UNIT,
                    ref='{"a":"b"}',
                )
            ],
            data=ItemsCreateRequestData(
                props=ItemsCreateRequestDataProps(
                    path="/a",
                ),
                ext={"key": "value"},
            ),
        )
        """
        _response = self._raw_client.create(
            info=info, created=created, meta=meta, data=data, request_options=request_options
        )
        return _response.data


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawItemsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        info: ItemsCreateRequestInfo,
        created: typing.Optional[dt.datetime] = OMIT,
        meta: typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]] = OMIT,
        data: typing.Optional[ItemsCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        info : ItemsCreateRequestInfo

        created : typing.Optional[dt.datetime]

        meta : typing.Optional[typing.Sequence[ItemsCreateRequestMetaItem]]

        data : typing.Optional[ItemsCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern.items import (
            ItemsCreateRequestData,
            ItemsCreateRequestDataProps,
            ItemsCreateRequestInfo,
            ItemsCreateRequestMetaItemUnitId,
            ItemsCreateRequestMetaItemUnitIdKind,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.items.create(
                info=ItemsCreateRequestInfo(
                    label="first",
                ),
                created=datetime.datetime.fromisoformat(
                    "2024-01-02 03:04:05+00:00",
                ),
                meta=[
                    ItemsCreateRequestMetaItemUnitId(
                        kind=ItemsCreateRequestMetaItemUnitIdKind.UNIT,
                        ref='{"a":"b"}',
                    )
                ],
                data=ItemsCreateRequestData(
                    props=ItemsCreateRequestDataProps(
                        path="/a",
                    ),
                    ext={"key": "value"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            info=info, created=created, meta=meta, data=data, request_options=request_options
        )
        return _response.data
