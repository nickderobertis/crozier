

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemVersionDefinition(UniversalBaseModel):
    """
    The version definition currently just holds a reference to the power cap.
    """

    power_cap_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="powerCapHash"),
        pydantic.Field(alias="powerCapHash", description="A reference to the power cap for this item version."),
    ] = None
    """
    A reference to the power cap for this item version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
