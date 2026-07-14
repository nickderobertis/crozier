

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.configuration_property import ConfigurationProperty
from ..types.log_level import LogLevel
from ..types.named_log_configuration import NamedLogConfiguration
from ..types.role_mapping import RoleMapping
from ..types.role_type import RoleType
from .raw_client import AsyncRawAdminClient, RawAdminClient


OMIT = typing.cast(typing.Any, ...)


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def list_config_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConfigurationProperty]:
        """
        Returns a list of all configuration properties that have been set.  The list is not paged.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConfigurationProperty]
            On a successful response, returns a list of configuration properties.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.list_config_properties()
        """
        _response = self._raw_client.list_config_properties(request_options=request_options)
        return _response.data

    def get_config_property(
        self, property_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigurationProperty:
        """
        Returns the value of a single configuration property.

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigurationProperty
            The configuration property value.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.get_config_property(
            property_name="propertyName",
        )
        """
        _response = self._raw_client.get_config_property(property_name, request_options=request_options)
        return _response.data

    def update_config_property(
        self, property_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the value of a single configuration property.

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.update_config_property(
            property_name="propertyName",
            value="true",
        )
        """
        _response = self._raw_client.update_config_property(property_name, value=value, request_options=request_options)
        return _response.data

    def reset_config_property(
        self, property_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Resets the value of a single configuration property.  This will return the property to
        its default value (see external documentation for supported properties and their default
        values).

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.reset_config_property(
            property_name="propertyName",
        )
        """
        _response = self._raw_client.reset_config_property(property_name, request_options=request_options)
        return _response.data

    def export_data(
        self, *, for_browser: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Exports registry data as a ZIP archive.

        Parameters
        ----------
        for_browser : typing.Optional[bool]
            Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called `href`.  This `href` will be a single-use, naked download link suitable for use by a web browser to download the content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Response when the export is successful.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.export_data()
        """
        with self._raw_client.export_data(for_browser=for_browser, request_options=request_options) as r:
            yield from r.data

    def import_data(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports registry data that was previously exported using the `/admin/export` operation.

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.import_data(request=request, request_options=request_options)
        return _response.data

    def list_log_configurations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NamedLogConfiguration]:
        """
        List all of the configured logging levels.  These override the default
        logging configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NamedLogConfiguration]
            The list of logging configurations.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.list_log_configurations()
        """
        _response = self._raw_client.list_log_configurations(request_options=request_options)
        return _response.data

    def get_log_configuration(
        self, logger: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The logger configuration for the named logger.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.get_log_configuration(
            logger="logger",
        )
        """
        _response = self._raw_client.get_log_configuration(logger, request_options=request_options)
        return _response.data

    def set_log_configuration(
        self, logger: str, *, level: LogLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Configures the logger referenced by the provided logger name with the given configuration.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        level : LogLevel


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The new configuration for the given logger.

        Examples
        --------
        from fern import FernApi, LogLevel

        client = FernApi()
        client.admin.set_log_configuration(
            logger="logger",
            level=LogLevel.DEBUG,
        )
        """
        _response = self._raw_client.set_log_configuration(logger, level=level, request_options=request_options)
        return _response.data

    def remove_log_configuration(
        self, logger: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Removes the configured logger configuration (if any) for the given logger.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The default logger configuration (now that the configuration for this logger has been removed, the
            default configuration is applied).

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.remove_log_configuration(
            logger="logger",
        )
        """
        _response = self._raw_client.remove_log_configuration(logger, request_options=request_options)
        return _response.data

    def list_role_mappings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoleMapping]:
        """
        Gets a list of all role mappings configured in the registry (if any).

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoleMapping]
            A successful response will return the list of role mappings.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.list_role_mappings()
        """
        _response = self._raw_client.list_role_mappings(request_options=request_options)
        return _response.data

    def create_role_mapping(
        self,
        *,
        principal_id: str,
        role: RoleType,
        principal_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new mapping between a user/principal and a role.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str


        role : RoleType


        principal_name : typing.Optional[str]
            A friendly name for the principal.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, RoleType

        client = FernApi()
        client.admin.create_role_mapping(
            principal_id="svc_account_84874587_123484",
            principal_name="famartin-svc-account",
            role=RoleType.READ_ONLY,
        )
        """
        _response = self._raw_client.create_role_mapping(
            principal_id=principal_id, role=role, principal_name=principal_name, request_options=request_options
        )
        return _response.data

    def get_role_mapping(
        self, principal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RoleMapping:
        """
        Gets the details of a single role mapping (by `principalId`).

        This operation can fail for the following reasons:

        * No role mapping for the `principalId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoleMapping
            When successful, returns the details of a role mapping.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.get_role_mapping(
            principal_id="principalId",
        )
        """
        _response = self._raw_client.get_role_mapping(principal_id, request_options=request_options)
        return _response.data

    def update_role_mapping(
        self, principal_id: str, *, role: RoleType, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a single role mapping for one user/principal.

        This operation can fail for the following reasons:

        * No role mapping for the principalId exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        role : RoleType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, RoleType

        client = FernApi()
        client.admin.update_role_mapping(
            principal_id="principalId",
            role=RoleType.READ_ONLY,
        )
        """
        _response = self._raw_client.update_role_mapping(principal_id, role=role, request_options=request_options)
        return _response.data

    def delete_role_mapping(
        self, principal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a single role mapping, effectively denying access to a user/principal.

        This operation can fail for the following reasons:

        * No role mapping for the principalId exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.delete_role_mapping(
            principal_id="principalId",
        )
        """
        _response = self._raw_client.delete_role_mapping(principal_id, request_options=request_options)
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def list_config_properties(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConfigurationProperty]:
        """
        Returns a list of all configuration properties that have been set.  The list is not paged.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConfigurationProperty]
            On a successful response, returns a list of configuration properties.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.list_config_properties()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_config_properties(request_options=request_options)
        return _response.data

    async def get_config_property(
        self, property_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigurationProperty:
        """
        Returns the value of a single configuration property.

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigurationProperty
            The configuration property value.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.get_config_property(
                property_name="propertyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config_property(property_name, request_options=request_options)
        return _response.data

    async def update_config_property(
        self, property_name: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the value of a single configuration property.

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.update_config_property(
                property_name="propertyName",
                value="true",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_config_property(
            property_name, value=value, request_options=request_options
        )
        return _response.data

    async def reset_config_property(
        self, property_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Resets the value of a single configuration property.  This will return the property to
        its default value (see external documentation for supported properties and their default
        values).

        This operation may fail for one of the following reasons:

        * Property not found or not configured (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        property_name : str
            The name of a configuration property.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.reset_config_property(
                property_name="propertyName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_config_property(property_name, request_options=request_options)
        return _response.data

    async def export_data(
        self, *, for_browser: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Exports registry data as a ZIP archive.

        Parameters
        ----------
        for_browser : typing.Optional[bool]
            Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called `href`.  This `href` will be a single-use, naked download link suitable for use by a web browser to download the content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Response when the export is successful.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.export_data()


        asyncio.run(main())
        """
        async with self._raw_client.export_data(for_browser=for_browser, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def import_data(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports registry data that was previously exported using the `/admin/export` operation.

        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.import_data(request=request, request_options=request_options)
        return _response.data

    async def list_log_configurations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NamedLogConfiguration]:
        """
        List all of the configured logging levels.  These override the default
        logging configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NamedLogConfiguration]
            The list of logging configurations.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.list_log_configurations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_log_configurations(request_options=request_options)
        return _response.data

    async def get_log_configuration(
        self, logger: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The logger configuration for the named logger.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.get_log_configuration(
                logger="logger",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_configuration(logger, request_options=request_options)
        return _response.data

    async def set_log_configuration(
        self, logger: str, *, level: LogLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Configures the logger referenced by the provided logger name with the given configuration.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        level : LogLevel


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The new configuration for the given logger.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LogLevel

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.set_log_configuration(
                logger="logger",
                level=LogLevel.DEBUG,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_log_configuration(logger, level=level, request_options=request_options)
        return _response.data

    async def remove_log_configuration(
        self, logger: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedLogConfiguration:
        """
        Removes the configured logger configuration (if any) for the given logger.

        Parameters
        ----------
        logger : str
            The name of a single logger.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedLogConfiguration
            The default logger configuration (now that the configuration for this logger has been removed, the
            default configuration is applied).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.remove_log_configuration(
                logger="logger",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_log_configuration(logger, request_options=request_options)
        return _response.data

    async def list_role_mappings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoleMapping]:
        """
        Gets a list of all role mappings configured in the registry (if any).

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoleMapping]
            A successful response will return the list of role mappings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.list_role_mappings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_role_mappings(request_options=request_options)
        return _response.data

    async def create_role_mapping(
        self,
        *,
        principal_id: str,
        role: RoleType,
        principal_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new mapping between a user/principal and a role.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str


        role : RoleType


        principal_name : typing.Optional[str]
            A friendly name for the principal.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RoleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.create_role_mapping(
                principal_id="svc_account_84874587_123484",
                principal_name="famartin-svc-account",
                role=RoleType.READ_ONLY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_role_mapping(
            principal_id=principal_id, role=role, principal_name=principal_name, request_options=request_options
        )
        return _response.data

    async def get_role_mapping(
        self, principal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RoleMapping:
        """
        Gets the details of a single role mapping (by `principalId`).

        This operation can fail for the following reasons:

        * No role mapping for the `principalId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoleMapping
            When successful, returns the details of a role mapping.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.get_role_mapping(
                principal_id="principalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_role_mapping(principal_id, request_options=request_options)
        return _response.data

    async def update_role_mapping(
        self, principal_id: str, *, role: RoleType, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a single role mapping for one user/principal.

        This operation can fail for the following reasons:

        * No role mapping for the principalId exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        role : RoleType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RoleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.update_role_mapping(
                principal_id="principalId",
                role=RoleType.READ_ONLY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_role_mapping(principal_id, role=role, request_options=request_options)
        return _response.data

    async def delete_role_mapping(
        self, principal_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a single role mapping, effectively denying access to a user/principal.

        This operation can fail for the following reasons:

        * No role mapping for the principalId exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        principal_id : str
            Unique id of a principal (typically either a user or service account).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.delete_role_mapping(
                principal_id="principalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_role_mapping(principal_id, request_options=request_options)
        return _response.data
