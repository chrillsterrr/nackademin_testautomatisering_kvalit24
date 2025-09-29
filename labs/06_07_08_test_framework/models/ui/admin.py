# View  where the admin user can manage the products
# that are in the Product Catalog to be used
# by all the users
from playwright.sync_api import expect
import os

class AdminPage:
    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url or os.getenv("APP_URL")


    def get_current_product_count(self):
        return self.product_cards.count()
    
    def create_product(self, product):
    # Don't navigate here - assume we're already on admin page
    # Just ensure page is ready
        self.page.wait_for_load_state("domcontentloaded")
        
        # Wait for input with better error message
        input_create_product = self.page.get_by_placeholder("Product Name")
        try:
            input_create_product.wait_for(state="visible", timeout=30000)
        except Exception as e:
            print(f"Failed to find 'Product Name' input. Current URL: {self.page.url}")
            self.page.screenshot(path="failed_state.png")
            raise e
        
        input_create_product.fill(product)
        self.page.get_by_role("button", name="Create Product").click()
    

    #def create_product(self, product):
    #    self.page.goto(self.base_url)
    #    # wait for input to appear
    #    input_create_product = self.page.get_by_placeholder("Product Name")
    #    input_create_product.wait_for(state="visible", timeout=10000)
    #    input_create_product.fill(product)
    #    self.page.get_by_role("button", name="Create Product").click()

    

    def delete_product_by_name(self,product):
        # complete logic
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