

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cle_definitions import CleDefinitions
from .cle_event import CleEvent


class Cle(UniversalBaseModel):
    """
    Common Lifecycle Enumeration (CLE) object based on ECMA-428 TC54 TG3 CLE Specification v1.0.0.
    Contains lifecycle events and optional reusable definitions for a component or product.
    """

    events: typing.List[CleEvent] = pydantic.Field()
    """
    Ordered array of CLE Event objects representing lifecycle events.
    MUST be ordered by ID in descending order (newest events with highest IDs first).
    """

    definitions: typing.Optional[CleDefinitions] = pydantic.Field(default=None)
    """
    Container for reusable policy definitions referenced by events
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
