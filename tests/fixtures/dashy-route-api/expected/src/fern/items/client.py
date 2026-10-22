

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item import Item
from ..types.item_fields_target import ItemFieldsTarget
from ..types.item_result import ItemResult
from ..types.write_result import WriteResult
from .raw_client import AsyncRawItemsClient, RawItemsClient
from .types.update_item_response import UpdateItemResponse


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

    def list_items(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Item]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Item]
            Items in the section

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.items.list_items(
            filename="conf.yml",
            sid="0",
        )
        """
        _response = self._raw_client.list_items(filename, sid, request_options=request_options)
        return _response.data

    def add_item(
        self,
        filename: str,
        sid: str,
        *,
        title: str,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemResult:
        """
        Appends a new item to the section. A `title` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        title : str
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemResult
            Item added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.items.add_item(
            filename="conf.yml",
            sid="0",
            title="Grafana",
            icon="hl-grafana",
            url="https://grafana.local",
        )
        """
        _response = self._raw_client.add_item(
            filename,
            sid,
            title=title,
            description=description,
            icon=icon,
            url=url,
            target=target,
            provider=provider,
            id=id,
            tags=tags,
            hotkey=hotkey,
            rel=rel,
            color=color,
            background_color=background_color,
            display_data=display_data,
            sub_items=sub_items,
            status_check=status_check,
            status_check_url=status_check_url,
            status_check_headers=status_check_headers,
            status_check_allow_insecure=status_check_allow_insecure,
            status_check_accept_codes=status_check_accept_codes,
            status_check_max_redirects=status_check_max_redirects,
            ping_check_enabled=ping_check_enabled,
            ping_check_host=ping_check_host,
            ping_check_interval=ping_check_interval,
            ping_check_count=ping_check_count,
            ping_check_timeout=ping_check_timeout,
            request_options=request_options,
        )
        return _response.data

    def get_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Item:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Item
            Item

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.items.get_item(
            filename="conf.yml",
            sid="0",
            iid="0",
        )
        """
        _response = self._raw_client.get_item(filename, sid, iid, request_options=request_options)
        return _response.data

    def delete_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WriteResult:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.items.delete_item(
            filename="conf.yml",
            sid="0",
            iid="0",
        )
        """
        _response = self._raw_client.delete_item(filename, sid, iid, request_options=request_options)
        return _response.data

    def update_item(
        self,
        filename: str,
        sid: str,
        iid: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemResponse:
        """
        Shallow-merges the supplied fields onto the item.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        title : typing.Optional[str]
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemResponse
            Updated item

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.items.update_item(
            filename="conf.yml",
            sid="0",
            iid="0",
            url="https://grafana.example.com",
        )
        """
        _response = self._raw_client.update_item(
            filename,
            sid,
            iid,
            title=title,
            description=description,
            icon=icon,
            url=url,
            target=target,
            provider=provider,
            id=id,
            tags=tags,
            hotkey=hotkey,
            rel=rel,
            color=color,
            background_color=background_color,
            display_data=display_data,
            sub_items=sub_items,
            status_check=status_check,
            status_check_url=status_check_url,
            status_check_headers=status_check_headers,
            status_check_allow_insecure=status_check_allow_insecure,
            status_check_accept_codes=status_check_accept_codes,
            status_check_max_redirects=status_check_max_redirects,
            ping_check_enabled=ping_check_enabled,
            ping_check_host=ping_check_host,
            ping_check_interval=ping_check_interval,
            ping_check_count=ping_check_count,
            ping_check_timeout=ping_check_timeout,
            request_options=request_options,
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

    async def list_items(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Item]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Item]
            Items in the section

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.items.list_items(
                filename="conf.yml",
                sid="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_items(filename, sid, request_options=request_options)
        return _response.data

    async def add_item(
        self,
        filename: str,
        sid: str,
        *,
        title: str,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ItemResult:
        """
        Appends a new item to the section. A `title` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        title : str
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ItemResult
            Item added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.items.add_item(
                filename="conf.yml",
                sid="0",
                title="Grafana",
                icon="hl-grafana",
                url="https://grafana.local",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_item(
            filename,
            sid,
            title=title,
            description=description,
            icon=icon,
            url=url,
            target=target,
            provider=provider,
            id=id,
            tags=tags,
            hotkey=hotkey,
            rel=rel,
            color=color,
            background_color=background_color,
            display_data=display_data,
            sub_items=sub_items,
            status_check=status_check,
            status_check_url=status_check_url,
            status_check_headers=status_check_headers,
            status_check_allow_insecure=status_check_allow_insecure,
            status_check_accept_codes=status_check_accept_codes,
            status_check_max_redirects=status_check_max_redirects,
            ping_check_enabled=ping_check_enabled,
            ping_check_host=ping_check_host,
            ping_check_interval=ping_check_interval,
            ping_check_count=ping_check_count,
            ping_check_timeout=ping_check_timeout,
            request_options=request_options,
        )
        return _response.data

    async def get_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Item:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Item
            Item

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.items.get_item(
                filename="conf.yml",
                sid="0",
                iid="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item(filename, sid, iid, request_options=request_options)
        return _response.data

    async def delete_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WriteResult:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.items.delete_item(
                filename="conf.yml",
                sid="0",
                iid="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_item(filename, sid, iid, request_options=request_options)
        return _response.data

    async def update_item(
        self,
        filename: str,
        sid: str,
        iid: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemResponse:
        """
        Shallow-merges the supplied fields onto the item.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        title : typing.Optional[str]
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemResponse
            Updated item

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.items.update_item(
                filename="conf.yml",
                sid="0",
                iid="0",
                url="https://grafana.example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item(
            filename,
            sid,
            iid,
            title=title,
            description=description,
            icon=icon,
            url=url,
            target=target,
            provider=provider,
            id=id,
            tags=tags,
            hotkey=hotkey,
            rel=rel,
            color=color,
            background_color=background_color,
            display_data=display_data,
            sub_items=sub_items,
            status_check=status_check,
            status_check_url=status_check_url,
            status_check_headers=status_check_headers,
            status_check_allow_insecure=status_check_allow_insecure,
            status_check_accept_codes=status_check_accept_codes,
            status_check_max_redirects=status_check_max_redirects,
            ping_check_enabled=ping_check_enabled,
            ping_check_host=ping_check_host,
            ping_check_interval=ping_check_interval,
            ping_check_count=ping_check_count,
            ping_check_timeout=ping_check_timeout,
            request_options=request_options,
        )
        return _response.data
