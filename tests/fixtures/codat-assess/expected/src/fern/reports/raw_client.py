

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.enhanced_cash_flow_transactions import EnhancedCashFlowTransactions
from ..types.enhanced_invoices_report import EnhancedInvoicesReport
from ..types.enhanced_report import EnhancedReport
from ..types.financial_metrics import FinancialMetrics
from ..types.report import Report
from .types.get_commerce_customer_retention_metrics_request_period_unit import (
    GetCommerceCustomerRetentionMetricsRequestPeriodUnit,
)
from .types.get_commerce_lifetime_value_metrics_request_period_unit import (
    GetCommerceLifetimeValueMetricsRequestPeriodUnit,
)
from .types.get_commerce_orders_metrics_request_period_unit import GetCommerceOrdersMetricsRequestPeriodUnit
from .types.get_commerce_refunds_metrics_request_period_unit import GetCommerceRefundsMetricsRequestPeriodUnit
from .types.get_commerce_revenue_metrics_request_period_unit import GetCommerceRevenueMetricsRequestPeriodUnit
from pydantic import ValidationError


class RawReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_accounts_for_enhanced_balance_sheet(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnhancedReport]:
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
        HttpResponse[EnhancedReport]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedBalanceSheet/accounts",
            method="GET",
            params={
                "reportDate": report_date,
                "numberOfPeriods": number_of_periods,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedReport,
                    parse_obj_as(
                        type_=EnhancedReport,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_enhanced_cash_flow_transactions(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnhancedCashFlowTransactions]:
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
        HttpResponse[EnhancedCashFlowTransactions]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedCashFlow/transactions",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedCashFlowTransactions,
                    parse_obj_as(
                        type_=EnhancedCashFlowTransactions,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_enhanced_invoices_report(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnhancedInvoicesReport]:
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
        HttpResponse[EnhancedInvoicesReport]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedInvoices",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedInvoicesReport,
                    parse_obj_as(
                        type_=EnhancedInvoicesReport,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_accounts_for_enhanced_profit_and_loss(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnhancedReport]:
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
        HttpResponse[EnhancedReport]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedProfitAndLoss/accounts",
            method="GET",
            params={
                "reportDate": report_date,
                "numberOfPeriods": number_of_periods,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedReport,
                    parse_obj_as(
                        type_=EnhancedReport,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/customerRetention",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/lifetimeValue",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/orders",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/refunds",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/revenue",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/enhancedBalanceSheet",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/enhancedProfitAndLoss",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[FinancialMetrics]:
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
        HttpResponse[FinancialMetrics]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/financialMetrics",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "showMetricInputs": show_metric_inputs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FinancialMetrics,
                    parse_obj_as(
                        type_=FinancialMetrics,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/subscriptions/mrr",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def request_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/subscriptions/process",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_accounts_for_enhanced_balance_sheet(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnhancedReport]:
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
        AsyncHttpResponse[EnhancedReport]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedBalanceSheet/accounts",
            method="GET",
            params={
                "reportDate": report_date,
                "numberOfPeriods": number_of_periods,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedReport,
                    parse_obj_as(
                        type_=EnhancedReport,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_enhanced_cash_flow_transactions(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnhancedCashFlowTransactions]:
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
        AsyncHttpResponse[EnhancedCashFlowTransactions]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedCashFlow/transactions",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedCashFlowTransactions,
                    parse_obj_as(
                        type_=EnhancedCashFlowTransactions,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_enhanced_invoices_report(
        self,
        company_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnhancedInvoicesReport]:
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
        AsyncHttpResponse[EnhancedInvoicesReport]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedInvoices",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedInvoicesReport,
                    parse_obj_as(
                        type_=EnhancedInvoicesReport,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_accounts_for_enhanced_profit_and_loss(
        self,
        company_id: str,
        *,
        report_date: str,
        number_of_periods: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnhancedReport]:
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
        AsyncHttpResponse[EnhancedReport]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"companies/{encode_path_param(company_id)}/reports/enhancedProfitAndLoss/accounts",
            method="GET",
            params={
                "reportDate": report_date,
                "numberOfPeriods": number_of_periods,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnhancedReport,
                    parse_obj_as(
                        type_=EnhancedReport,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/customerRetention",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/lifetimeValue",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/orders",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/refunds",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/commerceMetrics/revenue",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/enhancedBalanceSheet",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/enhancedProfitAndLoss",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "includeDisplayNames": include_display_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[FinancialMetrics]:
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
        AsyncHttpResponse[FinancialMetrics]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/financialMetrics",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "showMetricInputs": show_metric_inputs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FinancialMetrics,
                    parse_obj_as(
                        type_=FinancialMetrics,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/subscriptions/mrr",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def request_recurring_revenue_metrics(
        self, company_id: str, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/subscriptions/process",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
