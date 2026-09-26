

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawNavigationViewsClient, RawNavigationViewsClient
from .types.add_navigation_view_response import AddNavigationViewResponse
from .types.edit_navigation_view_request_body import EditNavigationViewRequestBody
from .types.edit_navigation_view_response import EditNavigationViewResponse
from .types.get_navigation_views_response import GetNavigationViewsResponse


OMIT = typing.cast(typing.Any, ...)


class NavigationViewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNavigationViewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNavigationViewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNavigationViewsClient
        """
        return self._raw_client

    def get_navigation_views(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNavigationViewsResponse:
        """
        Fetch all configured custom navigation views for the current user.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNavigationViewsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.navigation_views.get_navigation_views()
        """
        _response = self._raw_client.get_navigation_views(request_options=request_options)
        return _response.data

    def add_navigation_view(
        self,
        *,
        fragment: str,
        is_pinned: bool,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddNavigationViewResponse:
        """
        Adds a new custom left sidebar navigation view configuration
        for the current user.

        This can be used both to configure built-in navigation views,
        or to add new navigation views.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            A unique identifier for the view, used to determine navigation
            behavior when clicked.

            Clients should use this value to navigate to the corresponding URL hash.

        is_pinned : bool
            Determines whether the view appears directly in the sidebar or
            is hidden in the "More Views" menu.

            - `true` - Pinned and visible in the sidebar.
            - `false` - Hidden and accessible via the "More Views" menu.

        name : typing.Optional[str]
            The user-facing name for custom navigation views. Omit this
            field for built-in views.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddNavigationViewResponse
            Request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.navigation_views.add_navigation_view(
            fragment="narrow/is/alerted",
            is_pinned=True,
        )
        """
        _response = self._raw_client.add_navigation_view(
            fragment=fragment, is_pinned=is_pinned, name=name, request_options=request_options
        )
        return _response.data

    def remove_navigation_view(
        self, fragment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove a navigation view.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be removed.

            This also serves as the identifier for the navigation view.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.navigation_views.remove_navigation_view(
            fragment="narrow/is/alerted",
        )
        """
        _response = self._raw_client.remove_navigation_view(fragment, request_options=request_options)
        return _response.data

    def edit_navigation_view(
        self,
        fragment: str,
        *,
        request: EditNavigationViewRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditNavigationViewResponse:
        """
        Update the details of an existing configured navigation view,
        such as its name or whether it's pinned.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be updated.

            This also serves as the identifier for the navigation view.

        request : EditNavigationViewRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditNavigationViewResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.navigation_views.edit_navigation_view(
            fragment="fragment",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.edit_navigation_view(fragment, request=request, request_options=request_options)
        return _response.data


class AsyncNavigationViewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNavigationViewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNavigationViewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNavigationViewsClient
        """
        return self._raw_client

    async def get_navigation_views(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNavigationViewsResponse:
        """
        Fetch all configured custom navigation views for the current user.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNavigationViewsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.navigation_views.get_navigation_views()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_navigation_views(request_options=request_options)
        return _response.data

    async def add_navigation_view(
        self,
        *,
        fragment: str,
        is_pinned: bool,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddNavigationViewResponse:
        """
        Adds a new custom left sidebar navigation view configuration
        for the current user.

        This can be used both to configure built-in navigation views,
        or to add new navigation views.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            A unique identifier for the view, used to determine navigation
            behavior when clicked.

            Clients should use this value to navigate to the corresponding URL hash.

        is_pinned : bool
            Determines whether the view appears directly in the sidebar or
            is hidden in the "More Views" menu.

            - `true` - Pinned and visible in the sidebar.
            - `false` - Hidden and accessible via the "More Views" menu.

        name : typing.Optional[str]
            The user-facing name for custom navigation views. Omit this
            field for built-in views.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddNavigationViewResponse
            Request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.navigation_views.add_navigation_view(
                fragment="narrow/is/alerted",
                is_pinned=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_navigation_view(
            fragment=fragment, is_pinned=is_pinned, name=name, request_options=request_options
        )
        return _response.data

    async def remove_navigation_view(
        self, fragment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove a navigation view.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be removed.

            This also serves as the identifier for the navigation view.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.navigation_views.remove_navigation_view(
                fragment="narrow/is/alerted",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_navigation_view(fragment, request_options=request_options)
        return _response.data

    async def edit_navigation_view(
        self,
        fragment: str,
        *,
        request: EditNavigationViewRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditNavigationViewResponse:
        """
        Update the details of an existing configured navigation view,
        such as its name or whether it's pinned.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be updated.

            This also serves as the identifier for the navigation view.

        request : EditNavigationViewRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditNavigationViewResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.navigation_views.edit_navigation_view(
                fragment="fragment",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_navigation_view(
            fragment, request=request, request_options=request_options
        )
        return _response.data
