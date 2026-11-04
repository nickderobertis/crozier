

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .semantic_change import SemanticChange


class ComparePublicationsResponseData(UniversalBaseModel):
    from_publication_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="fromPublicationId"), pydantic.Field(alias="fromPublicationId")
    ]
    to_publication_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toPublicationId"), pydantic.Field(alias="toPublicationId")
    ]
    changed: bool
    changes: typing.List[SemanticChange]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
