import logging

def setup_logger(name, log_file = 'server.log', level = logging.DEBUG):
            
        logger = logging.getLogger(name)

        # Configure the custom logger
        logger.setLevel(level)

        # if code is running on vs code then write 'backend/server.log'
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger