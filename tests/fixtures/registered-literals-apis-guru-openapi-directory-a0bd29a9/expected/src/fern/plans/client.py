

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delegate_identity import DelegateIdentity
from ..types.plan_resource import PlanResource
from ..types.plan_resource_headers import PlanResourceHeaders
from ..types.plan_resource_identity import PlanResourceIdentity
from ..types.plan_resource_properties import PlanResourceProperties
from ..types.rp_subscription_properties import RpSubscriptionProperties
from .raw_client import AsyncRawPlansClient, RawPlansClient


OMIT = typing.cast(typing.Any, ...)


class PlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlansClient
        """
        return self._raw_client

    def put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
        client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
            subscription_id,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
        client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id, value=value, request_options=request_options
        )
        return _response.data

    def put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
        client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
            subscription_id,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
        client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id, value=value, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id, resource_group, value=value, request_options=request_options
        )
        return _response.data

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_name,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
            subscription_id,
            resource_group,
            resource_name,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id, resource_group, value=value, request_options=request_options
        )
        return _response.data

    def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_name,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
            subscription_id,
            resource_group,
            resource_name,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
        client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data


class AsyncPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlansClient
        """
        return self._raw_client

    async def put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            await client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
            subscription_id,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
            await client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id, value=value, request_options=request_options
        )
        return _response.data

    async def put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
        self,
        subscription_id: str,
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
            await client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
            subscription_id,
            properties=properties,
            registration_date=registration_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
            await client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id, value=value, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
            subscription_id, resource_group, value=value, request_options=request_options
        )
        return _response.data

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_name,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
            subscription_id,
            resource_group,
            resource_name,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        *,
        value: typing.Optional[typing.Sequence[PlanResource]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        value : typing.Optional[typing.Sequence[PlanResource]]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
            subscription_id, resource_group, value=value, request_options=request_options
        )
        return _response.data

    async def put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
            subscription_id,
            resource_group,
            resource_name,
            headers=headers,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        identity : typing.Optional[PlanResourceIdentity]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
            subscription_id,
            resource_group,
            resource_name,
            identity=identity,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
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

        resource_name : str

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
            subscription_id,
            resource_group,
            resource_name,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
            subscription_id,
            resource_group,
            resource_name,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        resource_name : str

        expiration : typing.Optional[dt.datetime]

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
            subscription_id, resource_group, resource_name, expiration=expiration, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
        self,
        subscription_id: str,
        resource_group: str,
        resource_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

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
            await client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
            subscription_id, resource_group, resource_name, request_options=request_options
        )
        return _response.data
