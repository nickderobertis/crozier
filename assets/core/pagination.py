

from __future__ import annotations

from dataclasses import dataclass
from typing import AsyncIterator, Awaitable, Callable, Generic, Iterator, List, Optional, TypeVar


T = TypeVar("T")

R = TypeVar("R")













@dataclass(frozen=True)
class SyncPager(Generic[T, R]):
    get_next: Optional[Callable[[], Optional[SyncPager[T, R]]]]
    has_next: bool
    items: Optional[List[T]]
    response: R




    def __iter__(self) -> Iterator[T]:
        for page in self.iter_pages():
            if page.items is not None:
                yield from page.items

    def iter_pages(self) -> Iterator[SyncPager[T, R]]:
        page: Optional[SyncPager[T, R]] = self
        while page is not None:
            yield page

            if not page.has_next or page.get_next is None:
                return

            page = page.get_next()
            if page is None or page.items is None or len(page.items) == 0:
                return

    def next_page(self) -> Optional[SyncPager[T, R]]:
        return self.get_next() if self.get_next is not None else None


@dataclass(frozen=True)
class AsyncPager(Generic[T, R]):
    get_next: Optional[Callable[[], Awaitable[Optional[AsyncPager[T, R]]]]]
    has_next: bool
    items: Optional[List[T]]
    response: R

    async def __aiter__(self) -> AsyncIterator[T]:
        async for page in self.iter_pages():
            if page.items is not None:
                for item in page.items:
                    yield item

    async def iter_pages(self) -> AsyncIterator[AsyncPager[T, R]]:
        page: Optional[AsyncPager[T, R]] = self
        while page is not None:
            yield page

            if not page.has_next or page.get_next is None:
                return

            page = await page.get_next()
            if page is None or page.items is None or len(page.items) == 0:
                return

    async def next_page(self) -> Optional[AsyncPager[T, R]]:
        return await self.get_next() if self.get_next is not None else None
