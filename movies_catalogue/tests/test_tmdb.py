import tmdb_client
from mock import patch, Mock
import pytest
from app import app
from unittest.mock import Mock

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
   mock_movie_detail = "{'adult': False, 'backdrop_path': '/8s4h9friP6Ci3adRGahHARVd76E.jpg'..."
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_detail
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_detail = tmdb_client.get_single_movie(movie_id=1)
   assert movie_detail == mock_movie_detail

def test_get_movie_images(monkeypatch):
   mock_movie_images= "{'success': False..."
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_images
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_images= tmdb_client.get_movies_images(movie_id=1)
   assert movies_images == mock_movie_images

def test_get_single_movie_cast(monkeypatch):
   mock_movie_detail_cast = "[{'adult': False, 'gender': 2, 'id': 107379..."
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_detail_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_detail_cast = tmdb_client.get_single_movie(movie_id=1)
   assert movie_detail_cast == mock_movie_detail_cast


@pytest.mark.parametrize('list_type', (
  ('popular'),
  ('now_playing'),
  ('top_rated'),
  ('upcoming')
))
def test_homepage(list_type, monkeypatch):
   api_mock = Mock( return_value=list_type)
   monkeypatch.setattr("tmdb_client.get_movies_list", api_mock)

   with app.test_client() as client:
      response = client.get('/')
      assert response.status_code == 200
      assert api_mock.return_value == list_type