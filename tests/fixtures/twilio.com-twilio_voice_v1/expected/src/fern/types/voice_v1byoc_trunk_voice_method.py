

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VoiceV1ByocTrunkVoiceMethod(enum.StrEnum):
    """
    The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
    """

    HEAD = "HEAD"
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"

    def visit(
        self,
        head: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VoiceV1ByocTrunkVoiceMethod.HEAD:
            return head()
        if self is VoiceV1ByocTrunkVoiceMethod.GET:
            return get()
        if self is VoiceV1ByocTrunkVoiceMethod.POST:
            return post()
        if self is VoiceV1ByocTrunkVoiceMethod.PATCH:
            return patch()
        if self is VoiceV1ByocTrunkVoiceMethod.PUT:
            return put()
        if self is VoiceV1ByocTrunkVoiceMethod.DELETE:
            return delete()
