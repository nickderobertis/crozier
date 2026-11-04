# Reference
<details><summary><code>client.<a href="src/fern/client.py">receipt_match</a>(...) -> CreateAsyncFileUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.receipt_match(
    receipt_name="receipt_name",
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

**receipt_name:** `str` — The name of the receipt (with the file extension). It will be used in the matching result email.
    
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

<details><summary><code>client.<a href="src/fern/client.py">receipt_upload</a>(...) -> CreateAsyncFileUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.receipt_upload(
    expense_id="expense_id",
    receipt_name="receipt_name",
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

**expense_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**receipt_name:** `str` — The name of the receipt (with the file extension).
    
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

## Card Expenses
<details><summary><code>client.card_expenses.<a href="src/fern/card_expenses/client.py">list_expenses</a>(...) -> PageExpandableExpense</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.card_expenses.list_expenses(
    purchased_at_start=datetime.datetime.fromisoformat("2023-01-01T23:59:59+00:00"),
    purchased_at_end=datetime.datetime.fromisoformat("2023-01-10T23:59:59+00:00"),
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

**expand_array:** `typing.Optional[typing.List[str]]` — Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.
    
</dd>
</dl>

<dl>
<dd>

**user_id_array:** `typing.Optional[typing.List[str]]` — Get expenses belong to provided user(s).
    
</dd>
</dl>

<dl>
<dd>

**parent_expense_id_array:** `typing.Optional[typing.List[str]]` — Get itemized expenses belong to provided parent expenses ID(s).
    
</dd>
</dl>

<dl>
<dd>

**budget_id_array:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**status_array:** `typing.Optional[typing.List[ExpenseStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_status_array:** `typing.Optional[typing.List[ExpensePaymentStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**purchased_at_start:** `typing.Optional[datetime.datetime]` — 
Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999
    
</dd>
</dl>

<dl>
<dd>

**purchased_at_end:** `typing.Optional[datetime.datetime]` — 
Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999
    
</dd>
</dl>

<dl>
<dd>

**load_custom_fields:** `typing.Optional[bool]` — Load custom fields for the expenses.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — 
The cursor to use for pagination. This is the `next_cursor` value returned from the previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

<details><summary><code>client.card_expenses.<a href="src/fern/card_expenses/client.py">get_expense</a>(...) -> ExpandableExpense</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an expense by its ID.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.card_expenses.get_expense(
    expense_id="expense_id",
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

**expense_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand_array:** `typing.Optional[typing.List[str]]` — Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.
    
</dd>
</dl>

<dl>
<dd>

**load_custom_fields:** `typing.Optional[bool]` — Load custom fields for the expense.
    
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

<details><summary><code>client.card_expenses.<a href="src/fern/card_expenses/client.py">update_expense</a>(...) -> Expense</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.
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
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.card_expenses.update_expense(
    expense_id="expense_id",
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

**expense_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**memo:** `typing.Optional[str]` — Expense memo.
    
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

