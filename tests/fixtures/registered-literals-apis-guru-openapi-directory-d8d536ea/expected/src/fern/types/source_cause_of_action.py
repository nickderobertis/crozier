

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SourceCauseOfAction(UniversalBaseModel):
    """
    Source Cause of Action data from the source site.
    """

    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(
            alias="firstFetchDate", description="When this Cause of Action was first fetched from the court site."
        ),
    ]
    """
    When this Cause of Action was first fetched from the court site.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if the cause of action is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if the cause of action is currently isVisible or not for the case.
    """

    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(
            alias="lastFetchDate", description="When this Cause of Action was last fetched from the court site."
        ),
    ]
    """
    When this Cause of Action was last fetched from the court site.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    source_cause_of_action: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceCauseOfAction"),
        pydantic.Field(alias="sourceCauseOfAction", description="Cause of Action data from the source site."),
    ] = None
    """
    Cause of Action data from the source site.
    """

    source_cause_of_action_raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceCauseOfActionRaw"),
        pydantic.Field(alias="sourceCauseOfActionRaw", description="Raw Cause of Action data from the source site."),
    ] = None
    """
    Raw Cause of Action data from the source site.
    """

    source_statute: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceStatute"),
        pydantic.Field(alias="sourceStatute", description="Statute of a Cause of Action."),
    ] = None
    """
    Statute of a Cause of Action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
