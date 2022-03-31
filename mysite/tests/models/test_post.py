import pytest

from blog.factories import PostFactory



@pytest.fixture
def post_publishead():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_publishead_post(post_publishead):
    assert post_publishead.title == 'pytest with factory'
