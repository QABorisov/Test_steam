import time

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
    search_with_sorting.wait_for_open()
    search_with_sorting.search_game(game_name)
    search_with_sorting.check_loading_search_page()
    assert search_with_sorting.get_result_search() == game_name, f"Не перешли на страницу с результатами поиска {game_name}"
    search_with_sorting.send_filter()
    search_with_sorting.sort_check()
    assert search_with_sorting.get_list_price_game(
        min_count), f"Сортировка из {min_count} игр {game_name} по убыванию цены некорректна"
