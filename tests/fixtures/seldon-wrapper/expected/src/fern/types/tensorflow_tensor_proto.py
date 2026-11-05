

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .tensorflow_data_type import TensorflowDataType
from .tensorflow_resource_handle_proto import TensorflowResourceHandleProto
from .tensorflow_tensor_shape_proto import TensorflowTensorShapeProto


class TensorflowTensorProto(UniversalBaseModel):
    """
    Protocol buffer representing a tensor.
    """

    bool_val: typing.Optional[typing.List[bool]] = None
    dcomplex_val: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    DT_COMPLEX128. dcomplex_val(2*i) and dcomplex_val(2*i+1) are real
    and imaginary parts of i-th double precision complex.
    """

    double_val: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    DT_DOUBLE.
    """

    dtype: typing.Optional[TensorflowDataType] = None
    float_val: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    DT_FLOAT.
    """

    half_val: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    DT_HALF, DT_BFLOAT16. Note that since protobuf has no int16 type, we'll
    have some pointless zero padding for each value here.
    """

    int64val: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="int64_val"), pydantic.Field(alias="int64_val")
    ] = None
    int_val: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    DT_INT32, DT_INT16, DT_INT8, DT_UINT8.
    """

    resource_handle_val: typing.Optional[typing.List[TensorflowResourceHandleProto]] = None
    scomplex_val: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    DT_COMPLEX64. scomplex_val(2*i) and scomplex_val(2*i+1) are real
    and imaginary parts of i-th single precision complex.
    """

    string_val: typing.Optional[typing.List[str]] = None
    tensor_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Serialized raw tensor content from either Tensor::AsProtoTensorContent or
    memcpy in tensorflow::grpc::EncodeTensorToByteBuffer. This representation
    can be used for all tensor types. The purpose of this representation is to
    reduce serialization overhead during RPC call by avoiding serialization of
    many repeated small items.
    """

    tensor_shape: typing.Optional[TensorflowTensorShapeProto] = pydantic.Field(default=None)
    """
    Shape of the tensor.  TODO(touts): sort out the 0-rank issues.
    """

    uint32val: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="uint32_val"), pydantic.Field(alias="uint32_val")
    ] = None
    uint64val: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="uint64_val"), pydantic.Field(alias="uint64_val")
    ] = None
    variant_val: typing.Optional[typing.List["TensorflowVariantTensorDataProto"]] = None
    version_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number.
    
    In version 0, if the "repeated xxx" representations contain only one
    element, that element is repeated to fill the shape.  This makes it easy
    to represent a constant Tensor with a single value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .tensorflow_variant_tensor_data_proto import TensorflowVariantTensorDataProto

update_forward_refs(TensorflowTensorProto, TensorflowVariantTensorDataProto=TensorflowVariantTensorDataProto)
