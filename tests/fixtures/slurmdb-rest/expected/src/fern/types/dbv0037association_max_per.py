

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_per_account import Dbv0037AssociationMaxPerAccount


class Dbv0037AssociationMaxPer(UniversalBaseModel):
    """
    Max per settings
    """

    account: typing.Optional[Dbv0037AssociationMaxPerAccount] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
