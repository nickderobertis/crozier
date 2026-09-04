

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .disbursement import Disbursement


class Disbursements(UniversalBaseModel):
    disbursements: typing.List[Disbursement] = pydantic.Field()
    """
    Contains a list of all disbursements related to the specified grant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
