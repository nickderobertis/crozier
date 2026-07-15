# Reference
## Balance Sheet
<details><summary><code>client.balance_sheet.<a href="src/fern/balance_sheet/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get BalanceSheet
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.balance_sheet.one()

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

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[BalanceSheetFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

## Bills
<details><summary><code>client.bills.<a href="src/fern/bills/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Bills
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.bills.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[BillsSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.bills.<a href="src/fern/bills/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Bill
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.bills.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance of bill due.
    
</dd>
</dl>

<dl>
<dd>

**bill_date:** `typing.Optional[dt.date]` — Date bill was issued - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**bill_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**deposit:** `typing.Optional[float]` — Amount of deposit made to this bill.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.date]` — The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**ledger_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[BillLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**paid_date:** `typing.Optional[dt.date]` — The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**po_number:** `typing.Optional[str]` — A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional bill reference.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[BillStatus]` — Invoice status
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**supplier:** `typing.Optional[LinkedSupplier]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Terms of payment.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[float]` — Total amount of bill, including tax.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this bill.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.bills.<a href="src/fern/bills/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Bill
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.bills.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.bills.<a href="src/fern/bills/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Bill
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.bills.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.bills.<a href="src/fern/bills/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Bill
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.bills.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance of bill due.
    
</dd>
</dl>

<dl>
<dd>

**bill_date:** `typing.Optional[dt.date]` — Date bill was issued - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**bill_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**deposit:** `typing.Optional[float]` — Amount of deposit made to this bill.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.date]` — The due date is the date on which a payment is scheduled to be received by the supplier - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**ledger_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[BillLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**paid_date:** `typing.Optional[dt.date]` — The paid date is the date on which a payment was sent to the supplier - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**po_number:** `typing.Optional[str]` — A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional bill reference.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[BillStatus]` — Invoice status
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**supplier:** `typing.Optional[LinkedSupplier]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Terms of payment.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[float]` — Total amount of bill, including tax.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this bill.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Company Info
<details><summary><code>client.company_info.<a href="src/fern/company_info/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get company info
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.company_info.one(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

## Credit Notes
<details><summary><code>client.credit_notes.<a href="src/fern/credit_notes/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Credit Notes
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.credit_notes.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.credit_notes.<a href="src/fern/credit_notes/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Credit Note
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.credit_notes.add(
    total_amount=49.99,
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

**total_amount:** `float` — Amount of transaction
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — The balance reflecting any payments made against the transaction.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**date_issued:** `typing.Optional[dt.datetime]` — Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**date_paid:** `typing.Optional[dt.datetime]` — Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier representing the entity
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[InvoiceLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Optional note to be associated with the credit note.
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — Credit note number.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional reference message ie: Debit remittance detail.
    
</dd>
</dl>

<dl>
<dd>

**remaining_credit:** `typing.Optional[float]` — Indicates the total credit amount still available to apply towards the payment.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreditNoteStatus]` — Status of credit notes
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Optional terms to be associated with the credit note.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreditNoteType]` — Type of payment
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.credit_notes.<a href="src/fern/credit_notes/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Credit Note
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.credit_notes.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.credit_notes.<a href="src/fern/credit_notes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Credit Note
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.credit_notes.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.credit_notes.<a href="src/fern/credit_notes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Credit Note
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.credit_notes.update(
    id_="id",
    total_amount=49.99,
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `float` — Amount of transaction
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Optional[typing.Sequence[CreditNoteAllocationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — The balance reflecting any payments made against the transaction.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**date_issued:** `typing.Optional[dt.datetime]` — Date credit note issued - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**date_paid:** `typing.Optional[dt.datetime]` — Date credit note paid - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier representing the entity
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[InvoiceLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Optional note to be associated with the credit note.
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — Credit note number.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional reference message ie: Debit remittance detail.
    
</dd>
</dl>

<dl>
<dd>

**remaining_credit:** `typing.Optional[float]` — Indicates the total credit amount still available to apply towards the payment.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreditNoteStatus]` — Status of credit notes
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Optional terms to be associated with the credit note.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreditNoteType]` — Type of payment
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Customers
<details><summary><code>client.customers.<a href="src/fern/customers/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Customers
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.customers.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[CustomersFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Customer
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.customers.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Display ID
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display name
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` — Is this an individual or business customer
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Some notes about this customer
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[LinkedParentCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[bool]` — If true, indicates this is a Project.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AccountingCustomerStatus]` — Customer status
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[Suffix]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[TaxNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Customer
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.customers.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Customer
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.customers.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Customer
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.customers.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Display ID
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display name
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` — Is this an individual or business customer
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Some notes about this customer
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[LinkedParentCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[bool]` — If true, indicates this is a Project.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AccountingCustomerStatus]` — Customer status
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[Suffix]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[TaxNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

## Invoice Items
<details><summary><code>client.invoice_items.<a href="src/fern/invoice_items/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Invoice Items
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoice_items.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[InvoiceItemsFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.invoice_items.<a href="src/fern/invoice_items/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Invoice Item
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoice_items.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[Active]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — User defined item code
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A short description of the item
    
</dd>
</dl>

<dl>
<dd>

**expense_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The ID of the item.
    
</dd>
</dl>

<dl>
<dd>

**income_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**inventory_date:** `typing.Optional[dt.date]` — The date of opening balance if inventory item is tracked - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Item name
    
</dd>
</dl>

<dl>
<dd>

**purchase_details:** `typing.Optional[InvoiceItemPurchaseDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**purchased:** `typing.Optional[bool]` — Item is available for purchase transactions
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[Quantity]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**sales_details:** `typing.Optional[InvoiceItemSalesDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**sold:** `typing.Optional[bool]` — Item will be available on sales transactions
    
</dd>
</dl>

<dl>
<dd>

**taxable:** `typing.Optional[bool]` — If true, transactions for this item are taxable
    
</dd>
</dl>

<dl>
<dd>

**tracked:** `typing.Optional[bool]` — Item is inventoried
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[InvoiceItemType]` — Item type
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[UnitPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.invoice_items.<a href="src/fern/invoice_items/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Invoice Item
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoice_items.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.invoice_items.<a href="src/fern/invoice_items/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Invoice Item
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoice_items.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.invoice_items.<a href="src/fern/invoice_items/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Invoice Item
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoice_items.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[Active]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — User defined item code
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A short description of the item
    
</dd>
</dl>

<dl>
<dd>

**expense_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The ID of the item.
    
</dd>
</dl>

<dl>
<dd>

**income_account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**inventory_date:** `typing.Optional[dt.date]` — The date of opening balance if inventory item is tracked - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Item name
    
</dd>
</dl>

<dl>
<dd>

**purchase_details:** `typing.Optional[InvoiceItemPurchaseDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**purchased:** `typing.Optional[bool]` — Item is available for purchase transactions
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[Quantity]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**sales_details:** `typing.Optional[InvoiceItemSalesDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**sold:** `typing.Optional[bool]` — Item will be available on sales transactions
    
</dd>
</dl>

<dl>
<dd>

**taxable:** `typing.Optional[bool]` — If true, transactions for this item are taxable
    
</dd>
</dl>

<dl>
<dd>

**tracked:** `typing.Optional[bool]` — Item is inventoried
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[InvoiceItemType]` — Item type
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[UnitPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Invoices
<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Invoices
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoices.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[InvoicesSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Invoice
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoices.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance of invoice due.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_memo:** `typing.Optional[str]` — Customer memo
    
</dd>
</dl>

<dl>
<dd>

**deposit:** `typing.Optional[float]` — Amount of deposit made to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**discount_amount:** `typing.Optional[float]` — Discount amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**discount_percentage:** `typing.Optional[float]` — Discount percentage applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.date]` — The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_date:** `typing.Optional[dt.date]` — Date invoice was issued - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**invoice_sent:** `typing.Optional[bool]` — Invoice sent to contact/customer.
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[InvoiceLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — Invoice number.
    
</dd>
</dl>

<dl>
<dd>

**po_number:** `typing.Optional[str]` — A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional invoice reference.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**source_document_url:** `typing.Optional[str]` — URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[InvoiceStatus]` — Invoice status
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Optional invoice template
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Terms of payment.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[float]` — Total amount of invoice, including tax.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[InvoiceType]` — Invoice type
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Invoice
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoices.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Invoice
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoices.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Invoice
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.invoices.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**balance:** `typing.Optional[float]` — Balance of invoice due.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_memo:** `typing.Optional[str]` — Customer memo
    
</dd>
</dl>

<dl>
<dd>

**deposit:** `typing.Optional[float]` — Amount of deposit made to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**discount_amount:** `typing.Optional[float]` — Discount amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**discount_percentage:** `typing.Optional[float]` — Discount percentage applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.date]` — The invoice due date is the date on which a payment or invoice is scheduled to be received by the seller - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_date:** `typing.Optional[dt.date]` — Date invoice was issued - YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**invoice_sent:** `typing.Optional[bool]` — Invoice sent to contact/customer.
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[InvoiceLineItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — Invoice number.
    
</dd>
</dl>

<dl>
<dd>

**po_number:** `typing.Optional[str]` — A PO Number uniquely identifies a purchase order and is generally defined by the buyer. The buyer will match the PO number in the invoice to the Purchase Order.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional invoice reference.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**source_document_url:** `typing.Optional[str]` — URL link to a source document - shown as 'Go to [appName]' in the downstream app. Currently only supported for Xero.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[InvoiceStatus]` — Invoice status
    
</dd>
</dl>

<dl>
<dd>

**sub_total:** `typing.Optional[float]` — Sub-total amount, normally before tax.
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Applicable tax id/code override if tax is not supplied on a line item basis.
    
</dd>
</dl>

<dl>
<dd>

**tax_inclusive:** `typing.Optional[TaxInclusive]` 
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Optional invoice template
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[str]` — Terms of payment.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[float]` — Total amount of invoice, including tax.
    
</dd>
</dl>

<dl>
<dd>

**total_tax:** `typing.Optional[float]` — Total tax amount applied to this invoice.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[InvoiceType]` — Invoice type
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Journal Entries
<details><summary><code>client.journal_entries.<a href="src/fern/journal_entries/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Journal Entries
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.journal_entries.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.journal_entries.<a href="src/fern/journal_entries/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Journal Entry
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.journal_entries.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**journal_symbol:** `typing.Optional[str]` — Journal symbol of the entry. For example IND for indirect costs
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[JournalEntryLineItem]]` — Requires a minimum of 2 line items that sum to 0
    
</dd>
</dl>

<dl>
<dd>

**memo:** `typing.Optional[str]` — Reference for the journal entry.
    
</dd>
</dl>

<dl>
<dd>

**posted_at:** `typing.Optional[dt.datetime]` — This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Journal entry title
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.journal_entries.<a href="src/fern/journal_entries/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Journal Entry
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.journal_entries.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.journal_entries.<a href="src/fern/journal_entries/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Journal Entry
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.journal_entries.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.journal_entries.<a href="src/fern/journal_entries/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Journal Entry
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.journal_entries.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**journal_symbol:** `typing.Optional[str]` — Journal symbol of the entry. For example IND for indirect costs
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[JournalEntryLineItem]]` — Requires a minimum of 2 line items that sum to 0
    
</dd>
</dl>

<dl>
<dd>

**memo:** `typing.Optional[str]` — Reference for the journal entry.
    
</dd>
</dl>

<dl>
<dd>

**posted_at:** `typing.Optional[dt.datetime]` — This is the date on which the journal entry was added. This can be different from the creation date and can also be backdated.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Journal entry title
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Ledger Accounts
<details><summary><code>client.ledger_accounts.<a href="src/fern/ledger_accounts/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Ledger Accounts
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.ledger_accounts.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.ledger_accounts.<a href="src/fern/ledger_accounts/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Ledger Account
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.ledger_accounts.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the account is active or not.
    
</dd>
</dl>

<dl>
<dd>

**bank_account:** `typing.Optional[BankAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]` — The categories of the account.
    
</dd>
</dl>

<dl>
<dd>

**classification:** `typing.Optional[LedgerAccountClassification]` — The classification of account.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The code assigned to the account.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**current_balance:** `typing.Optional[float]` — The current balance of the account.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the account.
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — The human readable display ID used when displaying the account
    
</dd>
</dl>

<dl>
<dd>

**fully_qualified_name:** `typing.Optional[str]` — The fully qualified name of the account.
    
</dd>
</dl>

<dl>
<dd>

**header:** `typing.Optional[bool]` — Whether the account is a header or not.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**last_reconciliation_date:** `typing.Optional[dt.date]` — Reconciliation Date means the last calendar day of each Reconciliation Period.
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the account.
    
</dd>
</dl>

<dl>
<dd>

**nominal_code:** `typing.Optional[str]` — The nominal code of the ledger account.
    
</dd>
</dl>

<dl>
<dd>

**opening_balance:** `typing.Optional[float]` — The opening balance of the account.
    
</dd>
</dl>

<dl>
<dd>

**parent_account:** `typing.Optional[LedgerAccountParentAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[LedgerAccountStatus]` — The status of the account.
    
</dd>
</dl>

<dl>
<dd>

**sub_account:** `typing.Optional[bool]` — Whether the account is a sub account or not.
    
</dd>
</dl>

<dl>
<dd>

**sub_accounts:** `typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]` — The sub accounts of the account.
    
</dd>
</dl>

<dl>
<dd>

**sub_type:** `typing.Optional[str]` — The sub type of account.
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_type:** `typing.Optional[str]` — The tax type of the account.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LedgerAccountType]` — The type of account.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.ledger_accounts.<a href="src/fern/ledger_accounts/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Ledger Account
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.ledger_accounts.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.ledger_accounts.<a href="src/fern/ledger_accounts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Ledger Account
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.ledger_accounts.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.ledger_accounts.<a href="src/fern/ledger_accounts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Ledger Account
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.ledger_accounts.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the account is active or not.
    
</dd>
</dl>

<dl>
<dd>

**bank_account:** `typing.Optional[BankAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]` — The categories of the account.
    
</dd>
</dl>

<dl>
<dd>

**classification:** `typing.Optional[LedgerAccountClassification]` — The classification of account.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The code assigned to the account.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**current_balance:** `typing.Optional[float]` — The current balance of the account.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the account.
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — The human readable display ID used when displaying the account
    
</dd>
</dl>

<dl>
<dd>

**fully_qualified_name:** `typing.Optional[str]` — The fully qualified name of the account.
    
</dd>
</dl>

<dl>
<dd>

**header:** `typing.Optional[bool]` — Whether the account is a header or not.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**last_reconciliation_date:** `typing.Optional[dt.date]` — Reconciliation Date means the last calendar day of each Reconciliation Period.
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the account.
    
</dd>
</dl>

<dl>
<dd>

**nominal_code:** `typing.Optional[str]` — The nominal code of the ledger account.
    
</dd>
</dl>

<dl>
<dd>

**opening_balance:** `typing.Optional[float]` — The opening balance of the account.
    
</dd>
</dl>

<dl>
<dd>

**parent_account:** `typing.Optional[LedgerAccountParentAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[LedgerAccountStatus]` — The status of the account.
    
</dd>
</dl>

<dl>
<dd>

**sub_account:** `typing.Optional[bool]` — Whether the account is a sub account or not.
    
</dd>
</dl>

<dl>
<dd>

**sub_accounts:** `typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]` — The sub accounts of the account.
    
</dd>
</dl>

<dl>
<dd>

**sub_type:** `typing.Optional[str]` — The sub type of account.
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_type:** `typing.Optional[str]` — The tax type of the account.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LedgerAccountType]` — The type of account.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Payments
<details><summary><code>client.payments.<a href="src/fern/payments/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Payments
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payments.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Payment
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
import datetime

from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payments.add(
    total_amount=49.99,
    transaction_date=datetime.datetime.fromisoformat(
        "2021-05-01 12:00:00+00:00",
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

**total_amount:** `float` — Amount of payment
    
</dd>
</dl>

<dl>
<dd>

**transaction_date:** `dt.datetime` — Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**accounts_receivable_account_id:** `typing.Optional[str]` — Unique identifier for the account to allocate payment to.
    
</dd>
</dl>

<dl>
<dd>

**accounts_receivable_account_type:** `typing.Optional[str]` — Type of accounts receivable account.
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Optional[typing.Sequence[PaymentAllocationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Payment id to be displayed.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier representing the entity
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Optional note to be associated with the payment.
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[str]` — Payment method name
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `typing.Optional[str]` — Unique identifier for the payment method.
    
</dd>
</dl>

<dl>
<dd>

**payment_method_reference:** `typing.Optional[str]` — Optional reference message returned by payment method on processing
    
</dd>
</dl>

<dl>
<dd>

**reconciled:** `typing.Optional[bool]` — Payment has been reconciled
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional payment reference message ie: Debit remittance detail.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PaymentStatus]` — Status of payment
    
</dd>
</dl>

<dl>
<dd>

**supplier:** `typing.Optional[LinkedSupplier]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PaymentType]` — Type of payment
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Payment
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payments.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Payment
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payments.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Payment
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
import datetime

from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payments.update(
    id_="id",
    total_amount=49.99,
    transaction_date=datetime.datetime.fromisoformat(
        "2021-05-01 12:00:00+00:00",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `float` — Amount of payment
    
</dd>
</dl>

<dl>
<dd>

**transaction_date:** `dt.datetime` — Date transaction was entered - YYYY:MM::DDThh:mm:ss.sTZD
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**accounts_receivable_account_id:** `typing.Optional[str]` — Unique identifier for the account to allocate payment to.
    
</dd>
</dl>

<dl>
<dd>

**accounts_receivable_account_type:** `typing.Optional[str]` — Type of accounts receivable account.
    
</dd>
</dl>

<dl>
<dd>

**allocations:** `typing.Optional[typing.Sequence[PaymentAllocationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_rate:** `typing.Optional[CurrencyRate]` 
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[LinkedCustomer]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Payment id to be displayed.
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Unique identifier representing the entity
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Optional note to be associated with the payment.
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[str]` — Payment method name
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `typing.Optional[str]` — Unique identifier for the payment method.
    
</dd>
</dl>

<dl>
<dd>

**payment_method_reference:** `typing.Optional[str]` — Optional reference message returned by payment method on processing
    
</dd>
</dl>

<dl>
<dd>

**reconciled:** `typing.Optional[bool]` — Payment has been reconciled
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Optional payment reference message ie: Debit remittance detail.
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PaymentStatus]` — Status of payment
    
</dd>
</dl>

<dl>
<dd>

**supplier:** `typing.Optional[LinkedSupplier]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PaymentType]` — Type of payment
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Profit and Loss
<details><summary><code>client.profit_and_loss.<a href="src/fern/profit_and_loss/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Profit and Loss
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.profit_and_loss.one(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ProfitAndLossFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

## Suppliers
<details><summary><code>client.suppliers.<a href="src/fern/suppliers/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Suppliers
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.suppliers.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[SuppliersFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.suppliers.<a href="src/fern/suppliers/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Supplier
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.suppliers.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Display ID
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display name
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` — Is this an individual or business supplier
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Some notes about this supplier
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SupplierStatus]` — Supplier status
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[Suffix]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[TaxNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

<details><summary><code>client.suppliers.<a href="src/fern/suppliers/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Supplier
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.suppliers.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.suppliers.<a href="src/fern/suppliers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Supplier
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.suppliers.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.suppliers.<a href="src/fern/suppliers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Supplier
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.suppliers.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[LinkedLedgerAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_id:** `typing.Optional[str]` — Display ID
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Display name
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[DownstreamId]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` — Is this an individual or business supplier
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Some notes about this supplier
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SupplierStatus]` — Supplier status
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[Suffix]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[TaxNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_rate:** `typing.Optional[LinkedTaxRate]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

## Tax Rates
<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Tax Rates. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Connectors Affected: Quickbooks
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tax_rates.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TaxRatesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Tax Rate
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tax_rates.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Tax code assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Sequence[TaxRateComponentsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of tax rate
    
</dd>
</dl>

<dl>
<dd>

**effective_tax_rate:** `typing.Optional[float]` — Effective tax rate
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — ID assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**original_tax_rate_id:** `typing.Optional[str]` — ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.
    
</dd>
</dl>

<dl>
<dd>

**report_tax_type:** `typing.Optional[str]` — Report Tax type to aggregate tax collected or paid for reporting purposes
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaxRateStatus]` — Tax rate status
    
</dd>
</dl>

<dl>
<dd>

**tax_payable_account_id:** `typing.Optional[str]` — Unique identifier for the account for tax collected.
    
</dd>
</dl>

<dl>
<dd>

**tax_remitted_account_id:** `typing.Optional[str]` — Unique identifier for the account for tax remitted.
    
</dd>
</dl>

<dl>
<dd>

**total_tax_rate:** `typing.Optional[float]` — Not compounded sum of the components of a tax rate
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Tax type used to indicate the source of tax collected or paid
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Tax Rate. Note: Not all connectors return the actual rate/percentage value. In this case, only the tax code or reference is returned. Support will soon be added to return the actual rate/percentage by doing additional calls in the background to provide the full view of a given tax rate. Connectors Affected: Quickbooks
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Tax Rate
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tax_rates.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.tax_rates.<a href="src/fern/tax_rates/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Tax Rate
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

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tax_rates.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Tax code assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Sequence[TaxRateComponentsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of tax rate
    
</dd>
</dl>

<dl>
<dd>

**effective_tax_rate:** `typing.Optional[float]` — Effective tax rate
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — ID assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name assigned to identify this tax rate.
    
</dd>
</dl>

<dl>
<dd>

**original_tax_rate_id:** `typing.Optional[str]` — ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.
    
</dd>
</dl>

<dl>
<dd>

**report_tax_type:** `typing.Optional[str]` — Report Tax type to aggregate tax collected or paid for reporting purposes
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaxRateStatus]` — Tax rate status
    
</dd>
</dl>

<dl>
<dd>

**tax_payable_account_id:** `typing.Optional[str]` — Unique identifier for the account for tax collected.
    
</dd>
</dl>

<dl>
<dd>

**tax_remitted_account_id:** `typing.Optional[str]` — Unique identifier for the account for tax remitted.
    
</dd>
</dl>

<dl>
<dd>

**total_tax_rate:** `typing.Optional[float]` — Not compounded sum of the components of a tax rate
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Tax type used to indicate the source of tax collected or paid
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

