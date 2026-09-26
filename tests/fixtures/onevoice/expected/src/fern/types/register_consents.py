

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterConsents(UniversalBaseModel):
    """
    Per-slug version map submitted with /auth/register. The handler enforces
    version-equality (vs `legalconfig.*Version`) and returns 400
    consent_required listing the missing slugs, so individual fields are
    NOT marked `required` at the schema level — a missing field is treated
    as a stale consent, not a schema violation.
    """

    tos: typing.Optional[str] = None
    privacy: typing.Optional[str] = None
    pdn: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
