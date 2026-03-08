import pytest
from Utils.config_reader import ConfigReader
from Pages.page_test_search import TestSearch
from Pages.page_test_sort import TestSort


@pytest.mark.parametrize("game_name, min_count",
                         [
                             ("The Witcher", 10),
                             ("Fallout", 20)
                         ])
def test_steam(browser, game_name, min_count):
    config = ConfigReader()
    link = config.get("link")
    timeout = config.get("timeout")
    poll_frequency = config.get("poll_frequency")
    search = TestSearch(timeout, poll_frequency)
    sorting = TestSort(timeout, poll_frequency)
    browser.get(link)
    search.wait_for_open()
    search.search_game(game_name)
    sorting.check_loading_search_page()
    assert sorting.get_result_search() == game_name, f"Не перешли на страницу с результатами поиска {game_name}"
    sorting.send_filter()
    sorting.wait_for_sort()
    list_game = sorting.get_list_price_game(
        min_count)
    list_sorted_game = list_game.copy()
    list_sorted_game.sort(reverse=True)
    assert list_game == list_sorted_game, f"Сортировка из {min_count} игр {game_name} по убыванию цены некорректна"
