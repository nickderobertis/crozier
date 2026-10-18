

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadRequestErrorBodyOne(UniversalBaseModel):
    """
    An example JSON response when the user group being deactivated
    is used for a setting or as a subgroup.

    **Changes**: New in Zulip 10.0 (feature level 298). Previously,
    this error returned the `"BAD_REQUEST"` code.
    """

    result: typing.Any
    msg: typing.Any
    code: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
