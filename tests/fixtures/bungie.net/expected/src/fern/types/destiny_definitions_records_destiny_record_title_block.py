

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsRecordsDestinyRecordTitleBlock(UniversalBaseModel):
    gilding_tracking_record_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="gildingTrackingRecordHash")
    ] = None
    has_title: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hasTitle")] = None
    titles_by_gender: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="titlesByGender")
    ] = None
    titles_by_gender_hash: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="titlesByGenderHash")
    ] = pydantic.Field(default=None)
    """
    For those who prefer to use the definitions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
