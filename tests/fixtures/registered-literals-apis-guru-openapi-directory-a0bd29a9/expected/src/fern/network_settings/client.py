

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.network_settings_resource import NetworkSettingsResource
from ..types.network_settings_resource_properties import NetworkSettingsResourceProperties
from ..types.rp_subscription_properties import RpSubscriptionProperties
from .raw_client import AsyncRawNetworkSettingsClient, RawNetworkSettingsClient


OMIT = typing.cast(typing.Any, ...)


class NetworkSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetworkSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetworkSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetworkSettingsClient
        """
        return self._raw_client

    def put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        properties: typing.Optional[RpSubscriptionProperties] = OMIT,
        registration_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        properties : typing.Optional[RpSubscriptionProperties]

        registration_date : typing.Optional[dt.datetime]

        state : typing.Optional[str]

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
        client.network_settings.put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
            subscription_id="subscriptionId",
            resource_type="resourceType",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
            subscription_id,
            resource_type,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id="subscriptionId",
            resource_type="resourceType",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id, resource_type, value=value, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id, resource_group, resource_type, value=value, request_options=request_options
        )
        return _response.data

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
        client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_type="resourceType",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data


class AsyncNetworkSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetworkSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetworkSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetworkSettingsClient
        """
        return self._raw_client

    async def put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        properties: typing.Optional[RpSubscriptionProperties] = OMIT,
        registration_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        properties : typing.Optional[RpSubscriptionProperties]

        registration_date : typing.Optional[dt.datetime]

        state : typing.Optional[str]

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
            await client.network_settings.put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
                subscription_id="subscriptionId",
                resource_type="resourceType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
            subscription_id,
            resource_type,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
                subscription_id="subscriptionId",
                resource_type="resourceType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id, resource_type, value=value, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        *,
        value: typing.Optional[typing.Sequence[NetworkSettingsResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        value : typing.Optional[typing.Sequence[NetworkSettingsResource]]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
            subscription_id, resource_group, resource_type, value=value, request_options=request_options
        )
        return _response.data

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
            subscription_id, resource_group, resource_type, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_type: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[NetworkSettingsResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_type : str

        resource_name : str

        id : typing.Optional[str]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[NetworkSettingsResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            await client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_type="resourceType",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_type,
            resource_name,
            id=id,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data
