

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RawOrderedDataChildChildArrayItem(UniversalBaseModel):
    """
    Contact object Data Schema.
    """

    child_array: typing_extensions.Annotated[
        typing.List[typing.Dict[str, typing.Any]], FieldMetadata(alias="childArray"), pydantic.Field(alias="childArray")
    ]
    lbl: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label of the docket from the source.
    """

    ord: int = pydantic.Field()
    """
    Structure order.
    """

    val: typing.Optional[str] = pydantic.Field(default=None)
    """
    List of available addresses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
