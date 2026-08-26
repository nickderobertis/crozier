

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .setup_root_error_type import SetupRootErrorType


class SetupRootError(UniversalBaseModel):
    edges_with_vars: typing.List[typing.List[typing.Any]]
    type: SetupRootErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
