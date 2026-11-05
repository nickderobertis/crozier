

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TensorShapeProtoDim(UniversalBaseModel):
    """
    One dimension of the tensor.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional name of the tensor dimension.
    """

    size: typing.Optional[str] = pydantic.Field(default=None)
    """
    Size of the tensor in that dimension.
    This value must be >= -1, but values of -1 are reserved for "unknown"
    shapes (values of -1 mean "unknown" dimension).  Certain wrappers
    that work with TensorShapeProto may fail at runtime when deserializing
    a TensorShapeProto containing a dim value of -1.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
