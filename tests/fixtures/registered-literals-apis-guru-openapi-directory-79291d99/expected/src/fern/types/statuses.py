

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .status import Status


class Statuses(UniversalBaseModel):
    """
    A collection of STATUS containers.
    """

    status: typing_extensions.Annotated[Status, FieldMetadata(alias="STATUS"), pydantic.Field(alias="STATUS")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
