

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ignored_parameters_unsupported import IgnoredParametersUnsupported


class EditNavigationViewResponse(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    ignored_parameters_unsupported: typing.Optional[IgnoredParametersUnsupported] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
