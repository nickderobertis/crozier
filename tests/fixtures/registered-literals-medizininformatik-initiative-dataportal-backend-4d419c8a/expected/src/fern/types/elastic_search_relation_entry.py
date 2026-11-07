

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ElasticSearchRelationEntry(UniversalBaseModel):
    name: typing.Optional[str] = None
    contextualized_termcode_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contextualizedTermcodeHash"),
        pydantic.Field(alias="contextualizedTermcodeHash"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
