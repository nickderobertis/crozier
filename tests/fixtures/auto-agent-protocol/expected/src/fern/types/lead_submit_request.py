

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .appointment import Appointment
from .consent_grant import ConsentGrant
from .customer import Customer
from .lead_submit_request_type import LeadSubmitRequestType
from .vehicle import Vehicle


class LeadSubmitRequest(UniversalBaseModel):
    """
    Unified lead submission for the `lead.submit` AAP skill. A single request carries the consented customer plus any combination of `vehicle_of_interest`, `trade_in`, and `appointment` — matching how dealerships actually take leads (e.g. test-drive a new car while getting a trade-in appraised in the same visit).

    Design principle: capture whatever the customer actually provided. `vehicle_of_interest`, `trade_in`, and `appointment` are entirely optional, and within them no individual field is required at the schema level — the buyer agent should pass through whatever pieces of information the user shared (a VIN, a make+model, just a year, mileage only — anything is welcome). The dealer is responsible for handling partial input gracefully.

    Validation rules:
    - `customer` and `consent` are always required (lead is never anonymous; consent is always required).
    - If `vehicle_of_interest.condition` is set, it MUST be one of `new`, `used`, `cpo`.
    - If `trade_in.condition` is set, it MUST be one of `excellent`, `good`, `fair`, `poor`.
    - `consent.scope` MUST be `["lead_submission"]`.

    Carried inside an A2A `Message.parts[].data` DataPart via `SendMessage` (JSON-RPC 2.0 or HTTP+JSON binding).
    """

    type: LeadSubmitRequestType = pydantic.Field()
    """
    AAP message type discriminator.
    """

    customer: Customer = pydantic.Field()
    """
    Buyer contact info. Required.
    """

    consent: ConsentGrant = pydantic.Field()
    """
    Consent record covering this submission. Required. `scope` MUST be ["lead_submission"].
    """

    vehicle_of_interest: typing.Optional[Vehicle] = pydantic.Field(default=None)
    """
    The vehicle the buyer is interested in purchasing. Optional. Pass through whatever the customer provided (VIN alone, year+make+model, just a model name, etc.) — no individual field is required. When `condition` is set it MUST be one of `new` | `used` | `cpo`.
    """

    trade_in: typing.Optional[Vehicle] = pydantic.Field(default=None)
    """
    The vehicle the buyer wants to trade in. Optional. Pass through whatever the customer provided (just a make+model and a mileage is a perfectly valid trade-in lead). When `condition` is set it MUST be one of `excellent` | `good` | `fair` | `poor`. Pricing fields are typically absent on the request side and are populated by the dealer's appraisal response.
    """

    appointment: typing.Optional[Appointment] = pydantic.Field(default=None)
    """
    An appointment request the buyer wants scheduled alongside this lead. Optional. `appointment_type` is one of `sales` | `service` | `test_drive` | `trade_in`, and `appointment_at` is the requested start time. The vehicle for the appointment is implicit: `vehicle_of_interest` for a test drive, `trade_in` for a trade-in appraisal.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional free-text message from the buyer to the dealer.
    """

    source_agent: str = pydantic.Field()
    """
    Identifier of the buyer agent that originated this lead (e.g. 'chatgpt-shopping', 'gemini-assistant', 'lumika-bdc'). Used for analytics and consent attribution.
    """

    submitted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO 8601 / RFC 3339 timestamp at which the buyer agent finalized this submission (e.g. '2026-04-30T11:05:08Z').
    """

    idempotency_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional client-generated key (UUID recommended) the dealer agent uses to dedupe retried submissions. Two requests carrying the same `idempotency_key` MUST produce the same response (the dealer returns the original `lead_id` and status). Strongly RECOMMENDED for production buyer agents that retry on network failure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
