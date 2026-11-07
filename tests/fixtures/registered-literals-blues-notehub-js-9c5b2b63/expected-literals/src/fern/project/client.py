

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.aws_role_config import AwsRoleConfig
from ..types.device_dfu_history import DeviceDfuHistory
from ..types.device_dfu_history_page import DeviceDfuHistoryPage
from ..types.device_dfu_status import DeviceDfuStatus
from ..types.device_dfu_status_page import DeviceDfuStatusPage
from ..types.env_tree_json_node import EnvTreeJsonNode
from ..types.environment_variables import EnvironmentVariables
from ..types.firmware_info import FirmwareInfo
from ..types.fleet import Fleet
from ..types.fleet_connectivity_assurance import FleetConnectivityAssurance
from ..types.fleet_rule import FleetRule
from ..types.get_project_secrets_response import GetProjectSecretsResponse
from ..types.notefile_schema import NotefileSchema
from ..types.product import Product
from ..types.project import Project
from ..types.project_secret import ProjectSecret
from .raw_client import AsyncRawProjectClient, RawProjectClient
from .types.add_device_to_fleets_response import AddDeviceToFleetsResponse
from .types.delete_device_from_fleets_response import DeleteDeviceFromFleetsResponse
from .types.delete_firmware_request_firmware_type import DeleteFirmwareRequestFirmwareType
from .types.download_firmware_request_firmware_type import DownloadFirmwareRequestFirmwareType
from .types.get_device_dfu_history_request_firmware_type import GetDeviceDfuHistoryRequestFirmwareType
from .types.get_device_dfu_status_request_firmware_type import GetDeviceDfuStatusRequestFirmwareType
from .types.get_device_fleets_response import GetDeviceFleetsResponse
from .types.get_devices_dfu_history_request_firmware_type import GetDevicesDfuHistoryRequestFirmwareType
from .types.get_devices_dfu_history_request_sort_by import GetDevicesDfuHistoryRequestSortBy
from .types.get_devices_dfu_history_request_sort_order import GetDevicesDfuHistoryRequestSortOrder
from .types.get_devices_dfu_status_request_firmware_type import GetDevicesDfuStatusRequestFirmwareType
from .types.get_devices_dfu_status_request_sort_by import GetDevicesDfuStatusRequestSortBy
from .types.get_devices_dfu_status_request_sort_order import GetDevicesDfuStatusRequestSortOrder
from .types.get_firmware_info_request_sort_by import GetFirmwareInfoRequestSortBy
from .types.get_firmware_info_request_sort_order import GetFirmwareInfoRequestSortOrder
from .types.get_fleets_response import GetFleetsResponse
from .types.get_products_response import GetProductsResponse
from .types.get_project_members_response import GetProjectMembersResponse
from .types.get_projects_response import GetProjectsResponse
from .types.perform_dfu_action_request_action import PerformDfuActionRequestAction
from .types.perform_dfu_action_request_firmware_type import PerformDfuActionRequestFirmwareType
from .types.update_firmware_request_firmware_type import UpdateFirmwareRequestFirmwareType
from .types.upload_firmware_request_firmware_type import UploadFirmwareRequestFirmwareType


OMIT = typing.cast(typing.Any, ...)


class ProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectClient
        """
        return self._raw_client

    def get_project_by_product(
        self, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a Project by ProductUID

        Parameters
        ----------
        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project_by_product(
            product_uid="com.blues.airnote",
        )
        """
        _response = self._raw_client.get_project_by_product(product_uid, request_options=request_options)
        return _response.data

    def get_projects(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProjectsResponse:
        """
        Get Projects accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_projects()
        """
        _response = self._raw_client.get_projects(request_options=request_options)
        return _response.data

    def create_project(
        self, *, billing_account_uid: str, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Create a Project

        Parameters
        ----------
        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.create_project(
            billing_account_uid="billing_account_uid",
            label="label",
        )
        """
        _response = self._raw_client.create_project(
            billing_account_uid=billing_account_uid, label=label, request_options=request_options
        )
        return _response.data

    def get_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_project(project_or_product_uid, request_options=request_options)
        return _response.data

    def delete_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

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
        client.project.delete_project(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.delete_project(project_or_product_uid, request_options=request_options)
        return _response.data

    def get_aws_role_config(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AwsRoleConfig:
        """
        Returns the AWS Account ID and External ID needed to configure an IAM role
        trust policy for role-based authentication on AWS routes.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AwsRoleConfig
            AWS role configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_aws_role_config(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_aws_role_config(project_or_product_uid, request_options=request_options)
        return _response.data

    def clone_project(
        self,
        project_or_product_uid: str,
        *,
        billing_account_uid: str,
        label: str,
        disable_clone_fleets: typing.Optional[bool] = OMIT,
        disable_clone_routes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Clone a Project

        Parameters
        ----------
        project_or_product_uid : str

        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        disable_clone_fleets : typing.Optional[bool]
            Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified.

        disable_clone_routes : typing.Optional[bool]
            Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.clone_project(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            billing_account_uid="billing_account_uid",
            label="label",
        )
        """
        _response = self._raw_client.clone_project(
            project_or_product_uid,
            billing_account_uid=billing_account_uid,
            label=label,
            disable_clone_fleets=disable_clone_fleets,
            disable_clone_routes=disable_clone_routes,
            request_options=request_options,
        )
        return _response.data

    def get_device_dfu_history(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuHistoryRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuHistory:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuHistoryRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuHistory
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_device_dfu_history(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            firmware_type="host",
        )
        """
        _response = self._raw_client.get_device_dfu_history(
            project_or_product_uid, device_uid, firmware_type, request_options=request_options
        )
        return _response.data

    def get_device_dfu_status(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuStatusRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuStatus:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuStatusRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuStatus
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_device_dfu_status(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            firmware_type="host",
        )
        """
        _response = self._raw_client.get_device_dfu_status(
            project_or_product_uid, device_uid, firmware_type, request_options=request_options
        )
        return _response.data

    def get_device_fleets(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceFleetsResponse:
        """
        Get Device Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_device_fleets(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_fleets(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def add_device_to_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddDeviceToFleetsResponse:
        """
        Add Device to Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to add to the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddDeviceToFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.add_device_to_fleets(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            fleet_uids=["fleet_uids"],
        )
        """
        _response = self._raw_client.add_device_to_fleets(
            project_or_product_uid, device_uid, fleet_uids=fleet_uids, request_options=request_options
        )
        return _response.data

    def delete_device_from_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDeviceFromFleetsResponse:
        """
        Remove Device from Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to remove from the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDeviceFromFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.delete_device_from_fleets(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            fleet_uids=["fleet_uids"],
        )
        """
        _response = self._raw_client.delete_device_from_fleets(
            project_or_product_uid, device_uid, fleet_uids=fleet_uids, request_options=request_options
        )
        return _response.data

    def perform_dfu_action(
        self,
        project_or_product_uid: str,
        firmware_type: PerformDfuActionRequestFirmwareType,
        action: PerformDfuActionRequestAction,
        *,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update/cancel host or notecard firmware updates

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : PerformDfuActionRequestFirmwareType

        action : PerformDfuActionRequestAction

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        filename : typing.Optional[str]
            The name of the firmware file

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
        client.project.perform_dfu_action(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            firmware_type="host",
            action="update",
        )
        """
        _response = self._raw_client.perform_dfu_action(
            project_or_product_uid,
            firmware_type,
            action,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            filename=filename,
            request_options=request_options,
        )
        return _response.data

    def get_devices_dfu_history(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuHistoryRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuHistoryRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuHistoryRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuHistoryPage:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuHistoryRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuHistoryRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuHistoryRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuHistoryPage
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_devices_dfu_history(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            firmware_type="host",
        )
        """
        _response = self._raw_client.get_devices_dfu_history(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            sort_by=sort_by,
            sort_order=sort_order,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    def get_devices_dfu_status(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuStatusRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuStatusRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuStatusRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuStatusPage:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuStatusRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuStatusRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuStatusRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuStatusPage
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_devices_dfu_status(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            firmware_type="host",
        )
        """
        _response = self._raw_client.get_devices_dfu_status(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            sort_by=sort_by,
            sort_order=sort_order,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    def get_project_environment_hierarchy(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved project environment hierarchy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project_environment_hierarchy(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_project_environment_hierarchy(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    def get_project_environment_variables(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Get environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_project_environment_variables(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    def set_project_environment_variables(
        self,
        project_or_product_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.set_project_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            environment_variables={"key": "value"},
        )
        """
        _response = self._raw_client.set_project_environment_variables(
            project_or_product_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    def delete_project_environment_variable(
        self, project_or_product_uid: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Delete an environment variable of a project by key

        Parameters
        ----------
        project_or_product_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.delete_project_environment_variable(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            key="key",
        )
        """
        _response = self._raw_client.delete_project_environment_variable(
            project_or_product_uid, key, request_options=request_options
        )
        return _response.data

    def get_firmware_info(
        self,
        project_or_product_uid: str,
        *,
        product: typing.Optional[str] = None,
        firmware_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        md5: typing.Optional[str] = None,
        unpublished: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetFirmwareInfoRequestSortBy] = None,
        sort_order: typing.Optional[GetFirmwareInfoRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FirmwareInfo]:
        """
        Get Available Firmware Information

        Parameters
        ----------
        project_or_product_uid : str

        product : typing.Optional[str]

        firmware_type : typing.Optional[str]

        version : typing.Optional[str]

        target : typing.Optional[str]

        filename : typing.Optional[str]

        md5 : typing.Optional[str]

        unpublished : typing.Optional[bool]

        sort_by : typing.Optional[GetFirmwareInfoRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[GetFirmwareInfoRequestSortOrder]
            Sort order (asc for ascending, desc for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FirmwareInfo]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_firmware_info(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            filename="notecard-7.2.2.16518$20240410043100.bin",
        )
        """
        _response = self._raw_client.get_firmware_info(
            project_or_product_uid,
            product=product,
            firmware_type=firmware_type,
            version=version,
            target=target,
            filename=filename,
            md5=md5,
            unpublished=unpublished,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def download_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DownloadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Download firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DownloadFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Firmware binary
        """
        with self._raw_client.download_firmware(
            project_or_product_uid, firmware_type, filename, request_options=request_options
        ) as r:
            yield from r.data

    def update_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UpdateFirmwareRequestFirmwareType,
        filename: str,
        *,
        info: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FirmwareInfo:
        """
        Update the metadata of an existing host firmware entry. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UpdateFirmwareRequestFirmwareType

        filename : str

        info : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary JSON metadata associated with this firmware entry.

        notes : typing.Optional[str]
            Notes describing this firmware version.

        version : typing.Optional[str]
            The firmware version string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FirmwareInfo
            Update successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.update_firmware(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            firmware_type="host",
            filename="filename",
        )
        """
        _response = self._raw_client.update_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            info=info,
            notes=notes,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def upload_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UploadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        version: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FirmwareInfo:
        """
        Upload firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UploadFirmwareRequestFirmwareType

        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        version : typing.Optional[str]
            Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty

        notes : typing.Optional[str]
            Optional notes describing what's different about this firmware version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FirmwareInfo
            Upload successful
        """
        _response = self._raw_client.upload_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            request=request,
            version=version,
            notes=notes,
            request_options=request_options,
        )
        return _response.data

    def delete_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DeleteFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a host firmware binary. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DeleteFirmwareRequestFirmwareType

        filename : str

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
        client.project.delete_firmware(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            firmware_type="host",
            filename="filename",
        )
        """
        _response = self._raw_client.delete_firmware(
            project_or_product_uid, firmware_type, filename, request_options=request_options
        )
        return _response.data

    def get_fleets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFleetsResponse:
        """
        Get Project Fleets

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_fleets(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_fleets(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_fleet(
        self,
        project_or_product_uid: str,
        *,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleet:
        """
        Create Fleet

        Parameters
        ----------
        project_or_product_uid : str

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label, or name,  for the Fleet.

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.create_fleet(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.create_fleet(
            project_or_product_uid,
            connectivity_assurance=connectivity_assurance,
            label=label,
            smart_rule=smart_rule,
            smart_rule_enabled=smart_rule_enabled,
            request_options=request_options,
        )
        return _response.data

    def get_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Fleet:
        """
        Get Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_fleet(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.get_fleet(project_or_product_uid, fleet_uid, request_options=request_options)
        return _response.data

    def update_fleet(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        add_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        remove_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        watchdog_mins: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleet:
        """
        Update Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        add_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to add to fleet

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label for the Fleet.

        remove_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to remove from fleet

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        watchdog_mins : typing.Optional[int]
            A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.update_fleet(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.update_fleet(
            project_or_product_uid,
            fleet_uid,
            add_devices=add_devices,
            connectivity_assurance=connectivity_assurance,
            label=label,
            remove_devices=remove_devices,
            smart_rule=smart_rule,
            smart_rule_enabled=smart_rule_enabled,
            watchdog_mins=watchdog_mins,
            request_options=request_options,
        )
        return _response.data

    def delete_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

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
        client.project.delete_fleet(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.delete_fleet(project_or_product_uid, fleet_uid, request_options=request_options)
        return _response.data

    def get_fleet_environment_hierarchy(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved fleet environment hierarchy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_fleet_environment_hierarchy(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.get_fleet_environment_hierarchy(
            project_or_product_uid, fleet_uid, request_options=request_options
        )
        return _response.data

    def get_fleet_environment_variables(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Get environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_fleet_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.get_fleet_environment_variables(
            project_or_product_uid, fleet_uid, request_options=request_options
        )
        return _response.data

    def set_fleet_environment_variables(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.set_fleet_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
            environment_variables={"key": "value"},
        )
        """
        _response = self._raw_client.set_fleet_environment_variables(
            project_or_product_uid,
            fleet_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    def delete_fleet_environment_variable(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Delete environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.delete_fleet_environment_variable(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
            key="key",
        )
        """
        _response = self._raw_client.delete_fleet_environment_variable(
            project_or_product_uid, fleet_uid, key, request_options=request_options
        )
        return _response.data

    def set_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
        client.project.set_global_event_transformation(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.set_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    def disable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
        client.project.disable_global_event_transformation(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.disable_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    def enable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
        client.project.enable_global_event_transformation(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.enable_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    def get_project_members(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectMembersResponse:
        """
        Get Project Members

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectMembersResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project_members(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_project_members(project_or_product_uid, request_options=request_options)
        return _response.data

    def get_products(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        Get Products within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_products(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_products(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_product(
        self,
        project_or_product_uid: str,
        *,
        label: str,
        product_uid: str,
        auto_provision_fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        disable_devices_by_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Product:
        """
        Create Product within a Project

        Parameters
        ----------
        project_or_product_uid : str

        label : str
            The label for the Product.

        product_uid : str
            The requested uid for the Product. Will be prefixed with the user's reversed email.

        auto_provision_fleets : typing.Optional[typing.Sequence[str]]

        disable_devices_by_default : typing.Optional[bool]
            If `true`, devices provisioned to this product will be automatically disabled by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.create_product(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            label="label",
            product_uid="product_uid",
        )
        """
        _response = self._raw_client.create_product(
            project_or_product_uid,
            label=label,
            product_uid=product_uid,
            auto_provision_fleets=auto_provision_fleets,
            disable_devices_by_default=disable_devices_by_default,
            request_options=request_options,
        )
        return _response.data

    def delete_product(
        self, project_or_product_uid: str, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product

        Parameters
        ----------
        project_or_product_uid : str

        product_uid : str

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
        client.project.delete_product(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            product_uid="com.blues.bridge:sensors",
        )
        """
        _response = self._raw_client.delete_product(
            project_or_product_uid, product_uid, request_options=request_options
        )
        return _response.data

    def get_notefile_schemas(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotefileSchema]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotefileSchema]
            List of notefile schema definitions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_notefile_schemas(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_notefile_schemas(project_or_product_uid, request_options=request_options)
        return _response.data

    def get_project_secrets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectSecretsResponse:
        """
        Get all secrets for a project (metadata only, values are never returned)

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectSecretsResponse
            The response body from a get project secrets request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.get_project_secrets(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_project_secrets(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_project_secret(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSecret:
        """
        Create a new project secret

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            The secret name (alphanumeric and underscores only).

        value : str
            The secret value (encrypted at rest, never returned after creation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSecret
            Secret created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.create_project_secret(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            name="name",
            value="value",
        )
        """
        _response = self._raw_client.create_project_secret(
            project_or_product_uid, name=name, value=value, request_options=request_options
        )
        return _response.data

    def update_project_secret(
        self,
        project_or_product_uid: str,
        secret_name: str,
        *,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSecret:
        """
        Update the value of an existing project secret

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        value : str
            The new secret value (encrypted at rest, never returned).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSecret
            Secret updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.project.update_project_secret(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            secret_name="secretName",
            value="value",
        )
        """
        _response = self._raw_client.update_project_secret(
            project_or_product_uid, secret_name, value=value, request_options=request_options
        )
        return _response.data

    def delete_project_secret(
        self, project_or_product_uid: str, secret_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a project secret by name

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

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
        client.project.delete_project_secret(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            secret_name="secretName",
        )
        """
        _response = self._raw_client.delete_project_secret(
            project_or_product_uid, secret_name, request_options=request_options
        )
        return _response.data


class AsyncProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectClient
        """
        return self._raw_client

    async def get_project_by_product(
        self, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a Project by ProductUID

        Parameters
        ----------
        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project_by_product(
                product_uid="com.blues.airnote",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_by_product(product_uid, request_options=request_options)
        return _response.data

    async def get_projects(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProjectsResponse:
        """
        Get Projects accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_projects()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_projects(request_options=request_options)
        return _response.data

    async def create_project(
        self, *, billing_account_uid: str, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Create a Project

        Parameters
        ----------
        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.create_project(
                billing_account_uid="billing_account_uid",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project(
            billing_account_uid=billing_account_uid, label=label, request_options=request_options
        )
        return _response.data

    async def get_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project(project_or_product_uid, request_options=request_options)
        return _response.data

    async def delete_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

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
            await client.project.delete_project(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project(project_or_product_uid, request_options=request_options)
        return _response.data

    async def get_aws_role_config(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AwsRoleConfig:
        """
        Returns the AWS Account ID and External ID needed to configure an IAM role
        trust policy for role-based authentication on AWS routes.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AwsRoleConfig
            AWS role configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_aws_role_config(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_aws_role_config(project_or_product_uid, request_options=request_options)
        return _response.data

    async def clone_project(
        self,
        project_or_product_uid: str,
        *,
        billing_account_uid: str,
        label: str,
        disable_clone_fleets: typing.Optional[bool] = OMIT,
        disable_clone_routes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Clone a Project

        Parameters
        ----------
        project_or_product_uid : str

        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        disable_clone_fleets : typing.Optional[bool]
            Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified.

        disable_clone_routes : typing.Optional[bool]
            Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.clone_project(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                billing_account_uid="billing_account_uid",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clone_project(
            project_or_product_uid,
            billing_account_uid=billing_account_uid,
            label=label,
            disable_clone_fleets=disable_clone_fleets,
            disable_clone_routes=disable_clone_routes,
            request_options=request_options,
        )
        return _response.data

    async def get_device_dfu_history(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuHistoryRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuHistory:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuHistoryRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuHistory
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_device_dfu_history(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                firmware_type="host",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_dfu_history(
            project_or_product_uid, device_uid, firmware_type, request_options=request_options
        )
        return _response.data

    async def get_device_dfu_status(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuStatusRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuStatus:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuStatusRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuStatus
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_device_dfu_status(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                firmware_type="host",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_dfu_status(
            project_or_product_uid, device_uid, firmware_type, request_options=request_options
        )
        return _response.data

    async def get_device_fleets(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceFleetsResponse:
        """
        Get Device Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_device_fleets(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_fleets(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def add_device_to_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddDeviceToFleetsResponse:
        """
        Add Device to Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to add to the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddDeviceToFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.add_device_to_fleets(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                fleet_uids=["fleet_uids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_device_to_fleets(
            project_or_product_uid, device_uid, fleet_uids=fleet_uids, request_options=request_options
        )
        return _response.data

    async def delete_device_from_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDeviceFromFleetsResponse:
        """
        Remove Device from Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to remove from the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDeviceFromFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.delete_device_from_fleets(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                fleet_uids=["fleet_uids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_device_from_fleets(
            project_or_product_uid, device_uid, fleet_uids=fleet_uids, request_options=request_options
        )
        return _response.data

    async def perform_dfu_action(
        self,
        project_or_product_uid: str,
        firmware_type: PerformDfuActionRequestFirmwareType,
        action: PerformDfuActionRequestAction,
        *,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update/cancel host or notecard firmware updates

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : PerformDfuActionRequestFirmwareType

        action : PerformDfuActionRequestAction

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        filename : typing.Optional[str]
            The name of the firmware file

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
            await client.project.perform_dfu_action(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                firmware_type="host",
                action="update",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_dfu_action(
            project_or_product_uid,
            firmware_type,
            action,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            filename=filename,
            request_options=request_options,
        )
        return _response.data

    async def get_devices_dfu_history(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuHistoryRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuHistoryRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuHistoryRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuHistoryPage:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuHistoryRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuHistoryRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuHistoryRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuHistoryPage
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_devices_dfu_history(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                firmware_type="host",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_devices_dfu_history(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            sort_by=sort_by,
            sort_order=sort_order,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    async def get_devices_dfu_status(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuStatusRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuStatusRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuStatusRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceDfuStatusPage:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuStatusRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuStatusRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuStatusRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceDfuStatusPage
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_devices_dfu_status(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                firmware_type="host",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_devices_dfu_status(
            project_or_product_uid,
            firmware_type,
            page_size=page_size,
            page_num=page_num,
            sort_by=sort_by,
            sort_order=sort_order,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    async def get_project_environment_hierarchy(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved project environment hierarchy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project_environment_hierarchy(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_environment_hierarchy(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def get_project_environment_variables(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Get environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_environment_variables(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def set_project_environment_variables(
        self,
        project_or_product_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.set_project_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                environment_variables={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_project_environment_variables(
            project_or_product_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    async def delete_project_environment_variable(
        self, project_or_product_uid: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Delete an environment variable of a project by key

        Parameters
        ----------
        project_or_product_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.delete_project_environment_variable(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_environment_variable(
            project_or_product_uid, key, request_options=request_options
        )
        return _response.data

    async def get_firmware_info(
        self,
        project_or_product_uid: str,
        *,
        product: typing.Optional[str] = None,
        firmware_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        md5: typing.Optional[str] = None,
        unpublished: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetFirmwareInfoRequestSortBy] = None,
        sort_order: typing.Optional[GetFirmwareInfoRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FirmwareInfo]:
        """
        Get Available Firmware Information

        Parameters
        ----------
        project_or_product_uid : str

        product : typing.Optional[str]

        firmware_type : typing.Optional[str]

        version : typing.Optional[str]

        target : typing.Optional[str]

        filename : typing.Optional[str]

        md5 : typing.Optional[str]

        unpublished : typing.Optional[bool]

        sort_by : typing.Optional[GetFirmwareInfoRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[GetFirmwareInfoRequestSortOrder]
            Sort order (asc for ascending, desc for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FirmwareInfo]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_firmware_info(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                filename="notecard-7.2.2.16518$20240410043100.bin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_firmware_info(
            project_or_product_uid,
            product=product,
            firmware_type=firmware_type,
            version=version,
            target=target,
            filename=filename,
            md5=md5,
            unpublished=unpublished,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def download_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DownloadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Download firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DownloadFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Firmware binary
        """
        async with self._raw_client.download_firmware(
            project_or_product_uid, firmware_type, filename, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def update_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UpdateFirmwareRequestFirmwareType,
        filename: str,
        *,
        info: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FirmwareInfo:
        """
        Update the metadata of an existing host firmware entry. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UpdateFirmwareRequestFirmwareType

        filename : str

        info : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary JSON metadata associated with this firmware entry.

        notes : typing.Optional[str]
            Notes describing this firmware version.

        version : typing.Optional[str]
            The firmware version string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FirmwareInfo
            Update successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.update_firmware(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                firmware_type="host",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            info=info,
            notes=notes,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def upload_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UploadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        version: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FirmwareInfo:
        """
        Upload firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UploadFirmwareRequestFirmwareType

        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        version : typing.Optional[str]
            Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty

        notes : typing.Optional[str]
            Optional notes describing what's different about this firmware version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FirmwareInfo
            Upload successful
        """
        _response = await self._raw_client.upload_firmware(
            project_or_product_uid,
            firmware_type,
            filename,
            request=request,
            version=version,
            notes=notes,
            request_options=request_options,
        )
        return _response.data

    async def delete_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DeleteFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a host firmware binary. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DeleteFirmwareRequestFirmwareType

        filename : str

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
            await client.project.delete_firmware(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                firmware_type="host",
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_firmware(
            project_or_product_uid, firmware_type, filename, request_options=request_options
        )
        return _response.data

    async def get_fleets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFleetsResponse:
        """
        Get Project Fleets

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFleetsResponse
            The response body from a fleets endpoint.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_fleets(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleets(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_fleet(
        self,
        project_or_product_uid: str,
        *,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleet:
        """
        Create Fleet

        Parameters
        ----------
        project_or_product_uid : str

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label, or name,  for the Fleet.

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.create_fleet(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_fleet(
            project_or_product_uid,
            connectivity_assurance=connectivity_assurance,
            label=label,
            smart_rule=smart_rule,
            smart_rule_enabled=smart_rule_enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Fleet:
        """
        Get Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_fleet(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet(project_or_product_uid, fleet_uid, request_options=request_options)
        return _response.data

    async def update_fleet(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        add_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        remove_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        watchdog_mins: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Fleet:
        """
        Update Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        add_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to add to fleet

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label for the Fleet.

        remove_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to remove from fleet

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        watchdog_mins : typing.Optional[int]
            A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Fleet
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.update_fleet(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_fleet(
            project_or_product_uid,
            fleet_uid,
            add_devices=add_devices,
            connectivity_assurance=connectivity_assurance,
            label=label,
            remove_devices=remove_devices,
            smart_rule=smart_rule,
            smart_rule_enabled=smart_rule_enabled,
            watchdog_mins=watchdog_mins,
            request_options=request_options,
        )
        return _response.data

    async def delete_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

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
            await client.project.delete_fleet(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_fleet(
            project_or_product_uid, fleet_uid, request_options=request_options
        )
        return _response.data

    async def get_fleet_environment_hierarchy(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved fleet environment hierarchy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_fleet_environment_hierarchy(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_environment_hierarchy(
            project_or_product_uid, fleet_uid, request_options=request_options
        )
        return _response.data

    async def get_fleet_environment_variables(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentVariables:
        """
        Get environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_fleet_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_environment_variables(
            project_or_product_uid, fleet_uid, request_options=request_options
        )
        return _response.data

    async def set_fleet_environment_variables(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.set_fleet_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
                environment_variables={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_fleet_environment_variables(
            project_or_product_uid,
            fleet_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    async def delete_fleet_environment_variable(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Delete environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariables
            The response body from an environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.delete_fleet_environment_variable(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_fleet_environment_variable(
            project_or_product_uid, fleet_uid, key, request_options=request_options
        )
        return _response.data

    async def set_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
            await client.project.set_global_event_transformation(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def disable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
            await client.project.disable_global_event_transformation(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def enable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

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
            await client.project.enable_global_event_transformation(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_global_event_transformation(
            project_or_product_uid, request_options=request_options
        )
        return _response.data

    async def get_project_members(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectMembersResponse:
        """
        Get Project Members

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectMembersResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project_members(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_members(project_or_product_uid, request_options=request_options)
        return _response.data

    async def get_products(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        Get Products within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_products(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_products(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_product(
        self,
        project_or_product_uid: str,
        *,
        label: str,
        product_uid: str,
        auto_provision_fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        disable_devices_by_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Product:
        """
        Create Product within a Project

        Parameters
        ----------
        project_or_product_uid : str

        label : str
            The label for the Product.

        product_uid : str
            The requested uid for the Product. Will be prefixed with the user's reversed email.

        auto_provision_fleets : typing.Optional[typing.Sequence[str]]

        disable_devices_by_default : typing.Optional[bool]
            If `true`, devices provisioned to this product will be automatically disabled by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.create_product(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                label="label",
                product_uid="product_uid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_product(
            project_or_product_uid,
            label=label,
            product_uid=product_uid,
            auto_provision_fleets=auto_provision_fleets,
            disable_devices_by_default=disable_devices_by_default,
            request_options=request_options,
        )
        return _response.data

    async def delete_product(
        self, project_or_product_uid: str, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product

        Parameters
        ----------
        project_or_product_uid : str

        product_uid : str

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
            await client.project.delete_product(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                product_uid="com.blues.bridge:sensors",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_product(
            project_or_product_uid, product_uid, request_options=request_options
        )
        return _response.data

    async def get_notefile_schemas(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotefileSchema]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotefileSchema]
            List of notefile schema definitions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_notefile_schemas(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notefile_schemas(project_or_product_uid, request_options=request_options)
        return _response.data

    async def get_project_secrets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectSecretsResponse:
        """
        Get all secrets for a project (metadata only, values are never returned)

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectSecretsResponse
            The response body from a get project secrets request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.get_project_secrets(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_secrets(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_project_secret(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSecret:
        """
        Create a new project secret

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            The secret name (alphanumeric and underscores only).

        value : str
            The secret value (encrypted at rest, never returned after creation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSecret
            Secret created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.create_project_secret(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                name="name",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_secret(
            project_or_product_uid, name=name, value=value, request_options=request_options
        )
        return _response.data

    async def update_project_secret(
        self,
        project_or_product_uid: str,
        secret_name: str,
        *,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSecret:
        """
        Update the value of an existing project secret

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        value : str
            The new secret value (encrypted at rest, never returned).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSecret
            Secret updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.project.update_project_secret(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                secret_name="secretName",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_secret(
            project_or_product_uid, secret_name, value=value, request_options=request_options
        )
        return _response.data

    async def delete_project_secret(
        self, project_or_product_uid: str, secret_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a project secret by name

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

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
            await client.project.delete_project_secret(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                secret_name="secretName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_secret(
            project_or_product_uid, secret_name, request_options=request_options
        )
        return _response.data
