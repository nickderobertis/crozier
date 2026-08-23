

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .additional_parameter import AdditionalParameter
from .metadata import Metadata


class DescriptionTypeAdditionalParameters(Metadata):
    parameters: typing.Optional[typing.List[AdditionalParameter]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
