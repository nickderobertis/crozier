

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .consent_grant_allowed_channels_item import ConsentGrantAllowedChannelsItem
from .consent_grant_scope_item import ConsentGrantScopeItem


class ConsentGrant(UniversalBaseModel):
    """
    Explicit consent record for a single `lead.submit` submission. Required whenever a `lead.submit.request` includes customer contact info (which is always — `customer` is required on the unified lead). Provides an auditable record of what the user authorized, when, through which channels, and via which buyer agent.

    Error-code mapping: a dealer agent MUST reject lead submissions with `CONTACT_CONSENT_REQUIRED` if `consent` is missing entirely; with `INVALID_CONSENT` if the grant is malformed, `expires_at` has passed at the time the dealer would use the contact data, or the dealer intends to use a contact channel not present in `allowed_channels`.
    """

    granted_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 / RFC 3339 timestamp at which the user authorized this share (e.g. '2026-04-30T11:05:00Z'). MUST include a timezone offset (Z or ±HH:MM).
    """

    allowed_channels: typing.List[ConsentGrantAllowedChannelsItem] = pydantic.Field()
    """
    Channels the user has authorized the dealer to use for follow-up.
    """

    consent_text: str = pydantic.Field()
    """
    Verbatim text the user agreed to (e.g. the disclosure shown by the buyer agent). MUST be non-empty — this is the audit trail of what the user actually saw.
    """

    source_agent: str = pydantic.Field()
    """
    Identifier of the buyer agent that captured the consent (e.g. 'chatgpt-shopping', 'gemini-assistant', 'lumika-bdc').
    """

    scope: typing.List[ConsentGrantScopeItem] = pydantic.Field()
    """
    Scope of the consent. AAP defines a single value `lead_submission` covering the unified `lead.submit` skill (which spans general inquiries, vehicle interest, trade-in, and appointments). The request body itself shows what was actually submitted; the meaningful audit granularity is `allowed_channels`.
    """

    expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Optional ISO 8601 / RFC 3339 timestamp after which this consent grant is no longer valid (e.g. '2027-04-30T11:05:00Z'). Useful for jurisdictions with mandatory re-consent windows (some US state TCPA-style rules cap consent at ~12 months for SMS). The dealer MUST reject `lead.submit` with `INVALID_CONSENT` if `expires_at` is in the past at the time the dealer would use the contact data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
