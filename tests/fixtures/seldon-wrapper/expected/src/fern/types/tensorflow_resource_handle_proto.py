

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TensorflowResourceHandleProto(UniversalBaseModel):
    """
    Protocol buffer representing a handle to a tensorflow resource. Handles are
    not valid across executions, but can be serialized back and forth from within
    a single run.
    """

    container: typing.Optional[str] = pydantic.Field(default=None)
    """
    Container in which this resource is placed.
    """

    device: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique name for the device containing the resource.
    """

    hash_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hash code for the type of the resource. Is only valid in the same device
    and in the same execution.
    """

    maybe_type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For debug-only, the name of the type pointed to by this handle, if
    available.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique name of this resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
