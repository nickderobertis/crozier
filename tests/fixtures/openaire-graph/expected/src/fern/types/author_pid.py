

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .author_pid_scheme_value import AuthorPidSchemeValue
from .provenance import Provenance


class AuthorPid(UniversalBaseModel):
    id: typing.Optional[AuthorPidSchemeValue] = None
    provenance: typing.Optional[Provenance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
