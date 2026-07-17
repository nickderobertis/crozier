# Reference
## PayrollAu
<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_employees</a>(...) -> Employees</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_employees(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 employees will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_employee</a>(...) -> Employees</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Employee
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_employee(
    request=[
        Employee(
            date_of_birth="/Date(322560000000+0000)/",
            first_name="Karen",
            last_name="Jones",
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

**request:** `typing.List[Employee]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_employee</a>(...) -> Employees</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_employee(
    employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**employee_id:** `str` — Employee id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_employee</a>(...) -> Employees</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties on a single employee
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
from fern import FernApi, Employee
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_employee(
    employee_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        Employee(
            date_of_birth="/Date(322560000000+0000)/",
            first_name="Karen",
            last_name="Jones",
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

**employee_id:** `str` — Employee id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[Employee]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_leave_applications</a>(...) -> LeaveApplications</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_leave_applications(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 objects will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_leave_application</a>(...) -> LeaveApplications</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LeaveApplication
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_leave_application(
    request=[
        LeaveApplication()
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

**request:** `typing.List[LeaveApplication]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_leave_application</a>(...) -> LeaveApplications</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_leave_application(
    leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**leave_application_id:** `str` — Leave Application id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_leave_application</a>(...) -> LeaveApplications</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LeaveApplication
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_leave_application(
    leave_application_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        LeaveApplication()
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

**leave_application_id:** `str` — Leave Application id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[LeaveApplication]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_pay_items</a>(...) -> PayItems</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_pay_items(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 objects will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_pay_item</a>(...) -> PayItems</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_pay_item()

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

**request:** `PayItem` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_pay_runs</a>(...) -> PayRuns</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_pay_runs(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 PayRuns will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_pay_run</a>(...) -> PayRuns</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PayRun
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_pay_run(
    request=[
        PayRun(
            payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
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

**request:** `typing.List[PayRun]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_pay_run</a>(...) -> PayRuns</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_pay_run(
    pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**pay_run_id:** `str` — PayRun id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_pay_run</a>(...) -> PayRuns</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties on a single PayRun
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
from fern import FernApi, PayRun
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_pay_run(
    pay_run_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        PayRun(
            payroll_calendar_id="bfac31bd-ea62-4fc8-a5e7-7965d9504b15",
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

**pay_run_id:** `str` — PayRun id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PayRun]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_payroll_calendars</a>(...) -> PayrollCalendars</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_payroll_calendars(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 objects will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_payroll_calendar</a>(...) -> PayrollCalendars</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PayrollCalendar
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_payroll_calendar(
    request=[
        PayrollCalendar()
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

**request:** `typing.List[PayrollCalendar]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_payroll_calendar</a>(...) -> PayrollCalendars</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_payroll_calendar(
    payroll_calendar_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**payroll_calendar_id:** `str` — Payroll Calendar id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_payslip</a>(...) -> PayslipObject</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_payslip(
    payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**payslip_id:** `str` — Payslip id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_payslip</a>(...) -> Payslips</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update lines on a single payslips
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
from fern import FernApi, PayslipLines
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_payslip(
    payslip_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        PayslipLines()
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

**payslip_id:** `str` — Payslip id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PayslipLines]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_settings</a>() -> SettingsObject</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_settings()

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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_superfund_products</a>(...) -> SuperFundProducts</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_superfund_products(
    usi="OSF0001AU",
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

**abn:** `typing.Optional[str]` — The ABN of the Regulated SuperFund
    
</dd>
</dl>

<dl>
<dd>

**usi:** `typing.Optional[str]` — The USI of the Regulated SuperFund
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_superfunds</a>(...) -> SuperFunds</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_superfunds(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_superfund</a>(...) -> SuperFunds</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SuperFund, SuperFundType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_superfund(
    request=[
        SuperFund(
            type=SuperFundType.REGULATED,
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

**request:** `typing.List[SuperFund]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_superfund</a>(...) -> SuperFunds</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_superfund(
    super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**super_fund_id:** `str` — Superfund id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_superfund</a>(...) -> SuperFunds</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties on a single Superfund
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
from fern import FernApi, SuperFund, SuperFundType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_superfund(
    super_fund_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        SuperFund(
            type=SuperFundType.REGULATED,
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

**super_fund_id:** `str` — Superfund id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[SuperFund]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_timesheets</a>(...) -> Timesheets</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_timesheets(
    where="Status==\"ACTIVE\"",
    order="EmailAddress%20DESC",
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

**where:** `typing.Optional[str]` — Filter by an any element
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Order by an any element
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — e.g. page=1 – Up to 100 timesheets will be returned in a single API call
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` — Only records created or modified since this timestamp will be returned
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">create_timesheet</a>(...) -> Timesheets</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Timesheet
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.create_timesheet(
    request=[
        Timesheet(
            employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
            end_date="/Date(322560000000+0000)/",
            start_date="/Date(322560000000+0000)/",
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

**request:** `typing.List[Timesheet]` 
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">get_timesheet</a>(...) -> TimesheetObject</code></summary>
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
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.get_timesheet(
    timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
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

**timesheet_id:** `str` — Timesheet id for single object
    
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

<details><summary><code>client.payroll_au.<a href="src/fern/payroll_au/client.py">update_timesheet</a>(...) -> Timesheets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update properties on a single timesheet
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
from fern import FernApi, Timesheet
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    xero_tenant_id="<Xero-Tenant-Id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.payroll_au.update_timesheet(
    timesheet_id="4ff1e5cc-9835-40d5-bb18-09fdb118db9c",
    request=[
        Timesheet(
            employee_id="72a0d0c2-0cf8-4f0b-ade1-33231f47b41b",
            end_date="/Date(322560000000+0000)/",
            start_date="/Date(322560000000+0000)/",
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

**timesheet_id:** `str` — Timesheet id for single object
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[Timesheet]` 
    
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

