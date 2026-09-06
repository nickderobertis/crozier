

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dealer_db_models_license_activation import DealerDbModelsLicenseActivation
from .raw_client import AsyncRawLicenseactivationsClient, RawLicenseactivationsClient
from .types.dealer_db_models_license_activation_create_license_activation_type import (
    DealerDbModelsLicenseActivationCreateLicenseActivationType,
)


OMIT = typing.cast(typing.Any, ...)


class LicenseactivationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLicenseactivationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLicenseactivationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLicenseactivationsClient
        """
        return self._raw_client

    def post(
        self,
        *,
        dealer_code: str,
        postal_code: str,
        system_info: str,
        voucher_code: str,
        license_activation_type: typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsLicenseActivation:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code of the dealer activating the license

        postal_code : str
            The dealer's postal code (zip code)

        system_info : str
            Information about  the system being activated

        voucher_code : str
            The Voucher Code to use for activation

        license_activation_type : typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType]
            The type of license to create (e.g. EDT, EDT Lite)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicenseActivation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenseactivations.post(
            dealer_code="DealerCode",
            postal_code="PostalCode",
            system_info="SystemInfo",
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.post(
            dealer_code=dealer_code,
            postal_code=postal_code,
            system_info=system_info,
            voucher_code=voucher_code,
            license_activation_type=license_activation_type,
            request_options=request_options,
        )
        return _response.data

    def postregisteredtlite(
        self,
        *,
        expiration_date: dt.datetime,
        instance_id: str,
        voucher_code: str,
        dealer_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        expiration_date : dt.datetime
            The date at which the content of the EDT Lite expires.

        instance_id : str
            The identifier for the EDT Lite.

        voucher_code : str
            The voucher code with which the EDT Lite was created.

        dealer_code : typing.Optional[str]
            The dealer code with which the EDT Lite was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.licenseactivations.postregisteredtlite(
            expiration_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            instance_id="InstanceID",
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.postregisteredtlite(
            expiration_date=expiration_date,
            instance_id=instance_id,
            voucher_code=voucher_code,
            dealer_code=dealer_code,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        id: str,
        *,
        license_version: str,
        system_info: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsLicenseActivation:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license.

        license_version : str
            The license version to update

        system_info : typing.Optional[str]
            Information about  the system being activated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicenseActivation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenseactivations.put(
            id="ID",
            license_version="LicenseVersion",
        )
        """
        _response = self._raw_client.put(
            id, license_version=license_version, system_info=system_info, request_options=request_options
        )
        return _response.data

    def putconfirm(
        self, id: str, *, license_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license

        license_version : str
            The license version to confirm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenseactivations.putconfirm(
            id="ID",
            license_version="LicenseVersion",
        )
        """
        _response = self._raw_client.putconfirm(id, license_version=license_version, request_options=request_options)
        return _response.data


class AsyncLicenseactivationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLicenseactivationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLicenseactivationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLicenseactivationsClient
        """
        return self._raw_client

    async def post(
        self,
        *,
        dealer_code: str,
        postal_code: str,
        system_info: str,
        voucher_code: str,
        license_activation_type: typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsLicenseActivation:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code of the dealer activating the license

        postal_code : str
            The dealer's postal code (zip code)

        system_info : str
            Information about  the system being activated

        voucher_code : str
            The Voucher Code to use for activation

        license_activation_type : typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType]
            The type of license to create (e.g. EDT, EDT Lite)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicenseActivation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenseactivations.post(
                dealer_code="DealerCode",
                postal_code="PostalCode",
                system_info="SystemInfo",
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            dealer_code=dealer_code,
            postal_code=postal_code,
            system_info=system_info,
            voucher_code=voucher_code,
            license_activation_type=license_activation_type,
            request_options=request_options,
        )
        return _response.data

    async def postregisteredtlite(
        self,
        *,
        expiration_date: dt.datetime,
        instance_id: str,
        voucher_code: str,
        dealer_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        expiration_date : dt.datetime
            The date at which the content of the EDT Lite expires.

        instance_id : str
            The identifier for the EDT Lite.

        voucher_code : str
            The voucher code with which the EDT Lite was created.

        dealer_code : typing.Optional[str]
            The dealer code with which the EDT Lite was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenseactivations.postregisteredtlite(
                expiration_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                instance_id="InstanceID",
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postregisteredtlite(
            expiration_date=expiration_date,
            instance_id=instance_id,
            voucher_code=voucher_code,
            dealer_code=dealer_code,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        id: str,
        *,
        license_version: str,
        system_info: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DealerDbModelsLicenseActivation:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license.

        license_version : str
            The license version to update

        system_info : typing.Optional[str]
            Information about  the system being activated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicenseActivation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenseactivations.put(
                id="ID",
                license_version="LicenseVersion",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id, license_version=license_version, system_info=system_info, request_options=request_options
        )
        return _response.data

    async def putconfirm(
        self, id: str, *, license_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license

        license_version : str
            The license version to confirm

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
            await client.licenseactivations.putconfirm(
                id="ID",
                license_version="LicenseVersion",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putconfirm(
            id, license_version=license_version, request_options=request_options
        )
        return _response.data
