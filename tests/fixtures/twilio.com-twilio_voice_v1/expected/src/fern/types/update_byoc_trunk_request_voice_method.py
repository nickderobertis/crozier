

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateByocTrunkRequestVoiceMethod(str, enum.Enum):
    """
    The HTTP method we should use to call `voice_url`
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
        if self is UpdateByocTrunkRequestVoiceMethod.HEAD:
            return head()
        if self is UpdateByocTrunkRequestVoiceMethod.GET:
            return get()
        if self is UpdateByocTrunkRequestVoiceMethod.POST:
            return post()
        if self is UpdateByocTrunkRequestVoiceMethod.PATCH:
            return patch()
        if self is UpdateByocTrunkRequestVoiceMethod.PUT:
            return put()
        if self is UpdateByocTrunkRequestVoiceMethod.DELETE:
            return delete()
