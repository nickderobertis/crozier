

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_tax_rate_response import CreateTaxRateResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_tax_rate_response import DeleteTaxRateResponse
from ..types.get_tax_rate_response import GetTaxRateResponse
from ..types.get_tax_rates_response import GetTaxRatesResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.row_version import RowVersion
from ..types.tax_rate_components_item import TaxRateComponentsItem
from ..types.tax_rate_status import TaxRateStatus
from ..types.tax_rates_filter import TaxRatesFilter
from ..types.update_tax_rate_response import UpdateTaxRateResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawTaxRatesClient, RawTaxRatesClient


OMIT = typing.cast(typing.Any, ...)


class TaxRatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaxRatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaxRatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaxRatesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[TaxRatesFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTaxRatesResponse:
        """
        List Tax Rates. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Connectors Affected: Quickbooks

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[TaxRatesFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTaxRatesResponse
            TaxRates

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        code: typing.Optional[str] = OMIT,
        components: typing.Optional[typing.Sequence[TaxRateComponentsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        effective_tax_rate: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        original_tax_rate_id: typing.Optional[str] = OMIT,
        report_tax_type: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[TaxRateStatus] = OMIT,
        tax_payable_account_id: typing.Optional[str] = OMIT,
        tax_remitted_account_id: typing.Optional[str] = OMIT,
        total_tax_rate: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTaxRateResponse:
        """
        Create Tax Rate

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        code : typing.Optional[str]
            Tax code assigned to identify this tax rate.

        components : typing.Optional[typing.Sequence[TaxRateComponentsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of tax rate

        effective_tax_rate : typing.Optional[float]
            Effective tax rate

        id : typing.Optional[str]
            ID assigned to identify this tax rate.

        name : typing.Optional[str]
            Name assigned to identify this tax rate.

        original_tax_rate_id : typing.Optional[str]
            ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.

        report_tax_type : typing.Optional[str]
            Report Tax type to aggregate tax collected or paid for reporting purposes

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[TaxRateStatus]
            Tax rate status

        tax_payable_account_id : typing.Optional[str]
            Unique identifier for the account for tax collected.

        tax_remitted_account_id : typing.Optional[str]
            Unique identifier for the account for tax remitted.

        total_tax_rate : typing.Optional[float]
            Not compounded sum of the components of a tax rate

        type : typing.Optional[str]
            Tax type used to indicate the source of tax collected or paid

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTaxRateResponse
            TaxRate created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            code=code,
            components=components,
            created_at=created_at,
            created_by=created_by,
            description=description,
            effective_tax_rate=effective_tax_rate,
            id=id,
            name=name,
            original_tax_rate_id=original_tax_rate_id,
            report_tax_type=report_tax_type,
            row_version=row_version,
            status=status,
            tax_payable_account_id=tax_payable_account_id,
            tax_remitted_account_id=tax_remitted_account_id,
            total_tax_rate=total_tax_rate,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTaxRateResponse:
        """
        Get Tax Rate. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Support will soon be added to return the actual rate/percentage by doing additional calls in the background to provide the full view of a given tax rate. Connectors Affected: Quickbooks

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTaxRateResponse
            TaxRate

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTaxRateResponse:
        """
        Delete Tax Rate

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTaxRateResponse
            TaxRates deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        code: typing.Optional[str] = OMIT,
        components: typing.Optional[typing.Sequence[TaxRateComponentsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        effective_tax_rate: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        original_tax_rate_id: typing.Optional[str] = OMIT,
        report_tax_type: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[TaxRateStatus] = OMIT,
        tax_payable_account_id: typing.Optional[str] = OMIT,
        tax_remitted_account_id: typing.Optional[str] = OMIT,
        total_tax_rate: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTaxRateResponse:
        """
        Update Tax Rate

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        code : typing.Optional[str]
            Tax code assigned to identify this tax rate.

        components : typing.Optional[typing.Sequence[TaxRateComponentsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of tax rate

        effective_tax_rate : typing.Optional[float]
            Effective tax rate

        id : typing.Optional[str]
            ID assigned to identify this tax rate.

        name : typing.Optional[str]
            Name assigned to identify this tax rate.

        original_tax_rate_id : typing.Optional[str]
            ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.

        report_tax_type : typing.Optional[str]
            Report Tax type to aggregate tax collected or paid for reporting purposes

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[TaxRateStatus]
            Tax rate status

        tax_payable_account_id : typing.Optional[str]
            Unique identifier for the account for tax collected.

        tax_remitted_account_id : typing.Optional[str]
            Unique identifier for the account for tax remitted.

        total_tax_rate : typing.Optional[float]
            Not compounded sum of the components of a tax rate

        type : typing.Optional[str]
            Tax type used to indicate the source of tax collected or paid

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTaxRateResponse
            TaxRate updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tax_rates.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            code=code,
            components=components,
            created_at=created_at,
            created_by=created_by,
            description=description,
            effective_tax_rate=effective_tax_rate,
            id=id,
            name=name,
            original_tax_rate_id=original_tax_rate_id,
            report_tax_type=report_tax_type,
            row_version=row_version,
            status=status,
            tax_payable_account_id=tax_payable_account_id,
            tax_remitted_account_id=tax_remitted_account_id,
            total_tax_rate=total_tax_rate,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncTaxRatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaxRatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaxRatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaxRatesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[TaxRatesFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTaxRatesResponse:
        """
        List Tax Rates. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Connectors Affected: Quickbooks

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[TaxRatesFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTaxRatesResponse
            TaxRates

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        code: typing.Optional[str] = OMIT,
        components: typing.Optional[typing.Sequence[TaxRateComponentsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        effective_tax_rate: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        original_tax_rate_id: typing.Optional[str] = OMIT,
        report_tax_type: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[TaxRateStatus] = OMIT,
        tax_payable_account_id: typing.Optional[str] = OMIT,
        tax_remitted_account_id: typing.Optional[str] = OMIT,
        total_tax_rate: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTaxRateResponse:
        """
        Create Tax Rate

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        code : typing.Optional[str]
            Tax code assigned to identify this tax rate.

        components : typing.Optional[typing.Sequence[TaxRateComponentsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of tax rate

        effective_tax_rate : typing.Optional[float]
            Effective tax rate

        id : typing.Optional[str]
            ID assigned to identify this tax rate.

        name : typing.Optional[str]
            Name assigned to identify this tax rate.

        original_tax_rate_id : typing.Optional[str]
            ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.

        report_tax_type : typing.Optional[str]
            Report Tax type to aggregate tax collected or paid for reporting purposes

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[TaxRateStatus]
            Tax rate status

        tax_payable_account_id : typing.Optional[str]
            Unique identifier for the account for tax collected.

        tax_remitted_account_id : typing.Optional[str]
            Unique identifier for the account for tax remitted.

        total_tax_rate : typing.Optional[float]
            Not compounded sum of the components of a tax rate

        type : typing.Optional[str]
            Tax type used to indicate the source of tax collected or paid

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTaxRateResponse
            TaxRate created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            code=code,
            components=components,
            created_at=created_at,
            created_by=created_by,
            description=description,
            effective_tax_rate=effective_tax_rate,
            id=id,
            name=name,
            original_tax_rate_id=original_tax_rate_id,
            report_tax_type=report_tax_type,
            row_version=row_version,
            status=status,
            tax_payable_account_id=tax_payable_account_id,
            tax_remitted_account_id=tax_remitted_account_id,
            total_tax_rate=total_tax_rate,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTaxRateResponse:
        """
        Get Tax Rate. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Support will soon be added to return the actual rate/percentage by doing additional calls in the background to provide the full view of a given tax rate. Connectors Affected: Quickbooks

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTaxRateResponse
            TaxRate

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTaxRateResponse:
        """
        Delete Tax Rate

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTaxRateResponse
            TaxRates deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        code: typing.Optional[str] = OMIT,
        components: typing.Optional[typing.Sequence[TaxRateComponentsItem]] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        effective_tax_rate: typing.Optional[float] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        original_tax_rate_id: typing.Optional[str] = OMIT,
        report_tax_type: typing.Optional[str] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[TaxRateStatus] = OMIT,
        tax_payable_account_id: typing.Optional[str] = OMIT,
        tax_remitted_account_id: typing.Optional[str] = OMIT,
        total_tax_rate: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTaxRateResponse:
        """
        Update Tax Rate

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        code : typing.Optional[str]
            Tax code assigned to identify this tax rate.

        components : typing.Optional[typing.Sequence[TaxRateComponentsItem]]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            Description of tax rate

        effective_tax_rate : typing.Optional[float]
            Effective tax rate

        id : typing.Optional[str]
            ID assigned to identify this tax rate.

        name : typing.Optional[str]
            Name assigned to identify this tax rate.

        original_tax_rate_id : typing.Optional[str]
            ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.

        report_tax_type : typing.Optional[str]
            Report Tax type to aggregate tax collected or paid for reporting purposes

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[TaxRateStatus]
            Tax rate status

        tax_payable_account_id : typing.Optional[str]
            Unique identifier for the account for tax collected.

        tax_remitted_account_id : typing.Optional[str]
            Unique identifier for the account for tax remitted.

        total_tax_rate : typing.Optional[float]
            Not compounded sum of the components of a tax rate

        type : typing.Optional[str]
            Tax type used to indicate the source of tax collected or paid

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTaxRateResponse
            TaxRate updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tax_rates.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            code=code,
            components=components,
            created_at=created_at,
            created_by=created_by,
            description=description,
            effective_tax_rate=effective_tax_rate,
            id=id,
            name=name,
            original_tax_rate_id=original_tax_rate_id,
            report_tax_type=report_tax_type,
            row_version=row_version,
            status=status,
            tax_payable_account_id=tax_payable_account_id,
            tax_remitted_account_id=tax_remitted_account_id,
            total_tax_rate=total_tax_rate,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
