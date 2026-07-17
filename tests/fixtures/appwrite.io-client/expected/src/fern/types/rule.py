

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Rule(UniversalBaseModel):
    """
    Rule
    """

    collection: typing_extensions.Annotated[
        str, FieldMetadata(alias="$collection"), pydantic.Field(alias="$collection", description="Rule Collection.")
    ]
    """
    Rule Collection.
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Rule ID.")
    ]
    """
    Rule ID.
    """

    array: bool = pydantic.Field()
    """
    Is array?
    """

    default: str = pydantic.Field()
    """
    Rule default value.
    """

    key: str = pydantic.Field()
    """
    Rule key.
    """

    label: str = pydantic.Field()
    """
    Rule label.
    """

    list_: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list", description="List of allowed values"),
    ]
    """
    List of allowed values
    """

    required: bool = pydantic.Field()
    """
    Is required?
    """

    type: str = pydantic.Field()
    """
    Rule type. Possible values: 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
