import luigi
from time import sleep
from loguru import logger


class ReadFileTask(luigi.Task):
    filename = luigi.Parameter()
    sleep_time_in_seconds = luigi.IntParameter()

    def run(self):
        pass

    def output(self):
        pass

    def requires(self):
        pass


if __name__ == '__main__':
    luigi.run()
