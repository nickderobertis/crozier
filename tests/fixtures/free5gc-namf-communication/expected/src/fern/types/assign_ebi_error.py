

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assign_ebi_failed import AssignEbiFailed
from .problem_details import ProblemDetails


class AssignEbiError(UniversalBaseModel):
    error: ProblemDetails
    failure_details: typing_extensions.Annotated[
        AssignEbiFailed, FieldMetadata(alias="failureDetails"), pydantic.Field(alias="failureDetails")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
