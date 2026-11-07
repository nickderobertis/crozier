

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .raw_ordered_data_child import RawOrderedDataChild


class RawOrderedData(UniversalBaseModel):
    child_array: typing_extensions.Annotated[
        typing.List[typing.Optional[RawOrderedDataChild]],
        FieldMetadata(alias="childArray"),
        pydantic.Field(
            alias="childArray",
            description="Any docket text that belongs to the main docket text is added in the child.",
        ),
    ]
    """
    Any docket text that belongs to the main docket text is added in the child.
    """

    lbl: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label of the docket from the source.
    """

    ord: int = pydantic.Field()
    """
    Structure order
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
