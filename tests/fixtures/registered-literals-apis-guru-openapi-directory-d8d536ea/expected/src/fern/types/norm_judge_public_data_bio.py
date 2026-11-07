

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NormJudgePublicDataBio(UniversalBaseModel):
    birth_city: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="birthCity"),
        pydantic.Field(alias="birthCity", description="The Birth City of the Judge."),
    ] = None
    """
    The Birth City of the Judge.
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="The Date of Birth of the Judge."),
    ] = None
    """
    The Date of Birth of the Judge.
    """

    birth_state: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="birthState"),
        pydantic.Field(alias="birthState", description="The Birth State of the Judge."),
    ] = None
    """
    The Birth State of the Judge.
    """

    death_city: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deathCity"),
        pydantic.Field(alias="deathCity", description="The Death City of the Judge."),
    ] = None
    """
    The Death City of the Judge.
    """

    death_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deathDate"),
        pydantic.Field(alias="deathDate", description="The Date of the Death of the Judge."),
    ] = None
    """
    The Date of the Death of the Judge.
    """

    death_state: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deathState"),
        pydantic.Field(alias="deathState", description="The Death State of the Judge."),
    ] = None
    """
    The Death State of the Judge.
    """

    ethnicity: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ethnic Group of the Judge.
    """

    political_affiliation: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="politicalAffiliation"),
        pydantic.Field(alias="politicalAffiliation", description="The Political Affiliation of the Judge."),
    ] = None
    """
    The Political Affiliation of the Judge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
