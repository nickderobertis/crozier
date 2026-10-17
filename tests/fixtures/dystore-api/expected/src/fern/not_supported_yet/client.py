

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotSupportedYetClient, RawNotSupportedYetClient
from .types.add_composable_to_cart_request_data import AddComposableToCartRequestData
from .types.forgot_password_request_data import ForgotPasswordRequestData
from .types.new_password_request_data import NewPasswordRequestData
from .types.register_request_data import RegisterRequestData
from .types.register_without_password_request_data import RegisterWithoutPasswordRequestData


OMIT = typing.cast(typing.Any, ...)


class NotSupportedYetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotSupportedYetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotSupportedYetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotSupportedYetClient
        """
        return self._raw_client

    def get_user_orders(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get user orders

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.get_user_orders(
            include="product_lines,product_lines.purchasable,product_lines.purchasable.product,product_lines.purchasable.product.thumbnail",
        )
        """
        _response = self._raw_client.get_user_orders(include=include, request_options=request_options)
        return _response.data

    def get_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.get_user()
        """
        _response = self._raw_client.get_user(request_options=request_options)
        return _response.data

    def delete_temp_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete temp file

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.delete_temp_file()
        """
        _response = self._raw_client.delete_temp_file(request_options=request_options)
        return _response.data

    def upload_file(
        self, *, file: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upload file

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.upload_file()
        """
        _response = self._raw_client.upload_file(file=file, request_options=request_options)
        return _response.data

    def forgot_password(
        self,
        *,
        data: typing.Optional[ForgotPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Forgot Password

        Parameters
        ----------
        data : typing.Optional[ForgotPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.not_supported_yet import (
            ForgotPasswordRequestData,
            ForgotPasswordRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.forgot_password(
            data=ForgotPasswordRequestData(
                attributes=ForgotPasswordRequestDataAttributes(
                    email="cms@webiz.cz",
                ),
                type="users",
            ),
        )
        """
        _response = self._raw_client.forgot_password(data=data, request_options=request_options)
        return _response.data

    def login(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Login

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.login(
            email="jakub@dy.st",
            password="hesloheslo",
        )
        """
        _response = self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    def generate_sanctum_token(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Generate Sanctum token

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.generate_sanctum_token(
            email="jakub@dy.st",
            password="hesloheslo",
        )
        """
        _response = self._raw_client.generate_sanctum_token(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    def logout(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Logout

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.logout(
            email="cms@webiz.cz",
            password="password",
        )
        """
        _response = self._raw_client.logout(email=email, password=password, request_options=request_options)
        return _response.data

    def new_password(
        self,
        *,
        data: typing.Optional[NewPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        New Password

        Parameters
        ----------
        data : typing.Optional[NewPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.not_supported_yet import (
            NewPasswordRequestData,
            NewPasswordRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.new_password(
            data=NewPasswordRequestData(
                attributes=NewPasswordRequestDataAttributes(
                    email="cms@webiz.cz",
                    password="password",
                    password_confirmation="password",
                    token="8821c9ada30b0ea31929318c260f130dc37913044dc49bfd88221879b6c31184",
                ),
                type="users",
            ),
        )
        """
        _response = self._raw_client.new_password(data=data, request_options=request_options)
        return _response.data

    def register_without_password(
        self,
        *,
        data: typing.Optional[RegisterWithoutPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register Without Password

        Parameters
        ----------
        data : typing.Optional[RegisterWithoutPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.not_supported_yet import (
            RegisterWithoutPasswordRequestData,
            RegisterWithoutPasswordRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.register_without_password(
            data=RegisterWithoutPasswordRequestData(
                attributes=RegisterWithoutPasswordRequestDataAttributes(
                    email="cms7@webiz.cz",
                ),
                type="users",
            ),
        )
        """
        _response = self._raw_client.register_without_password(data=data, request_options=request_options)
        return _response.data

    def register(
        self,
        *,
        data: typing.Optional[RegisterRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register

        Parameters
        ----------
        data : typing.Optional[RegisterRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.not_supported_yet import (
            RegisterRequestData,
            RegisterRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.register(
            data=RegisterRequestData(
                attributes=RegisterRequestDataAttributes(
                    email="cms6@webiz.cz",
                    password="password",
                    password_confirmation="password",
                ),
                type="users",
            ),
        )
        """
        _response = self._raw_client.register(data=data, request_options=request_options)
        return _response.data

    def add_composable_to_cart(
        self,
        *,
        data: typing.Optional[AddComposableToCartRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add Composable To Cart

        Parameters
        ----------
        data : typing.Optional[AddComposableToCartRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.not_supported_yet import (
            AddComposableToCartRequestData,
            AddComposableToCartRequestDataAttributes,
            AddComposableToCartRequestDataAttributesComponentsItem,
            AddComposableToCartRequestDataAttributesComposable,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.add_composable_to_cart(
            data=AddComposableToCartRequestData(
                attributes=AddComposableToCartRequestDataAttributes(
                    components=[
                        AddComposableToCartRequestDataAttributesComponentsItem(
                            purchasable_id=60908.0,
                            purchasable_type="Lunar\\Models\\ProductVariant",
                        ),
                        AddComposableToCartRequestDataAttributesComponentsItem(
                            purchasable_id=60921.0,
                            purchasable_type="Lunar\\Models\\ProductVariant",
                        ),
                    ],
                    composable=AddComposableToCartRequestDataAttributesComposable(
                        purchasable_id=60906.0,
                        purchasable_type="Lunar\\Models\\ProductVariant",
                    ),
                ),
                type="cart-lines",
            ),
        )
        """
        _response = self._raw_client.add_composable_to_cart(data=data, request_options=request_options)
        return _response.data

    def csrf_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        CSRF token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.not_supported_yet.csrf_token()
        """
        _response = self._raw_client.csrf_token(request_options=request_options)
        return _response.data


class AsyncNotSupportedYetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotSupportedYetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotSupportedYetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotSupportedYetClient
        """
        return self._raw_client

    async def get_user_orders(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get user orders

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.get_user_orders(
                include="product_lines,product_lines.purchasable,product_lines.purchasable.product,product_lines.purchasable.product.thumbnail",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_orders(include=include, request_options=request_options)
        return _response.data

    async def get_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.get_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(request_options=request_options)
        return _response.data

    async def delete_temp_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete temp file

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.delete_temp_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_temp_file(request_options=request_options)
        return _response.data

    async def upload_file(
        self, *, file: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upload file

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.upload_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file(file=file, request_options=request_options)
        return _response.data

    async def forgot_password(
        self,
        *,
        data: typing.Optional[ForgotPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Forgot Password

        Parameters
        ----------
        data : typing.Optional[ForgotPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.not_supported_yet import (
            ForgotPasswordRequestData,
            ForgotPasswordRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.forgot_password(
                data=ForgotPasswordRequestData(
                    attributes=ForgotPasswordRequestDataAttributes(
                        email="cms@webiz.cz",
                    ),
                    type="users",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forgot_password(data=data, request_options=request_options)
        return _response.data

    async def login(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Login

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.login(
                email="jakub@dy.st",
                password="hesloheslo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(email=email, password=password, request_options=request_options)
        return _response.data

    async def generate_sanctum_token(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Generate Sanctum token

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.generate_sanctum_token(
                email="jakub@dy.st",
                password="hesloheslo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_sanctum_token(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    async def logout(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Logout

        Parameters
        ----------
        email : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.logout(
                email="cms@webiz.cz",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(email=email, password=password, request_options=request_options)
        return _response.data

    async def new_password(
        self,
        *,
        data: typing.Optional[NewPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        New Password

        Parameters
        ----------
        data : typing.Optional[NewPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.not_supported_yet import (
            NewPasswordRequestData,
            NewPasswordRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.new_password(
                data=NewPasswordRequestData(
                    attributes=NewPasswordRequestDataAttributes(
                        email="cms@webiz.cz",
                        password="password",
                        password_confirmation="password",
                        token="8821c9ada30b0ea31929318c260f130dc37913044dc49bfd88221879b6c31184",
                    ),
                    type="users",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.new_password(data=data, request_options=request_options)
        return _response.data

    async def register_without_password(
        self,
        *,
        data: typing.Optional[RegisterWithoutPasswordRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register Without Password

        Parameters
        ----------
        data : typing.Optional[RegisterWithoutPasswordRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.not_supported_yet import (
            RegisterWithoutPasswordRequestData,
            RegisterWithoutPasswordRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.register_without_password(
                data=RegisterWithoutPasswordRequestData(
                    attributes=RegisterWithoutPasswordRequestDataAttributes(
                        email="cms7@webiz.cz",
                    ),
                    type="users",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_without_password(data=data, request_options=request_options)
        return _response.data

    async def register(
        self,
        *,
        data: typing.Optional[RegisterRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Register

        Parameters
        ----------
        data : typing.Optional[RegisterRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.not_supported_yet import (
            RegisterRequestData,
            RegisterRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.register(
                data=RegisterRequestData(
                    attributes=RegisterRequestDataAttributes(
                        email="cms6@webiz.cz",
                        password="password",
                        password_confirmation="password",
                    ),
                    type="users",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register(data=data, request_options=request_options)
        return _response.data

    async def add_composable_to_cart(
        self,
        *,
        data: typing.Optional[AddComposableToCartRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add Composable To Cart

        Parameters
        ----------
        data : typing.Optional[AddComposableToCartRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.not_supported_yet import (
            AddComposableToCartRequestData,
            AddComposableToCartRequestDataAttributes,
            AddComposableToCartRequestDataAttributesComponentsItem,
            AddComposableToCartRequestDataAttributesComposable,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.add_composable_to_cart(
                data=AddComposableToCartRequestData(
                    attributes=AddComposableToCartRequestDataAttributes(
                        components=[
                            AddComposableToCartRequestDataAttributesComponentsItem(
                                purchasable_id=60908.0,
                                purchasable_type="Lunar\\Models\\ProductVariant",
                            ),
                            AddComposableToCartRequestDataAttributesComponentsItem(
                                purchasable_id=60921.0,
                                purchasable_type="Lunar\\Models\\ProductVariant",
                            ),
                        ],
                        composable=AddComposableToCartRequestDataAttributesComposable(
                            purchasable_id=60906.0,
                            purchasable_type="Lunar\\Models\\ProductVariant",
                        ),
                    ),
                    type="cart-lines",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_composable_to_cart(data=data, request_options=request_options)
        return _response.data

    async def csrf_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        CSRF token

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.not_supported_yet.csrf_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.csrf_token(request_options=request_options)
        return _response.data
