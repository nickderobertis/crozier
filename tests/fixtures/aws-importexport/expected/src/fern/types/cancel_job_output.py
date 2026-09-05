

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .success import Success


class CancelJobOutput(UniversalBaseModel):
    """
    Output structure for the CancelJob operation.
    """

    success: typing_extensions.Annotated[
        typing.Optional[Success], FieldMetadata(alias="Success"), pydantic.Field(alias="Success")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
