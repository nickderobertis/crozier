

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomerCreationSourceFilter(UniversalBaseModel):
    """
    The creation source filter.

    If one or more creation sources are set, customer profiles are included in,
    or excluded from, the result if they match at least one of the filter criteria.
    """

    rule: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether a customer profile matching the filter criteria
    should be included in the result or excluded from the result.
    
    Default: `INCLUDE`.
    """

    values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of creation sources used as filtering criteria.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
