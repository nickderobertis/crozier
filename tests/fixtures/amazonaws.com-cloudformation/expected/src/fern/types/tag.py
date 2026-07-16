

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Tag(UniversalBaseModel):
    """
    The Tag type enables you to specify a key-value pair that can be used to store information about an CloudFormation stack.
    """

    key: typing_extensions.Annotated[str, FieldMetadata(alias="Key")] = pydantic.Field()
    """
     <i>Required</i>. A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (Amazon Web Services) have the reserved prefix: <code>aws:</code>.
    """

    value: typing_extensions.Annotated[str, FieldMetadata(alias="Value")] = pydantic.Field()
    """
     <i>Required</i>. A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
