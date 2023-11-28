from inject import Binder, clear_and_configure

from core.domains.product.repository.product_repository import ProductRepository


def configure_app(binder: Binder) -> None:
    service_to_bind = [ProductRepository]

    for service in service_to_bind:
        binder.bind_to_provider(service, service)


def init_provider() -> None:
    clear_and_configure(configure_app)
