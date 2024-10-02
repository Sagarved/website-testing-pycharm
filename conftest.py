import pytest
# import os
# import logging
#
# # Setup logger
# logger = logging.getLogger(__name__)
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # This will capture screenshots for all tests (pass or fail) and embed them in the report.
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.when == "call" and (report.passed or report.failed):
#     # Capture screenshot at the end of the test execution
#         if "driver" in item.fixturenames:  # Check if the test uses a driver fixture
#             driver = item.funcargs['driver']
#             screenshot_dir = "logs"
#             if not os.path.exists(screenshot_dir):
#                 os.makedirs(screenshot_dir)  # Create the directory if it doesn't exist
#
#             # Replace colons and special characters in the nodeid to create a valid filename
#             #screenshot_path = os.path.join(screenshot_dir, f"{item.nodeid.replace('::', '_').remove}.png")
#             image_name = f"logs/{item.nodeid.replace('::', '_').replace('tests','')}.png"
#             print(image_name)
#             logger.info('Saving Screenshot from conftest')
#
#             screenshot_path = image_name#os.path.join(screenshot_dir,image_name)
#             driver.save_screenshot(screenshot_path)
#
#             # Attach the screenshot to the HTML report for both pass and fail cases
#             # with open(screenshot_path, "rb") as f:
#             #     pytest_html = item.config.pluginmanager.getplugin('html')
#             #     #extra = pytest_html.extras.png(f.read(), mime_type='image/png')
#             #     extra = pytest_html.extras.png(f.read())
#             #     report.extra = getattr(report, 'extra', []) + [extra]
#
#             if os.path.exists(screenshot_path):
#                 with open(screenshot_path, "rb") as image_file:
#                     # Attach the image to the HTML report
#                     extra = pytest_html.extras.png(image_file.read())
#                     report.extra = getattr(report, 'extra', []) + [extra]
#
