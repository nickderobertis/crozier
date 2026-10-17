

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectUpgradeEligibilityResponseOutputWarningsItem_PgGraphqlIntrospectionChange(UniversalBaseModel):
    type: typing.Literal["pg_graphql_introspection_change"] = "pg_graphql_introspection_change"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputWarningsItem_LtreeReindexRequired(UniversalBaseModel):
    type: typing.Literal["ltree_reindex_required"] = "ltree_reindex_required"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputWarningsItem_OperatorEstimatorGate(UniversalBaseModel):
    type: typing.Literal["operator_estimator_gate"] = "operator_estimator_gate"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputWarningsItem_BtreeGistNanReindex(UniversalBaseModel):
    type: typing.Literal["btree_gist_nan_reindex"] = "btree_gist_nan_reindex"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProjectUpgradeEligibilityResponseOutputWarningsItem = typing_extensions.Annotated[
    typing.Union[
        ProjectUpgradeEligibilityResponseOutputWarningsItem_PgGraphqlIntrospectionChange,
        ProjectUpgradeEligibilityResponseOutputWarningsItem_LtreeReindexRequired,
        ProjectUpgradeEligibilityResponseOutputWarningsItem_OperatorEstimatorGate,
        ProjectUpgradeEligibilityResponseOutputWarningsItem_BtreeGistNanReindex,
    ],
    pydantic.Field(discriminator="type"),
]
