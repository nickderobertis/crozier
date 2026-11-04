

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .id4n_properties import Id4NProperties


class ListOfId4NProperties(UniversalBaseModel):
    """
    A list of id4n properties
    """

    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[Id4NProperties]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list", description="A list containing the id4n with its properties."),
    ] = None
    """
    A list containing the id4n with its properties.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
