

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service import Service


class Services(UniversalBaseModel):
    """
    A collection of objects that describe requests and responses for services.
    """

    service: typing_extensions.Annotated[Service, FieldMetadata(alias="SERVICE"), pydantic.Field(alias="SERVICE")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
