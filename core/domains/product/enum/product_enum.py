from enum import Enum


class ProductType(Enum):
    HANDMADE = "제조 음료"
    BOTTLE = "병 음료"
    BAKERY = "베이커리"


class ProductSellingStatus(Enum):
    SELLING = "판매중"
    HOLD = "판매보류"
    STOP_SELLING = "판매중지"

    @classmethod
    def for_display(cls):
        return [ProductSellingStatus.SELLING, ProductSellingStatus.HOLD]


class OrderStatus(Enum):
    INIT = "주문생성"
    CANCELED = "주문취소"
    PAYMENT_COMPLETED = "결제완료"
    PAYMENT_FAILED = "결제실패"
    RECEIVED = "주문접수"
    COMPLETED = "처리완료"
