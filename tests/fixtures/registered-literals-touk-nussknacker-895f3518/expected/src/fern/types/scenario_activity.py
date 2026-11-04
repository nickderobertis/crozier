

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .additional_field import AdditionalField
from .scenario_activity_attachment import ScenarioActivityAttachment
from .scenario_activity_comment import ScenarioActivityComment
from .scenario_activity_type import ScenarioActivityType


class ScenarioActivity(UniversalBaseModel):
    id: str
    user: str
    date: dt.datetime
    scenario_version_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="scenarioVersionId"), pydantic.Field(alias="scenarioVersionId")
    ] = None
    comment: typing.Optional[ScenarioActivityComment] = None
    attachment: typing.Optional[ScenarioActivityAttachment] = None
    additional_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[AdditionalField]],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    override_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="overrideIcon"), pydantic.Field(alias="overrideIcon")
    ] = None
    override_displayable_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="overrideDisplayableName"),
        pydantic.Field(alias="overrideDisplayableName"),
    ] = None
    override_supported_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="overrideSupportedActions"),
        pydantic.Field(alias="overrideSupportedActions"),
    ] = None
    type: ScenarioActivityType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
