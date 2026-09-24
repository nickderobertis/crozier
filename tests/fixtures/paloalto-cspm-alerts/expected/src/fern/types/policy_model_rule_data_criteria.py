

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .policy_model_rule_data_criteria_exposure import PolicyModelRuleDataCriteriaExposure


class PolicyModelRuleDataCriteria(UniversalBaseModel):
    """
    Rule criteria for DLP data policy
    """

    classification_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="classificationResult"),
        pydantic.Field(alias="classificationResult", description="Data policy. Required for DLP rule criteria."),
    ] = None
    """
    Data policy. Required for DLP rule criteria.
    """

    exposure: typing.Optional[PolicyModelRuleDataCriteriaExposure] = pydantic.Field(default=None)
    """
    File exposure
    """

    extension: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    File extensions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
