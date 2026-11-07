

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class TensorflowVariantTensorDataProto(UniversalBaseModel):
    """
    Protocol buffer representing the serialization format of DT_VARIANT tensors.
    """

    metadata: typing.Optional[str] = pydantic.Field(default=None)
    """
    Portions of the object that are not Tensors.
    """

    tensors: typing.Optional[typing.List["TensorflowTensorProto"]] = pydantic.Field(default=None)
    """
    Tensors contained within objects being serialized.
    """

    type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the type of objects being serialized.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .tensorflow_tensor_proto import TensorflowTensorProto

update_forward_refs(TensorflowVariantTensorDataProto, TensorflowTensorProto=TensorflowTensorProto)
