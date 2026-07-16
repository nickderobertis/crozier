

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent(UniversalBaseModel):
    failed_requirement_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="failedRequirementIndexes"),
        pydantic.Field(
            alias="failedRequirementIndexes",
            description="Index into the unlock requirements to display failure descriptions",
        ),
    ] = None
    """
    Index into the unlock requirements to display failure descriptions
    """

    plug_item_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="plugItemHash"), pydantic.Field(alias="plugItemHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
