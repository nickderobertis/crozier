

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_classification import AtlasClassification
from .atlas_entity_header_status import AtlasEntityHeaderStatus
from .atlas_term_assignment_header import AtlasTermAssignmentHeader


class AtlasEntityHeader(UniversalBaseModel):
    type_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeName"), pydantic.Field(alias="typeName")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    guid: typing.Optional[str] = None
    status: typing.Optional[AtlasEntityHeaderStatus] = None
    display_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayText"), pydantic.Field(alias="displayText")
    ] = None
    classification_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="classificationNames"),
        pydantic.Field(alias="classificationNames"),
    ] = None
    classifications: typing.Optional[typing.List[AtlasClassification]] = None
    meaning_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="meaningNames"), pydantic.Field(alias="meaningNames")
    ] = None
    meanings: typing.Optional[typing.List[AtlasTermAssignmentHeader]] = None
    is_incomplete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isIncomplete"), pydantic.Field(alias="isIncomplete")
    ] = None
    labels: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
