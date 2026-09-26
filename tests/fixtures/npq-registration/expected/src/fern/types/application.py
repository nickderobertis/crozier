

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_attributes import ApplicationAttributes
from .application_type import ApplicationType
from .id_attribute import IdAttribute


class Application(UniversalBaseModel):
    """
    A single NPQ application
    """

    id: IdAttribute
    type: ApplicationType = pydantic.Field()
    """
    The data type
    """

    attributes: ApplicationAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
