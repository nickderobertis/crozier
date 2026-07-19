

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobStepStepHet(UniversalBaseModel):
    """
    Heterogeneous job details
    """

    component: typing.Optional[int] = pydantic.Field(default=None)
    """
    Parent HetJob component id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
