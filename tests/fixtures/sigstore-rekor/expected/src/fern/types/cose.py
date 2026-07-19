

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cose_schema import CoseSchema


class Cose(UniversalBaseModel):
    """
    COSE object
    """

    kind: str
    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    spec: CoseSchema

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
