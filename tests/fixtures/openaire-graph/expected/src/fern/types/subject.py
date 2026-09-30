

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provenance import Provenance
from .subject_scheme_value import SubjectSchemeValue


class Subject(UniversalBaseModel):
    subject: typing.Optional[SubjectSchemeValue] = None
    provenance: typing.Optional[Provenance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
