from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""

    CATALOG_LINK = (By.CSS_SELECTOR, '[class="nav-item js-nav-item"] [href="/collection/all"]')
    CATALOG_TITLE = (By.CSS_SELECTOR, '[class="section-title"]')


class CatalogPageLocators:
    """Локаторы для страницы каталога"""

    SMARTPHONE_LINK = (By.CSS_SELECTOR,'[class="subcollection_card-thumb subcollection_card-thumb--1x1 subcollection_card-thumb--contain"]')
    SMARTPHONE_TITLE = (By.CSS_SELECTOR, '[class="section-title"]')


class SmartphonesPageLocators:
    """Локаторы для страницы смартфонов"""

    BRAND_GOOGLE = (By.CSS_SELECTOR, '[id="filter-value-175885426"]')
    DATA_256 = (By.CSS_SELECTOR, '[id="filter-value-109849128"]')
    SELECT_PRODUCT_1 = (By.CSS_SELECTOR, '[class="product_card-thumb product_card-thumb--1x1 product_card-thumb--contain"]')
    DESCRIPTION = (By.CSS_SELECTOR, '[data-target="description"]')


class ProductPageLocators:
    """Локаторы для страницы продукта"""

    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="product-title"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-prices .product-price")
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[class="button button--primary button--block button--medium"]')
    OPEN_BASKET = (By.CSS_SELECTOR, '[class="button button--primary button--block button--large"]')
    BASKET_WORD = (By.CSS_SELECTOR, '[class="text-title"]')


class BasketPageLocators:
    """Локаторы для страницы корзины"""

    SUBMIT_BUTTON = (By.CSS_SELECTOR,'[class="button button--primary button--block button--large"]')


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""

    ORDER_PRODUCT_NAME = (By.CSS_SELECTOR, '[class="co-basket_item-description"]')
    ORDER_TOTAL_PRICE = (By.ID,'total_price')
    FIO = (By.CSS_SELECTOR, '[id="client_contact_name"]')
    PHONE = (By.CSS_SELECTOR, '[id="client_phone"]')
    CITY = (By.CSS_SELECTOR, '[id="shipping_address_full_locality_name"]')
    DELIVERY = (By.CSS_SELECTOR, '[for="order_delivery_variant_id_8609044"]')
    ADDRESS = (By.CSS_SELECTOR, '[id="shipping_address_address"]')
    COMMENT = (By.CSS_SELECTOR, '[id="order_comment"]')
    DELIVERY_TIME = (By.CSS_SELECTOR, '[id="delivery-time-intervals-select"]')
    EMAIL = (By.CSS_SELECTOR, '[id="client_email"]')
    NOTIFICATION_CHECKBOX = (By.CSS_SELECTOR,'.co-toggable_field[for="client_messenger_subscription_1"]') #   добавил ошибку в локатор _1
    DATE = (By.CSS_SELECTOR, '[id="delivery-date-calendar"]')
    DAY = (By.CSS_SELECTOR, '[class="rd-day-body"]')
    SPINNER = (By.CSS_SELECTOR, ".spinner.slide-up")
