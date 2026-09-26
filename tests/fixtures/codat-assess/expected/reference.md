# Reference
## Reports
<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_accounts_for_enhanced_balance_sheet</a>(...) -> EnhancedReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_accounts_for_enhanced_balance_sheet(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_date="29-09-2020",
    number_of_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_enhanced_cash_flow_transactions</a>(...) -> EnhancedCashFlowTransactions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_enhanced_cash_flow_transactions(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    page=1,
    page_size=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_enhanced_invoices_report</a>(...) -> EnhancedInvoicesReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of invoices linked to the corresponding banking transaction
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_enhanced_invoices_report(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    page=1,
    page_size=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_accounts_for_enhanced_profit_and_loss</a>(...) -> EnhancedReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_accounts_for_enhanced_profit_and_loss(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_date="29-09-2020",
    number_of_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_commerce_customer_retention_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the customer retention metrics for a specific company connection, over one or more periods of time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.reports import GetCommerceCustomerRetentionMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_commerce_customer_retention_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetCommerceCustomerRetentionMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetCommerceCustomerRetentionMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_commerce_lifetime_value_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the lifetime value metric for a specific company connection, over one or more periods of time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.reports import GetCommerceLifetimeValueMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_commerce_lifetime_value_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetCommerceLifetimeValueMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetCommerceLifetimeValueMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_commerce_orders_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the order information for a specific company connection, over one or more periods of time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.reports import GetCommerceOrdersMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_commerce_orders_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetCommerceOrdersMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetCommerceOrdersMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_commerce_refunds_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the refunds information for a specific company connection, over one or more periods of time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.reports import GetCommerceRefundsMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_commerce_refunds_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetCommerceRefundsMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetCommerceRefundsMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_commerce_revenue_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the revenue and revenue growth for a specific company connection, over one or more periods of time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.reports import GetCommerceRevenueMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_commerce_revenue_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetCommerceRevenueMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetCommerceRevenueMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_enhanced_balance_sheet</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a fully categorized balance sheet statement for a given company, over one or more period(s).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_enhanced_balance_sheet(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_enhanced_profit_and_loss</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a fully categorized profit and loss statement for a given company, over one or more period(s).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_enhanced_profit_and_loss(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_enhanced_financial_metrics</a>(...) -> FinancialMetrics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all the available financial metrics for a given company, over one or more periods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_enhanced_financial_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**show_metric_inputs:** `typing.Optional[bool]` — If set to true, then the system includes the input values within the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_recurring_revenue_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets key metrics for subscription revenue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.get_recurring_revenue_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">request_recurring_revenue_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request production of key subscription revenue metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.reports.request_recurring_revenue_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Categories
<details><summary><code>client.categories.<a href="src/fern/categories/client.py">list_available_account_categories</a>() -> Categories</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists available account categories Codat's categorisation engine can provide. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.categories.list_available_account_categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">list_accounts_categories</a>(...) -> CategorisedAccounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists suggested and confirmed chart of account categories for the given company and data connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.categories.list_accounts_categories(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    page=1,
    page_size=100,
    order_by="-modifiedDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">update_accounts_categories</a>(...) -> typing.List[CategorisedAccount]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Comfirms the categories for all or a batch of accounts for a specific connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.categories.update_accounts_categories(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.List[ConfirmCategoriesCategoriesItem]]` — List of confirmed account categories set manually by the user. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">get_account_category</a>(...) -> CategorisedAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get category for specific nominal account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.categories.get_account_category(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    account_id="accountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — Nominal account id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">update_account_category</a>(...) -> CategorisedAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update category for a specific nominal account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccountCategory
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.categories.update_account_category(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    account_id="accountId",
    confirmed=AccountCategory(
        detail_type="Cash",
        subtype="Current",
        type="Asset",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` — Nominal account id
    
</dd>
</dl>

<dl>
<dd>

**confirmed:** `AccountCategory` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data integrity
<details><summary><code>client.data_integrity.<a href="src/fern/data_integrity/client.py">get_data_integrity_details</a>(...) -> Details</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.data_integrity import GetDataIntegrityDetailsRequestDataType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.data_integrity.get_data_integrity_details(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type=GetDataIntegrityDetailsRequestDataType.BANKING_ACCOUNTS,
    page=1,
    page_size=100,
    order_by="-modifiedDate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `GetDataIntegrityDetailsRequestDataType` — A key for a Codat data type.
    
</dd>
</dl>

<dl>
<dd>

**page:** `int` — Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_integrity.<a href="src/fern/data_integrity/client.py">get_data_integrity_status</a>(...) -> Status</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets match status for a given company and datatype.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.data_integrity import GetDataIntegrityStatusRequestDataType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.data_integrity.get_data_integrity_status(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type=GetDataIntegrityStatusRequestDataType.BANKING_ACCOUNTS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `GetDataIntegrityStatusRequestDataType` — A key for a Codat data type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_integrity.<a href="src/fern/data_integrity/client.py">get_data_integrity_summaries</a>(...) -> Summaries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets match summary for a given company and datatype, optionally restricted by a Codat query string.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.data_integrity import GetDataIntegritySummariesRequestDataType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.data_integrity.get_data_integrity_summaries(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type=GetDataIntegritySummariesRequestDataType.BANKING_ACCOUNTS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `GetDataIntegritySummariesRequestDataType` — A key for a Codat data type.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Excel reports
<details><summary><code>client.excel_reports.<a href="src/fern/excel_reports/client.py">get_excel_report_generation_status</a>(...) -> ExcelStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of the latest report requested.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.excel_reports import GetExcelReportGenerationStatusRequestReportType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.excel_reports.get_excel_report_generation_status(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_type=GetExcelReportGenerationStatusRequestReportType.AUDIT,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `GetExcelReportGenerationStatusRequestReportType` — The type of report you want to generate and download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.excel_reports.<a href="src/fern/excel_reports/client.py">generate_excel_report</a>(...) -> ExcelStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an Excel report which can subsequently be downloaded.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.excel_reports import GenerateExcelReportRequestReportType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.excel_reports.generate_excel_report(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_type=GenerateExcelReportRequestReportType.AUDIT,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `GenerateExcelReportRequestReportType` — The type of report you want to generate and download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.excel_reports.<a href="src/fern/excel_reports/client.py">get_excel_report</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the previously generated Excel report to a local drive.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.excel_reports.get_excel_report(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `GetExcelReportRequestReportType` — The type of report you want to generate and download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.excel_reports.<a href="src/fern/excel_reports/client.py">download_excel_report</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the previously generated Excel report to a local drive.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.excel_reports.download_excel_report(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_type:** `DownloadExcelReportRequestReportType` — The type of report you want to generate and download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.excel_reports.<a href="src/fern/excel_reports/client.py">get_accounting_marketing_metrics</a>(...) -> Report</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request an Excel report for download.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.excel_reports import GetAccountingMarketingMetricsRequestPeriodUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.excel_reports.get_accounting_marketing_metrics(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    report_date="29-09-2020",
    period_length=1,
    number_of_periods=1,
    period_unit=GetAccountingMarketingMetricsRequestPeriodUnit.DAY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_date:** `str` — The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.
    
</dd>
</dl>

<dl>
<dd>

**period_length:** `int` — The number of months per period. E.g. 2 = 2 months per period.
    
</dd>
</dl>

<dl>
<dd>

**number_of_periods:** `int` — The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.
    
</dd>
</dl>

<dl>
<dd>

**period_unit:** `GetAccountingMarketingMetricsRequestPeriodUnit` — The period unit of time returned.
    
</dd>
</dl>

<dl>
<dd>

**include_display_names:** `typing.Optional[bool]` — Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.
    
</dd>
</dl>

<dl>
<dd>

**show_input_values:** `typing.Optional[bool]` — If set to true, then the system includes the input values within the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

