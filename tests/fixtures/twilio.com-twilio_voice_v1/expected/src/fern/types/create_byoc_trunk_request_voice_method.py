

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateByocTrunkRequestVoiceMethod(str, enum.Enum):
    """
    The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
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
        if self is CreateByocTrunkRequestVoiceMethod.HEAD:
            return head()
        if self is CreateByocTrunkRequestVoiceMethod.GET:
            return get()
        if self is CreateByocTrunkRequestVoiceMethod.POST:
            return post()
        if self is CreateByocTrunkRequestVoiceMethod.PATCH:
            return patch()
        if self is CreateByocTrunkRequestVoiceMethod.PUT:
            return put()
        if self is CreateByocTrunkRequestVoiceMethod.DELETE:
            return delete()
