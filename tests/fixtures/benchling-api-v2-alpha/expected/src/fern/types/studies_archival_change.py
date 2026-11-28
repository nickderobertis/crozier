

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StudiesArchivalChange(UniversalBaseModel):
    """
    IDs of all items that were archived or unarchived.
    """

    study_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="studyIds"), pydantic.Field(alias="studyIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
