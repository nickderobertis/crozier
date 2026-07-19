

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_short_info import Dbv0037AssociationShortInfo


class Dbv0037UserAssociations(UniversalBaseModel):
    """
    Assigned associations
    """

    root: typing.Optional[Dbv0037AssociationShortInfo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
