

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_capability_type import FilterCapabilityType


class FilterCapability(UniversalBaseModel):
    """
    Describes a search filter field the implementation supports. The `type` tells clients which UI element suits the field (e.g. a date picker for `date`, a toggle for `boolean`) and which request syntax the field accepts: `date` and `number` filters accept a single range object or a non-empty array of range objects (matched as an OR of the ranges) as well as an array of values; `string` and `boolean` filters accept an array of values only.

    New filter types are added by revision of this specification; clients MUST hide filters with a `type` value they do not recognise rather than fail.
    """

    type: FilterCapabilityType = pydantic.Field()
    """
    The filter's value type. `date` values are ISO 8601 strings. `boolean` values are the strings `"true"` and `"false"`.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional human-readable display label for the filter field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
