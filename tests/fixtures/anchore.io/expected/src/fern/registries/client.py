

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.registry_configuration_list import RegistryConfigurationList
from .raw_client import AsyncRawRegistriesClient, RawRegistriesClient


OMIT = typing.cast(typing.Any, ...)


class RegistriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRegistriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRegistriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRegistriesClient
        """
        return self._raw_client

    def list_registries(
        self, *, anchore_account: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistryConfigurationList:
        """
        List all configured registries the system can/will watch

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Registry listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registries.list_registries()
        """
        _response = self._raw_client.list_registries(anchore_account=anchore_account, request_options=request_options)
        return _response.data

    def create_registry(
        self,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Adds a new registry to the system

        Parameters
        ----------
        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry add time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Saved registry configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registries.create_registry()
        """
        _response = self._raw_client.create_registry(
            validate=validate,
            anchore_account=anchore_account,
            registry=registry,
            registry_name=registry_name,
            registry_pass=registry_pass,
            registry_type=registry_type,
            registry_user=registry_user,
            registry_verify=registry_verify,
            request_options=request_options,
        )
        return _response.data

    def get_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Get information on a specific registry

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Registry configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registries.get_registry(
            registry="registry",
        )
        """
        _response = self._raw_client.get_registry(
            registry, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def update_registry(
        self,
        registry_: str,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Replaces an existing registry record with the given record

        Parameters
        ----------
        registry_ : str

        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry update time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Updated registry configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registries.update_registry(
            registry_="registry",
        )
        """
        _response = self._raw_client.update_registry(
            registry_,
            validate=validate,
            anchore_account=anchore_account,
            registry=registry,
            registry_name=registry_name,
            registry_pass=registry_pass,
            registry_type=registry_type,
            registry_user=registry_user,
            registry_verify=registry_verify,
            request_options=request_options,
        )
        return _response.data

    def delete_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a registry configuration record from the system. Does not remove any images.

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.registries.delete_registry(
            registry="registry",
        )
        """
        _response = self._raw_client.delete_registry(
            registry, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data


class AsyncRegistriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRegistriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRegistriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRegistriesClient
        """
        return self._raw_client

    async def list_registries(
        self, *, anchore_account: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RegistryConfigurationList:
        """
        List all configured registries the system can/will watch

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Registry listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registries.list_registries()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_registries(
            anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def create_registry(
        self,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Adds a new registry to the system

        Parameters
        ----------
        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry add time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Saved registry configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registries.create_registry()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_registry(
            validate=validate,
            anchore_account=anchore_account,
            registry=registry,
            registry_name=registry_name,
            registry_pass=registry_pass,
            registry_type=registry_type,
            registry_user=registry_user,
            registry_verify=registry_verify,
            request_options=request_options,
        )
        return _response.data

    async def get_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Get information on a specific registry

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Registry configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registries.get_registry(
                registry="registry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_registry(
            registry, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def update_registry(
        self,
        registry_: str,
        *,
        validate: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        registry: typing.Optional[str] = OMIT,
        registry_name: typing.Optional[str] = OMIT,
        registry_pass: typing.Optional[str] = OMIT,
        registry_type: typing.Optional[str] = OMIT,
        registry_user: typing.Optional[str] = OMIT,
        registry_verify: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegistryConfigurationList:
        """
        Replaces an existing registry record with the given record

        Parameters
        ----------
        registry_ : str

        validate : typing.Optional[bool]
            flag to determine whether or not to validate registry/credential at registry update time

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        registry : typing.Optional[str]
            hostname:port string for accessing the registry, as would be used in a docker pull operation. May include some or all of a repository and wildcards (e.g. docker.io/library/* or gcr.io/myproject/myrepository)

        registry_name : typing.Optional[str]
            human readable name associated with registry record

        registry_pass : typing.Optional[str]
            Password portion of credential to use for this registry

        registry_type : typing.Optional[str]
            Type of registry

        registry_user : typing.Optional[str]
            Username portion of credential to use for this registry

        registry_verify : typing.Optional[bool]
            Use TLS/SSL verification for the registry URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegistryConfigurationList
            Updated registry configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.registries.update_registry(
                registry_="registry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_registry(
            registry_,
            validate=validate,
            anchore_account=anchore_account,
            registry=registry,
            registry_name=registry_name,
            registry_pass=registry_pass,
            registry_type=registry_type,
            registry_user=registry_user,
            registry_verify=registry_verify,
            request_options=request_options,
        )
        return _response.data

    async def delete_registry(
        self,
        registry: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a registry configuration record from the system. Does not remove any images.

        Parameters
        ----------
        registry : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

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
            await client.registries.delete_registry(
                registry="registry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_registry(
            registry, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data
