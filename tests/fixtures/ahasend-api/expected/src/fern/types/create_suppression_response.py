

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_suppression_response_object import CreateSuppressionResponseObject
from .suppression import Suppression


class CreateSuppressionResponse(UniversalBaseModel):
    object: CreateSuppressionResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[Suppression] = pydantic.Field()
    """
    Array of suppressions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
