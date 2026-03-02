import pytest
from Utils.config_reader import ConfigReader
from Pages.page_test_search import TestSearch


@pytest.mark.parametrize("game_name, min_count",
                         [
                             ("The Witcher", 10),
                             ("Fallout", 20)
                         ])
def test_steam(browser, game_name, min_count):
    config = ConfigReader()
    link = config.get("link")
    timeout = config.get("timeout")
    search_with_sorting = TestSearch(timeout)
    browser.get(link)
    search_with_sorting.check_home_page()
    search_with_sorting.search_game(game_name)
    assert search_with_sorting.get_result_search() == game_name, f"Не перешли на страницу с результатами поиска {game_name}"
    search_with_sorting.send_filter()
    search_with_sorting.sort_check()
    assert search_with_sorting.get_results_count() >= min_count, f"Ожидаем минимум {min_count} игр, фактически: {search_with_sorting.get_results_count()}"
