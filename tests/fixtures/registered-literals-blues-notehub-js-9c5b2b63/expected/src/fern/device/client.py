

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.device import Device
from ..types.env_tree_json_node import EnvTreeJsonNode
from ..types.environment_variables import EnvironmentVariables
from ..types.notefile_list import NotefileList
from .raw_client import AsyncRawDeviceClient, RawDeviceClient
from .types.get_db_note_response import GetDbNoteResponse
from .types.get_device_environment_variables_by_pin_response import GetDeviceEnvironmentVariablesByPinResponse
from .types.get_device_environment_variables_response import GetDeviceEnvironmentVariablesResponse
from .types.get_device_health_log_request_log_type_item import GetDeviceHealthLogRequestLogTypeItem
from .types.get_device_health_log_response import GetDeviceHealthLogResponse
from .types.get_device_journey_response import GetDeviceJourneyResponse
from .types.get_device_journeys_response import GetDeviceJourneysResponse
from .types.get_device_latest_events_response import GetDeviceLatestEventsResponse
from .types.get_device_plans_response import GetDevicePlansResponse
from .types.get_device_public_key_response import GetDevicePublicKeyResponse
from .types.get_device_public_keys_response import GetDevicePublicKeysResponse
from .types.get_device_sessions_response import GetDeviceSessionsResponse
from .types.get_devices_response import GetDevicesResponse
from .types.get_fleet_devices_response import GetFleetDevicesResponse
from .types.get_notefile_response import GetNotefileResponse
from .types.signal_device_response import SignalDeviceResponse


OMIT = typing.cast(typing.Any, ...)


class DeviceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceClient
        """
        return self._raw_client

    def get_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceEnvironmentVariablesByPinResponse:
        """
        Get environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceEnvironmentVariablesByPinResponse
            The response body from a get device environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_environment_variables_by_pin(
            product_uid="com.blues.bridge:sensors",
            device_uid="dev:000000000000000",
            auth_token="X-Auth-Token",
        )
        """
        _response = self._raw_client.get_device_environment_variables_by_pin(
            product_uid, device_uid, auth_token=auth_token, request_options=request_options
        )
        return _response.data

    def set_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

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
        client.device.set_device_environment_variables_by_pin(
            product_uid="com.blues.bridge:sensors",
            device_uid="dev:000000000000000",
            auth_token="X-Auth-Token",
            environment_variables={"key": "value"},
        )
        """
        _response = self._raw_client.set_device_environment_variables_by_pin(
            product_uid,
            device_uid,
            auth_token=auth_token,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    def get_devices(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDevicesResponse:
        """
        Get Devices of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

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
        GetDevicesResponse
            List of Devices

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_devices(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_devices(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
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

    def get_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Device:
        """
        Get Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device(project_or_product_uid, device_uid, request_options=request_options)
        return _response.data

    def delete_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
        client.device.delete_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.delete_device(project_or_product_uid, device_uid, request_options=request_options)
        return _response.data

    def disable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
        client.device.disable_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.disable_device(project_or_product_uid, device_uid, request_options=request_options)
        return _response.data

    def enable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
        client.device.enable_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.enable_device(project_or_product_uid, device_uid, request_options=request_options)
        return _response.data

    def get_device_environment_hierarchy(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved device environment hierarchy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_environment_hierarchy(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_environment_hierarchy(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def get_device_environment_variables(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceEnvironmentVariablesResponse:
        """
        Get environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceEnvironmentVariablesResponse
            The response body from a get device environment variables request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_environment_variables(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def set_device_environment_variables(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
        client.device.set_device_environment_variables(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            environment_variables={"key": "value"},
        )
        """
        _response = self._raw_client.set_device_environment_variables(
            project_or_product_uid,
            device_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    def delete_device_environment_variable(
        self,
        project_or_product_uid: str,
        device_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Delete environment variable of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
        client.device.delete_device_environment_variable(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            key="key",
        )
        """
        _response = self._raw_client.delete_device_environment_variable(
            project_or_product_uid, device_uid, key, request_options=request_options
        )
        return _response.data

    def list_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotefileList:
        """
        Lists .qi and .db files for the device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more files to obtain change information from.

        pending : typing.Optional[bool]
            show only files that are pending sync to the Notecard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotefileList
            All notefiles and their notes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.list_notefiles(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.list_notefiles(
            project_or_product_uid, device_uid, files=files, pending=pending, request_options=request_options
        )
        return _response.data

    def delete_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes Notefiles and the Notes they contain.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Sequence[str]]
            Name of notefiles to delete

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
        client.device.delete_notefiles(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.delete_notefiles(
            project_or_product_uid, device_uid, files=files, request_options=request_options
        )
        return _response.data

    def get_device_health_log(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        log_type: typing.Optional[
            typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceHealthLogResponse:
        """
        Get Device Health Log

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        log_type : typing.Optional[typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]]
            Return only specified log types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceHealthLogResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_health_log(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_health_log(
            project_or_product_uid,
            device_uid,
            start_date=start_date,
            end_date=end_date,
            log_type=log_type,
            request_options=request_options,
        )
        return _response.data

    def get_device_journeys(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceJourneysResponse:
        """
        Get the list of journeys for a device, derived from events whose body contains `journey` and `jcount` fields. Returns journey metadata only (no event payloads). Capped at 100 most recent journeys; `has_more` is true when the cap is hit.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceJourneysResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_journeys(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_journeys(
            project_or_product_uid,
            device_uid,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    def get_device_journey(
        self,
        project_or_product_uid: str,
        device_uid: str,
        journey_id: int,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceJourneyResponse:
        """
        Get a single journey for a device along with its events. The events array is paginated via `pageSize` / `pageNum`; use `journey.has_more` to detect additional pages.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        journey_id : int
            Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceJourneyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_journey(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            journey_id=1000000,
        )
        """
        _response = self._raw_client.get_device_journey(
            project_or_product_uid,
            device_uid,
            journey_id,
            page_size=page_size,
            page_num=page_num,
            request_options=request_options,
        )
        return _response.data

    def get_device_latest_events(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceLatestEventsResponse:
        """
        Get Device Latest Events

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceLatestEventsResponse
            The response body for a Latest Events request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_latest_events(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_latest_events(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def create_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates an empty Notefile on the device.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

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
        client.device.create_notefile(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
        )
        """
        _response = self._raw_client.create_notefile(
            project_or_product_uid, device_uid, notefile_id, request_options=request_options
        )
        return _response.data

    def get_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        max: typing.Optional[int] = None,
        deleted: typing.Optional[bool] = None,
        delete: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotefileResponse:
        """
        For .qi files, returns the queued up notes.  For .db files, returns all notes in the notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        max : typing.Optional[int]
            The maximum number of Notes to return in the request.

        deleted : typing.Optional[bool]
            true to return deleted notes.

        delete : typing.Optional[bool]
            true to delete the notes returned by the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotefileResponse
            The note changes object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_notefile(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
        )
        """
        _response = self._raw_client.get_notefile(
            project_or_product_uid,
            device_uid,
            notefile_id,
            max=max,
            deleted=deleted,
            delete=delete,
            request_options=request_options,
        )
        return _response.data

    def add_qi_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
        client.device.add_qi_note(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
        )
        """
        _response = self._raw_client.add_qi_note(
            project_or_product_uid, device_uid, notefile_id, body=body, payload=payload, request_options=request_options
        )
        return _response.data

    def get_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        delete: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDbNoteResponse:
        """
        Get a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        delete : typing.Optional[bool]
            Whether to delete the note from the DB notefile

        deleted : typing.Optional[bool]
            Whether to return deleted notes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDbNoteResponse
            The requested note

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_db_note(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
            note_id="noteID",
        )
        """
        _response = self._raw_client.get_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            delete=delete,
            deleted=deleted,
            request_options=request_options,
        )
        return _response.data

    def add_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a Note to a .db notefile.  if noteID is '-' then payload is ignored and empty notefile is created

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
        client.device.add_db_note(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
            note_id="noteID",
        )
        """
        _response = self._raw_client.add_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            body=body,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    def update_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a note in a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
        client.device.update_db_note(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
            note_id="noteID",
        )
        """
        _response = self._raw_client.update_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            body=body,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    def delete_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

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
        client.device.delete_note(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            notefile_id="notefileID",
            note_id="noteID",
        )
        """
        _response = self._raw_client.delete_note(
            project_or_product_uid, device_uid, notefile_id, note_id, request_options=request_options
        )
        return _response.data

    def get_device_plans(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDevicePlansResponse:
        """
        Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePlansResponse
            Response body for /plans

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_plans(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_plans(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def provision_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        product_uid: str,
        device_sn: typing.Optional[str] = OMIT,
        fleet_uids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Provision Device for a Project

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        product_uid : str
            The ProductUID that the device should use.

        device_sn : typing.Optional[str]
            The serial number to assign to the device.

        fleet_uids : typing.Optional[typing.Sequence[str]]
            The fleetUIDs to provision the device to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.provision_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
            product_uid="product_uid",
        )
        """
        _response = self._raw_client.provision_device(
            project_or_product_uid,
            device_uid,
            product_uid=product_uid,
            device_sn=device_sn,
            fleet_uids=fleet_uids,
            request_options=request_options,
        )
        return _response.data

    def get_device_public_key(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDevicePublicKeyResponse:
        """
        Get Device Public Key

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePublicKeyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_public_key(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_public_key(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    def get_device_sessions(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        first_sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceSessionsResponse:
        """
        Get Device Sessions

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        first_sync : typing.Optional[bool]
            When true, filters results to only show first sync sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceSessionsResponse
            The response body for a session request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_sessions(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.get_device_sessions(
            project_or_product_uid,
            device_uid,
            page_size=page_size,
            page_num=page_num,
            start_date=start_date,
            end_date=end_date,
            first_sync=first_sync,
            request_options=request_options,
        )
        return _response.data

    def signal_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalDeviceResponse:
        """
        Send a signal from Notehub to a Notecard.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        body : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalDeviceResponse
            A status response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.signal_device(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            device_uid="dev:000000000000000",
        )
        """
        _response = self._raw_client.signal_device(
            project_or_product_uid, device_uid, body=body, request_options=request_options
        )
        return _response.data

    def get_device_public_keys(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDevicePublicKeysResponse:
        """
        Get Device Public Keys of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePublicKeysResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_device_public_keys(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_device_public_keys(
            project_or_product_uid, page_size=page_size, page_num=page_num, request_options=request_options
        )
        return _response.data

    def get_fleet_devices(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFleetDevicesResponse:
        """
        Get Devices of a Fleet within a Project

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

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
        GetFleetDevicesResponse
            List of Devices

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.device.get_fleet_devices(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
        )
        """
        _response = self._raw_client.get_fleet_devices(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data


class AsyncDeviceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceClient
        """
        return self._raw_client

    async def get_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceEnvironmentVariablesByPinResponse:
        """
        Get environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceEnvironmentVariablesByPinResponse
            The response body from a get device environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_environment_variables_by_pin(
                product_uid="com.blues.bridge:sensors",
                device_uid="dev:000000000000000",
                auth_token="X-Auth-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_environment_variables_by_pin(
            product_uid, device_uid, auth_token=auth_token, request_options=request_options
        )
        return _response.data

    async def set_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

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
            await client.device.set_device_environment_variables_by_pin(
                product_uid="com.blues.bridge:sensors",
                device_uid="dev:000000000000000",
                auth_token="X-Auth-Token",
                environment_variables={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_device_environment_variables_by_pin(
            product_uid,
            device_uid,
            auth_token=auth_token,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    async def get_devices(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDevicesResponse:
        """
        Get Devices of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

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
        GetDevicesResponse
            List of Devices

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_devices(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_devices(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
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

    async def get_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Device:
        """
        Get Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def delete_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            await client.device.delete_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_device(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def disable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            await client.device.disable_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_device(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def enable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            await client.device.enable_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_device(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def get_device_environment_hierarchy(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvTreeJsonNode:
        """
        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvTreeJsonNode
            Successfully retrieved device environment hierarchy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_environment_hierarchy(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_environment_hierarchy(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def get_device_environment_variables(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceEnvironmentVariablesResponse:
        """
        Get environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceEnvironmentVariablesResponse
            The response body from a get device environment variables request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_environment_variables(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def set_device_environment_variables(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Set environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            await client.device.set_device_environment_variables(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                environment_variables={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_device_environment_variables(
            project_or_product_uid,
            device_uid,
            environment_variables=environment_variables,
            environment_variable_notes=environment_variable_notes,
            request_options=request_options,
        )
        return _response.data

    async def delete_device_environment_variable(
        self,
        project_or_product_uid: str,
        device_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentVariables:
        """
        Delete environment variable of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            await client.device.delete_device_environment_variable(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_device_environment_variable(
            project_or_product_uid, device_uid, key, request_options=request_options
        )
        return _response.data

    async def list_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotefileList:
        """
        Lists .qi and .db files for the device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more files to obtain change information from.

        pending : typing.Optional[bool]
            show only files that are pending sync to the Notecard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotefileList
            All notefiles and their notes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.list_notefiles(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notefiles(
            project_or_product_uid, device_uid, files=files, pending=pending, request_options=request_options
        )
        return _response.data

    async def delete_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes Notefiles and the Notes they contain.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Sequence[str]]
            Name of notefiles to delete

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
            await client.device.delete_notefiles(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_notefiles(
            project_or_product_uid, device_uid, files=files, request_options=request_options
        )
        return _response.data

    async def get_device_health_log(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        log_type: typing.Optional[
            typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceHealthLogResponse:
        """
        Get Device Health Log

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        log_type : typing.Optional[typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]]
            Return only specified log types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceHealthLogResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_health_log(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_health_log(
            project_or_product_uid,
            device_uid,
            start_date=start_date,
            end_date=end_date,
            log_type=log_type,
            request_options=request_options,
        )
        return _response.data

    async def get_device_journeys(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceJourneysResponse:
        """
        Get the list of journeys for a device, derived from events whose body contains `journey` and `jcount` fields. Returns journey metadata only (no event payloads). Capped at 100 most recent journeys; `has_more` is true when the cap is hit.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceJourneysResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_journeys(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_journeys(
            project_or_product_uid,
            device_uid,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    async def get_device_journey(
        self,
        project_or_product_uid: str,
        device_uid: str,
        journey_id: int,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceJourneyResponse:
        """
        Get a single journey for a device along with its events. The events array is paginated via `pageSize` / `pageNum`; use `journey.has_more` to detect additional pages.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        journey_id : int
            Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceJourneyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_journey(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                journey_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_journey(
            project_or_product_uid,
            device_uid,
            journey_id,
            page_size=page_size,
            page_num=page_num,
            request_options=request_options,
        )
        return _response.data

    async def get_device_latest_events(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDeviceLatestEventsResponse:
        """
        Get Device Latest Events

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceLatestEventsResponse
            The response body for a Latest Events request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_latest_events(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_latest_events(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def create_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates an empty Notefile on the device.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

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
            await client.device.create_notefile(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notefile(
            project_or_product_uid, device_uid, notefile_id, request_options=request_options
        )
        return _response.data

    async def get_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        max: typing.Optional[int] = None,
        deleted: typing.Optional[bool] = None,
        delete: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotefileResponse:
        """
        For .qi files, returns the queued up notes.  For .db files, returns all notes in the notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        max : typing.Optional[int]
            The maximum number of Notes to return in the request.

        deleted : typing.Optional[bool]
            true to return deleted notes.

        delete : typing.Optional[bool]
            true to delete the notes returned by the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotefileResponse
            The note changes object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_notefile(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notefile(
            project_or_product_uid,
            device_uid,
            notefile_id,
            max=max,
            deleted=deleted,
            delete=delete,
            request_options=request_options,
        )
        return _response.data

    async def add_qi_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
            await client.device.add_qi_note(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_qi_note(
            project_or_product_uid, device_uid, notefile_id, body=body, payload=payload, request_options=request_options
        )
        return _response.data

    async def get_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        delete: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDbNoteResponse:
        """
        Get a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        delete : typing.Optional[bool]
            Whether to delete the note from the DB notefile

        deleted : typing.Optional[bool]
            Whether to return deleted notes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDbNoteResponse
            The requested note

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_db_note(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
                note_id="noteID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            delete=delete,
            deleted=deleted,
            request_options=request_options,
        )
        return _response.data

    async def add_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add a Note to a .db notefile.  if noteID is '-' then payload is ignored and empty notefile is created

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
            await client.device.add_db_note(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
                note_id="noteID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            body=body,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    async def update_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a note in a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

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
            await client.device.update_db_note(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
                note_id="noteID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_db_note(
            project_or_product_uid,
            device_uid,
            notefile_id,
            note_id,
            body=body,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    async def delete_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

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
            await client.device.delete_note(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                notefile_id="notefileID",
                note_id="noteID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_note(
            project_or_product_uid, device_uid, notefile_id, note_id, request_options=request_options
        )
        return _response.data

    async def get_device_plans(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDevicePlansResponse:
        """
        Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePlansResponse
            Response body for /plans

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_plans(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_plans(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def provision_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        product_uid: str,
        device_sn: typing.Optional[str] = OMIT,
        fleet_uids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Provision Device for a Project

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        product_uid : str
            The ProductUID that the device should use.

        device_sn : typing.Optional[str]
            The serial number to assign to the device.

        fleet_uids : typing.Optional[typing.Sequence[str]]
            The fleetUIDs to provision the device to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.provision_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
                product_uid="product_uid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provision_device(
            project_or_product_uid,
            device_uid,
            product_uid=product_uid,
            device_sn=device_sn,
            fleet_uids=fleet_uids,
            request_options=request_options,
        )
        return _response.data

    async def get_device_public_key(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDevicePublicKeyResponse:
        """
        Get Device Public Key

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePublicKeyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_public_key(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_public_key(
            project_or_product_uid, device_uid, request_options=request_options
        )
        return _response.data

    async def get_device_sessions(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        first_sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDeviceSessionsResponse:
        """
        Get Device Sessions

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        first_sync : typing.Optional[bool]
            When true, filters results to only show first sync sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDeviceSessionsResponse
            The response body for a session request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_sessions(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_sessions(
            project_or_product_uid,
            device_uid,
            page_size=page_size,
            page_num=page_num,
            start_date=start_date,
            end_date=end_date,
            first_sync=first_sync,
            request_options=request_options,
        )
        return _response.data

    async def signal_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalDeviceResponse:
        """
        Send a signal from Notehub to a Notecard.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        body : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalDeviceResponse
            A status response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.signal_device(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                device_uid="dev:000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signal_device(
            project_or_product_uid, device_uid, body=body, request_options=request_options
        )
        return _response.data

    async def get_device_public_keys(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDevicePublicKeysResponse:
        """
        Get Device Public Keys of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDevicePublicKeysResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_device_public_keys(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_public_keys(
            project_or_product_uid, page_size=page_size, page_num=page_num, request_options=request_options
        )
        return _response.data

    async def get_fleet_devices(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFleetDevicesResponse:
        """
        Get Devices of a Fleet within a Project

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

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
        GetFleetDevicesResponse
            List of Devices

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.device.get_fleet_devices(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_devices(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            tag=tag,
            serial_number=serial_number,
            notecard_firmware=notecard_firmware,
            location=location,
            host_firmware=host_firmware,
            product_uid=product_uid,
            sku=sku,
            request_options=request_options,
        )
        return _response.data
