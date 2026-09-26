

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ccs_project import CcsProject
from .data_flow import DataFlow


class DefaultValues(UniversalBaseModel):
    ccs_project: CcsProject
    dataflow: typing.Optional[DataFlow] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
