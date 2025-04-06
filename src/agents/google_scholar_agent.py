from playwright.sync_api import sync_playwright
from .base_agent import BaseSearchAgent


class GoogleScholarAgent(BaseSearchAgent):
    def __init__(self, query, agent_id, output_dir, credentials=None):
        super().__init__(query, agent_id, output_dir)
        self.credentials = credentials

    def login(self, page):
        # Логика авторизации, если переданы учетные данные
        if self.credentials:
            # Код для входа в аккаунт Google
            pass

    def search(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Авторизация если нужно
            self.login(page)

            # Выполнение поиска
            page.goto(
                f"https://scholar.google.com/scholar?q={self.query.replace(' ', '+')}")

            # Пауза для загрузки результатов
            page.wait_for_selector(".gs_r")

            # Получение результатов
            results = page.query_selector_all(".gs_r")

            for result in results[:10]:  # Берем первые 10 результатов
                title = result.query_selector(".gs_rt")
                link = result.query_selector(".gs_rt a")
                if title and link:
                    self.results.append({
                        "title": title.inner_text(),
                        "url": link.get_attribute("href"),
                    })

            browser.close()
        return self.results
