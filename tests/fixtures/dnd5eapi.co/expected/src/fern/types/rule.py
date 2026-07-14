

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference


class Rule(ApiReference):
    """
    `Rule`
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the rule.
    """

    subsections: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of sections for each subheading underneath the rule in the SRD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
