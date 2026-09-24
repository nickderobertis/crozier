

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rule_model_data_criteria import RuleModelDataCriteria
from .rule_model_type import RuleModelType


class RuleModel(UniversalBaseModel):
    """
    Model for Rule
    """

    api_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiName"), pydantic.Field(alias="apiName", description="API name")
    ] = None
    """
    API name
    """

    cloud_account: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cloudAccount"),
        pydantic.Field(alias="cloudAccount", description="Cloud account"),
    ] = None
    """
    Cloud account
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cloudType"),
        pydantic.Field(alias="cloudType", description="Cloud type"),
    ] = None
    """
    Cloud type
    """

    criteria: str = pydantic.Field()
    """
    Saved search ID that defines the rule criteria.
    """

    data_criteria: typing_extensions.Annotated[
        typing.Optional[RuleModelDataCriteria],
        FieldMetadata(alias="dataCriteria"),
        pydantic.Field(alias="dataCriteria", description="Rule criteria for DLP data policy"),
    ] = None
    """
    Rule criteria for DLP data policy
    """

    name: str = pydantic.Field()
    """
    Name
    """

    parameters: typing.Dict[str, str] = pydantic.Field()
    """
    Parameters (e.g. {"savedSearch": "true"})
    """

    resource_id_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceIdPath"),
        pydantic.Field(alias="resourceIdPath", description="Resource ID path"),
    ] = None
    """
    Resource ID path
    """

    resource_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceType"),
        pydantic.Field(alias="resourceType", description="Resource type"),
    ] = None
    """
    Resource type
    """

    type: RuleModelType = pydantic.Field()
    """
    Type of rule or RQL query
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
