

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AdminListUsersRequestOrder(str, enum.Enum):
    CREATED = "created"
    LAST_EMAILED = "last_emailed"
    SEEN = "seen"
    USERNAME = "username"
    EMAIL = "email"
    TRUST_LEVEL = "trust_level"
    DAYS_VISITED = "days_visited"
    POSTS_READ = "posts_read"
    TOPICS_VIEWED = "topics_viewed"
    POSTS = "posts"
    READ_TIME = "read_time"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        last_emailed: typing.Callable[[], T_Result],
        seen: typing.Callable[[], T_Result],
        username: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        trust_level: typing.Callable[[], T_Result],
        days_visited: typing.Callable[[], T_Result],
        posts_read: typing.Callable[[], T_Result],
        topics_viewed: typing.Callable[[], T_Result],
        posts: typing.Callable[[], T_Result],
        read_time: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdminListUsersRequestOrder.CREATED:
            return created()
        if self is AdminListUsersRequestOrder.LAST_EMAILED:
            return last_emailed()
        if self is AdminListUsersRequestOrder.SEEN:
            return seen()
        if self is AdminListUsersRequestOrder.USERNAME:
            return username()
        if self is AdminListUsersRequestOrder.EMAIL:
            return email()
        if self is AdminListUsersRequestOrder.TRUST_LEVEL:
            return trust_level()
        if self is AdminListUsersRequestOrder.DAYS_VISITED:
            return days_visited()
        if self is AdminListUsersRequestOrder.POSTS_READ:
            return posts_read()
        if self is AdminListUsersRequestOrder.TOPICS_VIEWED:
            return topics_viewed()
        if self is AdminListUsersRequestOrder.POSTS:
            return posts()
        if self is AdminListUsersRequestOrder.READ_TIME:
            return read_time()
