

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .after_action_failure_policy import AfterActionFailurePolicy
from .delay import Delay
from .http_class_callback import HttpClassCallback
from .http_object_callback import HttpObjectCallback
from .http_request import HttpRequest


class AfterAction(UniversalBaseModel):
    """
    an action run before or after the expectation's own action
    """

    http_request: typing_extensions.Annotated[
        typing.Optional[HttpRequest], FieldMetadata(alias="httpRequest"), pydantic.Field(alias="httpRequest")
    ] = None
    http_class_callback: typing_extensions.Annotated[
        typing.Optional[HttpClassCallback],
        FieldMetadata(alias="httpClassCallback"),
        pydantic.Field(alias="httpClassCallback"),
    ] = None
    http_object_callback: typing_extensions.Annotated[
        typing.Optional[HttpObjectCallback],
        FieldMetadata(alias="httpObjectCallback"),
        pydantic.Field(alias="httpObjectCallback"),
    ] = None
    delay: typing.Optional[Delay] = None
    blocking: typing.Optional[bool] = None
    timeout: typing.Optional[Delay] = None
    failure_policy: typing_extensions.Annotated[
        typing.Optional[AfterActionFailurePolicy],
        FieldMetadata(alias="failurePolicy"),
        pydantic.Field(alias="failurePolicy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(AfterAction)
