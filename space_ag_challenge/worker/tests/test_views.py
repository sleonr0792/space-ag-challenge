# Create your tests here.

import pytest
from rest_framework.reverse import reverse

from ..models import FieldWorker
from ..views import FieldWorkerViewSet

pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_worker_field(db):
    return FieldWorker.objects.create(first_name="test", last_name=" test 2")


def test_worker_field_list_count(client, create_worker_field):
    view = FieldWorkerViewSet()
    assert view.queryset.count() == 1


def test_worker_field_detail(client, create_worker_field):

    worker = create_worker_field
    response = client.get(
        reverse("field-workers:field-workers-detail", kwargs={"pk": worker.id})
    )
    assert response.data.get("first_name") == "test"


def test_create_a_field_worker(client):
    client.post(
        reverse("field-workers:field-workers-list"),
        {"first_name": "foo", "last_name": "bar"},
    )

    assert FieldWorker.objects.count() == 1


def test_not_create_field_worker(client):
    response = client.post(
        reverse("field-workers:field-workers-list"),
        {"first_name": "", "last_name": "bar"},
    )
    assert response.status_code == 400


def test_update_field_worker_info(client, create_worker_field):
    field_worker = create_worker_field
    new_name = "foo_change"
    new_last_name = "bar_change"
    response = client.put(
        reverse("field-workers:field-workers-detail", kwargs={"pk": field_worker.id}),
        data={"first_name": new_name, "last_name": new_last_name},
        content_type="application/json",
    )
    assert response.status_code == 200
    field_worker_upload = FieldWorker.objects.get(pk=field_worker.id)
    assert field_worker_upload.first_name == new_name
    assert field_worker_upload.last_name == new_last_name


def test_delete_field_worker(client, create_worker_field):
    field_worker = create_worker_field
    response = client.delete(
        reverse("field-workers:field-workers-detail", kwargs={"pk": field_worker.id}),
    )

    assert response.status_code == 204
    assert FieldWorker.objects.count() == 0
