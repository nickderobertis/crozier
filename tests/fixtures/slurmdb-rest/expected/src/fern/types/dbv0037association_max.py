

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_jobs import Dbv0037AssociationMaxJobs
from .dbv0037association_max_per import Dbv0037AssociationMaxPer
from .dbv0037association_max_tres import Dbv0037AssociationMaxTres


class Dbv0037AssociationMax(UniversalBaseModel):
    """
    Max settings
    """

    jobs: typing.Optional[Dbv0037AssociationMaxJobs] = None
    per: typing.Optional[Dbv0037AssociationMaxPer] = None
    tres: typing.Optional[Dbv0037AssociationMaxTres] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
