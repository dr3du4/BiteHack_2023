import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()



def get_AGH(kierunek):
    driver.get("https://rekrutacja.agh.edu.pl/kierunki-studiow/")
    driver.maximize_window()
    driver.implicitly_wait(1)
    subject = driver.find_element(By.XPATH, f"//div[@class='field-of-study']//a[contains(text(),'Socjologia')]")
    location = subject.location
    driver.execute_script(f"window.scrollTo(0, {location['y']})")
    time.sleep(5)
    subject.click()

    try:
        G1 = driver.find_element(By.XPATH,
                                 "//h4[contains(text(),'G1')]//parent::div//parent::div//div[@class='subjects-list']")
        helper = "G1\n" + G1.text
        subjectsG1 = helper.split("\n")
        G2 = driver.find_element(By.XPATH,
                                 "//h4[contains(text(),'G2')]//parent::div//parent::div//div[@class='subjects-list']")
        helper = "G2\n" + G2.text
        subjectsG2 = helper.split("\n")
        if (G1.text == G2.text):
            return subjectsG1
        else:
            return subjectsG1
    except:
        G = driver.find_element(By.XPATH,
                                "//h4[contains(text(),'G1')]//parent::div//parent::div//div[@class='subjects-list columns']")
        helper = "G1 and G2\n" + G.text
        subjectsG1 = helper.split("\n")
        return subjectsG1


def get_PolitechnikaLodzka(kierunek):
    driver.get("https://rekrutacja.p.lodz.pl/pl/przedmioty-kwalifikacyjne")
    driver.maximize_window()
    driver.implicitly_wait(1)
    polish = driver.find_element(By.XPATH, "//h3[@id='ui-accordion-1-header-0']")
    polish.click()
    subject_basic = driver.find_element(By.XPATH, f"//div//table/tbody/tr/td[text()='{kierunek}']//parent::tr//td[2]")
    g1 = subject_basic.get_attribute("innerText")
    g1 = g1.replace(u'\xa0', u' ')
    g1 = g1.split("■")
    g1[0] = 'G1'

    subject_extended = driver.find_element(By.XPATH,
                                           f"//div//table/tbody/tr/td[text()='{kierunek}']//parent::tr//td[3]")
    g2 = subject_extended.get_attribute("innerText")
    try:
        g2 = g2.replace(u'\xa0', u' ')
        g2 = g2.split(" lub ")
        g2.remove('dyplom zawodowy')
        g2[0] = g2[0][4:]
        g2.insert(0, 'G2')
    finally:
        return (print(g1 + g2))

def get_PolitechnikaKrakowska(kierunek):
    pass

def get_PolitechnikaWarszawska(kierunek):
    pass

def get_PolitechnikaWroclawska(kierunek):
    pass

# na sztywno
def get_PolitechnikaPoznanska(kierunek):
    pass

def get_PolitechnikaSlaska(kierunek):
    pass

def get_PolitechnikaOpolska(kierunek):
    pass

def get_PolitechnikaGdanska(kierunek):
    pass

def get_PolitechnikaBialostocka(kierunek):
    pass

def get_PolitechnikaLubelska(kierunek):
    pass

def get_PolitechnikaKoszalinska(kierunek):
    pass

def get_PolitechnikaRzeszowska(kierunek):
    pass

def get_PolitechnikaSzczecinska(kierunek):
    pass

def get_PolitechnikaBydgoska(kierunek):
    pass

def get_PolitechnikaCzestochowska(kierunek):
    pass

# calc_AGH("ceramika")