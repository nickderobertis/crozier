

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .matched_object import MatchedObject


class NormAttorneySearchResult(UniversalBaseModel):
    first_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstFetchDate"), pydantic.Field(alias="firstFetchDate")
    ]
    has_associated_public_data: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasAssociatedPublicData"), pydantic.Field(alias="hasAssociatedPublicData")
    ]
    last_fetch_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastFetchDate"), pydantic.Field(alias="lastFetchDate")
    ]
    matched_object_array: typing_extensions.Annotated[
        typing.List[typing.Optional[MatchedObject]],
        FieldMetadata(alias="matchedObjectArray"),
        pydantic.Field(alias="matchedObjectArray"),
    ]
    name: str
    norm_attorney_details_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyDetailsAPI"), pydantic.Field(alias="normAttorneyDetailsAPI")
    ]
    norm_attorney_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="normAttorneyId"), pydantic.Field(alias="normAttorneyId")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
