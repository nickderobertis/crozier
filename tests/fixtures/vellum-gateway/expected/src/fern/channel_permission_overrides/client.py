

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChannelPermissionOverridesClient, RawChannelPermissionOverridesClient
from .types.channel_permission_override_delete_request_contact_type import (
    ChannelPermissionOverrideDeleteRequestContactType,
)
from .types.channel_permission_override_delete_request_selector import ChannelPermissionOverrideDeleteRequestSelector
from .types.channel_permission_override_delete_response import ChannelPermissionOverrideDeleteResponse
from .types.channel_permission_override_set_request_contact_type import ChannelPermissionOverrideSetRequestContactType
from .types.channel_permission_override_set_request_selector import ChannelPermissionOverrideSetRequestSelector
from .types.channel_permission_override_set_request_threshold import ChannelPermissionOverrideSetRequestThreshold
from .types.channel_permission_override_set_response import ChannelPermissionOverrideSetResponse
from .types.channel_permission_overrides_list_response import ChannelPermissionOverridesListResponse
from .types.channel_permission_resolve_request_channel_type import ChannelPermissionResolveRequestChannelType
from .types.channel_permission_resolve_request_contact_type import ChannelPermissionResolveRequestContactType
from .types.channel_permission_resolve_response import ChannelPermissionResolveResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelPermissionOverridesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelPermissionOverridesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelPermissionOverridesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelPermissionOverridesClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelPermissionOverridesListResponse:
        """
        Returns every persisted cell (cascade selector × contact-type → RiskThreshold). Unset cells fall through the cascade; the list contains only explicit overrides.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverridesListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.channel_permission_overrides.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def channel_permission_override_set(
        self,
        *,
        selector: ChannelPermissionOverrideSetRequestSelector,
        contact_type: ChannelPermissionOverrideSetRequestContactType,
        threshold: ChannelPermissionOverrideSetRequestThreshold,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionOverrideSetResponse:
        """
        Upserts one cell, identified by the selector × contact-type in the body. The adapter must be a known channel id.

        Parameters
        ----------
        selector : ChannelPermissionOverrideSetRequestSelector

        contact_type : ChannelPermissionOverrideSetRequestContactType

        threshold : ChannelPermissionOverrideSetRequestThreshold

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverrideSetResponse
            Successful response

        Examples
        --------
        from fern.channel_permission_overrides import (
            ChannelPermissionOverrideSetRequestContactType,
            ChannelPermissionOverrideSetRequestSelector_Workspace,
            ChannelPermissionOverrideSetRequestThreshold,
        )

        from fern import FernApi

        client = FernApi()
        client.channel_permission_overrides.channel_permission_override_set(
            selector=ChannelPermissionOverrideSetRequestSelector_Workspace(),
            contact_type=ChannelPermissionOverrideSetRequestContactType.GUARDIAN,
            threshold=ChannelPermissionOverrideSetRequestThreshold.NONE,
        )
        """
        _response = self._raw_client.channel_permission_override_set(
            selector=selector,
            contact_type=contact_type,
            threshold=threshold,
            note=note,
            request_options=request_options,
        )
        return _response.data

    def channel_permission_resolve(
        self,
        *,
        adapter: str,
        contact_type: ChannelPermissionResolveRequestContactType,
        channel_type: typing.Optional[ChannelPermissionResolveRequestChannelType] = OMIT,
        channel_external_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionResolveResponse:
        """
        Read-only cascade resolution for one coordinate: walks channel → channel_type → adapter → workspace for the given selector keys and contact-type, returning the winning cell's threshold and scope, or null when no cell matches (the caller then falls through to the global thresholds). Same resolver the runtime evaluator uses over IPC.

        Parameters
        ----------
        adapter : str

        contact_type : ChannelPermissionResolveRequestContactType

        channel_type : typing.Optional[ChannelPermissionResolveRequestChannelType]

        channel_external_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionResolveResponse
            Successful response

        Examples
        --------
        from fern.channel_permission_overrides import (
            ChannelPermissionResolveRequestContactType,
        )

        from fern import FernApi

        client = FernApi()
        client.channel_permission_overrides.channel_permission_resolve(
            adapter="adapter",
            contact_type=ChannelPermissionResolveRequestContactType.GUARDIAN,
        )
        """
        _response = self._raw_client.channel_permission_resolve(
            adapter=adapter,
            contact_type=contact_type,
            channel_type=channel_type,
            channel_external_id=channel_external_id,
            request_options=request_options,
        )
        return _response.data

    def channel_permission_override_delete(
        self,
        *,
        selector: ChannelPermissionOverrideDeleteRequestSelector,
        contact_type: ChannelPermissionOverrideDeleteRequestContactType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionOverrideDeleteResponse:
        """
        Removes one cell by its composite key (selector × contact-type), letting the next cascade tier up win. Returns whether a cell was removed.

        Parameters
        ----------
        selector : ChannelPermissionOverrideDeleteRequestSelector

        contact_type : ChannelPermissionOverrideDeleteRequestContactType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverrideDeleteResponse
            Successful response

        Examples
        --------
        from fern.channel_permission_overrides import (
            ChannelPermissionOverrideDeleteRequestContactType,
            ChannelPermissionOverrideDeleteRequestSelector_Workspace,
        )

        from fern import FernApi

        client = FernApi()
        client.channel_permission_overrides.channel_permission_override_delete(
            selector=ChannelPermissionOverrideDeleteRequestSelector_Workspace(),
            contact_type=ChannelPermissionOverrideDeleteRequestContactType.GUARDIAN,
        )
        """
        _response = self._raw_client.channel_permission_override_delete(
            selector=selector, contact_type=contact_type, request_options=request_options
        )
        return _response.data


class AsyncChannelPermissionOverridesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelPermissionOverridesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelPermissionOverridesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelPermissionOverridesClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChannelPermissionOverridesListResponse:
        """
        Returns every persisted cell (cascade selector × contact-type → RiskThreshold). Unset cells fall through the cascade; the list contains only explicit overrides.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverridesListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_permission_overrides.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def channel_permission_override_set(
        self,
        *,
        selector: ChannelPermissionOverrideSetRequestSelector,
        contact_type: ChannelPermissionOverrideSetRequestContactType,
        threshold: ChannelPermissionOverrideSetRequestThreshold,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionOverrideSetResponse:
        """
        Upserts one cell, identified by the selector × contact-type in the body. The adapter must be a known channel id.

        Parameters
        ----------
        selector : ChannelPermissionOverrideSetRequestSelector

        contact_type : ChannelPermissionOverrideSetRequestContactType

        threshold : ChannelPermissionOverrideSetRequestThreshold

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverrideSetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.channel_permission_overrides import (
            ChannelPermissionOverrideSetRequestContactType,
            ChannelPermissionOverrideSetRequestSelector_Workspace,
            ChannelPermissionOverrideSetRequestThreshold,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_permission_overrides.channel_permission_override_set(
                selector=ChannelPermissionOverrideSetRequestSelector_Workspace(),
                contact_type=ChannelPermissionOverrideSetRequestContactType.GUARDIAN,
                threshold=ChannelPermissionOverrideSetRequestThreshold.NONE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.channel_permission_override_set(
            selector=selector,
            contact_type=contact_type,
            threshold=threshold,
            note=note,
            request_options=request_options,
        )
        return _response.data

    async def channel_permission_resolve(
        self,
        *,
        adapter: str,
        contact_type: ChannelPermissionResolveRequestContactType,
        channel_type: typing.Optional[ChannelPermissionResolveRequestChannelType] = OMIT,
        channel_external_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionResolveResponse:
        """
        Read-only cascade resolution for one coordinate: walks channel → channel_type → adapter → workspace for the given selector keys and contact-type, returning the winning cell's threshold and scope, or null when no cell matches (the caller then falls through to the global thresholds). Same resolver the runtime evaluator uses over IPC.

        Parameters
        ----------
        adapter : str

        contact_type : ChannelPermissionResolveRequestContactType

        channel_type : typing.Optional[ChannelPermissionResolveRequestChannelType]

        channel_external_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionResolveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.channel_permission_overrides import (
            ChannelPermissionResolveRequestContactType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_permission_overrides.channel_permission_resolve(
                adapter="adapter",
                contact_type=ChannelPermissionResolveRequestContactType.GUARDIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.channel_permission_resolve(
            adapter=adapter,
            contact_type=contact_type,
            channel_type=channel_type,
            channel_external_id=channel_external_id,
            request_options=request_options,
        )
        return _response.data

    async def channel_permission_override_delete(
        self,
        *,
        selector: ChannelPermissionOverrideDeleteRequestSelector,
        contact_type: ChannelPermissionOverrideDeleteRequestContactType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelPermissionOverrideDeleteResponse:
        """
        Removes one cell by its composite key (selector × contact-type), letting the next cascade tier up win. Returns whether a cell was removed.

        Parameters
        ----------
        selector : ChannelPermissionOverrideDeleteRequestSelector

        contact_type : ChannelPermissionOverrideDeleteRequestContactType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelPermissionOverrideDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.channel_permission_overrides import (
            ChannelPermissionOverrideDeleteRequestContactType,
            ChannelPermissionOverrideDeleteRequestSelector_Workspace,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.channel_permission_overrides.channel_permission_override_delete(
                selector=ChannelPermissionOverrideDeleteRequestSelector_Workspace(),
                contact_type=ChannelPermissionOverrideDeleteRequestContactType.GUARDIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.channel_permission_override_delete(
            selector=selector, contact_type=contact_type, request_options=request_options
        )
        return _response.data
