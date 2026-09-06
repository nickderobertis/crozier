

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .age_restriction_dto import AgeRestrictionDto


class UserDto(UniversalBaseModel):
    age_restriction: typing_extensions.Annotated[
        typing.Optional[AgeRestrictionDto],
        FieldMetadata(alias="ageRestriction"),
        pydantic.Field(alias="ageRestriction"),
    ] = None
    email: str
    id: str
    labels_allow: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="labelsAllow"), pydantic.Field(alias="labelsAllow")
    ]
    labels_exclude: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="labelsExclude"), pydantic.Field(alias="labelsExclude")
    ]
    roles: typing.List[str]
    shared_all_libraries: typing_extensions.Annotated[
        bool, FieldMetadata(alias="sharedAllLibraries"), pydantic.Field(alias="sharedAllLibraries")
    ]
    shared_libraries_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sharedLibrariesIds"), pydantic.Field(alias="sharedLibrariesIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
