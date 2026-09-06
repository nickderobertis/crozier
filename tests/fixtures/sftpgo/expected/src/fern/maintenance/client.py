

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.admin import Admin
from ..types.api_key import ApiKey
from ..types.api_response import ApiResponse
from ..types.base_virtual_folder import BaseVirtualFolder
from ..types.dump_data_scopes import DumpDataScopes
from ..types.event_action import EventAction
from ..types.event_rule import EventRule
from ..types.group import Group
from ..types.role import Role
from ..types.services_status import ServicesStatus
from ..types.share import Share
from ..types.user import User
from ..types.version_info import VersionInfo
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient
from .types.dumpdata_response import DumpdataResponse


OMIT = typing.cast(typing.Any, ...)


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Returns version details such as the version number, build date, commit hash and enabled features

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.get_version()
        """
        _response = self._raw_client.get_version(request_options=request_options)
        return _response.data

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServicesStatus:
        """
        Retrieves the status of the active services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServicesStatus
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data

    def dumpdata(
        self,
        *,
        output_file: typing.Optional[str] = None,
        output_data: typing.Optional[int] = None,
        indent: typing.Optional[int] = None,
        scopes: typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DumpdataResponse:
        """
        Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata

        Parameters
        ----------
        output_file : typing.Optional[str]
            Path for the file to write the JSON serialized data to. This path is relative to the configured "backups_path". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead.

        output_data : typing.Optional[int]
            output data:
              * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required
              * `1` the backup will be returned as response body

        indent : typing.Optional[int]
            indent:
              * `0` no indentation. This is the default
              * `1` format the output JSON

        scopes : typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]]
            You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DumpdataResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.dumpdata()
        """
        _response = self._raw_client.dumpdata(
            output_file=output_file,
            output_data=output_data,
            indent=indent,
            scopes=scopes,
            request_options=request_options,
        )
        return _response.data

    def loaddata_from_file(
        self,
        *,
        input_file: str,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        input_file : str
            Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured "backups_path". The max allowed file size is 10MB

        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.loaddata_from_file(
            input_file="input-file",
        )
        """
        _response = self._raw_client.loaddata_from_file(
            input_file=input_file, scan_quota=scan_quota, mode=mode, request_options=request_options
        )
        return _response.data

    def loaddata_from_request_body(
        self,
        *,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        users: typing.Optional[typing.Sequence[User]] = OMIT,
        folders: typing.Optional[typing.Sequence[BaseVirtualFolder]] = OMIT,
        groups: typing.Optional[typing.Sequence[Group]] = OMIT,
        admins: typing.Optional[typing.Sequence[Admin]] = OMIT,
        api_keys: typing.Optional[typing.Sequence[ApiKey]] = OMIT,
        shares: typing.Optional[typing.Sequence[Share]] = OMIT,
        event_actions: typing.Optional[typing.Sequence[EventAction]] = OMIT,
        event_rules: typing.Optional[typing.Sequence[EventRule]] = OMIT,
        roles: typing.Optional[typing.Sequence[Role]] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        users : typing.Optional[typing.Sequence[User]]

        folders : typing.Optional[typing.Sequence[BaseVirtualFolder]]

        groups : typing.Optional[typing.Sequence[Group]]

        admins : typing.Optional[typing.Sequence[Admin]]

        api_keys : typing.Optional[typing.Sequence[ApiKey]]

        shares : typing.Optional[typing.Sequence[Share]]

        event_actions : typing.Optional[typing.Sequence[EventAction]]

        event_rules : typing.Optional[typing.Sequence[EventRule]]

        roles : typing.Optional[typing.Sequence[Role]]

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.maintenance.loaddata_from_request_body()
        """
        _response = self._raw_client.loaddata_from_request_body(
            scan_quota=scan_quota,
            mode=mode,
            users=users,
            folders=folders,
            groups=groups,
            admins=admins,
            api_keys=api_keys,
            shares=shares,
            event_actions=event_actions,
            event_rules=event_rules,
            roles=roles,
            version=version,
            request_options=request_options,
        )
        return _response.data


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    async def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Returns version details such as the version number, build date, commit hash and enabled features

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.get_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version(request_options=request_options)
        return _response.data

    async def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServicesStatus:
        """
        Retrieves the status of the active services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServicesStatus
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data

    async def dumpdata(
        self,
        *,
        output_file: typing.Optional[str] = None,
        output_data: typing.Optional[int] = None,
        indent: typing.Optional[int] = None,
        scopes: typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DumpdataResponse:
        """
        Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata

        Parameters
        ----------
        output_file : typing.Optional[str]
            Path for the file to write the JSON serialized data to. This path is relative to the configured "backups_path". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead.

        output_data : typing.Optional[int]
            output data:
              * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required
              * `1` the backup will be returned as response body

        indent : typing.Optional[int]
            indent:
              * `0` no indentation. This is the default
              * `1` format the output JSON

        scopes : typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]]
            You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DumpdataResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.dumpdata()


        asyncio.run(main())
        """
        _response = await self._raw_client.dumpdata(
            output_file=output_file,
            output_data=output_data,
            indent=indent,
            scopes=scopes,
            request_options=request_options,
        )
        return _response.data

    async def loaddata_from_file(
        self,
        *,
        input_file: str,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        input_file : str
            Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured "backups_path". The max allowed file size is 10MB

        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.loaddata_from_file(
                input_file="input-file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.loaddata_from_file(
            input_file=input_file, scan_quota=scan_quota, mode=mode, request_options=request_options
        )
        return _response.data

    async def loaddata_from_request_body(
        self,
        *,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        users: typing.Optional[typing.Sequence[User]] = OMIT,
        folders: typing.Optional[typing.Sequence[BaseVirtualFolder]] = OMIT,
        groups: typing.Optional[typing.Sequence[Group]] = OMIT,
        admins: typing.Optional[typing.Sequence[Admin]] = OMIT,
        api_keys: typing.Optional[typing.Sequence[ApiKey]] = OMIT,
        shares: typing.Optional[typing.Sequence[Share]] = OMIT,
        event_actions: typing.Optional[typing.Sequence[EventAction]] = OMIT,
        event_rules: typing.Optional[typing.Sequence[EventRule]] = OMIT,
        roles: typing.Optional[typing.Sequence[Role]] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        users : typing.Optional[typing.Sequence[User]]

        folders : typing.Optional[typing.Sequence[BaseVirtualFolder]]

        groups : typing.Optional[typing.Sequence[Group]]

        admins : typing.Optional[typing.Sequence[Admin]]

        api_keys : typing.Optional[typing.Sequence[ApiKey]]

        shares : typing.Optional[typing.Sequence[Share]]

        event_actions : typing.Optional[typing.Sequence[EventAction]]

        event_rules : typing.Optional[typing.Sequence[EventRule]]

        roles : typing.Optional[typing.Sequence[Role]]

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.maintenance.loaddata_from_request_body()


        asyncio.run(main())
        """
        _response = await self._raw_client.loaddata_from_request_body(
            scan_quota=scan_quota,
            mode=mode,
            users=users,
            folders=folders,
            groups=groups,
            admins=admins,
            api_keys=api_keys,
            shares=shares,
            event_actions=event_actions,
            event_rules=event_rules,
            roles=roles,
            version=version,
            request_options=request_options,
        )
        return _response.data
