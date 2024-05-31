from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

target_url = "https://www.saucedemo.com/v1/inventory.html"

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/v1/")

username = driver.find_element(By.XPATH, "//div[@class='login-box']//input[@name='user-name']").send_keys("standard_user")
password = driver.find_element(By.XPATH, "//div[@class='login-box']//input[@name='password']").send_keys("secret_sauce")
btn_login = driver.find_element(By.XPATH, "//div[@class='login-box']//input[@type='submit']").click()
assert driver.current_url == target_url

for i in range(1,6,1):
    product = driver.find_element(By.XPATH, f"(//*[@class='inventory_item'])[{i}]//div[@class='inventory_item_label']//a//div").click()
    description = driver.find_element(By.XPATH, "//div[@class='inventory_details_name']").text
    add_to_cart = driver.find_element(By.XPATH, "//button[@class='btn_primary btn_inventory']").click()
    cart = driver.find_element(By.XPATH, "//*[@fill='currentColor']").click()
    assert description == driver.find_element(By.XPATH, f"(//div[@class='cart_item'])[{i}]//div[@class='inventory_item_name']").text, "Item não encontrado no carrinho"
    add_to_cart = driver.find_element(By.XPATH, "//a[@class='btn_secondary']").click()
    
driver.find_element(By.XPATH, "//*[@fill='currentColor']").click()
driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']").click()
driver.find_element(By.ID, "first-name").send_keys("Username")
driver.find_element(By.ID, "last-name").send_keys("Aristidiles")
driver.find_element(By.ID, "postal-code").send_keys("00000-000")
driver.find_element(By.XPATH, "//input[@class='btn_primary cart_button']").click()
driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()
assert driver.find_element(By.XPATH, "//h2[@class='complete-header']").is_displayed()
