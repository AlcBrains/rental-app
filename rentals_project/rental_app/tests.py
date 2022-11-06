from django.test import RequestFactory, TestCase
from .models import Rental, Reservation
from .views import ReservationsList


# models test
class RentalTests(TestCase):
    def create_test_rental(self, name):
        return Rental.objects.create(name=name)

    def test_rental_creation(self):
        test_object = self.create_test_rental("TestRental")
        self.assertTrue(isinstance(test_object, Rental))
        self.assertEqual("TestRental", test_object.name)


class ReservationTests(TestCase):
    def create_test_reservation(self, rental, checkin, checkout):
        return Reservation.objects.create(rental=rental, checkin=checkin, checkout=checkout)

    def test_reservation_creation(self):
        # borrowing rental creation
        test_rental = RentalTests().create_test_rental(name="TestRental")
        test_reservation = self.create_test_reservation(
            test_rental, '2022-01-01', '2022-01-03')
        self.assertTrue(isinstance(test_reservation, Reservation))
        self.assertEqual('2022-01-01', test_reservation.checkin)


# manager test
class ReservationsManagerTest(TestCase):
    test_reservations = [
        {"rental": 1, "checkin": "2022-01-01", "checkout": "2022-01-13"},
        {"rental": 1, "checkin": "2022-01-20", "checkout": "2022-02-10"},
        {"rental": 1, "checkin": "2022-02-20", "checkout": "2022-03-10"},
        {"rental": 2, "checkin": '2022-01-02', "checkout": "2022-01-20"},
        {"rental": 2, "checkin": '2022-01-20', "checkout": "2022-01-11"}
    ]

    def test_reservations_list_queryset_has_annotation(self):

        # need to create some rentals first
        test_rental = Rental.objects.create(name="TestRental1")
        another_test_rental = Rental.objects.create(name="TestRental2")

        for reservation in self.test_reservations:
            Reservation.objects.create(rental=test_rental if reservation['rental'] == 1 else another_test_rental,
                                       checkin=reservation['checkin'], checkout=reservation['checkout'])

        objects = Reservation.objects.get_queryset()
        self.assertIsNotNone(objects)
        self.assertIsNone(objects[0].prev_res_id)
        self.assertEqual(objects[1].prev_res_id, 1)
        self.assertEqual(objects[2].prev_res_id, 2)
        self.assertIsNone(objects[3].prev_res_id)
        self.assertEqual(objects[4].prev_res_id, 4)


# views test
class ReservationsListTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_reservations_list_view_exists(self):
        # Create an instance of a GET request.
        request = self.factory.get('')
        # Test my_view() as if it were deployed at /
        response = ReservationsList.as_view()(request)

        self.assertEqual(response.status_code, 200)
