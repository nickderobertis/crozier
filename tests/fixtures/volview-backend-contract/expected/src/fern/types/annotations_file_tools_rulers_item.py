

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .annotations_file_tools_rulers_item_frame_of_reference import AnnotationsFileToolsRulersItemFrameOfReference


class AnnotationsFileToolsRulersItem(UniversalBaseModel):
    first_point: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="firstPoint"), pydantic.Field(alias="firstPoint")
    ]
    second_point: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="secondPoint"), pydantic.Field(alias="secondPoint")
    ]
    frame_of_reference: typing_extensions.Annotated[
        AnnotationsFileToolsRulersItemFrameOfReference,
        FieldMetadata(alias="frameOfReference"),
        pydantic.Field(alias="frameOfReference"),
    ]
    slice: typing.Optional[float] = None
    frame: typing.Optional[int] = None
    label_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="labelName"), pydantic.Field(alias="labelName")
    ] = None
    name: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
