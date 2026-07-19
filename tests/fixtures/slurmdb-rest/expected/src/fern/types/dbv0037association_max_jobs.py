

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_jobs_per import Dbv0037AssociationMaxJobsPer


class Dbv0037AssociationMaxJobs(UniversalBaseModel):
    """
    Max jobs settings
    """

    per: typing.Optional[Dbv0037AssociationMaxJobsPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
