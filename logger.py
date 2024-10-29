import logging

activity_handler = logging.FileHandler("activity.log")
activity_handler.setLevel(logging.INFO)
activity_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
activity_handler.setFormatter(activity_formatter)

activity_logger = logging.getLogger('activity')
activity_logger.setLevel(logging.INFO)
activity_logger.addHandler(activity_handler)
activity_logger.addHandler(logging.StreamHandler())

error_handler = logging.FileHandler("errors.log")
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)

error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(error_handler)
error_logger.addHandler(logging.StreamHandler())
