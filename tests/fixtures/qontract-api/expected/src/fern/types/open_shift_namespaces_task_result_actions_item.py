

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpenShiftNamespacesTaskResultActionsItem_CreateNamespace(UniversalBaseModel):
    action_type: typing.Literal["create_namespace"] = "create_namespace"
    cluster: str
    namespace: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class OpenShiftNamespacesTaskResultActionsItem_DeleteNamespace(UniversalBaseModel):
    action_type: typing.Literal["delete_namespace"] = "delete_namespace"
    cluster: str
    namespace: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


OpenShiftNamespacesTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[
        OpenShiftNamespacesTaskResultActionsItem_CreateNamespace,
        OpenShiftNamespacesTaskResultActionsItem_DeleteNamespace,
    ],
    pydantic.Field(discriminator="action_type"),
]
