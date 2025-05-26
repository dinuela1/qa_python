import pytest as pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['', 'Very long name'*3])
    def test_add_new_book_length_0_and_42_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_valid_name_not_existing_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Зайчики и кролики')
        collector.set_book_genre('Зайчики и кролики', 'Смешарики')
        assert collector.get_book_genre('Зайчики и кролики') == ''

    def test_get_book_genre_existing_name_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сойка')
        collector.set_book_genre('Сойка', 'Ужасы')
        assert collector.get_book_genre('Сойка') == 'Ужасы'

    def test_get_books_with_specific_genre_horror_get(self):
        collector = BooksCollector()
        collector.add_new_book('Тюльпаны')
        collector.set_book_genre('Тюльпаны', 'Ужасы')
        collector.add_new_book('Лютики')
        collector.set_book_genre('Лютики', 'Ужасы')
        collector.add_new_book('Иван-чай')
        collector.set_book_genre('Иван-чай', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Тюльпаны', 'Лютики']

    def test_get_books_genre_valid_name_no_genre_get(self):
        collector = BooksCollector()
        collector.add_new_book('Birds')
        assert collector.get_books_genre() == {'Birds': ''}

    def test_get_books_for_children_gets_only_valid_genre_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тюльпаны')
        collector.set_book_genre('Тюльпаны', 'Ужасы')
        collector.add_new_book('Иван-чай')
        collector.set_book_genre('Иван-чай', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Иван-чай']

    def test_add_book_in_favorites_not_existing_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('My favorite book!')
        assert 'My favorite book!' not in collector.favorites

    def test_delete_book_from_favorites_existing_favorite_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Coolest book')
        collector.add_book_in_favorites('Coolest book')
        collector.delete_book_from_favorites('Coolest book')
        assert 'Coolest book' not in collector.favorites

    def test_get_list_of_favorites_books_two_book_shows_list(self):
        collector = BooksCollector()
        collector.add_new_book('book1')
        collector.add_book_in_favorites('book1')
        collector.add_new_book('book2')
        collector.add_book_in_favorites('book2')
        assert collector.get_list_of_favorites_books() == ['book1', 'book2']
