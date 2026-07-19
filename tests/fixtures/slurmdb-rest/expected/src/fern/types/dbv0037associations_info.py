

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association import Dbv0037Association
from .dbv0037error import Dbv0037Error


class Dbv0037AssociationsInfo(UniversalBaseModel):
    errors: typing.Optional[typing.List[Dbv0037Error]] = pydantic.Field(default=None)
    """
    Slurm errors
    """

    associations: typing.Optional[typing.List[Dbv0037Association]] = pydantic.Field(default=None)
    """
    Array of associations
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
