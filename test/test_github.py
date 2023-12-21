from selene import browser, by, be
from selene.support.shared.jquery_style import s
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sdudnik")
@allure.feature("Issue в репозитории с помощью")
@allure.story("Проверка наличия Issue")
@allure.link("https://github.com", name="Testing")
def test_git_open_with_selene(browser_open_with_selene):
    s(".header-search-button").click()
    s(".QueryBuilder-InputWrapper").click()
    s(".QueryBuilder-InputWrapper>input").send_keys("idudnik/qa_guru_9_allure")
    s(".QueryBuilder-InputWrapper>input").submit()
    s(".header-search-button").click()
    s(by.link_text("idudnik/qa_guru_9_allure")).click()
    s("#issues-tab").click()
    s(by.text("github long opening with pytest")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sdudnik")
@allure.feature("Issue в репозитории с помощью")
@allure.story("Проверка наличия Issue")
@allure.link("https://github.com", name="Testing")
def test_dynamic_step():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Открываем поисковую строку"):
        s(".header-search-button").click()
        s(".QueryBuilder-InputWrapper").click()
    with allure.step("Ищем репозиторий"):
        s(".QueryBuilder-InputWrapper>input").send_keys("idudnik/qa_guru_9_allure")
        s(".QueryBuilder-InputWrapper>input").submit()
        s(".header-search-button").click()
    with allure.step("Переходим на вкладку Issues"):
        s(by.link_text("idudnik/qa_guru_9_allure")).click()
        s("#issues-tab").click()
    with allure.step("Проверяем наличие Issues"):
        s(by.text("github long opening with pytest")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "sdudnik")
@allure.feature("Issue в репозитории с помощью")
@allure.story("Проверка наличия Issue")
@allure.link("https://github.com", name="Testing")

def test_decorator_steps():
    open_main_page()
    open_search_page()
    search_repository("idudnik/qa_guru_9_allure")
    go_to_issues_tab("idudnik/qa_guru_9_allure")
    check_the_tab()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Открываем поисковую строку")
def open_search_page():
    s(".header-search-button").click()
    s(".QueryBuilder-InputWrapper").click()


@allure.step("Ищем репозиторий {repo}")
def search_repository(repo):
    s(".QueryBuilder-InputWrapper>input").send_keys(repo)
    s(".QueryBuilder-InputWrapper>input").submit()
    s(".header-search-button").click()


@allure.step("Переходим на вкладку Issues {repo}")
def go_to_issues_tab(repo):
    s(by.link_text(repo)).click()
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issues")
def check_the_tab():
    s(by.text("github long opening with pytest")).should(be.visible)
