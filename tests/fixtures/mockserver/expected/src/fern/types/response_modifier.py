

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .response_modifier_condition import ResponseModifierCondition
from .response_modifier_cookies import ResponseModifierCookies
from .response_modifier_headers import ResponseModifierHeaders


class ResponseModifier(UniversalBaseModel):
    """
    a response modifier; may itself be conditional and/or wrap a further chain
    """

    headers: typing.Optional[ResponseModifierHeaders] = None
    cookies: typing.Optional[ResponseModifierCookies] = None
    condition: typing.Optional[ResponseModifierCondition] = pydantic.Field(default=None)
    """
    apply this modifier only when the in-flight response (and optionally the original request) match
    """

    modifiers: typing.Optional[typing.List["ResponseModifier"]] = pydantic.Field(default=None)
    """
    ordered chain of modifiers, each applied in turn so a later modifier sees the earlier one's output
    """

    json_patch: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="jsonPatch"),
        pydantic.Field(
            alias="jsonPatch",
            description="RFC 6902 JSON Patch (array of add/remove/replace/move/copy/test operations) applied to a forwarded response body when that body is valid JSON; applied before jsonMergePatch; a non-JSON body or a failed operation leaves the body unchanged",
        ),
    ] = None
    """
    RFC 6902 JSON Patch (array of add/remove/replace/move/copy/test operations) applied to a forwarded response body when that body is valid JSON; applied before jsonMergePatch; a non-JSON body or a failed operation leaves the body unchanged
    """

    json_merge_patch: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="jsonMergePatch"),
        pydantic.Field(
            alias="jsonMergePatch",
            description="RFC 7386 JSON Merge Patch applied to a forwarded response body when that body is valid JSON; members overwrite, or when null delete, the corresponding body members; a non-JSON body leaves the body unchanged",
        ),
    ] = None
    """
    RFC 7386 JSON Merge Patch applied to a forwarded response body when that body is valid JSON; members overwrite, or when null delete, the corresponding body members; a non-JSON body leaves the body unchanged
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ResponseModifier)
