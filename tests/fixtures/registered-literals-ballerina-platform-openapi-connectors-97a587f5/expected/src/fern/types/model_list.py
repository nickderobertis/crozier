

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model import Model
from .type_discriminator import TypeDiscriminator


class ModelList(UniversalBaseModel):
    """
    Represents a list of models.
    """

    object: typing.Optional[TypeDiscriminator] = None
    data: typing.Optional[typing.List[Model]] = pydantic.Field(default=None)
    """
    The list of items.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
