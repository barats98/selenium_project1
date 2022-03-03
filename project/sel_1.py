from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random

class AOS:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.driver.implicitly_wait(8)

    def logo(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='logo']>a[ng-click='go_up()']")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='logo']>a[ng-click='go_up()']")

    def return_to_home_page(self):
        self.logo().click()

    def back(self):
        self.driver.back()

    def category_speakers(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#headphonesTxt")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='speakersImg']")

    def category_tablets(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#headphonesTxt")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='tabletsImg']")

    def category_laptops(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#headphonesTxt")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='laptopsImg']")

    def category_mice(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#headphonesTxt")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[id='miceImg']")

    def category_headphones(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span#headphonesTxt")))
        return self.driver.find_element(By.CSS_SELECTOR,"span#headphonesTxt")

    def select_category_speakers(self):
        self.category_speakers().click()

    def select_category_tablets(self):
        self.category_tablets().click()

    def select_category_laptops(self):
        self.category_laptops().click()

    def select_category_mice(self):
        self.category_mice().click()

    def select_category_headphones(self):
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        self.category_headphones().click()

    def select_random_category(self):
        categorylist=[]
        self.wait.until(EC.element_to_be_clickable((By.ID,"tabletsImg")))
        categorylist.append(self.category_speakers())
        categorylist.append(self.category_tablets())
        categorylist.append(self.category_laptops())
        categorylist.append(self.category_mice())
        categorylist.append(self.category_headphones())
        rand=random.randint(0,len(categorylist)-1)
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        categorylist[rand].click()

    def products(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.roboto-medium.ng-scope")))
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        productlist=self.driver.find_elements(By.CSS_SELECTOR,"ul>li[class='ng-scope']>div[class='AddToCard']")
        return productlist

    def select_product(self,productnum:int=1):
        """enter number of product from top left to bottom right (1-number of products)"""
        # self.driver.implicitly_wait(8)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.titleItemsCount")))
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        numberofitemsinpage = self.driver.find_element(By.CSS_SELECTOR, "a.titleItemsCount")
        if int(numberofitemsinpage.text.split()[0]) < productnum:
            productnum = len(self.products())
        productlist = self.products()
        product = productlist[productnum-1]
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        product.click()

    def select_random_product(self):
        productlist=self.products()
        randomnum=random.randint(0,len(productlist)-1)
        product=productlist[randomnum]
        # self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button#checkOutPopUp")))
        # use this wait when selecting more than 4 different products (pop up window blocks the link)
        product.click()

    def select_product_by_id(self,id:int):
        id=str(id)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.titleItemsCount")))
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ng-scope>img")))
        product=self.driver.find_element(By.CSS_SELECTOR,f"[id='{id}']")
        product.click()

    def add_to_cart_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='save_to_cart']")))
        return self.driver.find_element(By.CSS_SELECTOR,"button[name='save_to_cart']")

    def add_to_cart(self):
        self.add_to_cart_button().click()

    def add_quantity_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='plus']")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='plus']")

    def reduce_quantity_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='minus']")))
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='minus']")

    def add_quantity(self,num:int=1):
        for i in range(num):
            self.add_quantity_button().click()

    def reduce_quantity(self,num:int=1):
        for i in range(num):
            self.reduce_quantity_button().click()

    def change_quantity(self,num:int):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='quantity'][ng-model='numAttr']")))
        quantity = self.driver.find_element(By.CSS_SELECTOR, "input[name='quantity'][ng-model='numAttr']")
        for i in range(5):
            quantity.send_keys(Keys.BACK_SPACE)
        quantity.send_keys(num)

    def product_page_name(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.roboto-regular.screen768")))
        name=self.driver.find_element(By.CSS_SELECTOR,"h1.roboto-regular.screen768")
        return name.text

    def product_page_price(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h2.roboto-thin.screen768")))
        price=self.driver.find_element(By.CSS_SELECTOR,"div#Description>h2.roboto-thin.screen768.ng-binding")
        return price.text

    def product_page_quantity(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='quantity'][ng-model='numAttr']")))
        quantity=self.driver.find_element(By.CSS_SELECTOR,"input[name='quantity'][ng-model='numAttr']")
        return quantity.get_attribute("value")

    def product_page_color(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[ng-if='product.colors.length > 0']>div[class='']>span.colorSelected")))
        color=self.driver.find_element(By.CSS_SELECTOR,"div[ng-if='product.colors.length > 0']>div[class='']>span.colorSelected")
        return color.get_attribute("title")

    def shopping_cart_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shoppingCartLink")))
        shoppingcarticon=self.driver.find_element(By.CSS_SELECTOR,"#shoppingCartLink")
        return shoppingcarticon

    def shopping_cart_icon_qty(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"a[id='shoppingCartLink']")))
        a=self.driver.find_elements(By.CSS_SELECTOR, "span.cart.ng-binding")
        b=a[-1]
        if b.text=="":
            return 0
        else:
            return b.text

    def shopping_cart_popup_product_info(self,productorder:int=1):
        hover=ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,"#menuCart > path:nth-child(1)"))
        hover.perform()
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li>tool-tip-cart>div>table")))
        products_names=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>h3")
        products_colors_qty=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>label")
        products_prices=self.driver.find_elements(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>p")
        if productorder>len(products_names):
            productorder=len(products_names)
        return products_names[productorder-1].text,products_colors_qty[(2*productorder-2)].text.split()[-1],products_colors_qty[(2*productorder-1)].text.split()[-1],products_prices[(productorder-1)].text

    def shopping_cart_popup_product_name(self,productorder:int=1):
        productname=self.shopping_cart_popup_product_info(productorder)[0]
        return productname

    def shopping_cart_popup_product_qty(self,productorder:int=1):
        productqty=self.shopping_cart_popup_product_info(productorder)[1]
        return productqty

    def shopping_cart_popup_product_color(self,productorder:int=1):
        productcolor=self.shopping_cart_popup_product_info(productorder)[2]
        return productcolor

    def shopping_cart_popup_product_price(self,productorder:int=1):
        productprice=self.shopping_cart_popup_product_info(productorder)[3]
        return productprice

    def shopping_cart_icon_remove_product(self,productorderinpopup:int=1):
        hover = ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "svg#menuCart>path[fill='#313131']"))
        hover.perform()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"table>tbody>tr>td>div>div.removeProduct")))
        removebuttons=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>div>div.removeProduct")
        if productorderinpopup>len(removebuttons):
            selected_remove_button=removebuttons[len(removebuttons)-1]
        else:
            selected_remove_button = removebuttons[productorderinpopup - 1]
        selected_remove_button.click()

    def move_to_shopping_cart_page(self):
        self.shopping_cart_icon().click()

    def shopping_cart_page_title(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"h3.roboto-regular.sticky")))
        return self.driver.find_element(By.CSS_SELECTOR,"h3.roboto-regular.sticky")

    def shopping_cart_page_info(self,productorderinpage:int=1):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "h3.roboto-regular.sticky")))
        allproductsnames=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>label.roboto-regular.productName")
        allproductscolors=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>span.productColor")
        allproductqtys=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td.smollCell.quantityMobile>label.ng-binding")
        allproductsprices=self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td.smollCell>p")
        if productorderinpage>len(allproductsnames):
            productorderinpage=len(allproductsnames)
        productname=allproductsnames[productorderinpage-1]
        productcolor=allproductscolors[productorderinpage-1]
        productquantity=allproductqtys[productorderinpage-1]
        productprice=allproductsprices[productorderinpage-1]
        return productname.text,productquantity.text,productcolor.get_attribute("title"),productprice.text

    def shopping_cart_page_product_name(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[0]

    def shopping_cart_page_product_color(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[1]

    def shopping_cart_page_product_qty(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[2]

    def shopping_cart_page_product_price(self,productorderinpage:int=1):
        return self.shopping_cart_page_info(productorderinpage)[3]

    def shopping_cart_page_total_price(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"td[colspan='2']")))
        total=self.driver.find_element(By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tfoot>tr>td>span.roboto-medium.cart-total")
        return total.text

    def shopping_cart_page_edit_product(self,orderofproduct:int=1):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table>tbody>tr>td>span")))
        self.wait.until_not(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"li>tool-tip-cart>div>table>tbody>tr>td>a>h3")))
        editbuttons=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>span>a.edit")
        if orderofproduct>len(editbuttons):
            orderofproduct=len(editbuttons)
        editb=editbuttons[orderofproduct-1]
        editb.click()

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#checkOutButton")))
        checkoutbutton=self.driver.find_element(By.CSS_SELECTOR,"button#checkOutButton")
        checkoutbutton.click()

    def order_payment_page_username_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='usernameInOrderPayment'][type='text']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='usernameInOrderPayment'][type='text']")

    def order_payment_page_enter_username(self,username):
        usernamefield=self.order_payment_page_username_field()
        usernamefield.send_keys(username)

    def order_payment_page_password_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='passwordInOrderPayment'][type='password']")))
        return self.driver.find_element(By.CSS_SELECTOR,"input[name='passwordInOrderPayment'][type='password']")

    def order_payment_page_enter_password(self,password):
        passwordfield=self.order_payment_page_password_field()
        passwordfield.send_keys(password)

    def order_payment_page_login_button(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#login_btnundefined")))
        return self.driver.find_element(By.CSS_SELECTOR,"button#login_btnundefined")

    def order_payment_page_login(self):
        loginbutton=self.order_payment_page_login_button()
        loginbutton.click()

    def order_payment_page_registration_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#registration_btnundefined")))
        return self.driver.find_element(By.CSS_SELECTOR,"button#registration_btnundefined")

    def order_payment_page_registration(self):
        registrationbutton=self.order_payment_page_registration_button()
        registrationbutton.click()

    def create_account_page_username_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='usernameRegisterPage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='usernameRegisterPage']")

    def create_account_page_enter_username(self,username):
        usernamefield=self.create_account_page_username_field()
        usernamefield.send_keys(username)

    def create_account_page_password_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passwordRegisterPage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='passwordRegisterPage']")

    def create_account_page_enter_password(self,password):
        passwordfield= self.create_account_page_password_field()
        passwordfield.send_keys(password)

    def create_account_page_confirm_password_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")

    def create_account_page_confirm_password(self,password):
        confirmpasswordfield=self.create_account_page_confirm_password_field()
        confirmpasswordfield.send_keys(password)

    def create_account_page_email_field(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='emailRegisterPage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='emailRegisterPage']")

    def create_account_page_enter_email(self,email):
        emailfield=self.create_account_page_email_field()
        emailfield.send_keys(email)

    def create_account_page_conditions_check(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='i_agree']")))
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def create_account_page_click_on_conditions(self):
        AOS_condtions_check=self.create_account_page_conditions_check()
        AOS_condtions_check.click()

    def create_account_page_register_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#register_btnundefined")))
        return self.driver.find_element(By.CSS_SELECTOR, "button#register_btnundefined")

    def create_account_page_click_register(self):
        registerbutton=self.create_account_page_register_button()
        # driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.CONTROL, Keys.END)
        registerbutton.click()

    def create_account(self,username,password,email):
        self.create_account_page_enter_username(username)
        self.create_account_page_enter_password(password)
        self.create_account_page_confirm_password(password)
        self.create_account_page_enter_email(email)
        self.create_account_page_click_on_conditions()
        self.create_account_page_click_register()






service_chrome = Service(r"/Applications/Aa.programms/PycharmProjects/chromedriver")
driver=webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com")
driver.maximize_window()


a=AOS(driver)
a.select_category_headphones()
a.select_product(0)
a.back()
a.select_random_product()
a.add_to_cart()
p1name=a.product_page_name()
p1quantity=a.product_page_quantity()
p1color=a.product_page_color()
p1price=a.shopping_cart_popup_product_price()
a.back()
a.back()
a.select_random_category()
a.select_product(0)
a.add_to_cart()
p2name=a.product_page_name()
p2quantity=a.product_page_quantity()
p2color=a.product_page_color()
p2price=a.shopping_cart_popup_product_price()
a.back()
a.back()
for i in range(2):
    a.select_random_category()
    a.select_random_product()
    a.add_to_cart()
    a.back()
    a.back()
a.select_random_category()
# a.select_category_speakers()
# a.select_product_by_id(25)
a.select_random_product()
a.change_quantity(7)
a.shopping_cart_icon_remove_product()
a.add_to_cart()
a.move_to_shopping_cart_page()
print(a.shopping_cart_page_info())
a.shopping_cart_page_edit_product(1)
print(a.product_page_color())
print(a.product_page_quantity())
a.change_quantity(21)
a.add_to_cart()
print(a.shopping_cart_page_product_qty())
a.move_to_shopping_cart_page()
sleep(1)
print(a.shopping_cart_popup_product_info())
a.checkout()
a.order_payment_page_enter_username("zubi")
a.order_payment_page_enter_password("1234567")
a.order_payment_page_login()
a.order_payment_page_registration()
a.create_account_page_enter_email("zub@clxskxnksl.com")
a.create_account_page_enter_username("alonnnn")
a.create_account_page_enter_password("1mskA9s0")
a.create_account_page_confirm_password("1mskA9s0")
a.create_account_page_click_on_conditions()
a.create_account_page_click_register()





# a.select_product(4)
# a.add_quantity(2)
# product1qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(2)
# a.add_quantity(5)
# sleep(1)
# a.reduce_quantity(2)
# product2qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(0)
# product3qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# product3popup=a.shopping_cart_popup_product_info(1)
# product2popup=a.shopping_cart_popup_product_info(2)
# product1popup=a.shopping_cart_popup_product_info(3)
# sleep(1)
# if int(a.shopping_cart_icon_qty())==(product1qty+product2qty+product3qty):
#     print("shopping cart quantity is identical to the sum of product quantities added to cart. the sum is: ",a.shopping_cart_icon_qty())
# print(product3popup)
# print(product2popup)
# print(product1popup)
# print(a.shopping_cart_popup_product_info())
# # a.shopping_cart_icon_remove_product()
# print(a.shopping_cart_popup_product_name(1))
# print(a.shopping_cart_popup_product_qty())
# print(a.shopping_cart_popup_product_color())
# print(a.shopping_cart_popup_product_price())
# print(a.product_page_color())
# a.return_to_home_page()
# a.select_random_category()
# sleep(1)
# driver.back()
# sleep(1)
# a.select_random_category()


# Test 1:
# a=AOS(driver)
# a.select_category_speakers()
# a.select_product(4)
# a.add_quantity(2)
# product1qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(2)
# a.add_quantity(5)
# sleep(1)
# a.reduce_quantity(2)
# product2qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(0)
# product3qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# assertEqual(int(a.shopping_cart_icon_qty()),(product1qty+product2qty+product3qty))
# a.return_to_home_page()
# driver.close()

# Test 2:
# a=AOS(driver)
# a.select_category_speakers()
# a.select_product(4)
# a.add_quantity(2)
# product1qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(2)
# a.add_quantity(5)
# sleep(1)
# a.reduce_quantity(2)
# product2qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# driver.back()
# a.select_product(0)
# product3qty=int(a.product_page_quantity())
# a.add_to_cart()
# sleep(1)
# if p2name[0:27]==a.shopping_cart_popup_product_name(1)[0:27] and p2quantity==a.shopping_cart_popup_product_qty(1) and p2color==a.shopping_cart_popup_product_color(1):
#     print("Success")

# Test 3:
# if ((p2name[0:27]+"...") or (p2name)) and p2price and p2price not in a.shopping_cart_popup_product_info(1):
#     print("Removed")
# print(a.shopping_cart_popup_product_info(1))





