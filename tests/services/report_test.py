from datetime import datetime, timedelta

from services import report_service, flight_service, package_service


def test_package_report_mocked_db(mocker):
    report_date = datetime.now() - timedelta(days=1)
    mocked_packages_finder = mocker.patch('services.report_service.db.find_all_transported_packages_on',
                                          return_value=[mocker.MagicMock(),
                                                        mocker.MagicMock(),
                                                        mocker.MagicMock()])

    report_1 = report_service.packages_report(report_date)

    mocked_packages_finder.assert_called_with(report_date)
    assert report_1.total_packages == 3
    assert report_1.profits == 3 * report_service.PROFIT_PER_PACKAGE
