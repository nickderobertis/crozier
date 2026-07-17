# Reference
## Operations
<details><summary><code>client.operations.<a href="src/fern/operations/client.py">get_museum_hours</a>(...) -> MuseumHours</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get upcoming museum operating hours.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.operations.get_museum_hours(
    start_date=datetime.date.fromisoformat("2023-02-23"),
    page=2,
    limit=15,
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

**start_date:** `typing.Optional[datetime.date]` — Starting date to retrieve future operating hours from. Defaults to today's date.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of days per page.
    
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

## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">list_special_events</a>(...) -> SpecialEventCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a list of upcoming special events at the museum.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.list_special_events(
    start_date=datetime.date.fromisoformat("2023-02-23"),
    end_date=datetime.date.fromisoformat("2023-04-18"),
    page=2,
    limit=15,
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

**start_date:** `typing.Optional[datetime.date]` — Starting date to retrieve future operating hours from. Defaults to today's date.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End of a date range to retrieve special events for. Defaults to 7 days after `startDate`.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of days per page.
    
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">create_special_event</a>(...) -> SpecialEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new special event for the museum.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.create_special_event(
    name="Mermaid Treasure Identification and Analysis",
    location="Under the seaaa 🦀 🎶 🌊.",
    event_description="Join us as we review and classify a rare collection of 20 thingamabobs, gadgets, gizmos, whoosits, and whatsits, kindly donated by Ariel.",
    dates=[
        datetime.date.fromisoformat("2023-09-05"),
        datetime.date.fromisoformat("2023-09-08")
    ],
    price=0,
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

**request:** `SpecialEvent` 
    
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">get_special_event</a>(...) -> SpecialEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a special event.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_special_event(
    event_id="dad4bce8-f5cb-4078-a211-995864315e39",
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

**event_id:** `str` — Identifier for a special event.
    
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">delete_special_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a special event from the collection. Allows museum to cancel planned events.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.delete_special_event(
    event_id="dad4bce8-f5cb-4078-a211-995864315e39",
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

**event_id:** `str` — Identifier for a special event.
    
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">update_special_event</a>(...) -> SpecialEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a special event.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.update_special_event(
    event_id="dad4bce8-f5cb-4078-a211-995864315e39",
    location="On the beach.",
    price=15,
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

**event_id:** `str` — Identifier for a special event.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[EventName]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[EventLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**event_description:** `typing.Optional[EventDescription]` 
    
</dd>
</dl>

<dl>
<dd>

**dates:** `typing.Optional[EventDates]` 
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[EventPrice]` 
    
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

## Tickets
<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">buy_museum_tickets</a>(...) -> MuseumTicketsConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purchase museum tickets for general entry or special events.
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
from fern import FernApi, TicketType
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tickets.buy_museum_tickets(
    ticket_date=datetime.date.fromisoformat("2023-09-07"),
    ticket_type=TicketType.GENERAL,
    email="todd@example.com",
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

**ticket_date:** `Date` — Date when this ticket can be used for museum entry.
    
</dd>
</dl>

<dl>
<dd>

**ticket_type:** `TicketType` 
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `typing.Optional[TicketId]` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[EventId]` — Unique identifier for a special event. Required if purchasing tickets for the museum's special events.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[Email]` 
    
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

<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">get_ticket_code</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return an image of your ticket with scannable QR code. Used for event entry.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tickets.get_ticket_code(
    ticket_id="ticketId",
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

**ticket_id:** `str` — Identifier for a ticket to a museum event. Used to generate ticket image.
    
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

