# Reference
## AccountingAccount
<details><summary><code>client.accounting_account.<a href="src/fern/accounting_account/client.py">accounting_account_get_account</a>(...) -> AccountingGetAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of an account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_account.accounting_account_get_account(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_account.<a href="src/fern/accounting_account/client.py">accounting_account_delete_account</a>(...) -> AccountingDeleteAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_account.accounting_account_delete_account(
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

**id:** `str` 
    
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

<details><summary><code>client.accounting_account.<a href="src/fern/accounting_account/client.py">accounting_account_update_account</a>(...) -> AccountingCreateOrUpdateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_account.accounting_account_update_account(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccountingCreateOrUpdateAccountRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_account.<a href="src/fern/accounting_account/client.py">accounting_account_get_accounts</a>(...) -> AccountingGetAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the accounts
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_account.accounting_account_get_accounts()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_account.<a href="src/fern/accounting_account/client.py">accounting_account_create_account</a>(...) -> AccountingCreateOrUpdateAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Post Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_account.accounting_account_create_account(
    request={"key": "value"},
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

**request:** `AccountingCreateOrUpdateAccountRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AccountingExpense
<details><summary><code>client.accounting_expense.<a href="src/fern/accounting_expense/client.py">accounting_expense_get_expense</a>(...) -> AccountingGetExpenseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of an Expense
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_expense.accounting_expense_get_expense(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_expense.<a href="src/fern/accounting_expense/client.py">accounting_expense_delete_expense</a>(...) -> AccountingDeleteExpenseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Expense
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_expense.accounting_expense_delete_expense(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_expense.<a href="src/fern/accounting_expense/client.py">accounting_expense_update_expense</a>(...) -> AccountingCreateOrUpdateExpenseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Expense
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_expense.accounting_expense_update_expense(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccountingCreateOrUpdateExpenseRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_expense.<a href="src/fern/accounting_expense/client.py">accounting_expense_get_expenses</a>(...) -> AccountingGetExpensesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the expenses
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_expense.accounting_expense_get_expenses()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_expense.<a href="src/fern/accounting_expense/client.py">accounting_expense_create_expense</a>(...) -> AccountingCreateOrUpdateExpenseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Post Expense
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_expense.accounting_expense_create_expense(
    request={"key": "value"},
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

**request:** `AccountingCreateOrUpdateExpenseRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AccountingProxy
<details><summary><code>client.accounting_proxy.<a href="src/fern/accounting_proxy/client.py">accounting_proxy_tunnel</a>(...) -> AccountingProxyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the native Accounting app's api for a specific connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_proxy.accounting_proxy_tunnel(
    path="path",
    method="method",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Any]` 
    
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

## AccountingVendor
<details><summary><code>client.accounting_vendor.<a href="src/fern/accounting_vendor/client.py">accounting_vendor_get_vendor</a>(...) -> AccountingGetVendorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a Vendor
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_vendor.accounting_vendor_get_vendor(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_vendor.<a href="src/fern/accounting_vendor/client.py">accounting_vendor_delete_vendor</a>(...) -> AccountingDeleteVendorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Vendor
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_vendor.accounting_vendor_delete_vendor(
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

**id:** `str` 
    
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

<details><summary><code>client.accounting_vendor.<a href="src/fern/accounting_vendor/client.py">accounting_vendor_update_vendor</a>(...) -> AccountingCreateOrUpdateVendorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Vendor
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_vendor.accounting_vendor_update_vendor(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccountingCreateOrUpdateVendorRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_vendor.<a href="src/fern/accounting_vendor/client.py">accounting_vendor_get_vendors</a>(...) -> AccountingGetVendorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the Vendors
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_vendor.accounting_vendor_get_vendors()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.accounting_vendor.<a href="src/fern/accounting_vendor/client.py">accounting_vendor_create_vendor</a>(...) -> AccountingCreateOrUpdateVendorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Post Vendor
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.accounting_vendor.accounting_vendor_create_vendor(
    request={"key": "value"},
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

**request:** `AccountingCreateOrUpdateVendorRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AtsCandidate
<details><summary><code>client.ats_candidate.<a href="src/fern/ats_candidate/client.py">ats_candidate_get_candidate</a>(...) -> AtsGetCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a candidate.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_candidate.ats_candidate_get_candidate(
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

**id:** `str` — The unique `id` of the candidate.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_candidate.<a href="src/fern/ats_candidate/client.py">ats_candidate_delete_candidate</a>(...) -> AtsDeleteCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete details of an Candidate
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_candidate.ats_candidate_delete_candidate(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_candidate.<a href="src/fern/ats_candidate/client.py">ats_candidate_update_candidate</a>(...) -> AtsCreateOrUpdateCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Candidate
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_candidate.ats_candidate_update_candidate(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AtsCreateOrUpdateCandidateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_candidate.<a href="src/fern/ats_candidate/client.py">ats_candidate_get_candidates</a>(...) -> AtsGetCandidatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the Candidates.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_candidate.ats_candidate_get_candidates()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_candidate.<a href="src/fern/ats_candidate/client.py">ats_candidate_create_candidate</a>(...) -> AtsCreateOrUpdateCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Candidate
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_candidate.ats_candidate_create_candidate(
    request={"key": "value"},
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

**request:** `AtsCreateOrUpdateCandidateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AtsDepartment
<details><summary><code>client.ats_department.<a href="src/fern/ats_department/client.py">ats_department_get_department</a>(...) -> AtsGetDepartmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a department.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_department.ats_department_get_department(
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

**id:** `str` — The unique `id` of the department.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_department.<a href="src/fern/ats_department/client.py">ats_department_delete_department</a>(...) -> AtsDeleteDepartmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete details of an Department
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_department.ats_department_delete_department(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_department.<a href="src/fern/ats_department/client.py">ats_department_update_department</a>(...) -> AtsCreateOrUpdateDepartmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Department
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_department.ats_department_update_department(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AtsCreateOrUpdateDepartmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_department.<a href="src/fern/ats_department/client.py">ats_department_get_departments</a>(...) -> AtsGetDepartmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the departments.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_department.ats_department_get_departments()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_department.<a href="src/fern/ats_department/client.py">ats_department_create_department</a>(...) -> AtsCreateOrUpdateDepartmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Department
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_department.ats_department_create_department(
    request={"key": "value"},
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

**request:** `AtsCreateOrUpdateDepartmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AtsJob
<details><summary><code>client.ats_job.<a href="src/fern/ats_job/client.py">ats_job_get_job</a>(...) -> AtsGetJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a job.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_job.ats_job_get_job(
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

**id:** `str` — The unique `id` of the job.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_job.<a href="src/fern/ats_job/client.py">ats_job_delete_job</a>(...) -> AtsDeleteJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete details of an Job
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_job.ats_job_delete_job(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_job.<a href="src/fern/ats_job/client.py">ats_job_update_job</a>(...) -> AtsCreateOrUpdateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Job
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_job.ats_job_update_job(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AtsCreateOrUpdateJobRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_job.<a href="src/fern/ats_job/client.py">ats_job_get_jobs</a>(...) -> AtsGetJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the jobs.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_job.ats_job_get_jobs()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_job.<a href="src/fern/ats_job/client.py">ats_job_create_job</a>(...) -> AtsCreateOrUpdateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Job
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_job.ats_job_create_job(
    request={"key": "value"},
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

**request:** `AtsCreateOrUpdateJobRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AtsOffer
<details><summary><code>client.ats_offer.<a href="src/fern/ats_offer/client.py">ats_offer_get_offer</a>(...) -> AtsGetOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a offer.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_offer.ats_offer_get_offer(
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

**id:** `str` — The unique `id` of the offer.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_offer.<a href="src/fern/ats_offer/client.py">ats_offer_delete_offer</a>(...) -> AtsDeleteOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete details of an Offer
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_offer.ats_offer_delete_offer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_offer.<a href="src/fern/ats_offer/client.py">ats_offer_update_offer</a>(...) -> AtsCreateOrUpdateOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Offer
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_offer.ats_offer_update_offer(
    id="id",
    request={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AtsCreateOrUpdateOfferRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_offer.<a href="src/fern/ats_offer/client.py">ats_offer_get_offers</a>(...) -> AtsGetOffersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the offers.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_offer.ats_offer_get_offers()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats_offer.<a href="src/fern/ats_offer/client.py">ats_offer_create_offer</a>(...) -> AtsCreateOrUpdateOfferResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Offer
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_offer.ats_offer_create_offer(
    request={"key": "value"},
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

**request:** `AtsCreateOrUpdateOfferRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## AtsProxy
<details><summary><code>client.ats_proxy.<a href="src/fern/ats_proxy/client.py">ats_proxy_tunnel</a>(...) -> AtsProxyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the native ATS api for a specific connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ats_proxy.ats_proxy_tunnel(
    path="path",
    method="method",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Any]` 
    
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

## ChatChannels
<details><summary><code>client.chat_channels.<a href="src/fern/chat_channels/client.py">chat_channels_get_channels</a>(...) -> ChatGetChannelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the channels
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.chat_channels.chat_channels_get_channels()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## ChatMessages
<details><summary><code>client.chat_messages.<a href="src/fern/chat_messages/client.py">chat_messages_create_message</a>(...) -> ChatCreateorUpdateMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new message
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.chat_messages.chat_messages_create_message(
    text="text",
    channel_id="channelId",
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

**request:** `ChatCreateorUpdateMessageRequest` 
    
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

## ChatUsers
<details><summary><code>client.chat_users.<a href="src/fern/chat_users/client.py">chat_users_get_users</a>(...) -> ChatGetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the users
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.chat_users.chat_users_get_users()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## Connection
<details><summary><code>client.connection.<a href="src/fern/connection/client.py">getconnection</a>(...) -> GetConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a connection for a specific tenant.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.getconnection(
    revert_t_id="x-revert-t-id",
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">deleteconnection</a>(...) -> DeleteConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a connection for a specific tenant.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.deleteconnection(
    revert_t_id="x-revert-t-id",
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">getallconnections</a>() -> GetAllConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of all the connection for a specific account at Revert.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.getallconnections()

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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">getwebhook</a>(...) -> GetConnectionWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a connection webhook for a specific tenant.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.getwebhook(
    revert_t_id="x-revert-t-id",
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">createwebhook</a>(...) -> CreateConnectionWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook endpoint that listens to a connection events of a specific tenant.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.createwebhook(
    revert_t_id="x-revert-t-id",
    webhook_url="webhookUrl",
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `str` 
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">deletewebhook</a>(...) -> DeleteConnectionWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the connection webhook for a specific tenant.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.deletewebhook(
    revert_t_id="x-revert-t-id",
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">getintegrationstatus</a>(...) -> GetConnectStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the OAuth connection event status. This endpoint responds with a `http.ServerResponse` instead of `json`.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.getintegrationstatus(
    revert_public_token="revertPublicToken",
    tenant_id="tenantId",
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

**revert_public_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `str` 
    
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

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">importconnections</a>(...) -> ImportConnectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import multiple connections for a specific environment. Use this to bulk import connections as a one-time exercise.
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
from fern import FernApi, ConnectionImport
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.connection.importconnections(
    revert_t_id="x-revert-t-id",
    connections=[
        ConnectionImport(
            tp_id="hubspot",
            tp_access_token="tp_access_token",
            tp_refresh_token="tp_refresh_token",
            tp_customer_id="tp_customer_id",
            t_id="t_id",
            app_client_id="app_client_id",
            app_client_secret="app_client_secret",
            app_id="app_id",
        )
    ],
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

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
</dd>
</dl>

<dl>
<dd>

**connections:** `typing.List[ConnectionImport]` 
    
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

## CrmCompany
<details><summary><code>client.crm_company.<a href="src/fern/crm_company/client.py">crm_company_get_company</a>(...) -> CrmGetCompanyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a company
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_company.crm_company_get_company(
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

**id:** `str` — The unique `id` of the company in the CRM.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_company.<a href="src/fern/crm_company/client.py">crm_company_update_company</a>(...) -> CrmCreateOrUpdateCompanyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a company
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
from fern import FernApi, CommonCompanyAddress
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_company.crm_company_update_company(
    id_="id",
    id="id",
    remote_id="remoteId",
    created_timestamp={"key": "value"},
    updated_timestamp={"key": "value"},
    name="name",
    industry="industry",
    description="description",
    annual_revenue=1,
    size=1,
    phone="phone",
    address=CommonCompanyAddress(
        city="city",
        state="state",
        country="country",
        zip="zip",
        postal_code="postalCode",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CommonCompany` 
    
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

<details><summary><code>client.crm_company.<a href="src/fern/crm_company/client.py">crm_company_get_companies</a>(...) -> CrmGetCompaniesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the companies
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_company.crm_company_get_companies()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_company.<a href="src/fern/crm_company/client.py">crm_company_create_company</a>(...) -> CrmCreateOrUpdateCompanyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new company
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
from fern import FernApi, CommonCompanyAddress
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_company.crm_company_create_company(
    name="name",
    industry="industry",
    description="description",
    annual_revenue=1,
    size=1,
    phone="phone",
    address=CommonCompanyAddress(
        city="city",
        state="state",
        country="country",
        zip="zip",
        postal_code="postalCode",
    ),
    id="id",
    remote_id="remoteId",
    created_timestamp={"key": "value"},
    updated_timestamp={"key": "value"},
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

**name:** `str` — Name of the company in a CRM.
    
</dd>
</dl>

<dl>
<dd>

**industry:** `str` — Industry associated with this company. (not supported by pipedrive)
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the company. (not supported by pipedrive)
    
</dd>
</dl>

<dl>
<dd>

**annual_revenue:** `int` — Annual revenue of the company. (not supported by pipedrive)
    
</dd>
</dl>

<dl>
<dd>

**size:** `int` — Number of employees or size of the company.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `str` — Phone number of the company. (not supported by pipedrive)
    
</dd>
</dl>

<dl>
<dd>

**address:** `CommonCompanyAddress` — Company address.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique `id` of this object in Revert
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `str` — The unique `id` of this object in the downstream CRM.
    
</dd>
</dl>

<dl>
<dd>

**created_timestamp:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**updated_timestamp:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**additional:** `typing.Optional[typing.Any]` — Any fields that are not unified yet/non-unifiable come inside this `json` object.
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[CommonCompanyAssociation]` 
    
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

<details><summary><code>client.crm_company.<a href="src/fern/crm_company/client.py">crm_company_search_companies</a>(...) -> CrmSearchCompaniesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for companies
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_company.crm_company_search_companies(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmContact
<details><summary><code>client.crm_contact.<a href="src/fern/crm_contact/client.py">crm_contact_get_contact</a>(...) -> CrmGetContactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a contact
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_contact.crm_contact_get_contact(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_contact.<a href="src/fern/crm_contact/client.py">crm_contact_update_contact</a>(...) -> CrmCreateOrUpdateContactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a contact
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_contact.crm_contact_update_contact(
    id="id",
    first_name="firstName",
    last_name="lastName",
    phone="phone",
    email="email",
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateContactRequest` 
    
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

<details><summary><code>client.crm_contact.<a href="src/fern/crm_contact/client.py">crm_contact_get_contacts</a>(...) -> CrmGetContactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the contacts
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_contact.crm_contact_get_contacts()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_contact.<a href="src/fern/crm_contact/client.py">crm_contact_create_contact</a>(...) -> CrmCreateOrUpdateContactResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new contact
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_contact.crm_contact_create_contact(
    first_name="firstName",
    last_name="lastName",
    phone="phone",
    email="email",
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateContactRequest` 
    
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

<details><summary><code>client.crm_contact.<a href="src/fern/crm_contact/client.py">crm_contact_search_contacts</a>(...) -> CrmSearchContactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for contacts
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_contact.crm_contact_search_contacts(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmDeal
<details><summary><code>client.crm_deal.<a href="src/fern/crm_deal/client.py">crm_deal_get_deal</a>(...) -> CrmGetDealResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a deal
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_deal.crm_deal_get_deal(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_deal.<a href="src/fern/crm_deal/client.py">crm_deal_update_deal</a>(...) -> CrmCreateOrUpdateDealResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a deal
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_deal.crm_deal_update_deal(
    id="id",
    amount=1,
    stage="stage",
    name="name",
    expected_close_date={"key": "value"},
    is_won=True,
    probability=1,
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateDealRequest` 
    
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

<details><summary><code>client.crm_deal.<a href="src/fern/crm_deal/client.py">crm_deal_get_deals</a>(...) -> CrmGetDealsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the deals
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_deal.crm_deal_get_deals()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_deal.<a href="src/fern/crm_deal/client.py">crm_deal_create_deal</a>(...) -> CrmCreateOrUpdateDealResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new deal
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_deal.crm_deal_create_deal(
    amount=1,
    stage="stage",
    name="name",
    expected_close_date={"key": "value"},
    is_won=True,
    probability=1,
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateDealRequest` 
    
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

<details><summary><code>client.crm_deal.<a href="src/fern/crm_deal/client.py">crm_deal_search_deals</a>(...) -> CrmSearchDealsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for deals
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_deal.crm_deal_search_deals(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmEvent
<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_get_event</a>(...) -> CrmGetEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a event
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_get_event(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_delete_event</a>(...) -> CrmDeleteEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete details of an event in a CRM
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_delete_event(
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

**id:** `str` 
    
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

<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_update_event</a>(...) -> CrmCreateOrUpdateEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a event
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_update_event(
    id="id",
    type="type",
    subject="subject",
    start_date_time="startDateTime",
    end_date_time="endDateTime",
    is_all_day_event=True,
    description="description",
    location="location",
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateEventRequest` 
    
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

<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_get_events</a>(...) -> CrmGetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the events
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_get_events()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_create_event</a>(...) -> CrmCreateOrUpdateEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new event
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_create_event(
    type="type",
    subject="subject",
    start_date_time="startDateTime",
    end_date_time="endDateTime",
    is_all_day_event=True,
    description="description",
    location="location",
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateEventRequest` 
    
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

<details><summary><code>client.crm_event.<a href="src/fern/crm_event/client.py">crm_event_search_events</a>(...) -> CrmSearchEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for events
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_event.crm_event_search_events(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmLead
<details><summary><code>client.crm_lead.<a href="src/fern/crm_lead/client.py">crm_lead_get_lead</a>(...) -> CrmGetLeadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a lead
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_lead.crm_lead_get_lead(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_lead.<a href="src/fern/crm_lead/client.py">crm_lead_update_lead</a>(...) -> CrmCreateOrUpdateLeadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a lead
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_lead.crm_lead_update_lead(
    id="id",
    first_name="firstName",
    last_name="lastName",
    phone="phone",
    email="email",
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateLeadRequest` 
    
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

<details><summary><code>client.crm_lead.<a href="src/fern/crm_lead/client.py">crm_lead_get_leads</a>(...) -> CrmGetLeadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the leads
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_lead.crm_lead_get_leads()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_lead.<a href="src/fern/crm_lead/client.py">crm_lead_create_lead</a>(...) -> CrmCreateOrUpdateLeadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new lead
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_lead.crm_lead_create_lead(
    first_name="firstName",
    last_name="lastName",
    phone="phone",
    email="email",
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateLeadRequest` 
    
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

<details><summary><code>client.crm_lead.<a href="src/fern/crm_lead/client.py">crm_lead_search_leads</a>(...) -> CrmSearchLeadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for leads
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_lead.crm_lead_search_leads(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmNote
<details><summary><code>client.crm_note.<a href="src/fern/crm_note/client.py">crm_note_get_note</a>(...) -> CrmGetNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a note
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_note.crm_note_get_note(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_note.<a href="src/fern/crm_note/client.py">crm_note_update_note</a>(...) -> CrmCreateOrUpdateNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a note
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_note.crm_note_update_note(
    id="id",
    content="content",
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateNoteRequest` 
    
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

<details><summary><code>client.crm_note.<a href="src/fern/crm_note/client.py">crm_note_get_notes</a>(...) -> CrmGetNotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the notes
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_note.crm_note_get_notes()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_note.<a href="src/fern/crm_note/client.py">crm_note_create_note</a>(...) -> CrmCreateOrUpdateNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new note
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_note.crm_note_create_note(
    content="content",
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateNoteRequest` 
    
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

<details><summary><code>client.crm_note.<a href="src/fern/crm_note/client.py">crm_note_search_notes</a>(...) -> CrmSearchNotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for notes
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_note.crm_note_search_notes(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmProperties
<details><summary><code>client.crm_properties.<a href="src/fern/crm_properties/client.py">crm_properties_get_object_properties</a>(...) -> CrmGetObjectPropertiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get object properties for connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_properties.crm_properties_get_object_properties(
    object_name="company",
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

**object_name:** `CommonStandardObject` 
    
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

<details><summary><code>client.crm_properties.<a href="src/fern/crm_properties/client.py">crm_properties_set_custom_properties</a>(...) -> CrmSetObjectPropertiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set custom properties on an object for a given connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_properties.crm_properties_set_custom_properties(
    object_name="company",
    name="name",
    type="type",
    description="description",
    additional={"key": "value"},
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

**object_name:** `CommonStandardObject` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmSetObjectPropertiesRequest` 
    
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

## CrmProxy
<details><summary><code>client.crm_proxy.<a href="src/fern/crm_proxy/client.py">crm_proxy_tunnel</a>(...) -> CrmProxyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the native CRM api for a specific connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_proxy.crm_proxy_tunnel(
    path="path",
    method="method",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Any]` 
    
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

## CrmTask
<details><summary><code>client.crm_task.<a href="src/fern/crm_task/client.py">crm_task_get_task</a>(...) -> CrmGetTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a task
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_task.crm_task_get_task(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_task.<a href="src/fern/crm_task/client.py">crm_task_update_task</a>(...) -> CrmCreateOrUpdateTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a task
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_task.crm_task_update_task(
    id="id",
    additional={"key": "value"},
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CrmCreateOrUpdateTaskRequest` 
    
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

<details><summary><code>client.crm_task.<a href="src/fern/crm_task/client.py">crm_task_get_tasks</a>(...) -> CrmGetTasksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the tasks
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_task.crm_task_get_tasks()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_task.<a href="src/fern/crm_task/client.py">crm_task_create_task</a>(...) -> CrmCreateOrUpdateTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new task
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_task.crm_task_create_task(
    additional={"key": "value"},
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

**request:** `CrmCreateOrUpdateTaskRequest` 
    
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

<details><summary><code>client.crm_task.<a href="src/fern/crm_task/client.py">crm_task_search_tasks</a>(...) -> CrmSearchTasksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for tasks
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_task.crm_task_search_tasks(
    search_criteria={"key": "value"},
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

**search_criteria:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## CrmUser
<details><summary><code>client.crm_user.<a href="src/fern/crm_user/client.py">crm_user_get_user</a>(...) -> CrmGetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a user
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_user.crm_user_get_user(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_user.<a href="src/fern/crm_user/client.py">crm_user_get_users</a>(...) -> CrmGetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the users
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_user.crm_user_get_users()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**associations:** `typing.Optional[str]` 
    
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

<details><summary><code>client.crm_user.<a href="src/fern/crm_user/client.py">crm_user_create_user</a>(...) -> CrmCreateOrUpdateUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.crm_user.crm_user_create_user(
    first_name="firstName",
    last_name="lastName",
    phone="phone",
    email="email",
    additional={"key": "value"},
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

**first_name:** `str` — The first name of a user in a CRM.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — The last name of a user in a CRM.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `str` — The phone number of a user in a CRM.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email of a user in a CRM.
    
</dd>
</dl>

<dl>
<dd>

**additional:** `typing.Any` 
    
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

## Fieldmapping
<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">getfieldmappingconfig</a>(...) -> GetFieldMappingConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get field mappings configs for a connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.getfieldmappingconfig(
    revert_public_token="x-revert-public-token",
    revert_t_id="x-revert-t-id",
    revert_t_token="x-revert-t-token",
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

**revert_public_token:** `str` — Your public key, to be used on the frontend usually.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_token:** `str` — The temp used to identify tenant.
    
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

<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">createfieldmapping</a>(...) -> CreateFieldMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create field mappings for a connection after user input
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
from fern import FernApi, FieldMappingType
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.createfieldmapping(
    revert_public_token="x-revert-public-token",
    revert_t_id="x-revert-t-id",
    revert_t_token="x-revert-t-token",
    standard_mappings=[
        FieldMappingType(
            source_field_name="sourceFieldName",
            target_field_name="targetFieldName",
            object="object",
        )
    ],
    custom_mappings=[
        FieldMappingType(
            source_field_name="sourceFieldName",
            target_field_name="targetFieldName",
            object="object",
        )
    ],
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

**revert_public_token:** `str` — Your public key, to be used on the frontend usually.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_token:** `str` — The temp used to identify tenant.
    
</dd>
</dl>

<dl>
<dd>

**standard_mappings:** `typing.List[FieldMappingType]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_mappings:** `typing.List[FieldMappingType]` 
    
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

<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">deletefieldmapping</a>(...) -> DeleteFieldMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete field mappings for a connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.deletefieldmapping(
    revert_api_token="x-revert-api-token",
    revert_t_id="x-revert-t-id",
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

**revert_api_token:** `str` — Your official API key for accessing revert apis.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">getfieldmappings</a>(...) -> GetFieldMappingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get field mappings for a connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.getfieldmappings(
    revert_api_token="x-revert-api-token",
    revert_t_id="x-revert-t-id",
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

**revert_api_token:** `str` — Your official API key for accessing revert apis.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
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

<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">createaccountfieldmappingconfig</a>(...) -> CreateAccountFieldMappingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create field mappings config for an account
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
from fern import FernApi, MappableFieldType
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.createaccountfieldmappingconfig(
    revert_api_token="x-revert-api-token",
    allow_connection_override_custom_fields=True,
    mappable_by_connection_field_list=[
        MappableFieldType(
            field_name="fieldName",
            object_name="company",
        )
    ],
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

**revert_api_token:** `str` — Your official API key for accessing revert apis.
    
</dd>
</dl>

<dl>
<dd>

**allow_connection_override_custom_fields:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**mappable_by_connection_field_list:** `typing.List[MappableFieldType]` 
    
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

<details><summary><code>client.fieldmapping.<a href="src/fern/fieldmapping/client.py">deleteaccountfieldmappingconfig</a>(...) -> DeleteAccountFieldMappingConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete field mappings config for an account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.fieldmapping.deleteaccountfieldmappingconfig(
    revert_api_token="x-revert-api-token",
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

**revert_api_token:** `str` — Your official API key for accessing revert apis.
    
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

## InternalAccount
<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_get_account_details</a>(...) -> InternalGetAccountDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a revert user account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_get_account_details(
    user_id="userId",
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

**user_id:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_update_account_credentials</a>(...) -> CommonApp</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update account credentials (customer app token, secret, scope)
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_update_account_credentials(
    tp_id="hubspot",
    is_revert_app=True,
    app_id="appId",
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

**tp_id:** `CommonTpid` 
    
</dd>
</dl>

<dl>
<dd>

**is_revert_app:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**app_config:** `typing.Optional[CommonAppConfig]` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_create_revert_app_for_account</a>(...) -> InternalGetAccountDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

create Revert App for Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_create_revert_app_for_account(
    user_id="userId",
    tp_id="hubspot",
    environment="environment",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tp_id:** `CommonTpid` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_delete_revert_appfor_account</a>(...) -> InternalDeleteRevertAppResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

delete Revert App for Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_delete_revert_appfor_account(
    app_id="appId",
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

**app_id:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_get_svix_account</a>(...) -> InternalSvixAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Svix Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_get_svix_account(
    id="id",
    environment="environment",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_create_svix_account</a>(...) -> InternalSvixAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Svix Account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_create_svix_account(
    environment="environment",
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

**environment:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_create_svix_account_magic_link</a>(...) -> InternalSvixMagicLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Svix Account Consumer Panel MagicLink
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_create_svix_account_magic_link(
    app_id="appId",
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

**app_id:** `str` 
    
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

<details><summary><code>client.internal_account.<a href="src/fern/internal_account/client.py">internal_account_set_onboarding_completed</a>(...) -> InternalsetOnboardingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set Onboarding Completed
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_account.internal_account_set_onboarding_completed(
    user_id="userId",
    environment="environment",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` 
    
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

## InternalAnalytics
<details><summary><code>client.internal_analytics.<a href="src/fern/internal_analytics/client.py">internal_analytics_get_analytics</a>(...) -> InternalGetAnalyticsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Analytics of your revert account
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_analytics.internal_analytics_get_analytics(
    user_id="userId",
    environment="environment",
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

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `str` 
    
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

## InternalApp
<details><summary><code>client.internal_app.<a href="src/fern/internal_app/client.py">internal_app_get_recent_api_calls_for_app</a>(...) -> InternalRecentAppApiCallsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Recent api calls for App
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_app.internal_app_get_recent_api_calls_for_app(
    app_id="appId",
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

**app_id:** `str` 
    
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

## InternalTelemetry
<details><summary><code>client.internal_telemetry.<a href="src/fern/internal_telemetry/client.py">internal_telemetry_create_telemetry_entry</a>(...) -> InternalCreateTelemetryEntryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create telemetry entry for a deployment
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.internal_telemetry.internal_telemetry_create_telemetry_entry(
    number_of_users=1,
    number_of_accounts=1,
    number_of_connections=1,
    number_of_api_calls=1,
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

**number_of_users:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_accounts:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_connections:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_api_calls:** `int` 
    
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

## Metadata
<details><summary><code>client.metadata.<a href="src/fern/metadata/client.py">getcrms</a>() -> CrmMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of CRMs available for this account from the database based on the public token.
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.metadata.getcrms()

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

## Sync
<details><summary><code>client.sync.<a href="src/fern/sync/client.py">triggersync</a>(...) -> TriggerSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger sync for a specific tenant
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.sync.triggersync(
    revert_api_token="x-revert-api-token",
    revert_t_id="x-revert-t-id",
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

**revert_api_token:** `str` — Your official API key for accessing revert apis.
    
</dd>
</dl>

<dl>
<dd>

**revert_t_id:** `str` — The unique customer id used when the customer linked their account.
    
</dd>
</dl>

<dl>
<dd>

**connection_api_key:** `typing.Optional[str]` — API key for third party provider
    
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

## TicketCollection
<details><summary><code>client.ticket_collection.<a href="src/fern/ticket_collection/client.py">ticket_collection_get_collections</a>(...) -> TicketGetCollectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the collections
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_collection.ticket_collection_get_collections()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

## TicketComment
<details><summary><code>client.ticket_comment.<a href="src/fern/ticket_comment/client.py">ticket_comment_get_comment</a>(...) -> TicketGetCommentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a comment
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_comment.ticket_comment_get_comment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_comment.<a href="src/fern/ticket_comment/client.py">ticket_comment_update_comment</a>(...) -> TicketCreateOrUpdateCommentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update comment
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_comment.ticket_comment_update_comment(
    id="id",
    body="body",
    task_id="taskId",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TicketCreateOrUpdateCommentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_comment.<a href="src/fern/ticket_comment/client.py">ticket_comment_get_comments</a>(...) -> TicketGetCommentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the comments
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_comment.ticket_comment_get_comments()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_comment.<a href="src/fern/ticket_comment/client.py">ticket_comment_create_comment</a>(...) -> TicketCreateOrUpdateCommentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Post comment
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_comment.ticket_comment_create_comment(
    body="body",
    task_id="taskId",
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

**request:** `TicketCreateOrUpdateCommentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## TicketProxy
<details><summary><code>client.ticket_proxy.<a href="src/fern/ticket_proxy/client.py">ticket_proxy_tunnel</a>(...) -> TicketProxyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call the native Ticketing app's api for a specific connection
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_proxy.ticket_proxy_tunnel(
    path="path",
    method="method",
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Any]` 
    
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

## TicketTask
<details><summary><code>client.ticket_task.<a href="src/fern/ticket_task/client.py">ticket_task_get_task</a>(...) -> TicketGetTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a task
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_task.ticket_task_get_task(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_task.<a href="src/fern/ticket_task/client.py">ticket_task_update_task</a>(...) -> TicketCreateOrUpdateTaskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a task
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_task.ticket_task_update_task(
    id="id",
    name="name",
    assignees=[
        "assignees"
    ],
    description="description",
    status="open",
    priority="urgent",
    creator_id="creatorId",
    due_date="dueDate",
    completed_date="completedDate",
    parent_id="parentId",
    list_id="listId",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TicketCreateOrUpdateTaskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_task.<a href="src/fern/ticket_task/client.py">ticket_task_get_tasks</a>(...) -> TicketGetTasksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the tasks
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_task.ticket_task_get_tasks()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_task.<a href="src/fern/ticket_task/client.py">ticket_task_create_task</a>(...) -> TicketCreateOrUpdateTaskResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_task.ticket_task_create_task(
    name="name",
    assignees=[
        "assignees"
    ],
    description="description",
    status="open",
    priority="urgent",
    creator_id="creatorId",
    due_date="dueDate",
    completed_date="completedDate",
    parent_id="parentId",
    list_id="listId",
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

**request:** `TicketCreateOrUpdateTaskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

## TicketUser
<details><summary><code>client.ticket_user.<a href="src/fern/ticket_user/client.py">ticket_user_get_user</a>(...) -> TicketGetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a user
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_user.ticket_user_get_user(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ticket_user.<a href="src/fern/ticket_user/client.py">ticket_user_get_users</a>(...) -> TicketGetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the users
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.ticket_user.ticket_user_get_users()

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

**fields:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
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

