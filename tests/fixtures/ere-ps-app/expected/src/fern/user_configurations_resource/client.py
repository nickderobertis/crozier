

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserConfigurationsResourceClient, RawUserConfigurationsResourceClient


OMIT = typing.cast(typing.Any, ...)


class UserConfigurationsResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserConfigurationsResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserConfigurationsResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserConfigurationsResourceClient
        """
        return self._raw_client

    def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_configurations_resource.get_config()
        """
        _response = self._raw_client.get_config(request_options=request_options)
        return _response.data

    def put_config(
        self,
        *,
        erixa_hotfolder: typing.Optional[str] = OMIT,
        erixa_drugstore_email: typing.Optional[str] = OMIT,
        erixa_user_email: typing.Optional[str] = OMIT,
        erixa_user_password: typing.Optional[str] = OMIT,
        erixa_api_key: typing.Optional[str] = OMIT,
        extractor_template_profile: typing.Optional[str] = OMIT,
        connector_base_url: typing.Optional[str] = OMIT,
        connector_mandant_id: typing.Optional[str] = OMIT,
        connector_workplace_id: typing.Optional[str] = OMIT,
        connector_client_system_id: typing.Optional[str] = OMIT,
        connector_user_id: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        connector_tv_mode: typing.Optional[str] = OMIT,
        connector_client_certificate: typing.Optional[str] = OMIT,
        connector_client_certificate_password: typing.Optional[str] = OMIT,
        connector_basic_auth_username: typing.Optional[str] = OMIT,
        connector_basic_auth_password: typing.Optional[str] = OMIT,
        kbv_pruefnummer: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        erixa_hotfolder : typing.Optional[str]

        erixa_drugstore_email : typing.Optional[str]

        erixa_user_email : typing.Optional[str]

        erixa_user_password : typing.Optional[str]

        erixa_api_key : typing.Optional[str]

        extractor_template_profile : typing.Optional[str]

        connector_base_url : typing.Optional[str]

        connector_mandant_id : typing.Optional[str]

        connector_workplace_id : typing.Optional[str]

        connector_client_system_id : typing.Optional[str]

        connector_user_id : typing.Optional[str]

        connector_version : typing.Optional[str]

        connector_tv_mode : typing.Optional[str]

        connector_client_certificate : typing.Optional[str]

        connector_client_certificate_password : typing.Optional[str]

        connector_basic_auth_username : typing.Optional[str]

        connector_basic_auth_password : typing.Optional[str]

        kbv_pruefnummer : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_configurations_resource.put_config()
        """
        _response = self._raw_client.put_config(
            erixa_hotfolder=erixa_hotfolder,
            erixa_drugstore_email=erixa_drugstore_email,
            erixa_user_email=erixa_user_email,
            erixa_user_password=erixa_user_password,
            erixa_api_key=erixa_api_key,
            extractor_template_profile=extractor_template_profile,
            connector_base_url=connector_base_url,
            connector_mandant_id=connector_mandant_id,
            connector_workplace_id=connector_workplace_id,
            connector_client_system_id=connector_client_system_id,
            connector_user_id=connector_user_id,
            connector_version=connector_version,
            connector_tv_mode=connector_tv_mode,
            connector_client_certificate=connector_client_certificate,
            connector_client_certificate_password=connector_client_certificate_password,
            connector_basic_auth_username=connector_basic_auth_username,
            connector_basic_auth_password=connector_basic_auth_password,
            kbv_pruefnummer=kbv_pruefnummer,
            request_options=request_options,
        )
        return _response.data


class AsyncUserConfigurationsResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserConfigurationsResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserConfigurationsResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserConfigurationsResourceClient
        """
        return self._raw_client

    async def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_configurations_resource.get_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config(request_options=request_options)
        return _response.data

    async def put_config(
        self,
        *,
        erixa_hotfolder: typing.Optional[str] = OMIT,
        erixa_drugstore_email: typing.Optional[str] = OMIT,
        erixa_user_email: typing.Optional[str] = OMIT,
        erixa_user_password: typing.Optional[str] = OMIT,
        erixa_api_key: typing.Optional[str] = OMIT,
        extractor_template_profile: typing.Optional[str] = OMIT,
        connector_base_url: typing.Optional[str] = OMIT,
        connector_mandant_id: typing.Optional[str] = OMIT,
        connector_workplace_id: typing.Optional[str] = OMIT,
        connector_client_system_id: typing.Optional[str] = OMIT,
        connector_user_id: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        connector_tv_mode: typing.Optional[str] = OMIT,
        connector_client_certificate: typing.Optional[str] = OMIT,
        connector_client_certificate_password: typing.Optional[str] = OMIT,
        connector_basic_auth_username: typing.Optional[str] = OMIT,
        connector_basic_auth_password: typing.Optional[str] = OMIT,
        kbv_pruefnummer: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        erixa_hotfolder : typing.Optional[str]

        erixa_drugstore_email : typing.Optional[str]

        erixa_user_email : typing.Optional[str]

        erixa_user_password : typing.Optional[str]

        erixa_api_key : typing.Optional[str]

        extractor_template_profile : typing.Optional[str]

        connector_base_url : typing.Optional[str]

        connector_mandant_id : typing.Optional[str]

        connector_workplace_id : typing.Optional[str]

        connector_client_system_id : typing.Optional[str]

        connector_user_id : typing.Optional[str]

        connector_version : typing.Optional[str]

        connector_tv_mode : typing.Optional[str]

        connector_client_certificate : typing.Optional[str]

        connector_client_certificate_password : typing.Optional[str]

        connector_basic_auth_username : typing.Optional[str]

        connector_basic_auth_password : typing.Optional[str]

        kbv_pruefnummer : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_configurations_resource.put_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.put_config(
            erixa_hotfolder=erixa_hotfolder,
            erixa_drugstore_email=erixa_drugstore_email,
            erixa_user_email=erixa_user_email,
            erixa_user_password=erixa_user_password,
            erixa_api_key=erixa_api_key,
            extractor_template_profile=extractor_template_profile,
            connector_base_url=connector_base_url,
            connector_mandant_id=connector_mandant_id,
            connector_workplace_id=connector_workplace_id,
            connector_client_system_id=connector_client_system_id,
            connector_user_id=connector_user_id,
            connector_version=connector_version,
            connector_tv_mode=connector_tv_mode,
            connector_client_certificate=connector_client_certificate,
            connector_client_certificate_password=connector_client_certificate_password,
            connector_basic_auth_username=connector_basic_auth_username,
            connector_basic_auth_password=connector_basic_auth_password,
            kbv_pruefnummer=kbv_pruefnummer,
            request_options=request_options,
        )
        return _response.data
