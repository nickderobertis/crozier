

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.background_checks_response import BackgroundChecksResponse
from ..types.basic_customer_data import BasicCustomerData
from ..types.comprehensive_check_response import ComprehensiveCheckResponse
from .raw_client import AsyncRawBackgroundChecksClient, RawBackgroundChecksClient
from .types.background_checks_request_check_types_item import BackgroundChecksRequestCheckTypesItem
from .types.background_checks_request_risk_profile import BackgroundChecksRequestRiskProfile
from .types.comprehensive_check_request_check_types_item import ComprehensiveCheckRequestCheckTypesItem


OMIT = typing.cast(typing.Any, ...)


class BackgroundChecksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBackgroundChecksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBackgroundChecksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBackgroundChecksClient
        """
        return self._raw_client

    def perform_background_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[BackgroundChecksRequestCheckTypesItem],
        customer_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        baseline_date: typing.Optional[dt.datetime] = OMIT,
        risk_profile: typing.Optional[BackgroundChecksRequestRiskProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BackgroundChecksResponse:
        """
        Führt spezifische Background Checks (Sanctions, PEP, etc.) durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[BackgroundChecksRequestCheckTypesItem]

        customer_data : typing.Optional[typing.Dict[str, typing.Any]]

        baseline_date : typing.Optional[dt.datetime]
            Datum für inkrementelle Updates

        risk_profile : typing.Optional[BackgroundChecksRequestRiskProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BackgroundChecksResponse
            Background Checks erfolgreich durchgeführt

        Examples
        --------
        from fern.background_checks import BackgroundChecksRequestCheckTypesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.background_checks.perform_background_checks(
            customer_id="customerId",
            check_types=[BackgroundChecksRequestCheckTypesItem.SANCTIONS],
        )
        """
        _response = self._raw_client.perform_background_checks(
            customer_id=customer_id,
            check_types=check_types,
            customer_data=customer_data,
            baseline_date=baseline_date,
            risk_profile=risk_profile,
            request_options=request_options,
        )
        return _response.data

    def perform_comprehensive_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[ComprehensiveCheckRequestCheckTypesItem],
        customer_data: typing.Optional[BasicCustomerData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComprehensiveCheckResponse:
        """
        Führt KYC, AML, PEP und andere regulatorische Checks durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[ComprehensiveCheckRequestCheckTypesItem]

        customer_data : typing.Optional[BasicCustomerData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComprehensiveCheckResponse
            Checks erfolgreich durchgeführt

        Examples
        --------
        from fern.background_checks import ComprehensiveCheckRequestCheckTypesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.background_checks.perform_comprehensive_checks(
            customer_id="customerId",
            check_types=[ComprehensiveCheckRequestCheckTypesItem.SANCTIONS],
        )
        """
        _response = self._raw_client.perform_comprehensive_checks(
            customer_id=customer_id,
            check_types=check_types,
            customer_data=customer_data,
            request_options=request_options,
        )
        return _response.data


class AsyncBackgroundChecksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBackgroundChecksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBackgroundChecksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBackgroundChecksClient
        """
        return self._raw_client

    async def perform_background_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[BackgroundChecksRequestCheckTypesItem],
        customer_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        baseline_date: typing.Optional[dt.datetime] = OMIT,
        risk_profile: typing.Optional[BackgroundChecksRequestRiskProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BackgroundChecksResponse:
        """
        Führt spezifische Background Checks (Sanctions, PEP, etc.) durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[BackgroundChecksRequestCheckTypesItem]

        customer_data : typing.Optional[typing.Dict[str, typing.Any]]

        baseline_date : typing.Optional[dt.datetime]
            Datum für inkrementelle Updates

        risk_profile : typing.Optional[BackgroundChecksRequestRiskProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BackgroundChecksResponse
            Background Checks erfolgreich durchgeführt

        Examples
        --------
        import asyncio

        from fern.background_checks import BackgroundChecksRequestCheckTypesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.background_checks.perform_background_checks(
                customer_id="customerId",
                check_types=[BackgroundChecksRequestCheckTypesItem.SANCTIONS],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_background_checks(
            customer_id=customer_id,
            check_types=check_types,
            customer_data=customer_data,
            baseline_date=baseline_date,
            risk_profile=risk_profile,
            request_options=request_options,
        )
        return _response.data

    async def perform_comprehensive_checks(
        self,
        *,
        customer_id: str,
        check_types: typing.Sequence[ComprehensiveCheckRequestCheckTypesItem],
        customer_data: typing.Optional[BasicCustomerData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComprehensiveCheckResponse:
        """
        Führt KYC, AML, PEP und andere regulatorische Checks durch

        Parameters
        ----------
        customer_id : str

        check_types : typing.Sequence[ComprehensiveCheckRequestCheckTypesItem]

        customer_data : typing.Optional[BasicCustomerData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComprehensiveCheckResponse
            Checks erfolgreich durchgeführt

        Examples
        --------
        import asyncio

        from fern.background_checks import ComprehensiveCheckRequestCheckTypesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.background_checks.perform_comprehensive_checks(
                customer_id="customerId",
                check_types=[ComprehensiveCheckRequestCheckTypesItem.SANCTIONS],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_comprehensive_checks(
            customer_id=customer_id,
            check_types=check_types,
            customer_data=customer_data,
            request_options=request_options,
        )
        return _response.data
