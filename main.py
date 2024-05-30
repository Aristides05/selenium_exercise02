from selenium import webdriver
from selenium.webdriver.common.by import By
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

for i in range(1,4,1):
    add_to_cart = driver.find_element(By.XPATH, f"(//button[@class='btn_primary btn_inventory'])[{i}]").click()
    btn = driver.find_element(By.XPATH, f"(//button[@class='btn_secondary btn_inventory'])[{i}]").text
    assert btn.lower() == "remove"
    print(f"Prduto {i} Adicionado ao carrinho")

sleep(2)
