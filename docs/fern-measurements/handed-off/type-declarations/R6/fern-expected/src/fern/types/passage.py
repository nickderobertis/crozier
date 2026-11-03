

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Passage(UniversalBaseModel):
    boat_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="boatName"),
        pydantic.Field(alias="boatName", description="\nThe boat's registered name."),
    ] = None
    """
    
    The boat's registered name.
    """

    hour: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
