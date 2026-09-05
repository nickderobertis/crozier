

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1alpha1resource_metadata import V1Alpha1ResourceMetadata
from ..types.v1alpha1trigger_rule_resource_create_response import V1Alpha1TriggerRuleResourceCreateResponse
from ..types.v1alpha1trigger_rule_resource_read_response import V1Alpha1TriggerRuleResourceReadResponse
from ..types.v1alpha1trigger_rule_resource_spec import V1Alpha1TriggerRuleResourceSpec
from ..types.v1alpha1trigger_rule_resource_update_response import V1Alpha1TriggerRuleResourceUpdateResponse
from .raw_client import AsyncRawTriggersClient, RawTriggersClient


OMIT = typing.cast(typing.Any, ...)


class TriggersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTriggersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTriggersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTriggersClient
        """
        return self._raw_client

    def list_triggers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1TriggerRuleResourceReadResponse]
            List of Trigger Rules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.triggers.list_triggers()
        """
        _response = self._raw_client.list_triggers(request_options=request_options)
        return _response.data

    def create_trigger(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1TriggerRuleResourceCreateResponse:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceCreateResponse
            The created Trigger Rule

        Examples
        --------
        from fern import (
            FernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1TriggerRuleAction,
            V1Alpha1TriggerRuleResourceSpec,
        )

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.triggers.create_trigger(
            metadata=V1Alpha1ResourceMetadata(
                name="name",
            ),
            spec=V1Alpha1TriggerRuleResourceSpec(
                rule={"key": "value"},
                action=V1Alpha1TriggerRuleAction(
                    target="target",
                ),
            ),
        )
        """
        _response = self._raw_client.create_trigger(
            metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    def get_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1TriggerRuleResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceReadResponse
            The Trigger Rule

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.triggers.get_trigger(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_trigger(identifier, request_options=request_options)
        return _response.data

    def update_trigger(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1TriggerRuleResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceUpdateResponse
            The updated Trigger Rule

        Examples
        --------
        from fern import (
            FernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1TriggerRuleAction,
            V1Alpha1TriggerRuleResourceSpec,
        )

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.triggers.update_trigger(
            identifier="identifier",
            metadata=V1Alpha1ResourceMetadata(
                name="name",
            ),
            spec=V1Alpha1TriggerRuleResourceSpec(
                rule={"key": "value"},
                action=V1Alpha1TriggerRuleAction(
                    target="target",
                ),
            ),
        )
        """
        _response = self._raw_client.update_trigger(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    def delete_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1TriggerRuleResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceReadResponse
            The deleted Trigger Rule

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.triggers.delete_trigger(
            identifier="identifier",
        )
        """
        _response = self._raw_client.delete_trigger(identifier, request_options=request_options)
        return _response.data


class AsyncTriggersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTriggersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTriggersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTriggersClient
        """
        return self._raw_client

    async def list_triggers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1TriggerRuleResourceReadResponse]
            List of Trigger Rules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.triggers.list_triggers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_triggers(request_options=request_options)
        return _response.data

    async def create_trigger(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1TriggerRuleResourceCreateResponse:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceCreateResponse
            The created Trigger Rule

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1TriggerRuleAction,
            V1Alpha1TriggerRuleResourceSpec,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.triggers.create_trigger(
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1TriggerRuleResourceSpec(
                    rule={"key": "value"},
                    action=V1Alpha1TriggerRuleAction(
                        target="target",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_trigger(
            metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    async def get_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1TriggerRuleResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceReadResponse
            The Trigger Rule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.triggers.get_trigger(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trigger(identifier, request_options=request_options)
        return _response.data

    async def update_trigger(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1TriggerRuleResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceUpdateResponse
            The updated Trigger Rule

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1TriggerRuleAction,
            V1Alpha1TriggerRuleResourceSpec,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.triggers.update_trigger(
                identifier="identifier",
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1TriggerRuleResourceSpec(
                    rule={"key": "value"},
                    action=V1Alpha1TriggerRuleAction(
                        target="target",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_trigger(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    async def delete_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1TriggerRuleResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1TriggerRuleResourceReadResponse
            The deleted Trigger Rule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.triggers.delete_trigger(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_trigger(identifier, request_options=request_options)
        return _response.data
