import luigi
from time import sleep
from loguru import logger


class FileDetectorTask(luigi.Task):
    filename = luigi.Parameter()
    sleep_time_in_seconds = luigi.IntParameter()

    def output(self):
        return luigi.LocalTarget(self.filename)

    def run(self):
        file_has_arrived = False
        while not file_has_arrived:
            try:
                logger.info(f'Trying to open [{self.filename}]')
                with open(self.filename, 'r') as fd:
                    file_has_arrived = True
                    logger.info('File has arrived.')
            except IOError as _:
                logger.info(f'File has not arrived yet. Sleeping [{self.sleep_time_in_seconds}] seconds')
                sleep(self.sleep_time_in_seconds)
            except Exception as exception:
                logger.exception(exception)


if __name__ == '__main__':
    """
    Run it like this:
    python FileDetector.py --local-scheduler FileDetectorTask --filename 'file1.txt' --sleep-time-in-seconds 60
    """
    luigi.run()
