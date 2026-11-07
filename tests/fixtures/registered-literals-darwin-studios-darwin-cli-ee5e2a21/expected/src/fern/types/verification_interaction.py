

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verification_interaction_kind import VerificationInteractionKind
from .verification_interaction_methods_item import VerificationInteractionMethodsItem
from .verification_interaction_state import VerificationInteractionState


class VerificationInteraction(UniversalBaseModel):
    """
    A verifier-owned claim and success policy bound to the selected capability revision. The caller can choose only one advertised method and cannot supply the verdict.
    """

    id: str
    kind: VerificationInteractionKind
    state: VerificationInteractionState
    claim: typing.Optional[str] = None
    revision: int
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    methods: typing.List[VerificationInteractionMethodsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
