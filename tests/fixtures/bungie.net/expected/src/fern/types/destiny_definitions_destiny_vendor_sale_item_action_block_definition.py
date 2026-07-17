

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition(UniversalBaseModel):
    """
    Not terribly useful, some basic cooldown interaction info.
    """

    execute_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="executeSeconds"), pydantic.Field(alias="executeSeconds")
    ] = None
    is_positive: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPositive"), pydantic.Field(alias="isPositive")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
