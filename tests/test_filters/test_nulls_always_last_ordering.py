from django.utils import timezone
from django_filters import OrderingFilter as BaseOrderingFilter

from jnt_django_graphene_toolbox.filters.mixins import (
    NullsAlwaysLastOrderingMixin,
)
from tests.test_filters.models import OrderTestModel


class DemoFilter(NullsAlwaysLastOrderingMixin, BaseOrderingFilter):
    """Test ordering filter."""


def test_asc_ordering(db):
    """Test asc ordering case."""
    now = timezone.now()

    issues = [
        OrderTestModel.objects.create(
            due_date=now - timezone.timedelta(days=1),
        ),
        OrderTestModel.objects.create(due_date=now),
        OrderTestModel.objects.create(due_date=None),
    ]

    test_filter = DemoFilter(fields=(("due_date",)))

    queryset = test_filter.filter(
        OrderTestModel.objects.all(), value=["due_date"],
    )

    assert list(queryset) == issues


def test_desc_ordering(db):
    """Test desc ordering case."""
    now = timezone.now()

    issues = [
        OrderTestModel.objects.create(due_date=None),
        OrderTestModel.objects.create(
            due_date=now - timezone.timedelta(days=1),
        ),
        OrderTestModel.objects.create(due_date=now),
    ]

    test_filter = DemoFilter(fields=(("due_date",)))

    queryset = test_filter.filter(
        OrderTestModel.objects.all(), value=["-due_date"],
    )

    issues.reverse()

    assert list(queryset) == issues
