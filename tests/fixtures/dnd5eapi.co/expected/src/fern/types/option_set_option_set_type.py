

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OptionSetOptionSetType(UniversalBaseModel):
    option_set_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option set; determines other attributes.
    """

    resource_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    A reference (by URL) to a collection in the database.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
