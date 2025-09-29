# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import expect
import os

class AdminPage:
    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url or os.getenv("APP_URL", "http://localhost:5173")

    def get_current_product_count(self):
        product_cards = self.page.locator(".product-item")
        return product_cards.count()

    def create_product(self, product):
        input_create_product = self.page.get_by_placeholder("Product Name")
        button_create_product = self.page.get_by_role("button", name="Create Product")
        input_create_product.fill(product)
        button_create_product.click()

    def delete_product_by_name(self, product):
        product_row = self.page.locator(f".product-item:has(span:text('{product}'))")
        delete_button = product_row.get_by_role("button", name="Delete")
        delete_button.click()

    def product_exists(self, product: str) -> bool:
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        return product_locator.is_visible()

    def product_is_visible(self, product):
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        expect(product_locator).to_be_visible()

    def product_to_not_be_visible(self, product):    
        product_locator = self.page.locator(f".product-item:has-text('{product}')")
        expect(product_locator).not_to_be_visible()