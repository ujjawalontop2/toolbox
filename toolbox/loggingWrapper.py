import logging

logger = logging.getLogger(__name__)
USE_LOGGING_DATA = True


def logTypeService(data, log_type):
    try:
        if log_type == 'debug':
            logger.debug(str(data))
        if log_type == "info":
            logger.info(str(data))
        if log_type == "error":
            logger.error(str(data))
        if log_type == "warning":
            logger.warning(str(data))
        return True
    except Exception:
        return False


def loggingService(source, data, log_type='info'):
    if USE_LOGGING_DATA:
        try:
            entity = data.get('entity')
            entity_id = data.get('entity_id')
            request = data.get('request_data')
            response = data.get('response_data')
            request_time = data.get('request_time')
            reponse_time = data.get('response_time')
            method_name = data.get('method')
            errors = data.get('errors')
            logging_key = f"{source}-{entity}-{entity_id}"
            log_dict = {
                f"{logging_key}": {
                    "method": method_name,
                    "request": request,
                    "response": response,
                    "request_time": request_time,
                    "reponse_time": reponse_time,
                    "errors": errors
                }
            }
            log = logTypeService(log_dict, log_type)
            return log
        except Exception as ex:
            log = logTypeService(str(ex), log_type="error")
            return log
    pass












