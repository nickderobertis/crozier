

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class OptionAlignments(UniversalBaseModel):
    alignments: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    A list of alignments of those who might follow the ideal.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the ideal.
    """

    option_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of option; determines other attributes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
