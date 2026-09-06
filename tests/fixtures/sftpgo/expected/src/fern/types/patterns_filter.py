

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PatternsFilter(UniversalBaseModel):
    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    virtual path as seen by users, if no other specific filter is defined, the filter applies for sub directories too. For example if filters are defined for the paths "/" and "/sub" then the filters for "/" are applied for any file outside the "/sub" directory
    """

    allowed_patterns: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of, case insensitive, allowed shell like patterns. Allowed patterns are evaluated before the denied ones
    """

    denied_patterns: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    list of, case insensitive, denied shell like patterns
    """

    deny_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    Policies for denied patterns
      * `0` - default policy. Denied files/directories matching the filters are visible in directory listing but cannot be uploaded/downloaded/overwritten/renamed
      * `1` - deny policy hide. This policy applies the same restrictions as the default one and denied files/directories matching the filters will also be hidden in directory listing. This mode may cause performance issues for large directories
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
