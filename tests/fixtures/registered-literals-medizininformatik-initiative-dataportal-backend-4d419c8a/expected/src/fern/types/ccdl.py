

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .criterion_list import CriterionList


class Ccdl(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    The json schema version
    """

    display: typing.Optional[str] = None
    inclusion_criteria: typing_extensions.Annotated[
        typing.List[CriterionList], FieldMetadata(alias="inclusionCriteria"), pydantic.Field(alias="inclusionCriteria")
    ]
    exclusion_criteria: typing_extensions.Annotated[
        typing.Optional[typing.List[CriterionList]],
        FieldMetadata(alias="exclusionCriteria"),
        pydantic.Field(alias="exclusionCriteria"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
