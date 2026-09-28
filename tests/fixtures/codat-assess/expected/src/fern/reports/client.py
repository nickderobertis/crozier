

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.enhanced_cash_flow_transactions import EnhancedCashFlowTransactions
from ..types.enhanced_invoices_report import EnhancedInvoicesReport
from ..types.enhanced_report import EnhancedReport
from ..types.financial_metrics import FinancialMetrics
from ..types.report import Report
from .raw_client import AsyncRawReportsClient, RawReportsClient
from .types.get_commerce_customer_retention_metrics_request_period_unit import (
    GetCommerceCustomerRetentionMetricsRequestPeriodUnit,
)
from .types.get_commerce_lifetime_value_metrics_request_period_unit import (
    GetCommerceLifetimeValueMetricsRequestPeriodUnit,
)
from .types.get_commerce_orders_metrics_request_period_unit import GetCommerceOrdersMetricsRequestPeriodUnit
from .types.get_commerce_refunds_metrics_request_period_unit import GetCommerceRefundsMetricsRequestPeriodUnit
from .types.get_commerce_revenue_metrics_request_period_unit import GetCommerceRevenueMetricsRequestPeriodUnit


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def get_accounts_for_enhanced_balance_sheet(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedReport:
        """
        The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

        Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

        Parameters
        ----------
        company_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedReport
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_accounts_for_enhanced_balance_sheet(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            report_date="29-09-2020",
            number_of_periods=1,
        )
        """
        _response = self._raw_client.get_accounts_for_enhanced_balance_sheet(
            company_id, report_date=report_date, number_of_periods=number_of_periods, request_options=request_options
        )
        return _response.data

    def get_enhanced_cash_flow_transactions(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedCashFlowTransactions:
        """
        The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

        Parameters
        ----------
        company_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedCashFlowTransactions
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_enhanced_cash_flow_transactions(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            page=1,
            page_size=100,
        )
        """
        _response = self._raw_client.get_enhanced_cash_flow_transactions(
            company_id, page=page, page_size=page_size, query=query, request_options=request_options
        )
        return _response.data

    def get_enhanced_invoices_report(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedInvoicesReport:
        """
        Gets a list of invoices linked to the corresponding banking transaction

        Parameters
        ----------
        company_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedInvoicesReport
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_enhanced_invoices_report(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            page=1,
            page_size=100,
        )
        """
        _response = self._raw_client.get_enhanced_invoices_report(
            company_id, page=page, page_size=page_size, query=query, request_options=request_options
        )
        return _response.data

    def get_accounts_for_enhanced_profit_and_loss(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedReport:
        """
        The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

        Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

        Parameters
        ----------
        company_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedReport
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_accounts_for_enhanced_profit_and_loss(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            report_date="29-09-2020",
            number_of_periods=1,
        )
        """
        _response = self._raw_client.get_accounts_for_enhanced_profit_and_loss(
            company_id, report_date=report_date, number_of_periods=number_of_periods, request_options=request_options
        )
        return _response.data

    def get_commerce_customer_retention_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceCustomerRetentionMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the customer retention metrics for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceCustomerRetentionMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.reports import GetCommerceCustomerRetentionMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_commerce_customer_retention_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetCommerceCustomerRetentionMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_commerce_customer_retention_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_commerce_lifetime_value_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceLifetimeValueMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the lifetime value metric for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceLifetimeValueMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.reports import GetCommerceLifetimeValueMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_commerce_lifetime_value_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetCommerceLifetimeValueMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_commerce_lifetime_value_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_commerce_orders_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceOrdersMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the order information for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceOrdersMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.reports import GetCommerceOrdersMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_commerce_orders_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetCommerceOrdersMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_commerce_orders_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_commerce_refunds_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceRefundsMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the refunds information for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceRefundsMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.reports import GetCommerceRefundsMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_commerce_refunds_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetCommerceRefundsMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_commerce_refunds_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_commerce_revenue_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceRevenueMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Get the revenue and revenue growth for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceRevenueMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.reports import GetCommerceRevenueMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_commerce_revenue_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetCommerceRevenueMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_commerce_revenue_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_enhanced_balance_sheet(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets a fully categorized balance sheet statement for a given company, over one or more period(s).

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_enhanced_balance_sheet(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
        )
        """
        _response = self._raw_client.get_enhanced_balance_sheet(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_enhanced_profit_and_loss(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_enhanced_profit_and_loss(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
        )
        """
        _response = self._raw_client.get_enhanced_profit_and_loss(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    def get_enhanced_financial_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        show_metric_inputs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancialMetrics:
        """
        Gets all the available financial metrics for a given company, over one or more periods.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        show_metric_inputs : typing.Optional[bool]
            If set to true, then the system includes the input values within the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancialMetrics
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_enhanced_financial_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
        )
        """
        _response = self._raw_client.get_enhanced_financial_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            show_metric_inputs=show_metric_inputs,
            request_options=request_options,
        )
        return _response.data

    def get_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Report:
        """
        Gets key metrics for subscription revenue.

        Parameters
        ----------
        company_id : str

        connection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_recurring_revenue_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
        )
        """
        _response = self._raw_client.get_recurring_revenue_metrics(
            company_id, connection_id, request_options=request_options
        )
        return _response.data

    def request_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Report:
        """
        Request production of key subscription revenue metrics.

        Parameters
        ----------
        company_id : str

        connection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.request_recurring_revenue_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
        )
        """
        _response = self._raw_client.request_recurring_revenue_metrics(
            company_id, connection_id, request_options=request_options
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def get_accounts_for_enhanced_balance_sheet(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedReport:
        """
        The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

        Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

        Parameters
        ----------
        company_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedReport
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_accounts_for_enhanced_balance_sheet(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                report_date="29-09-2020",
                number_of_periods=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_for_enhanced_balance_sheet(
            company_id, report_date=report_date, number_of_periods=number_of_periods, request_options=request_options
        )
        return _response.data

    async def get_enhanced_cash_flow_transactions(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedCashFlowTransactions:
        """
        The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

        Parameters
        ----------
        company_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedCashFlowTransactions
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_enhanced_cash_flow_transactions(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                page=1,
                page_size=100,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enhanced_cash_flow_transactions(
            company_id, page=page, page_size=page_size, query=query, request_options=request_options
        )
        return _response.data

    async def get_enhanced_invoices_report(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedInvoicesReport:
        """
        Gets a list of invoices linked to the corresponding banking transaction

        Parameters
        ----------
        company_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedInvoicesReport
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_enhanced_invoices_report(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                page=1,
                page_size=100,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enhanced_invoices_report(
            company_id, page=page, page_size=page_size, query=query, request_options=request_options
        )
        return _response.data

    async def get_accounts_for_enhanced_profit_and_loss(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnhancedReport:
        """
        The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

        Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

        Parameters
        ----------
        company_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnhancedReport
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_accounts_for_enhanced_profit_and_loss(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                report_date="29-09-2020",
                number_of_periods=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounts_for_enhanced_profit_and_loss(
            company_id, report_date=report_date, number_of_periods=number_of_periods, request_options=request_options
        )
        return _response.data

    async def get_commerce_customer_retention_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceCustomerRetentionMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the customer retention metrics for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceCustomerRetentionMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.reports import GetCommerceCustomerRetentionMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_commerce_customer_retention_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetCommerceCustomerRetentionMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_commerce_customer_retention_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_commerce_lifetime_value_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceLifetimeValueMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the lifetime value metric for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceLifetimeValueMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.reports import GetCommerceLifetimeValueMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_commerce_lifetime_value_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetCommerceLifetimeValueMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_commerce_lifetime_value_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_commerce_orders_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceOrdersMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the order information for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceOrdersMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.reports import GetCommerceOrdersMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_commerce_orders_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetCommerceOrdersMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_commerce_orders_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_commerce_refunds_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceRefundsMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets the refunds information for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceRefundsMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.reports import GetCommerceRefundsMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_commerce_refunds_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetCommerceRefundsMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_commerce_refunds_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_commerce_revenue_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetCommerceRevenueMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Get the revenue and revenue growth for a specific company connection, over one or more periods of time.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetCommerceRevenueMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.reports import GetCommerceRevenueMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_commerce_revenue_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetCommerceRevenueMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_commerce_revenue_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_enhanced_balance_sheet(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets a fully categorized balance sheet statement for a given company, over one or more period(s).

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_enhanced_balance_sheet(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enhanced_balance_sheet(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_enhanced_profit_and_loss(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        include_display_names: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_enhanced_profit_and_loss(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enhanced_profit_and_loss(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            include_display_names=include_display_names,
            request_options=request_options,
        )
        return _response.data

    async def get_enhanced_financial_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        show_metric_inputs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FinancialMetrics:
        """
        Gets all the available financial metrics for a given company, over one or more periods.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        show_metric_inputs : typing.Optional[bool]
            If set to true, then the system includes the input values within the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FinancialMetrics
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_enhanced_financial_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enhanced_financial_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            show_metric_inputs=show_metric_inputs,
            request_options=request_options,
        )
        return _response.data

    async def get_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Report:
        """
        Gets key metrics for subscription revenue.

        Parameters
        ----------
        company_id : str

        connection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_recurring_revenue_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recurring_revenue_metrics(
            company_id, connection_id, request_options=request_options
        )
        return _response.data

    async def request_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Report:
        """
        Request production of key subscription revenue metrics.

        Parameters
        ----------
        company_id : str

        connection_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.request_recurring_revenue_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_recurring_revenue_metrics(
            company_id, connection_id, request_options=request_options
        )
        return _response.data
