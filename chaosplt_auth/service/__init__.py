from abc import ABC, abstractmethod
from typing import Any, Dict

import attr

from .account import AccountService

__all__ = ["initialize_services", "shutdown_services", "Services"]


@attr.s
class Services:
    account: AccountService = attr.ib(default=None)


def initialize_services(services: Services, config: Dict[str, Any]):
    if not services.account:
        services.account = AccountService(config)


def shutdown_services(services: Services):
    pass
