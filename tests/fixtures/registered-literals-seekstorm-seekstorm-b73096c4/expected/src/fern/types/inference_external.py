

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .inference_external_external import InferenceExternalExternal


class InferenceExternal(UniversalBaseModel):
    """
    External inference
    """

    external: typing_extensions.Annotated[
        InferenceExternalExternal,
        FieldMetadata(alias="External"),
        pydantic.Field(alias="External", description="External inference"),
    ]
    """
    External inference
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
