

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PhysicalResourceIdContextKeyValuePair(UniversalBaseModel):
    """
    Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.
    """

    key: typing_extensions.Annotated[str, FieldMetadata(alias="Key")] = pydantic.Field()
    """
    The resource context key.
    """

    value: typing_extensions.Annotated[str, FieldMetadata(alias="Value")] = pydantic.Field()
    """
    The resource context value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
