

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cle_support_definition import CleSupportDefinition


class CleDefinitions(UniversalBaseModel):
    """
    Container for reusable CLE policy definitions
    """

    support: typing.Optional[typing.List[CleSupportDefinition]] = pydantic.Field(default=None)
    """
    List of support policies
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
