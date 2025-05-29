import pytest as pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['', 'Very long name'*3])
    def test_add_new_book_length_0_and_42_not_added(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_valid_name_existing_genre_set(self, collector):
        collector.add_new_book('Зайчики и кролики')
        collector.set_book_genre('Зайчики и кролики', 'Мультфильмы')
        assert collector.books_genre['Зайчики и кролики'] == 'Мультфильмы'

    def test_get_book_genre_existing_name_get_genre(self, collector):
        collector.books_genre = {'Сойка': 'Ужасы'}
        assert collector.get_book_genre('Сойка') == 'Ужасы'

    def test_get_books_with_specific_genre_horror_get(self, collector):
        collector.books_genre['Тюльпаны'] = 'Ужасы'
        collector.books_genre['Лютики'] = 'Ужасы'
        collector.books_genre['Иван-чай'] = 'Мультфильмы'
        assert collector.get_books_with_specific_genre('Ужасы') == ['Тюльпаны', 'Лютики']

    def test_get_books_genre_valid_name_no_genre_get(self, collector):
        collector.add_new_book('Birds')
        assert collector.get_books_genre() == {'Birds': ''}

    def test_get_books_for_children_gets_only_valid_genre_book(self, collector):
        collector.books_genre['Лютики'] = 'Ужасы'
        collector.books_genre['Иван-чай'] = 'Мультфильмы'
        assert collector.get_books_for_children() == ['Иван-чай']

    def test_add_book_in_favorites_existing_book_added(self, collector):
        collector.books_genre['My favorite book!'] = ''
        collector.add_book_in_favorites('My favorite book!')
        assert 'My favorite book!' in collector.favorites

    def test_delete_book_from_favorites_existing_favorite_book_deleted(self, collector):
        collector.books_genre['Coolest book'] = ''
        collector.add_book_in_favorites('Coolest book')
        collector.delete_book_from_favorites('Coolest book')
        assert 'Coolest book' not in collector.favorites

    def test_get_list_of_favorites_books_two_book_shows_list(self, collector):
        collector.books_genre['My favorite book!'] = ''
        collector.add_book_in_favorites('My favorite book!')
        collector.books_genre['Coolest book'] = ''
        collector.add_book_in_favorites('Coolest book')
        assert collector.get_list_of_favorites_books() == ['My favorite book!', 'Coolest book']
