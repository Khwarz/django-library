from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Test Book",
            subtitle="Test Book Subtitle",
            author="Test Author",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.subtitle, "Test Book Subtitle")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
