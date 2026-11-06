

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tensor_shape_proto_dim import TensorShapeProtoDim


class TensorflowTensorShapeProto(UniversalBaseModel):
    """
    Dimensions of a tensor.
    """

    dim: typing.Optional[typing.List[TensorShapeProtoDim]] = pydantic.Field(default=None)
    """
    Dimensions of the tensor, such as {"input", 30}, {"output", 40}
    for a 30 x 40 2D tensor.  If an entry has size -1, this
    corresponds to a dimension of unknown size. The names are
    optional.
    
    The order of entries in "dim" matters: It indicates the layout of the
    values in the tensor in-memory representation.
    
    The first entry in "dim" is the outermost dimension used to layout the
    values, the last entry is the innermost dimension.  This matches the
    in-memory layout of RowMajor Eigen tensors.
    
    If "dim.size()" > 0, "unknown_rank" must be false.
    """

    unknown_rank: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the number of dimensions in the shape is unknown.
    
    If true, "dim.size()" must be 0.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
