

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Links(UniversalBaseModel):
    """
    Links relevant to the payload
    """

    first: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="First")] = None
    last: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Last")] = None
    next: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Next")] = None
    prev: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Prev")] = None
    self_: typing_extensions.Annotated[str, FieldMetadata(alias="Self")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
