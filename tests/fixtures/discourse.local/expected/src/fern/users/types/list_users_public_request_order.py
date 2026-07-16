

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListUsersPublicRequestOrder(enum.StrEnum):
    LIKES_RECEIVED = "likes_received"
    LIKES_GIVEN = "likes_given"
    TOPIC_COUNT = "topic_count"
    POST_COUNT = "post_count"
    TOPICS_ENTERED = "topics_entered"
    POSTS_READ = "posts_read"
    DAYS_VISITED = "days_visited"

    def visit(
        self,
        likes_received: typing.Callable[[], T_Result],
        likes_given: typing.Callable[[], T_Result],
        topic_count: typing.Callable[[], T_Result],
        post_count: typing.Callable[[], T_Result],
        topics_entered: typing.Callable[[], T_Result],
        posts_read: typing.Callable[[], T_Result],
        days_visited: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListUsersPublicRequestOrder.LIKES_RECEIVED:
            return likes_received()
        if self is ListUsersPublicRequestOrder.LIKES_GIVEN:
            return likes_given()
        if self is ListUsersPublicRequestOrder.TOPIC_COUNT:
            return topic_count()
        if self is ListUsersPublicRequestOrder.POST_COUNT:
            return post_count()
        if self is ListUsersPublicRequestOrder.TOPICS_ENTERED:
            return topics_entered()
        if self is ListUsersPublicRequestOrder.POSTS_READ:
            return posts_read()
        if self is ListUsersPublicRequestOrder.DAYS_VISITED:
            return days_visited()
