

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .operation_display import OperationDisplay
from .operation_properties import OperationProperties


class Operation(UniversalBaseModel):
    """
    Operation entity.
    """

    display: typing.Optional[OperationDisplay] = pydantic.Field(default=None)
    """
    Operation display values.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the operation. Format: {resourceProviderNamespace}/{resourceType}/{read|write|delete|action}
    """

    origin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Origin of the operation. Can be : user|system|user,system
    """

    properties: typing.Optional[OperationProperties] = pydantic.Field(default=None)
    """
    Operation properties.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
