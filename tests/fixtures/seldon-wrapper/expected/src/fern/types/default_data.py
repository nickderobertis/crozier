

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .any_value import AnyValue
from .tensor import Tensor


class DefaultData(UniversalBaseModel):
    names: typing.Optional[typing.List[str]] = None
    ndarry: typing.Optional[typing.List[AnyValue]] = None
    tensor: typing.Optional[Tensor] = None
    tftensor: typing.Optional["TensorflowTensorProto"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .tensorflow_tensor_proto import TensorflowTensorProto
from .tensorflow_variant_tensor_data_proto import TensorflowVariantTensorDataProto

update_forward_refs(
    DefaultData,
    TensorflowTensorProto=TensorflowTensorProto,
    TensorflowVariantTensorDataProto=TensorflowVariantTensorDataProto,
)
