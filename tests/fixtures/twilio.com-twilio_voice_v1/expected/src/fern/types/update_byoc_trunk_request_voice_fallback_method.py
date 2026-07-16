

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateByocTrunkRequestVoiceFallbackMethod(str, enum.Enum):
    """
    The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
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
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.HEAD:
            return head()
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.GET:
            return get()
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.POST:
            return post()
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.PATCH:
            return patch()
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.PUT:
            return put()
        if self is UpdateByocTrunkRequestVoiceFallbackMethod.DELETE:
            return delete()
