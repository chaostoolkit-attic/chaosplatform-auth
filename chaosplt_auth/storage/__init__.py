from typing import Any, Dict, NoReturn

import attr
from chaos_relational_storage import initialize_storage as init_storage, \
    configure_storage, release_storage, RelationalStorage
import pkg_resources

from .concrete import AccessTokenService, OAuthTokenService
from .interface import BaseAuthStorage, BaseAccessTokenService, \
    BaseOAuthTokenService

__all__ = ["initialize_storage", "shutdown_storage", "AuthStorage"]


class AuthStorage(BaseAuthStorage):
    def __init__(self, config: Dict[str, Any]):
        self.driver = init_storage(config)
        configure_storage(self.driver)

        access_token = AccessTokenService(self.driver)
        oauth_token = OAuthTokenService(self.driver)
        BaseAuthStorage.__init__(self, access_token, oauth_token)

    def release(self) -> NoReturn:
        release_storage(self.driver)


def initialize_storage(config: Dict[str, Any]) -> AuthStorage:
    for plugin in pkg_resources.iter_entry_points('chaoshub.storage'):
        if plugin.name == "auth":
            service_class = plugin.load()
            return service_class(config)

    return AuthStorage(config)


def shutdown_storage(storage: AuthStorage) -> NoReturn:
    storage.release()
