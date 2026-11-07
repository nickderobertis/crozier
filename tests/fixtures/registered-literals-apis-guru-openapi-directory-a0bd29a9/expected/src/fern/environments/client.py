

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.billable_owner_body import BillableOwnerBody
from ..types.cloud_environment_result import CloudEnvironmentResult
from ..types.connection_info_body import ConnectionInfoBody
from ..types.environment_registration_callback_payload_body import EnvironmentRegistrationCallbackPayloadBody
from ..types.experimental_features_body import ExperimentalFeaturesBody
from ..types.failover_details import FailoverDetails
from ..types.identity_body import IdentityBody
from ..types.netmon_correlation_data_body import NetmonCorrelationDataBody
from ..types.personalization_info_body import PersonalizationInfoBody
from ..types.privacy_enum import PrivacyEnum
from ..types.runtime_constraints_body import RuntimeConstraintsBody
from ..types.secret_data_body import SecretDataBody
from ..types.seed_info_body import SeedInfoBody
from ..types.tunnel_type import TunnelType
from ..types.unfiltered_cloud_environment_result import UnfilteredCloudEnvironmentResult
from ..types.vm_logs_upload_info import VmLogsUploadInfo
from .raw_client import AsyncRawEnvironmentsClient, RawEnvironmentsClient


OMIT = typing.cast(typing.Any, ...)


class EnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvironmentsClient
        """
        return self._raw_client

    def get_api_v1environments(
        self,
        *,
        name: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        plan_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CloudEnvironmentResult]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1environments()
        """
        _response = self._raw_client.get_api_v1environments(
            name=name, plan_id=plan_id, deleted=deleted, request_options=request_options
        )
        return _response.data

    def post_api_v1environments(
        self,
        *,
        friendly_name: str,
        type: str,
        access: typing.Optional[bool] = None,
        analytics_tracking_id: typing.Optional[str] = OMIT,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        billable_owner: typing.Optional[BillableOwnerBody] = OMIT,
        connection: typing.Optional[ConnectionInfoBody] = OMIT,
        container_image: typing.Optional[str] = OMIT,
        create_as_prebuild: typing.Optional[bool] = OMIT,
        dev_container_json: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_api_url: typing.Optional[str] = OMIT,
        git_hub_app_url: typing.Optional[str] = OMIT,
        git_hub_pfs_auth_endpoint: typing.Optional[str] = OMIT,
        github_environment_endpoint: typing.Optional[str] = OMIT,
        has_devcontainer_json: typing.Optional[bool] = OMIT,
        identity: typing.Optional[IdentityBody] = OMIT,
        label: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        netmon_correlation_data: typing.Optional[NetmonCorrelationDataBody] = OMIT,
        personalization: typing.Optional[PersonalizationInfoBody] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        runtime_constraints: typing.Optional[RuntimeConstraintsBody] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        test_account: typing.Optional[bool] = OMIT,
        user_tier: typing.Optional[str] = OMIT,
        working_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        friendly_name : str

        type : str

        access : typing.Optional[bool]

        analytics_tracking_id : typing.Optional[str]

        auto_shutdown_delay_minutes : typing.Optional[int]

        billable_owner : typing.Optional[BillableOwnerBody]

        connection : typing.Optional[ConnectionInfoBody]

        container_image : typing.Optional[str]

        create_as_prebuild : typing.Optional[bool]

        dev_container_json : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_api_url : typing.Optional[str]

        git_hub_app_url : typing.Optional[str]

        git_hub_pfs_auth_endpoint : typing.Optional[str]

        github_environment_endpoint : typing.Optional[str]

        has_devcontainer_json : typing.Optional[bool]

        identity : typing.Optional[IdentityBody]

        label : typing.Optional[str]

        location : typing.Optional[str]

        netmon_correlation_data : typing.Optional[NetmonCorrelationDataBody]

        personalization : typing.Optional[PersonalizationInfoBody]

        plan_id : typing.Optional[str]

        platform : typing.Optional[str]

        runtime_constraints : typing.Optional[RuntimeConstraintsBody]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        seed : typing.Optional[SeedInfoBody]

        sku_name : typing.Optional[str]

        test_account : typing.Optional[bool]

        user_tier : typing.Optional[str]

        working_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments(
            friendly_name="friendlyName",
            type="type",
        )
        """
        _response = self._raw_client.post_api_v1environments(
            friendly_name=friendly_name,
            type=type,
            access=access,
            analytics_tracking_id=analytics_tracking_id,
            auto_shutdown_delay_minutes=auto_shutdown_delay_minutes,
            billable_owner=billable_owner,
            connection=connection,
            container_image=container_image,
            create_as_prebuild=create_as_prebuild,
            dev_container_json=dev_container_json,
            dev_container_path=dev_container_path,
            experimental_features=experimental_features,
            features=features,
            git_hub_api_url=git_hub_api_url,
            git_hub_app_url=git_hub_app_url,
            git_hub_pfs_auth_endpoint=git_hub_pfs_auth_endpoint,
            github_environment_endpoint=github_environment_endpoint,
            has_devcontainer_json=has_devcontainer_json,
            identity=identity,
            label=label,
            location=location,
            netmon_correlation_data=netmon_correlation_data,
            personalization=personalization,
            plan_id=plan_id,
            platform=platform,
            runtime_constraints=runtime_constraints,
            secrets=secrets,
            seed=seed,
            sku_name=sku_name,
            test_account=test_account,
            user_tier=user_tier,
            working_directory=working_directory,
            request_options=request_options,
        )
        return _response.data

    def get_environment_route(
        self,
        environment_id: str,
        *,
        connect: typing.Optional[bool] = None,
        pf_connect: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        connect : typing.Optional[bool]

        pf_connect : typing.Optional[bool]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_environment_route(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_environment_route(
            environment_id, connect=connect, pf_connect=pf_connect, deleted=deleted, request_options=request_options
        )
        return _response.data

    def delete_api_v1environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
        client.environments.delete_api_v1environments_environment_id(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.delete_api_v1environments_environment_id(
            environment_id, request_options=request_options
        )
        return _response.data

    def patch_api_v1environments_environment_id(
        self,
        environment_id: str,
        *,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        failover_details: typing.Optional[FailoverDetails] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        plan_access_token: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        auto_shutdown_delay_minutes : typing.Optional[int]

        failover_details : typing.Optional[FailoverDetails]

        friendly_name : typing.Optional[str]

        plan_access_token : typing.Optional[str]

        plan_id : typing.Optional[str]

        sku_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.patch_api_v1environments_environment_id(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.patch_api_v1environments_environment_id(
            environment_id,
            auto_shutdown_delay_minutes=auto_shutdown_delay_minutes,
            failover_details=failover_details,
            friendly_name=friendly_name,
            plan_access_token=plan_access_token,
            plan_id=plan_id,
            sku_name=sku_name,
            request_options=request_options,
        )
        return _response.data

    def update_environment_route(
        self,
        environment_id: str,
        *,
        type: str,
        payload: typing.Optional[EnvironmentRegistrationCallbackPayloadBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        type : str

        payload : typing.Optional[EnvironmentRegistrationCallbackPayloadBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.update_environment_route(
            environment_id="environmentId",
            type="type",
        )
        """
        _response = self._raw_client.update_environment_route(
            environment_id, type=type, payload=payload, request_options=request_options
        )
        return _response.data

    def get_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnfilteredCloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnfilteredCloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1environments_environment_id_archive(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments_environment_id_archive(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1environments_environment_id_export(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments_environment_id_export(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1environments_environment_id_export(
            environment_id, request_options=request_options
        )
        return _response.data

    def patch_api_v1environments_environment_id_folder(
        self,
        environment_id: str,
        *,
        recent_folder_paths: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        recent_folder_paths : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.patch_api_v1environments_environment_id_folder(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.patch_api_v1environments_environment_id_folder(
            environment_id, recent_folder_paths=recent_folder_paths, request_options=request_options
        )
        return _response.data

    def get_api_v1environments_environment_id_heartbeattoken(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1environments_environment_id_heartbeattoken(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1environments_environment_id_heartbeattoken(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1environments_environment_id_notify(
        self,
        environment_id: str,
        *,
        details: typing.Optional[str] = OMIT,
        display_mode: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        modal: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        environment_id : str

        details : typing.Optional[str]

        display_mode : typing.Optional[str]

        message : typing.Optional[str]

        modal : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments_environment_id_notify(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1environments_environment_id_notify(
            environment_id,
            details=details,
            display_mode=display_mode,
            message=message,
            modal=modal,
            request_options=request_options,
        )
        return _response.data

    def put_api_v1environments_environment_id_ports_port(
        self,
        environment_id: str,
        port: int,
        *,
        privacy: typing.Optional[PrivacyEnum] = OMIT,
        tunnel_type: typing.Optional[TunnelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        privacy : typing.Optional[PrivacyEnum]

        tunnel_type : typing.Optional[TunnelType]

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
        client.environments.put_api_v1environments_environment_id_ports_port(
            environment_id="environmentId",
            port=1,
        )
        """
        _response = self._raw_client.put_api_v1environments_environment_id_ports_port(
            environment_id, port, privacy=privacy, tunnel_type=tunnel_type, request_options=request_options
        )
        return _response.data

    def delete_api_v1environments_environment_id_ports_port(
        self, environment_id: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        port : int

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
        client.environments.delete_api_v1environments_environment_id_ports_port(
            environment_id="environmentId",
            port=1,
        )
        """
        _response = self._raw_client.delete_api_v1environments_environment_id_ports_port(
            environment_id, port, request_options=request_options
        )
        return _response.data

    def patch_api_v1environments_environment_id_restore(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
        client.environments.patch_api_v1environments_environment_id_restore(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.patch_api_v1environments_environment_id_restore(
            environment_id, request_options=request_options
        )
        return _response.data

    def put_api_v1environments_environment_id_secrets(
        self,
        environment_id: str,
        *,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            No Content

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.put_api_v1environments_environment_id_secrets(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.put_api_v1environments_environment_id_secrets(
            environment_id, secrets=secrets, request_options=request_options
        )
        return _response.data

    def post_api_v1environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments_environment_id_shutdown(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1environments_environment_id_shutdown(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1environments_environment_id_start(
        self,
        environment_id: str,
        *,
        access: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        access : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1environments_environment_id_start(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1environments_environment_id_start(
            environment_id, access=access, request_options=request_options
        )
        return _response.data

    def get_api_v1environments_environment_id_state(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
        client.environments.get_api_v1environments_environment_id_state(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1environments_environment_id_state(
            environment_id, request_options=request_options
        )
        return _response.data

    def get_api_v1environments_environment_id_updates(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1environments_environment_id_updates(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1environments_environment_id_updates(
            environment_id, request_options=request_options
        )
        return _response.data

    def get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
        self,
        environment_id_or_friendly_name: str,
        target_blob: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        environment_id_or_friendly_name : str

        target_blob : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
            environment_id_or_friendly_name="environmentIdOrFriendlyName",
            target_blob="targetBlob",
        )
        """
        _response = (
            self._raw_client.get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
                environment_id_or_friendly_name, target_blob, request_options=request_options
            )
        )
        return _response.data

    def get_api_v1geneva_actions_environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.get_api_v1geneva_actions_environments_environment_id(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1geneva_actions_environments_environment_id(
            environment_id, request_options=request_options
        )
        return _response.data

    def delete_api_v1geneva_actions_environments_environment_id(
        self,
        environment_id: str,
        *,
        deletion_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        deletion_type : typing.Optional[str]

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
        client.environments.delete_api_v1geneva_actions_environments_environment_id(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.delete_api_v1geneva_actions_environments_environment_id(
            environment_id, deletion_type=deletion_type, request_options=request_options
        )
        return _response.data

    def put_api_v1geneva_actions_environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.put_api_v1geneva_actions_environments_environment_id_archive(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.put_api_v1geneva_actions_environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    def put_api_v1geneva_actions_environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.put_api_v1geneva_actions_environments_environment_id_shutdown(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.put_api_v1geneva_actions_environments_environment_id_shutdown(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VmLogsUploadInfo:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmLogsUploadInfo
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
            environment_id, request_options=request_options
        )
        return _response.data


class AsyncEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvironmentsClient
        """
        return self._raw_client

    async def get_api_v1environments(
        self,
        *,
        name: typing.Optional[str] = None,
        plan_id: typing.Optional[str] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CloudEnvironmentResult]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        plan_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CloudEnvironmentResult]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1environments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1environments(
            name=name, plan_id=plan_id, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments(
        self,
        *,
        friendly_name: str,
        type: str,
        access: typing.Optional[bool] = None,
        analytics_tracking_id: typing.Optional[str] = OMIT,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        billable_owner: typing.Optional[BillableOwnerBody] = OMIT,
        connection: typing.Optional[ConnectionInfoBody] = OMIT,
        container_image: typing.Optional[str] = OMIT,
        create_as_prebuild: typing.Optional[bool] = OMIT,
        dev_container_json: typing.Optional[str] = OMIT,
        dev_container_path: typing.Optional[str] = OMIT,
        experimental_features: typing.Optional[ExperimentalFeaturesBody] = OMIT,
        features: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        git_hub_api_url: typing.Optional[str] = OMIT,
        git_hub_app_url: typing.Optional[str] = OMIT,
        git_hub_pfs_auth_endpoint: typing.Optional[str] = OMIT,
        github_environment_endpoint: typing.Optional[str] = OMIT,
        has_devcontainer_json: typing.Optional[bool] = OMIT,
        identity: typing.Optional[IdentityBody] = OMIT,
        label: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        netmon_correlation_data: typing.Optional[NetmonCorrelationDataBody] = OMIT,
        personalization: typing.Optional[PersonalizationInfoBody] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        runtime_constraints: typing.Optional[RuntimeConstraintsBody] = OMIT,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        seed: typing.Optional[SeedInfoBody] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        test_account: typing.Optional[bool] = OMIT,
        user_tier: typing.Optional[str] = OMIT,
        working_directory: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        friendly_name : str

        type : str

        access : typing.Optional[bool]

        analytics_tracking_id : typing.Optional[str]

        auto_shutdown_delay_minutes : typing.Optional[int]

        billable_owner : typing.Optional[BillableOwnerBody]

        connection : typing.Optional[ConnectionInfoBody]

        container_image : typing.Optional[str]

        create_as_prebuild : typing.Optional[bool]

        dev_container_json : typing.Optional[str]

        dev_container_path : typing.Optional[str]

        experimental_features : typing.Optional[ExperimentalFeaturesBody]

        features : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        git_hub_api_url : typing.Optional[str]

        git_hub_app_url : typing.Optional[str]

        git_hub_pfs_auth_endpoint : typing.Optional[str]

        github_environment_endpoint : typing.Optional[str]

        has_devcontainer_json : typing.Optional[bool]

        identity : typing.Optional[IdentityBody]

        label : typing.Optional[str]

        location : typing.Optional[str]

        netmon_correlation_data : typing.Optional[NetmonCorrelationDataBody]

        personalization : typing.Optional[PersonalizationInfoBody]

        plan_id : typing.Optional[str]

        platform : typing.Optional[str]

        runtime_constraints : typing.Optional[RuntimeConstraintsBody]

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        seed : typing.Optional[SeedInfoBody]

        sku_name : typing.Optional[str]

        test_account : typing.Optional[bool]

        user_tier : typing.Optional[str]

        working_directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments(
                friendly_name="friendlyName",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments(
            friendly_name=friendly_name,
            type=type,
            access=access,
            analytics_tracking_id=analytics_tracking_id,
            auto_shutdown_delay_minutes=auto_shutdown_delay_minutes,
            billable_owner=billable_owner,
            connection=connection,
            container_image=container_image,
            create_as_prebuild=create_as_prebuild,
            dev_container_json=dev_container_json,
            dev_container_path=dev_container_path,
            experimental_features=experimental_features,
            features=features,
            git_hub_api_url=git_hub_api_url,
            git_hub_app_url=git_hub_app_url,
            git_hub_pfs_auth_endpoint=git_hub_pfs_auth_endpoint,
            github_environment_endpoint=github_environment_endpoint,
            has_devcontainer_json=has_devcontainer_json,
            identity=identity,
            label=label,
            location=location,
            netmon_correlation_data=netmon_correlation_data,
            personalization=personalization,
            plan_id=plan_id,
            platform=platform,
            runtime_constraints=runtime_constraints,
            secrets=secrets,
            seed=seed,
            sku_name=sku_name,
            test_account=test_account,
            user_tier=user_tier,
            working_directory=working_directory,
            request_options=request_options,
        )
        return _response.data

    async def get_environment_route(
        self,
        environment_id: str,
        *,
        connect: typing.Optional[bool] = None,
        pf_connect: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        connect : typing.Optional[bool]

        pf_connect : typing.Optional[bool]

        deleted : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_environment_route(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_environment_route(
            environment_id, connect=connect, pf_connect=pf_connect, deleted=deleted, request_options=request_options
        )
        return _response.data

    async def delete_api_v1environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
            await client.environments.delete_api_v1environments_environment_id(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1environments_environment_id(
            environment_id, request_options=request_options
        )
        return _response.data

    async def patch_api_v1environments_environment_id(
        self,
        environment_id: str,
        *,
        auto_shutdown_delay_minutes: typing.Optional[int] = OMIT,
        failover_details: typing.Optional[FailoverDetails] = OMIT,
        friendly_name: typing.Optional[str] = OMIT,
        plan_access_token: typing.Optional[str] = OMIT,
        plan_id: typing.Optional[str] = OMIT,
        sku_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        auto_shutdown_delay_minutes : typing.Optional[int]

        failover_details : typing.Optional[FailoverDetails]

        friendly_name : typing.Optional[str]

        plan_access_token : typing.Optional[str]

        plan_id : typing.Optional[str]

        sku_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.patch_api_v1environments_environment_id(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1environments_environment_id(
            environment_id,
            auto_shutdown_delay_minutes=auto_shutdown_delay_minutes,
            failover_details=failover_details,
            friendly_name=friendly_name,
            plan_access_token=plan_access_token,
            plan_id=plan_id,
            sku_name=sku_name,
            request_options=request_options,
        )
        return _response.data

    async def update_environment_route(
        self,
        environment_id: str,
        *,
        type: str,
        payload: typing.Optional[EnvironmentRegistrationCallbackPayloadBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        type : str

        payload : typing.Optional[EnvironmentRegistrationCallbackPayloadBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.update_environment_route(
                environment_id="environmentId",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_environment_route(
            environment_id, type=type, payload=payload, request_options=request_options
        )
        return _response.data

    async def get_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnfilteredCloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnfilteredCloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1environments_environment_id_archive(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments_environment_id_archive(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments_environment_id_export(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments_environment_id_export(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments_environment_id_export(
            environment_id, request_options=request_options
        )
        return _response.data

    async def patch_api_v1environments_environment_id_folder(
        self,
        environment_id: str,
        *,
        recent_folder_paths: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        recent_folder_paths : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.patch_api_v1environments_environment_id_folder(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1environments_environment_id_folder(
            environment_id, recent_folder_paths=recent_folder_paths, request_options=request_options
        )
        return _response.data

    async def get_api_v1environments_environment_id_heartbeattoken(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1environments_environment_id_heartbeattoken(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1environments_environment_id_heartbeattoken(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments_environment_id_notify(
        self,
        environment_id: str,
        *,
        details: typing.Optional[str] = OMIT,
        display_mode: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        modal: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        environment_id : str

        details : typing.Optional[str]

        display_mode : typing.Optional[str]

        message : typing.Optional[str]

        modal : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments_environment_id_notify(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments_environment_id_notify(
            environment_id,
            details=details,
            display_mode=display_mode,
            message=message,
            modal=modal,
            request_options=request_options,
        )
        return _response.data

    async def put_api_v1environments_environment_id_ports_port(
        self,
        environment_id: str,
        port: int,
        *,
        privacy: typing.Optional[PrivacyEnum] = OMIT,
        tunnel_type: typing.Optional[TunnelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        port : int

        privacy : typing.Optional[PrivacyEnum]

        tunnel_type : typing.Optional[TunnelType]

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
            await client.environments.put_api_v1environments_environment_id_ports_port(
                environment_id="environmentId",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1environments_environment_id_ports_port(
            environment_id, port, privacy=privacy, tunnel_type=tunnel_type, request_options=request_options
        )
        return _response.data

    async def delete_api_v1environments_environment_id_ports_port(
        self, environment_id: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        port : int

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
            await client.environments.delete_api_v1environments_environment_id_ports_port(
                environment_id="environmentId",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1environments_environment_id_ports_port(
            environment_id, port, request_options=request_options
        )
        return _response.data

    async def patch_api_v1environments_environment_id_restore(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
            await client.environments.patch_api_v1environments_environment_id_restore(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1environments_environment_id_restore(
            environment_id, request_options=request_options
        )
        return _response.data

    async def put_api_v1environments_environment_id_secrets(
        self,
        environment_id: str,
        *,
        secrets: typing.Optional[typing.Sequence[SecretDataBody]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        secrets : typing.Optional[typing.Sequence[SecretDataBody]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            No Content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.put_api_v1environments_environment_id_secrets(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1environments_environment_id_secrets(
            environment_id, secrets=secrets, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments_environment_id_shutdown(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments_environment_id_shutdown(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1environments_environment_id_start(
        self,
        environment_id: str,
        *,
        access: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        access : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1environments_environment_id_start(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1environments_environment_id_start(
            environment_id, access=access, request_options=request_options
        )
        return _response.data

    async def get_api_v1environments_environment_id_state(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

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
            await client.environments.get_api_v1environments_environment_id_state(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1environments_environment_id_state(
            environment_id, request_options=request_options
        )
        return _response.data

    async def get_api_v1environments_environment_id_updates(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1environments_environment_id_updates(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1environments_environment_id_updates(
            environment_id, request_options=request_options
        )
        return _response.data

    async def get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
        self,
        environment_id_or_friendly_name: str,
        target_blob: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        environment_id_or_friendly_name : str

        target_blob : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
                environment_id_or_friendly_name="environmentIdOrFriendlyName",
                target_blob="targetBlob",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
            environment_id_or_friendly_name, target_blob, request_options=request_options
        )
        return _response.data

    async def get_api_v1geneva_actions_environments_environment_id(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.get_api_v1geneva_actions_environments_environment_id(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1geneva_actions_environments_environment_id(
            environment_id, request_options=request_options
        )
        return _response.data

    async def delete_api_v1geneva_actions_environments_environment_id(
        self,
        environment_id: str,
        *,
        deletion_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        environment_id : str

        deletion_type : typing.Optional[str]

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
            await client.environments.delete_api_v1geneva_actions_environments_environment_id(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1geneva_actions_environments_environment_id(
            environment_id, deletion_type=deletion_type, request_options=request_options
        )
        return _response.data

    async def put_api_v1geneva_actions_environments_environment_id_archive(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.put_api_v1geneva_actions_environments_environment_id_archive(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1geneva_actions_environments_environment_id_archive(
            environment_id, request_options=request_options
        )
        return _response.data

    async def put_api_v1geneva_actions_environments_environment_id_shutdown(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudEnvironmentResult:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudEnvironmentResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.put_api_v1geneva_actions_environments_environment_id_shutdown(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1geneva_actions_environments_environment_id_shutdown(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VmLogsUploadInfo:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmLogsUploadInfo
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
            environment_id, request_options=request_options
        )
        return _response.data
